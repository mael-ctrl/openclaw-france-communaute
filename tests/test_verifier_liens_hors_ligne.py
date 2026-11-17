"""Fixtures synthétiques locales ; aucun serveur, paquet tiers ou vrai site."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / 'outils/verifier_liens_hors_ligne.py'


class OfflineLinksTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='liens-test-', dir=os.environ.get('LIENS_TEST_TMP', ROOT))
        self.addCleanup(self.tmp.cleanup)
        self.folder = Path(self.tmp.name)
        self.site = self.folder / 'site'
        self.site.mkdir()

    def page(self, name, text):
        p = self.site / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding='utf-8')
        return p

    def run_cli(self, *options, root=None):
        self.assertTrue(CLI.is_file(), 'CLI autonome absent : RED attendu avant code')
        p = subprocess.run([sys.executable, '-I', '-B', str(CLI), str(root or self.site),
                            '--canonical-host', 'example.test', *options],
                           capture_output=True, text=True, timeout=8, cwd=self.folder)
        self.assertIn(p.returncode, (0, 1), p.stderr)
        self.assertEqual(p.stderr, '')
        result = json.loads(p.stdout)
        self.assertEqual(p.returncode, 1 if result['errors'] else 0)
        self.assertEqual(result['stats']['errors'], len(result['errors']))
        self.assertEqual(result['stats']['exemptions'], len(result['exemptions']))
        return result

    def codes(self, report):
        return [e['code'] for e in report['errors']]

    def test_missing_local_asset_and_fragment_are_reported(self):
        self.page('index.html', '<h1 id="ok">Titre</h1>\n<a href="#ok">oui</a>\n'
                  '<a href="#absent">non</a>\n<img src="absent.png">')
        r = self.run_cli()
        self.assertEqual(self.codes(r), ['missing_fragment', 'missing_target'])
        self.assertEqual([e['line'] for e in r['errors']], [3, 4])
        self.assertEqual(r['stats']['html_files'], 1)
        self.assertEqual(r['stats']['references'], 3)
        self.assertEqual(r['stats']['checked'], 3)
        self.assertEqual(r, self.run_cli())

    def test_directory_indexes_and_relative_parent(self):
        self.page('index.html', '<a href="/dossier/">a</a><a href="/dossier">b</a>'
                  '<a href="dossier/index.html?q=a&amp;b=c#fin">c</a><a href="vide/">d</a>')
        self.page('dossier/index.html', '<h2 id="fin">fin</h2><a href="../">racine</a>')
        (self.site / 'vide').mkdir()
        r = self.run_cli()
        self.assertEqual(self.codes(r), ['missing_target'])
        self.assertEqual(r['errors'][0]['target'], 'vide/index.html')
        self.assertEqual(r['stats']['checked'], 5)

    def test_explicit_host_and_external_exemptions(self):
        urls = ['https://example.test/d/#ok', '//EXAMPLE.test/d/#ok',
                'http://example.test:80/d/', 'https://example.test:443/d/',
                'https://other.test/missing', '//other.test/a', 'mailto:a@example.test',
                'https://buy.stripe.com/test', 'tel:0123456', 'javascript:void(0)',
                'data:text/html,hello', 'https://example.test.evil/missing',
                'https://example.test:8443/a', 'file:///never-read.html']
        self.page('index.html', ''.join('<a href="' + u + '">x</a>' for u in urls))
        self.page('d/index.html', '<h1 id="ok">ok</h1>')
        r = self.run_cli()
        self.assertEqual(r['errors'], [])
        self.assertEqual(r['stats']['checked'], 4)
        self.assertEqual(len(r['exemptions']), 10)
        self.assertEqual({e['code'] for e in r['exemptions']}, {'external_host', 'scheme', 'external_port'})

    def test_percent_html_escape_unicode_and_plus_are_decoded_once(self):
        self.page('index.html', '<a href="caf%C3%A9%20%26%20x.html#a%26b">1</a>'
                  '<a href="caf%C3%A9%20%26%20x.html#ancien">2</a>'
                  '<a href="plus+.html#x+y">3</a><a href="%252e.html#p">4</a>'
                  '<a href="entit%C3%A9.html#a&amp;amp;b">5</a>'
                  '<a href="caf%C3%A9%20%26%20x.html#%C3%A9t%C3%A9">6</a>')
        self.page('café & x.html', '<div id="a&amp;b"></div><a name="ancien"></a><p id="été"></p>')
        self.page('plus+.html', '<p id="x+y"></p>')
        self.page('%2e.html', '<p id="p"></p>')
        self.page('entité.html', '<p id="a&amp;amp;b"></p>')
        self.assertEqual(self.run_cli()['errors'], [])

    def test_fragment_literal_then_decoded_case_sensitive(self):
        self.page('index.html', '<p id="a%20b"></p><p id="Case"></p>'
                  '<a href="#a%20b">literal</a><a href="#case">case</a>'
                  '<a href="#">empty</a><a href="#TOP">top</a>'
                  '<a href="">self</a><a href="?v=2#Case">query</a>')
        r = self.run_cli()
        self.assertEqual(self.codes(r), ['missing_fragment'])
        self.assertEqual(r['errors'][0]['fragment'], 'case')

    def test_non_html_fragments_are_explicitly_exempt_after_existence_check(self):
        self.page('index.html', '<a href="ok.pdf#page=2">pdf</a><a href="absent.pdf#x">no</a>')
        self.page('ok.pdf', 'not parsed as HTML')
        r = self.run_cli()
        self.assertEqual(self.codes(r), ['missing_target'])
        self.assertEqual([e['code'] for e in r['exemptions']], ['non_html_fragment'])

    def test_malformed_local_urls_are_errors_not_crashes(self):
        urls = ['bad%GG.html', 'bad%FF.html', 'ok.html#%zz', 'a%00.html',
                'https://[', 'https://example.test:bad/', 'https://u@example.test/',
                'a\\\\b.html', '/%5csecret', '///odd/path']
        self.page('index.html', ''.join('<a href="' + u + '">x</a>' for u in urls))
        r = self.run_cli()
        self.assertEqual(len(r['errors']), len(urls))
        self.assertTrue(set(self.codes(r)) <= {'invalid_url', 'invalid_encoding'})

    def test_canonical_host_is_required_and_is_not_a_url(self):
        self.page('index.html', '')
        for options in ([], ['--canonical-host', 'https://example.test/path'],
                        ['--canonical-host', '*.example.test'], ['--canonical-host', 'a:443']):
            p = subprocess.run([sys.executable, '-I', '-B', str(CLI), str(self.site), *options],
                               capture_output=True, timeout=8)
            self.assertEqual(p.returncode, 2)

    def test_symlink_files_directories_and_dangling_links_are_refused(self):
        outside = self.folder / 'outside'
        outside.mkdir()
        (outside / 'private.html').write_bytes(b'\xffDO-NOT-READ')
        (self.site / 'leak.html').symlink_to(outside / 'private.html')
        (self.site / 'door').symlink_to(outside, target_is_directory=True)
        (self.site / 'dangling').symlink_to(outside / 'absent')
        self.page('index.html', '<a href="leak.html#x">x</a><img src="door/private.html">'
                  '<a href="dangling">d</a><a href="door/../index.html">alias</a>')
        r = self.run_cli()
        self.assertTrue(r['errors'])
        self.assertEqual(set(self.codes(r)), {'symlink_refused'})
        self.assertEqual(r['stats']['html_files'], 1)
        self.assertNotIn('DO-NOT-READ', json.dumps(r))

    def test_internal_symlinks_are_also_refused_explicitly(self):
        self.page('index.html', '<a href="alias.html">alias</a>')
        (self.site / 'alias.html').symlink_to('index.html')
        self.assertEqual(set(self.codes(self.run_cli())), {'symlink_refused'})

    def test_plain_and_encoded_traversal_cannot_escape_root(self):
        (self.folder / 'outside.html').write_text('<p id="ok">private</p>')
        urls = ['../outside.html#ok', '%2e%2e/outside.html',
                '/a/../../outside.html', '/%2e%2e%2foutside.html']
        self.page('index.html', ''.join('<a href="' + u + '">x</a>' for u in urls))
        r = self.run_cli()
        self.assertEqual(self.codes(r), ['outside_root'] * len(urls))
        self.assertNotIn('private', json.dumps(r))

    def test_root_symlink_or_symlink_parent_is_refused(self):
        self.page('index.html', '')
        alias = self.folder / 'alias'
        alias.symlink_to(self.site, target_is_directory=True)
        for root in (alias, alias / 'nested'):
            self.assertEqual(self.codes(self.run_cli(root=root)), ['unsafe_root'])

    def test_empty_missing_and_non_directory_roots_fail_closed(self):
        self.assertEqual(self.codes(self.run_cli()), ['no_html'])
        self.assertEqual(self.codes(self.run_cli(root=self.folder / 'missing')), ['unsafe_root'])
        p = self.page('not-root.txt', 'x')
        self.assertEqual(self.codes(self.run_cli(root=p)), ['unsafe_root'])

    def test_special_file_is_never_read(self):
        os.mkfifo(self.site / 'pipe.html')
        self.page('index.html', '<a href="pipe.html">pipe</a>')
        r = self.run_cli()
        self.assertEqual(set(self.codes(r)), {'special_file'})

    def test_base_href_is_an_error_without_guessing_relative_targets(self):
        self.page('index.html', '<base href="/other/"><a href="ok.html">x</a>')
        self.page('ok.html', '')
        r = self.run_cli()
        self.assertEqual(self.codes(r), ['base_unsupported'])
        self.assertIn('base_unsupported', [e['code'] for e in r['exemptions']])

    def test_template_ids_do_not_validate_real_fragments(self):
        self.page('index.html', '<template><div id="ghost"><a href="missing.html">x</a>'
                  '<template><img src="missing.png"></template></div></template>'
                  '<a href="#ghost">ghost</a><p id="real"></p><a href="#real">ok</a>')
        r = self.run_cli()
        self.assertEqual(self.codes(r), ['missing_fragment'])
        self.assertEqual([e['code'] for e in r['exemptions']], ['inert_template', 'inert_template'])

    def test_text_fragments_explicitly_exempt_but_missing_targets_still_fail(self):
        self.page('index.html', '<a href="#:~:text=phrase">text</a>'
                  '<a href="absent.html#:~:text=phrase">missing</a>')
        r = self.run_cli()
        self.assertEqual(self.codes(r), ['missing_target'])
        self.assertEqual([e['code'] for e in r['exemptions']], ['text_fragment'])

    def test_invalid_utf8_is_not_treated_as_non_html(self):
        self.page('index.html', '<a href="bad.html#x">bad</a>')
        (self.site / 'bad.html').write_bytes(b'\xff')
        r = self.run_cli()
        self.assertIn('html_encoding', self.codes(r))
        self.assertNotIn('non_html_fragment', [e['code'] for e in r['exemptions']])

    def test_budgets_fail_closed_and_report_partial_scope(self):
        self.page('index.html', '<p id="x"></p><a href="#x">x</a><a href="#x">x</a>')
        self.page('d/a.HTML', '<p>x</p>')
        for options in (('--max-files', '1'), ('--max-bytes', '10'),
                        ('--max-page-bytes', '10'), ('--max-links', '1'), ('--max-depth', '1')):
            with self.subTest(options=options):
                r = self.run_cli(*options)
                self.assertIn('budget_exceeded', self.codes(r))
                self.assertFalse(r['complete'])

    def test_htm_uppercase_comments_scripts_and_void_markup(self):
        self.page('INDEX.HTML', '<P ID="OK">x</P><img src="x.bin"/>'
                  '<!-- <a href="bad"> --> <script>"<a href=bad>"</script>')
        self.page('other.htm', '<a href="INDEX.HTML#OK">ok</a>')
        self.page('x.bin', '')
        r = self.run_cli()
        self.assertEqual(r['errors'], [])
        self.assertEqual(r['stats']['html_files'], 2)
        self.assertEqual(r['stats']['references'], 2)
        self.assertTrue(r['complete'])
        self.assertTrue(r['limits'])

    def test_case_sensitive_files_and_no_extension_rewrite(self):
        self.page('index.html', '<a href="PAGE.html">case</a><a href="page">rewrite</a>')
        self.page('page.html', '')
        self.assertEqual(self.codes(self.run_cli()), ['missing_target', 'missing_target'])


if __name__ == '__main__':
    unittest.main()
