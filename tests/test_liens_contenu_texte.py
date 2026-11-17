"""Les exemples de balises affichés en texte ne sont pas des liens/ancres."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

CLI = Path(__file__).resolve().parents[1] / 'outils/verifier_liens_hors_ligne.py'


class TextContentLinksTest(unittest.TestCase):
    def check(self, html):
        with tempfile.TemporaryDirectory(dir=os.environ.get('LIENS_TEST_TMP', CLI.parents[1])) as directory:
            Path(directory, 'index.html').write_text(html, encoding='utf-8')
            result = subprocess.run([sys.executable, '-I', '-B', str(CLI), directory,
                                     '--canonical-host', 'example.test'],
                                    text=True, capture_output=True, timeout=10)
        self.assertEqual(result.stderr, '')
        self.assertIn(result.returncode, (0, 1))
        return json.loads(result.stdout)

    def test_title_and_textarea_contents_are_not_markup(self):
        for tag in ('title', 'textarea'):
            with self.subTest(tag=tag):
                report = self.check(f'<{tag}><a id="ghost" href="absent">exemple</a></{tag}>'
                                    '<p id="real">réel</p><a href="#real">oui</a><a href="#ghost">non</a>')
                self.assertEqual(report['stats']['references'], 2)
                self.assertEqual([e['code'] for e in report['errors']], ['missing_fragment'])
                self.assertEqual(report['errors'][0]['fragment'], 'ghost')

    def test_solidus_does_not_close_text_or_script_elements(self):
        for tag in ('title', 'textarea', 'script', 'style'):
            with self.subTest(tag=tag):
                report = self.check(f'<{tag}/><a id="ghost" href="absent">texte</a></{tag}>'
                                    '<p id="real"></p><a href="#real">oui</a><a href="#ghost">non</a>')
                self.assertEqual(report['stats']['references'], 2)
                self.assertEqual([e['code'] for e in report['errors']], ['missing_fragment'])

    def test_solidus_does_not_make_template_content_active(self):
        report = self.check('<template/><a id="ghost" href="absent">inert</a></template>'
                            '<a href="#ghost">non</a>')
        self.assertEqual([e['code'] for e in report['errors']], ['missing_fragment'])
        self.assertEqual([e['code'] for e in report['exemptions']], ['inert_template'])


if __name__ == '__main__':
    unittest.main()
