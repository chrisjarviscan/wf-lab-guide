"""Check the primary participant routes, while preserving earlier-lab access."""
import argparse
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = None
# Until the official bumped release is generated, packaged 1.0.40 still opens Lab 4.
GENERATED_LAB = 4 if (ROOT / "build/VERSION").read_text().strip() == "1.0.40" else 5


def primary_text(text):
    return text.split('## Returning to an earlier lab?')[0]


class Lab3Entrypoints(unittest.TestCase):
    def test_both_screen_routes_start_current_lab(self):
        for name in ('README.md', 'START-HERE.md', 'build/README.template.md'):
            # Generated 1.0.40 remains Lab 4 until the official release build.
            lab = 5 if name == 'build/README.template.md' else GENERATED_LAB
            text = primary_text((ROOT / name).read_text())
            for heading in ("### I'm using Claude in my browser", "### I'm using the Claude desktop app"):
                route = text.split(heading, 1)[1].split('\n##', 1)[0]
                self.assertIn(f'Check my Lab {lab} access.', route, name)
                self.assertIn(f'ready to begin Lab {lab}', route, name)
                self.assertNotIn('ready to begin Lab 3', route, name)

    def test_start_here_matches_readme_and_keeps_earlier_route(self):
        readme = (ROOT / 'README.md').read_text()
        self.assertEqual(readme, (ROOT / 'START-HERE.md').read_text())
        earlier = readme.split('## Returning to an earlier lab?')[1]
        self.assertIn('ready to begin Lab 2', earlier)
        self.assertIn('ready to begin Lab 3', earlier)
        self.assertIn('October 19' if GENERATED_LAB == 4 else 'October 26', primary_text(readme))
        self.assertIn('October 23' if GENERATED_LAB == 4 else 'October 30', primary_text(readme))
        self.assertIn(f'pages/lab-{GENERATED_LAB}.md', readme)
        if GENERATED_LAB == 5:
            self.assertIn('ready to begin Lab 4', earlier)

    def test_hub_primary_cta_and_start_panel(self):
        if SOURCE is None:
            self.skipTest('--source required for hub entrypoint checks')
        hub = (SOURCE / 'RWI-WellsFargo-Participant-Hub-08-11-2026.html').read_text()
        cta = re.search(r'<a class="hero-start" href="([^"]+)">([^<]+)</a>', hub)
        self.assertIsNotNone(cta)
        # The participant page and installation template lead with Lab 5.
        self.assertIn('Lab%205/KIT-Lab5-', cta[1])
        self.assertEqual(cta[2], 'Start Lab 5: numbers to narrative to deck')
        hero = hub.split('<div class="controls">')[0]
        self.assertIn('Check my Lab 5 access.', hero)
        self.assertIn('ready to begin Lab 5', hero)
        self.assertNotIn('ready to begin Lab 3', hero)
        self.assertIn("If your guide is missing or out of date", hero)
        self.assertIn('KIT-Lab2-Writing-Org-Brain.html', hub)

    def test_install_template_primary_mode_and_earlier_route(self):
        if SOURCE is None:
            self.skipTest('--source required for hub entrypoint checks')
        page = (SOURCE / 'tools/lab-guide-page.template.html').read_text()
        primary = page.split('<details><summary>Return to Lab 4, Lab 3, Lab 2 or an earlier lab</summary>')[0]
        self.assertIn('Check my Lab 5 access.', primary)
        self.assertIn('ready to begin Lab 5', primary)
        self.assertNotIn('ready to begin Lab 3', primary.split('var script=')[0])
        self.assertIn('October 26', primary)
        self.assertIn('October 30', primary)
        self.assertIn('data-copy="Check my Lab 5 access."', primary)
        earlier = page[len(primary):]
        self.assertIn('ready to begin Lab 3', earlier)
        self.assertIn('ready to begin Lab 2', earlier)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', required=True, type=Path)
    args, remaining = parser.parse_known_args()
    SOURCE = args.source
    unittest.main(argv=[__file__] + remaining)
