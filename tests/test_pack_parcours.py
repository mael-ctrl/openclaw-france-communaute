"""Deux raccourcis natifs, sans nouveau paiement ni script."""
import re
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'engine'))
import annexes


class Liens(HTMLParser):
    def __init__(self):
        super().__init__()
        self.liens = []
        self.ids = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'a':
            self.liens.append(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])


class ParcoursPackTest(unittest.TestCase):
    def test_pas_de_raccourci_gratuit_si_extraits_indisponibles(self):
        with patch.object(annexes, 'extraits_pack', return_value=''):
            page = annexes.page_pack()
        self.assertNotIn('href="#extraits-pack"', page)
        self.assertIn('href="#prix-pack"', page)
        self.assertIn('Acheter le pack — 14 €', page)

    def test_raccourcis_avant_contenu_vers_extraits_et_prix_reels(self):
        page = annexes.page_pack()
        match = re.search(r'<nav class="hero-actions" aria-label="Parcours du pack">.*?</nav>', page, re.S)
        self.assertIsNotNone(match, 'Un choix gratuit/prix doit précéder la liste des livrables')
        bloc = match.group()
        parser = Liens()
        parser.feed(bloc)
        self.assertEqual([a['href'] for a in parser.liens], ['#extraits-pack', '#prix-pack'])
        self.assertIn('Essayer 3 prompts gratuits', bloc)
        self.assertIn('Voir le prix — 14 €', bloc)
        self.assertLess(page.index(bloc), page.index('<h2>Ce que tu reçois</h2>'))
        document = Liens()
        document.feed(page)
        for a in parser.liens:
            self.assertEqual(document.ids.count(a['href'][1:]), 1)
            self.assertNotIn('onclick', a)
            self.assertNotIn('target', a)
        self.assertIn('<h2 id="prix-pack">Combien</h2>', page)
        self.assertNotIn('<script', bloc)
        self.assertNotIn('<form', bloc)
        self.assertNotIn('stripe', bloc)
        self.assertEqual(page.count('href="https://buy.stripe.com/9B628s2cE6IL09P8421ck0n"'), 1)
        self.assertEqual(page.count('class="extrait-pack"'), 3)
        self.assertNotIn('href="/dl/', page)


if __name__ == '__main__':
    unittest.main()
