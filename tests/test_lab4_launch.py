"""Lab 4 runs from the guide: access check, guided session, homework, and the key never ships."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'plugins/wf-lab-guide/skills/lab-guide'


class Lab4Launch(unittest.TestCase):
    def test_skill_routes_lab4_phrases(self):
        text = (SKILL / 'SKILL.md').read_text()
        for phrase in ('Check my Lab 4 access', "I'm ready to begin Lab 4", 'Start my Lab 4 homework',
                       'How Claude runs Lab 4', 'assets/KIT-Lab4-Data-Clean-Extract.md'):
            self.assertIn(phrase, text)

    def test_kit_page_carries_the_guided_session(self):
        page = (SKILL / 'pages/lab-4.md').read_text()
        self.assertIn('## Start here', page)
        self.assertIn('## How Claude runs Lab 4', page)
        self.assertNotIn('## Choose your screen for Lab 4', page)
        for phrase in ('Check my Lab 4 access.', "I'm ready to begin Lab 4.", 'Start my Lab 4 homework.',
                       'Shorter, please', '"saved"', 'never opens a file with "key"'.lower()):
            self.assertIn(phrase.lower(), page.lower())
        self.assertNotIn('—', page.split('## Start here')[1].split('## Before you come')[0])

    def test_practice_key_and_sheet_are_not_bundled(self):
        manifest = json.loads((SKILL / 'assets/manifest.json').read_text())
        names = [f['asset'] for f in manifest['files']]
        self.assertIn('assets/KIT-Lab4-Data-Clean-Extract.md', names)
        for name in names:
            self.assertNotIn('Key', name)
            self.assertNotIn('Benevity', name)
        chat = (ROOT / 'download/lab-guide-chat.md').read_text()
        self.assertNotIn('BEGIN ASSET assets/MOCK-Placeholder-Key', chat)


if __name__ == '__main__':
    unittest.main()
