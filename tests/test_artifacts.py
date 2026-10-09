#!/usr/bin/env python3
"""Check shipped artifacts and prompt fidelity without a Claude login.

python3 tests/test_artifacts.py --source /path/to/published/hub
python3 tests/test_artifacts.py --source /path/to/published/hub --config-dir /external/settings --rebuild

These checks validate packaging and source fidelity, not Claude's live answers.
"""
import argparse
import datetime as dt
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "plugins/wf-lab-guide/skills/lab-guide"
SOURCE = None
CONFIG = None
REBUILD = False


def blocks(text):
    """Extract copyable prompts independently of the builder's Markdown parser."""
    return [m.group(2) for m in re.finditer(
        r"^([ \t]*)```(?:prompt|text)\s*\n(.*?)^\1```[ \t]*$", text, re.M | re.S)]


class CopyPrompts(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.active = False
        self.prompts = []

    def handle_starttag(self, tag, attrs):
        if tag == "textarea" and "copy-src" in dict(attrs).get("class", "").split():
            self.active = True
            self.prompts.append("")

    def handle_endtag(self, tag):
        if tag == "textarea":
            self.active = False

    def handle_data(self, data):
        if self.active:
            self.prompts[-1] += data


def artifact_hashes():
    paths = [p for p in SKILL.rglob("*") if p.is_file()] + list((ROOT / "download").glob("*"))
    paths += [ROOT / "README.md", ROOT / "plugins/wf-lab-guide/.claude-plugin/plugin.json"]
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(paths) if p.is_file()}


class Artifacts(unittest.TestCase):
    def test_start_flow_is_clear_and_checks_are_natural(self):
        questions = ("Is the guide working?", "Check and fix setup.")
        for rel in ("README.md", "START-HERE.md", "FACILITATOR-RUN-THROUGH.md"):
            text = (ROOT / rel).read_text()
            self.assertIn("Friday", text, rel)
            self.assertIn("October 9", text, rel)
            for question in questions:
                self.assertIn(question, text, rel)
                self.assertIn(len(question.split()), (4, 5))
            self.assertNotIn("Show me the exact Lab 2 setup readback prompt", text)
            self.assertNotIn("From the participant page's Lab 2 card, save these", text)
        skill = (SKILL / "SKILL.md").read_text()
        for phrase in (*questions, "Is my workspace ready?"):
            self.assertIn(phrase, skill)

    def test_workspace_helper_checks_then_repairs_missing_only(self):
        helper = SKILL / "scripts/prepare_workspace.py"
        self.assertTrue(helper.is_file(), "real packaged workspace helper is required")
        with tempfile.TemporaryDirectory() as tmp:
            workspace = Path(tmp) / "AI-Labs"
            (workspace / "Kits").mkdir(parents=True)
            (workspace / "Outputs").mkdir()
            agents = workspace / "AGENTS.md"
            agents.write_text("# Our rules\n- Use only approved sources.\n- Keep private details out.\n- Ask before changing existing files.\n")
            draft = workspace / "Outputs/existing-draft.md"
            draft.write_text("An existing draft that must remain exactly as saved.\n")
            existing_kit = workspace / "Kits/KIT-Lab2-Writing-Org-Brain.md"
            existing_kit.write_text("Existing participant kit: preserve this exact copy.\n")
            existing_log = workspace / "Outputs/ship-log.md"
            existing_log.write_text("# Ship log\nKeep this existing log exactly.\n")
            before = {p.relative_to(workspace).as_posix(): p.read_bytes()
                      for p in workspace.rglob("*") if p.is_file()}
            cmd = [sys.executable, str(helper), "--workspace", str(workspace)]
            check = subprocess.run(cmd, capture_output=True, text=True)
            # A missing setup may return nonzero; the read-only check must run
            # and report the condition rather than silently prepare anything.
            self.assertTrue(check.stdout.strip(), check.stderr)
            report = json.loads(check.stdout)
            self.assertFalse(report["lab_files_ready"])
            self.assertIn("readback", report["instructions"])
            self.assertEqual(before, {p.relative_to(workspace).as_posix(): p.read_bytes()
                                      for p in workspace.rglob("*") if p.is_file()})
            repair = subprocess.run(cmd + ["--prepare"], capture_output=True, text=True)
            self.assertEqual(repair.returncode, 0, repair.stdout + repair.stderr)
            self.assertTrue(json.loads(repair.stdout)["lab_files_ready"])
            for rel, content in before.items():
                self.assertEqual((workspace / rel).read_bytes(), content, rel)
            for name in ("Kits", "Working", "Recipes", "Outputs", "Org-Brain"):
                self.assertTrue((workspace / name).is_dir(), name)
            for name in ("KIT-Lab1-First-Safe-Win.md", "KIT-Lab2-Writing-Org-Brain.md",
                         "MOCK-Program-Update-Email-Thread.txt", "MOCK-OrgBrain-Starter-Pack.md",
                         "STARTER-AGENTS.md"):
                self.assertTrue((workspace / "Kits" / name).is_file(), name)
            after = {p.relative_to(workspace).as_posix(): p.read_bytes()
                     for p in workspace.rglob("*") if p.is_file()}
            rerun = subprocess.run(cmd + ["--prepare"], capture_output=True, text=True)
            self.assertEqual(rerun.returncode, 0, rerun.stdout + rerun.stderr)
            self.assertEqual(after, {p.relative_to(workspace).as_posix(): p.read_bytes()
                                     for p in workspace.rglob("*") if p.is_file()})
            wrong = Path(tmp) / "Not-AI-Labs"
            wrong.mkdir()
            reject = subprocess.run([sys.executable, str(helper), "--workspace", str(wrong), "--prepare"],
                                    capture_output=True, text=True)
            self.assertNotEqual(reject.returncode, 0)
            self.assertEqual(list(wrong.iterdir()), [])

    def test_workspace_helper_does_not_fabricate_missing_profile(self):
        helper = SKILL / "scripts/prepare_workspace.py"
        self.assertTrue(helper.is_file())
        with tempfile.TemporaryDirectory() as tmp:
            workspace = Path(tmp) / "AI-Labs"
            workspace.mkdir()
            prepare = subprocess.run([sys.executable, str(helper), "--workspace", str(workspace), "--prepare"],
                                     capture_output=True, text=True)
            self.assertEqual(prepare.returncode, 0, prepare.stdout + prepare.stderr)
            self.assertEqual(json.loads(prepare.stdout)["instructions"], "missing")
            self.assertFalse((workspace / "AGENTS.md").exists(), "a starter must not impersonate the participant's profile")
            self.assertTrue((workspace / "Kits/STARTER-AGENTS.md").is_file())

    def test_bundled_workspace_assets_match_published_sources(self):
        manifest = json.loads((SKILL / "assets/manifest.json").read_text())
        destinations = [item["destination"] for item in manifest["files"]]
        self.assertEqual(len(destinations), len(set(destinations)))
        for item in manifest["files"]:
            asset = SKILL / item["asset"]
            data = asset.read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(), item["sha256"])
            destination = Path(item["destination"])
            self.assertFalse(destination.is_absolute())
            self.assertNotIn("..", destination.parts)
            self.assertTrue(destination.parts[0] == "Kits" or destination.as_posix() == "Outputs/ship-log.md",
                            f"unapproved preparation target: {destination}")
            if SOURCE:
                source_path = Path(item["source"])
                self.assertFalse(source_path.is_absolute())
                self.assertNotIn("..", source_path.parts)
                self.assertEqual(source_path.parts[0], "04-Participant Kits")
                self.assertEqual(data, (SOURCE / source_path).read_bytes(),
                                 f"bundled {destination.name} changed from published source")
        with tempfile.TemporaryDirectory() as tmp:
            copied = Path(tmp) / "skill"
            shutil.copytree(SKILL, copied)
            injected = json.loads((copied / "assets/manifest.json").read_text())
            injected["files"][0]["destination"] = "Outputs/unapproved-file.md"
            (copied / "assets/manifest.json").write_text(json.dumps(injected))
            workspace = Path(tmp) / "AI-Labs"
            workspace.mkdir()
            rejected = subprocess.run([sys.executable, str(copied / "scripts/prepare_workspace.py"),
                                       "--workspace", str(workspace), "--prepare"], capture_output=True, text=True)
            self.assertNotEqual(rejected.returncode, 0, "helper accepted an unapproved Outputs destination")
            self.assertEqual(list(workspace.iterdir()), [], "invalid manifest caused partial workspace writes")

    def test_practical_help_ships_with_clear_authored_provenance(self):
        page = (SKILL / "pages/hub-practical-help.md").read_text()
        authored = (ROOT / "build/working-with-claude.md").read_text().rstrip()
        self.assertIn("Practical help authored for the Lab Guide; not a mirrored participant kit", page)
        self.assertEqual(page.split("-->\n\n", 1)[1].rstrip(), authored)
        self.assertIn("pages/hub-practical-help.md", (SKILL / "SKILL.md").read_text())
        scenarios = json.loads((ROOT / "tests/practical-scenarios.json").read_text())
        self.assertEqual({s["id"] for s in scenarios}, {f"P{n}" for n in range(1, 11)})
        for scenario in scenarios:
            self.assertGreaterEqual(len(scenario["acceptance"]), 3)
            for source in scenario["sources"]:
                self.assertTrue((SKILL / "pages" / source).is_file(), source)

    def test_every_zip_member_matches_plugin_bytes(self):
        expected = {"lab-guide/" + p.relative_to(SKILL).as_posix(): p.read_bytes()
                    for p in SKILL.rglob("*") if p.is_file() and not p.name.startswith(".")
                    and "__pycache__" not in p.parts and p.suffix != ".pyc"}
        with zipfile.ZipFile(ROOT / "download/lab-guide.zip") as z:
            self.assertEqual(sorted(z.namelist()), sorted(expected))
            self.assertEqual(len(z.namelist()), len(set(z.namelist())))
            for member, data in expected.items():
                self.assertEqual(z.read(member), data, member)
                self.assertEqual(z.getinfo(member).date_time, (2026, 1, 1, 0, 0, 0))

    def test_writing_skills_are_complete_pinned_and_available_in_every_route(self):
        provenance = json.loads((ROOT / "build/writing-skills/provenance.json").read_text())
        self.assertEqual(provenance["plugin_version"], "1.6.1")
        self.assertEqual({item["name"] for item in provenance["skills"]},
                         {"ai-syntax-avoidance", "ai-syntax-avoidance-extended"})
        bundle = (ROOT / "download/lab-guide-chat.md").read_text()
        for item in provenance["skills"]:
            name = item["name"]
            source = (ROOT / "build/writing-skills" / name / "SKILL.md").read_bytes()
            self.assertEqual(hashlib.sha256(source).hexdigest(), item["sha256"])
            for path in (SKILL.parent / name / "SKILL.md",
                         SKILL / "assets/writing-skills" / name / "SKILL.md",
                         ROOT / "download" / f"{name}.md"):
                self.assertEqual(path.read_bytes(), source, str(path))
            with zipfile.ZipFile(ROOT / "download" / f"{name}.zip") as z:
                self.assertEqual(z.namelist(), [f"{name}/SKILL.md"])
                self.assertEqual(z.read(f"{name}/SKILL.md"), source)
            rel = f"assets/writing-skills/{name}/SKILL.md"
            start = f"<!-- BEGIN ASSET {rel} -->\n"
            end = f"\n<!-- END ASSET {rel} -->"
            self.assertEqual(bundle.count(start), 1)
            self.assertEqual(bundle.split(start, 1)[1].split(end, 1)[0], source.decode().rstrip())

    def test_version_and_marketplace_resolution(self):
        version = (ROOT / "build/VERSION").read_text().strip()
        plugin = json.loads((ROOT / "plugins/wf-lab-guide/.claude-plugin/plugin.json").read_text())
        self.assertEqual(plugin["version"], version)
        market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        self.assertEqual(len(market["plugins"]), 1)
        entry = market["plugins"][0]
        self.assertEqual((ROOT / entry["source"]).resolve(), SKILL.parents[1].resolve())
        self.assertEqual(entry["name"], plugin["name"])
        for rel in ("README.md", "download/copy-prompt.md", "download/lab-guide-chat.md",
                    "plugins/wf-lab-guide/skills/lab-guide/SKILL.md"):
            self.assertIn(f"Lab Guide {version} ·", (ROOT / rel).read_text(), rel)
        for p in SKILL.rglob("*.md"):
            self.assertNotIn("{{", p.read_text(), str(p))

    def test_chat_attachment_contains_every_complete_source(self):
        bundle = (ROOT / "download/lab-guide-chat.md").read_text()
        names = re.findall(r"<!-- BEGIN SOURCE pages/([^ ]+) -->", bundle)
        expected = sorted(p.name for p in (SKILL / "pages").glob("*.md"))
        self.assertEqual(names, expected)
        for name in expected:
            start = f"<!-- BEGIN SOURCE pages/{name} -->\n"
            end = f"\n<!-- END SOURCE pages/{name} -->"
            content = bundle.split(start, 1)[1].split(end, 1)[0]
            self.assertEqual(content, (SKILL / "pages" / name).read_text().rstrip(), name)
        guide = re.sub(r"^---\n.*?\n---\n", "", (SKILL / "SKILL.md").read_text(), count=1, flags=re.S).lstrip()
        self.assertIn(guide.rstrip(), bundle)
        self.assertIn("matching Embedded source page", bundle)
        start = "<!-- BEGIN ASSET assets/MOCK-OrgBrain-Starter-Pack.md -->\n"
        end = "\n<!-- END ASSET assets/MOCK-OrgBrain-Starter-Pack.md -->"
        self.assertEqual(bundle.count(start), 1)
        practice = bundle.split(start, 1)[1].split(end, 1)[0]
        self.assertEqual(practice, (SKILL / "assets/MOCK-OrgBrain-Starter-Pack.md").read_text().rstrip())

    def test_kit_prompts_match_published_source_word_for_word(self):
        if SOURCE is None:
            self.skipTest("--source required for published prompt parity")
        checked = 0
        for n in range(1, 8):
            hits = list((SOURCE / f"04-Participant Kits/Lab {n}").glob(f"KIT-Lab{n}-*.md"))
            self.assertEqual(len(hits), 1)
            source = blocks(hits[0].read_text())
            shipped = blocks((SKILL / "pages" / f"lab-{n}.md").read_text())
            self.assertTrue(source, f"Lab {n} has no prompt blocks")
            self.assertEqual(shipped, source, f"Lab {n} prompt changed during mirroring")
            checked += len(source)
        self.assertGreaterEqual(checked, 30, "unexpectedly few kit prompts were checked")

    def test_setup_copy_prompts_match_live_html(self):
        if SOURCE is None:
            self.skipTest("--source required for participant setup prompt parity")
        cfg = json.loads((CONFIG / "sources.json").read_text()) if CONFIG else {}
        path = SOURCE / cfg.get("hub_file", "RWI-WellsFargo-Participant-Hub-08-11-2026.html")
        source = path.read_text()
        match = re.search(r'<section id="start"(?=\s|>).*?</section>', source, re.S)
        self.assertIsNotNone(match)
        parser = CopyPrompts()
        parser.feed(match.group())
        shipped = blocks((SKILL / "pages/hub-start.md").read_text())
        self.assertEqual(len(parser.prompts), 3)
        self.assertEqual([p.strip() for p in shipped], [p.strip() for p in parser.prompts])

    def test_participant_recovery_and_privacy_source_coverage(self):
        kit = (SKILL / "pages/lab-1.md").read_text()
        start = (SKILL / "pages/hub-start.md").read_text()
        account = (SKILL / "pages/hub-account-privacy.md").read_text()
        # Fixed participant cases: missing setup, failed folder access, stale
        # profile, no Projects, and sensitive writing must have usable routes.
        for expected in ("Not yet:", "prompt 1", "prompt 2", "Ready for Lab 1"):
            self.assertIn(expected, start)
        self.assertIn("Documents", start)
        self.assertIn("browser", start)
        for expected in ("delete the old `AGENTS.md`", "upload the fixed one",
                         "Start a new chat for each step instead", "Check before sending"):
            self.assertIn(expected, kit)
        for expected in ("Clients, donors, volunteers", "health or case details"):
            self.assertIn(expected, account)
        self.assertIn("your organization's own policy comes first", (SKILL / "SKILL.md").read_text())
        self.assertIn("Staff names in your everyday writing are fine", account)

    def test_missing_privacy_config_stops_before_output_mutation(self):
        before = artifact_hashes()
        with tempfile.TemporaryDirectory() as tmp:
            proc = subprocess.run([sys.executable, str(ROOT / "build/build_guide.py"),
                                   "--config-dir", tmp, "--bump"], capture_output=True, text=True)
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("release settings are missing", proc.stderr)
        self.assertEqual(before, artifact_hashes())

    def test_safety_gate_rejects_stale_zip_page_and_chat_attachment(self):
        if CONFIG is None:
            self.skipTest("--config-dir required to exercise the actual safety gate")
        with tempfile.TemporaryDirectory() as tmp:
            copied = Path(tmp) / "guide"
            shutil.copytree(ROOT, copied, ignore=shutil.ignore_patterns(".git", ".source", "__pycache__"))
            archive = copied / "download/lab-guide.zip"
            with zipfile.ZipFile(archive) as z:
                members = [(i, z.read(i.filename)) for i in z.infolist()]
            with zipfile.ZipFile(archive, "w") as z:
                for info, data in members:
                    z.writestr(info, data + b"\nStale copied source.\n" if info.filename.endswith("pages/lab-2.md") else data)
            bundle = copied / "download/lab-guide-chat.md"
            bundle.write_text(bundle.read_text().replace("<!-- BEGIN SOURCE pages/lab-2.md -->\n",
                                                        "<!-- BEGIN SOURCE pages/lab-2.md -->\nStale copied source.\n", 1))
            proc = subprocess.run([sys.executable, str(copied / "build/safety_check.py"),
                                   "--config-dir", str(CONFIG)], capture_output=True, text=True)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("ZIP's lab-guide/pages/lab-2.md differs", proc.stdout)
            self.assertIn("chat attachment's pages/lab-2.md differs", proc.stdout)

    def test_answer_scoring_fails_on_missing_or_wrong_answers(self):
        with tempfile.TemporaryDirectory() as tmp:
            private = Path(tmp) / "Projects/wf-lab-guide-local"
            private.mkdir(parents=True)
            questions = [{"id": "Q1", "must": [["October 5"]]},
                         {"id": "Q2", "must": [["browser"]]}]
            (private / "questions.json").write_text(json.dumps(questions))
            version = (ROOT / "build/VERSION").read_text().strip()
            results = Path(tmp) / "results.json"
            results.write_text(json.dumps([{"id": "Q1", "answer": f"Lab Guide {version} · October 5"}]))
            cmd = [sys.executable, str(ROOT / "tests/score.py"), str(results)]
            env = dict(os.environ, HOME=tmp)
            missing = subprocess.run(cmd, env=env, capture_output=True, text=True)
            self.assertEqual(missing.returncode, 1)
            self.assertIn("1/2 pass", missing.stdout)
            selected = subprocess.run(cmd + ["--only", "Q1"], env=env, capture_output=True, text=True)
            self.assertEqual(selected.returncode, 0)
            results.write_text(json.dumps([{"id": "Q1", "answer": f"Lab Guide {version} · Wrong date"}]))
            wrong = subprocess.run(cmd + ["--only", "Q1"], env=env, capture_output=True, text=True)
            self.assertEqual(wrong.returncode, 1)
            self.assertIn("missing 'October 5'", wrong.stdout)

    def test_full_build_is_byte_reproducible(self):
        if not REBUILD:
            self.skipTest("pass --rebuild with explicit source and privacy settings")
        self.assertIsNotNone(SOURCE)
        self.assertIsNotNone(CONFIG)
        manifest = ROOT / "build/last-build.json"
        build_date = (json.loads(manifest.read_text())["built"] if manifest.exists()
                      else dt.date.today().isoformat())
        cmd = [sys.executable, str(ROOT / "build/build_guide.py"), "--source", str(SOURCE),
               "--config-dir", str(CONFIG), "--date", build_date]
        for i in range(2):
            proc = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            if i == 0:
                first = artifact_hashes()
            else:
                self.assertEqual(first, artifact_hashes())


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path)
    ap.add_argument("--config-dir", type=Path)
    ap.add_argument("--rebuild", action="store_true")
    args, remaining = ap.parse_known_args()
    SOURCE, CONFIG, REBUILD = args.source, args.config_dir, args.rebuild
    unittest.main(argv=[sys.argv[0]] + remaining)
