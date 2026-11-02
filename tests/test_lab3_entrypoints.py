"""Check the primary participant routes, while preserving earlier-lab access."""
import argparse
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = None
# The official Lab 6 release starts Lab 6; earlier labs stay available.
GENERATED_LAB = 6


def primary_text(text):
    return text.split('## Returning to an earlier lab?')[0]


class Lab3Entrypoints(unittest.TestCase):
    def test_lab6_download_route_and_generic_selector_are_explicit(self):
        for name in ('build/SKILL.template.md', 'plugins/wf-lab-guide/skills/lab-guide/SKILL.md'):
            section = (ROOT / name).read_text().split('Classic Claude may show', 1)[1]
            self.assertIn('pages/lab-6.md', section)
            self.assertNotIn('uploading it again replaces', section)
        for name in ('plugins/wf-lab-guide/skills/lab-guide/pages/lab-6.md',
                     'plugins/wf-lab-guide/skills/lab-guide/SKILL.md', 'download/lab-guide-chat.md'):
            text = (ROOT / name).read_text()
            self.assertIn('not bundled in this guide', text)
            self.assertIn('https://wf-ai-labs.rw.institute/lab-guide/', text)
            self.assertIn('Download fictional practice ZIP', text)
            self.assertIn('Do not invent local assets', text)

    def test_both_screen_routes_start_current_lab(self):
        for name in ('README.md', 'START-HERE.md', 'build/README.template.md'):
            # Canonical templates and generated pages agree after the official build.
            lab = 6 if name == 'build/README.template.md' else GENERATED_LAB
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
        self.assertIn('November 2', primary_text(readme))
        self.assertIn('November 6', primary_text(readme))
        self.assertIn(f'pages/lab-{GENERATED_LAB}.md', readme)
        if GENERATED_LAB == 6:
            self.assertIn('ready to begin Lab 4', earlier)

    def test_hub_primary_cta_and_start_panel(self):
        if SOURCE is None:
            self.skipTest('--source required for hub entrypoint checks')
        hub = (SOURCE / 'RWI-WellsFargo-Participant-Hub-08-11-2026.html').read_text()
        cta = re.search(r'<a class="hero-start" href="([^"]+)">([^<]+)</a>', hub)
        self.assertIsNotNone(cta)
        # The participant page and installation template lead with Lab 6.
        self.assertIn('Lab%206/KIT-Lab6-', cta[1])
        self.assertEqual(cta[2], 'Start Lab 6: a reusable reviewer and checked research')
        hero = hub.split('<div class="controls">')[0]
        self.assertIn('Check my Lab 6 access.', hero)
        self.assertIn('ready to begin Lab 6', hero)
        self.assertNotIn('ready to begin Lab 3', hero)
        self.assertIn("If your guide is missing or out of date", hero)
        self.assertIn('KIT-Lab2-Writing-Org-Brain.html', hub)

    def test_install_template_primary_mode_and_earlier_route(self):
        if SOURCE is None:
            self.skipTest('--source required for hub entrypoint checks')
        page = (SOURCE / 'tools/lab-guide-page.template.html').read_text()
        primary = page.split('<details><summary>Return to Lab 5, Lab 4, Lab 3, Lab 2 or an earlier lab</summary>')[0]
        self.assertIn('Check my Lab 6 access.', primary)
        self.assertIn('ready to begin Lab 6', primary)
        self.assertNotIn('ready to begin Lab 3', primary.split('var script=')[0])
        self.assertIn('November 2', primary)
        self.assertIn('November 6', primary)
        self.assertIn('data-copy="Check my Lab 6 access."', primary)
        earlier = page[len(primary):]
        self.assertIn('ready to begin Lab 3', earlier)
        self.assertIn('ready to begin Lab 2', earlier)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', required=True, type=Path)
    args, remaining = parser.parse_known_args()
    SOURCE = args.source
    unittest.main(argv=[__file__] + remaining)
