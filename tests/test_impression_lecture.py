"""Contrat borné de la CSS print, complété par print_qa.cjs/Chromium."""
from pathlib import Path
import re
import unittest

class ImpressionLectureTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.css=(Path(__file__).resolve().parents[1]/'assets/style.css').read_text()
    def rules(self):
        marker='/* Impression éditoriale seulement : le manifeste partage section-lecture. */'
        self.assertEqual(self.css.count(marker),1)
        return self.css.split(marker)[1]
    def test_seulement_media_print_et_garde_article(self):
        rules=self.rules()
        self.assertTrue(rules.strip().startswith('@media print {'))
        self.assertEqual(rules.count('@media'),1)
        self.assertIn('body:has(> main > .section-lecture article.lecture)',rules)
        self.assertNotRegex(rules,r'(?m)^\s*(?:html|body|\*|nav|header|footer)\s*\{')
    def test_pas_de_pages_forcees_ni_zone_coupee(self):
        rules=self.rules()
        self.assertNotRegex(rules,r'@page|counter\(|(?:break-before|break-after)\s*:\s*(?:page|always|left|right)|overflow\s*:\s*(?:hidden|clip)|max-height|line-clamp|visibility\s*:\s*hidden')
    def test_sources_non_masquees_adresses_imprimees(self):
        rules=self.rules()
        self.assertEqual(len(re.findall(r'display\s*:\s*none',rules)),1)
        self.assertIn('article.lecture > .sommaire-article',rules)
        self.assertIn('content: " — " attr(href);',rules)
        self.assertIn('.source-boite .bouton {\n    display: inline;',rules)
        self.assertIn('overflow-wrap: anywhere;',rules)
    def test_titre_sources_reste_avec_premiere_source(self):
        self.assertIn('.section-lecture article.lecture .source-boite > p:first-child { break-after: avoid; }', self.rules())

    def test_divulgation_ia_breve_impression_seulement(self):
        rules=self.rules()
        self.assertIn('article.lecture:not(:has(.corps-article)) > .signature::before',rules)
        self.assertIn('content: "Le Crabe — IA rédactrice. ";',rules)

if __name__=='__main__':unittest.main()
