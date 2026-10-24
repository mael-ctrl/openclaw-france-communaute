"""Sommaire avant achat : titres fidèles au livrable, pas le pack intégral."""
import html
import json
import re
import sys
import unittest
from collections import Counter
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))
import annexes
import config


class PackSommaireTest(unittest.TestCase):
    def livrable(self):
        return json.loads((config.DOSSIER_PRIVE / "dl" /
                           "pack-du-crabe-100-prompts.json").read_text(encoding="utf-8"))

    def test_sommaire_reel_cent_titres_classes_sans_corps_prive(self):
        source = self.livrable()
        document = annexes.page_pack()
        self.assertIn('aria-labelledby="sommaire-pack"', document)
        bloc = re.search(r'<section aria-labelledby="sommaire-pack">.*?</section>', document, re.S).group()
        self.assertIn('Voir les 100 titres, par catégorie', bloc)
        self.assertIn('seuls les trois extraits', bloc)
        self.assertIn('<details class="sommaire-pack">', bloc)
        self.assertNotIn(' open', bloc)
        groupes = re.findall(r'<details class="sommaire-pack-categorie">(.*?)</details>', bloc, re.S)
        self.assertEqual(len(groupes), 10)
        attendus = {}
        for p in sorted(source, key=lambda p: p['id']):
            attendus.setdefault(p['categorie'], []).append(p)
        for (categorie, prompts), groupe in zip(attendus.items(), groupes):
            self.assertIn(html.escape(categorie, quote=True), groupe)
            titres = re.findall(r'<li value="(\d+)">(.*?)</li>', groupe, re.S)
            self.assertEqual([(int(i), html.unescape(t)) for i,t in titres],
                             [(p['id'], p['titre']) for p in prompts])
            self.assertEqual(len(titres), 10)
        for p in source:
            self.assertNotIn(html.escape(p['prompt'], quote=True), bloc)
            self.assertNotIn(html.escape(p['exemple_usage'], quote=True), bloc)
        self.assertNotIn('/dl/', bloc)
        self.assertNotIn('<script', bloc)
        self.assertNotIn('<form', bloc)
        self.assertLess(document.index('id="extraits-pack"'), document.index('id="sommaire-pack"'))
        self.assertLess(document.index('id="sommaire-pack"'), document.index('<h2>Combien</h2>'))
        self.assertIn('Acheter le pack — 14 €', document)
        self.assertIn('https://buy.stripe.com/9B628s2cE6IL09P8421ck0n', document)

    def test_sommaire_incomplet_invalide_ou_duplique_masque_sans_casser_achat(self):
        source = self.livrable()
        variantes = [None, {}, [], source[:-1], source + [source[0]],
                     [source[0]] * 100]
        for cle, valeur in [('id', True), ('id', -1), ('titre', ''),
                            ('categorie', '  '), ('prompt', None)]:
            variante = [dict(p) for p in source]
            variante[0][cle] = valeur
            variantes.append(variante)
        variantes.append([dict(p, categorie='unique') for p in source])
        for donnees in variantes:
            with self.subTest(type=type(donnees).__name__), patch.object(
                    annexes.construction, '_lire_json', return_value=donnees):
                self.assertEqual(annexes.sommaire_pack(), '')
        with patch.object(annexes, 'sommaire_pack', return_value=''):
            self.assertIn('Acheter le pack — 14 €', annexes.page_pack())

    def test_titres_et_categories_echappes_ordre_stable_source_intacte(self):
        source = self.livrable()
        for p in source:
            p['categorie'] += ' <img src=x onerror="bad()"> & suite'
            p['titre'] += ' </li><script>bad()</script> & fin'
        source.reverse()
        avant = json.dumps(source, ensure_ascii=False)
        with patch.object(annexes.construction, '_lire_json', return_value=source):
            bloc = annexes.sommaire_pack()
            self.assertEqual(bloc, annexes.sommaire_pack())
        self.assertEqual(json.dumps(source, ensure_ascii=False), avant)
        self.assertEqual([int(x) for x in re.findall(r'<li value="(\d+)">', bloc)], list(range(1, 101)))
        for p in source:
            self.assertIn(html.escape(p['titre'], quote=True), bloc)
            self.assertIn(html.escape(p['categorie'], quote=True), bloc)
        self.assertNotIn('<script>', bloc)
        self.assertNotIn('<img', bloc)


if __name__ == '__main__':
    unittest.main()
