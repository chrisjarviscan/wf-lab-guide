"""Every lab starts from the same short page: three routes, two phrases, and a
kit section that tells the guide how to run the session. Checks the guide's
side always, and the published kits and pages when --source is given."""
import argparse
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "plugins/wf-lab-guide/skills/lab-guide"
SOURCE = None


def github_files():
    """{lab: [files]} from the table in the guide template."""
    text = (ROOT / "build/SKILL.template.md").read_text()
    table = text.split("| Lab | Files selected for the GitHub-connected Project |", 1)[1].split("\n\n", 1)[0]
    return {int(m[1]): re.findall(r"`([^`]+)`", m[2]) for m in re.finditer(r"^\| (\d) \| (.+) \|$", table, re.M)}


class AllLabs(unittest.TestCase):
    def test_guide_runs_every_lab_and_never_carries_a_key(self):
        guide = (ROOT / "build/SKILL.template.md").read_text()
        builder = (ROOT / "build/build_guide.py").read_text()
        for text in ("## Every lab starts the same way", "Check my Lab N access", "I'm ready to begin Lab N",
                     "Continue Lab N", "by hand", "The guide never contains a placeholder key"):
            self.assertIn(text, guide)
        files = github_files()
        self.assertEqual(sorted(files), list(range(1, 8)))
        for n, names in files.items():
            self.assertEqual(names[:2], ["SKILL.md", f"pages/lab-{n}.md"])
            for name in names[2:]:
                self.assertTrue(name.startswith("assets/"), name)
                self.assertIn('"' + name.split("/", 1)[1] + '":', builder, f"Lab {n}: {name} is not bundled")
                self.assertNotIn("key", name.lower())
        manifest = SKILL / "assets/manifest.json"
        if manifest.is_file():
            for item in json.loads(manifest.read_text())["files"]:
                self.assertNotIn("key", item["asset"].lower(), "a placeholder key must never ship")

    def test_built_pages_carry_each_runbook(self):
        for n in range(1, 8):
            page = SKILL / "pages" / f"lab-{n}.md"
            if not page.is_file():
                self.skipTest("guide not built")
            text = page.read_text()
            self.assertIn("## Start here", text, n)
            self.assertIn(f"Check my Lab {n} access.", text, n)
            self.assertIn(f"I'm ready to begin Lab {n}.", text, n)
            self.assertRegex(text, r"(?m)^## How Claude runs (Lab %d|these steps)$" % n)

    def test_published_kits_and_pages_agree_with_the_guide(self):
        if SOURCE is None:
            self.skipTest("--source required")
        files = github_files()
        for n in range(1, 8):
            folder = SOURCE / f"04-Participant Kits/Lab {n}"
            kit = next(folder.glob(f"KIT-Lab{n}-*.md"))
            text = kit.read_text()
            self.assertIn("## Start here", text, n)
            self.assertRegex(text, r"(?m)^## How Claude runs (Lab %d|these steps)$" % n)
            start = text.split("## Start here", 1)[1].split("\n## ", 1)[0]
            page = (folder / (kit.stem + ".html")).read_text()
            self.assertTrue((folder / (kit.stem + "-worksheet.html")).is_file(), n)
            for phrase in (f"Check my Lab {n} access.", f"I'm ready to begin Lab {n}."):
                self.assertIn(phrase, start, n)
                self.assertIn(f'data-copy="{phrase}"', page, n)
            self.assertEqual(re.findall(r"<li><code>([^<]+)</code></li>", page), files[n], f"Lab {n} page file list")
            github_line = next(line for line in start.splitlines() if "Add from GitHub" in line)
            listed = re.findall(r"`([^`]+)`", github_line.split("lab-guide/`:", 1)[1])
            self.assertEqual(listed, files[n], f"Lab {n} kit file list")
            self.assertNotIn("Placeholder-Key", " ".join(files[n]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path)
    args, remaining = parser.parse_known_args()
    SOURCE = args.source
    unittest.main(argv=[__file__] + remaining)
