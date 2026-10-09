"""Exact occurrence exceptions must leave all surrounding text protected."""
import importlib.util
from pathlib import Path
import unittest
spec = importlib.util.spec_from_file_location('safety', Path(__file__).resolve().parents[1] / 'build/safety_check.py')
safety = importlib.util.module_from_spec(spec)
spec.loader.exec_module(safety)

class ExactExceptions(unittest.TestCase):
    def setUp(self):
        self.url = 'https://course.example.test/download/file.zip'
        self.rules = [dict(kind='url', value=self.url, markers=['course'], file=None),
                      dict(kind='quoted_literal', value='"GUIDE.md"', markers=['GUIDE'], file='tests/example.py')]
    def blocked(self, text, marker='course', rel='page.md'):
        return safety.has_unapproved_marker(rel, text, marker, self.rules)
    def test_exact_urls_in_markdown_html_and_text(self):
        for text in [self.url, '('+self.url+')', 'href="'+self.url+'"', '`'+self.url+'`']:
            self.assertFalse(self.blocked(text))
    def test_modified_urls_are_blocked(self):
        for value in ['abc'+self.url,self.url+'(private)',self.url+'[private]',self.url+'{private}',self.url+'?x=1',self.url+'/extra',self.url+'%2fextra',self.url+'#other',self.url.replace('example.test','example.test.evil'),self.url.replace('/download/','/internal/'),self.url.replace('file','%66ile')]:
            self.assertTrue(self.blocked(value),value)
    def test_other_occurrences_on_same_line_are_blocked(self):
        self.assertTrue(self.blocked(self.url+' course'))
        self.assertTrue(self.blocked(self.url+' secret', marker='secret'))
    def test_literal_requires_exact_file_and_quotes(self):
        self.assertFalse(self.blocked('"GUIDE.md"', 'GUIDE', 'tests/example.py'))
        for rel,text in [('other.py','"GUIDE.md"'),('tests/example.py','GUIDE.md'),('tests/example.py','"GUIDE.md" GUIDE')]:
            self.assertTrue(self.blocked(text,'GUIDE',rel))
    def test_no_policy_means_no_exception(self):
        self.assertTrue(safety.has_unapproved_marker('page.md', self.url, 'course', []))

if __name__ == '__main__': unittest.main(verbosity=2)
