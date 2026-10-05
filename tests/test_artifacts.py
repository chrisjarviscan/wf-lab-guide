#!/usr/bin/env python3
"""Check shipped artifacts and prompt fidelity without a Claude login.

python3 tests/test_artifacts.py --source /path/to/published/hub
python3 tests/test_artifacts.py --source /path/to/published/hub --config-dir /external/settings --rebuild

These checks validate packaging and source fidelity, not Claude's live answers.
"""
import argparse
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
    paths = list(SKILL.rglob("*.md")) + list((ROOT / "download").glob("*"))
    paths += [ROOT / "README.md", ROOT / "plugins/wf-lab-guide/.claude-plugin/plugin.json"]
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(paths) if p.is_file()}


class Artifacts(unittest.TestCase):
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
                    for p in SKILL.rglob("*.md")}
        with zipfile.ZipFile(ROOT / "download/lab-guide.zip") as z:
            self.assertEqual(sorted(z.namelist()), sorted(expected))
            self.assertEqual(len(z.namelist()), len(set(z.namelist())))
            for member, data in expected.items():
                self.assertEqual(z.read(member), data, member)
                self.assertEqual(z.getinfo(member).date_time, (2026, 1, 1, 0, 0, 0))

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
        cmd = [sys.executable, str(ROOT / "build/build_guide.py"), "--source", str(SOURCE),
               "--config-dir", str(CONFIG), "--date", "2026-10-05"]
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
