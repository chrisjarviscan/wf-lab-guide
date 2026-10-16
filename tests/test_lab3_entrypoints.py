"""Check the primary participant routes, while preserving earlier-lab access."""
import argparse
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = None


def primary_text(text):
    return text.split('## Returning to an earlier lab?')[0]


class Lab3Entrypoints(unittest.TestCase):
    def test_both_screen_routes_start_lab3(self):
        for name in ('README.md', 'START-HERE.md', 'build/README.template.md'):
            text = primary_text((ROOT / name).read_text())
            for heading in ("### I'm using Claude in my browser", "### I'm using the Claude desktop app"):
                route = text.split(heading, 1)[1].split('\n##', 1)[0]
                self.assertIn('Check my Lab 3 access.', route, name)
                self.assertIn('ready to begin Lab 3', route, name)
                self.assertNotIn('ready to begin Lab 2', route, name)

    def test_start_here_matches_readme_and_keeps_earlier_route(self):
        readme = (ROOT / 'README.md').read_text()
        self.assertEqual(readme, (ROOT / 'START-HERE.md').read_text())
        self.assertIn('ready to begin Lab 2', readme.split('## Returning to an earlier lab?')[1])
        self.assertIn('October 12', primary_text(readme))
        self.assertIn('October 16', primary_text(readme))
        self.assertIn('pages/lab-3.md', readme)

    def test_hub_primary_cta_and_start_panel(self):
        if SOURCE is None:
            self.skipTest('--source required for hub entrypoint checks')
        hub = (SOURCE / 'RWI-WellsFargo-Participant-Hub-08-11-2026.html').read_text()
        cta = re.search(r'<a class="hero-start" href="([^"]+)">([^<]+)</a>', hub)
        self.assertIsNotNone(cta)
        self.assertIn('Lab%203/KIT-Lab3-', cta[1])
        self.assertEqual(cta[2], 'Today’s win: Lab 3 worksheet')
        hero = hub.split('<div class="controls">')[0]
        self.assertIn('Check my Lab 3 access.', hero)
        self.assertIn('ready to begin Lab 3', hero)
        self.assertNotIn('ready to begin Lab 2', hero)
        self.assertIn('If your guide does not recognize Lab 3', hero)
        self.assertIn('KIT-Lab2-Writing-Org-Brain.html', hub)

    def test_install_template_primary_mode_and_earlier_route(self):
        if SOURCE is None:
            self.skipTest('--source required for hub entrypoint checks')
        page = (SOURCE / 'tools/lab-guide-page.template.html').read_text()
        primary = page.split('<details><summary>Return to Lab 2 or an earlier lab</summary>')[0]
        self.assertIn('Check my Lab 3 access.', primary)
        self.assertIn('ready to begin Lab 3', primary)
        self.assertNotIn('ready to begin Lab 2', primary)
        self.assertIn('October 12', primary)
        self.assertIn('October 16', primary)
        self.assertIn('data-copy="Check my Lab 3 access."', primary)
        self.assertIn('ready to begin Lab 2', page[len(primary):])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', required=True, type=Path)
    args, remaining = parser.parse_known_args()
    SOURCE = args.source
    unittest.main(argv=[__file__] + remaining)
