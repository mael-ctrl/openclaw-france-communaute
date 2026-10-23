"""Régression ciblée du bandeau : unittest, sans navigateur ni dépendance.

Exécute les vrais corps de bandeau_defilant/ech, extraits du source Python
pour ne pas charger Pillow, inutile à ce fragment HTML.
"""
import ast
import html
import os
from html.parser import HTMLParser
from pathlib import Path
import unittest

RACINE = Path(os.environ.get("SITE_RACINE", Path(__file__).resolve().parents[1]))
SOURCE = RACINE / "engine" / "construction.py"
module = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))
fonctions = [n for n in module.body if isinstance(n, ast.FunctionDef)
             and n.name in {"ech", "bandeau_defilant"}]
assert len(fonctions) == 2
espace = {"html": html}
exec(compile(ast.Module(body=fonctions, type_ignores=[]), str(SOURCE), "exec"), espace)
bandeau_defilant = espace["bandeau_defilant"]


class Fragment(HTMLParser):
    def __init__(self, document):
        super().__init__()
        self.liens = []
        self.conteneurs = []
        self.texte = []
        self.feed(document)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a":
            self.liens.append(attrs)
        if tag == "div":
            self.conteneurs.append(attrs)

    def handle_data(self, data):
        self.texte.append(data)


class BandeauClavierTest(unittest.TestCase):
    def test_aucun_lien_du_bandeau_masque_dans_ordre_tab(self):
        for nombre in (1, 6, 10, 12):
            with self.subTest(nombre=nombre):
                items = [{"slug": f"essai-{i}", "titre": f"Titre {i}"} for i in range(nombre)]
                fragment = Fragment(bandeau_defilant(items))
                self.assertTrue(fragment.liens)
                self.assertEqual(fragment.conteneurs[0].get("aria-hidden"), "true")
                tabulables = [a["href"] for a in fragment.liens
                              if int(a.get("tabindex", "0")) >= 0]
                self.assertEqual(tabulables, [], "Liens sous aria-hidden encore dans l'ordre Tab")

    def test_destinations_textes_et_deux_copies_restent_identiques(self):
        items = [{"slug": f"essai-{i}", "titre": f'Titre <{i}> & "suite"'} for i in range(12)]
        fragment = Fragment(bandeau_defilant(items))
        destinations = [f'/breves/{b["slug"]}/' for b in items[:10]]
        self.assertEqual([a["href"] for a in fragment.liens], destinations * 2)
        for item in items[:10]:
            self.assertEqual("".join(fragment.texte).count(item["titre"]), 2)
        self.assertTrue(all(a["class"] == "defile-item" for a in fragment.liens))
        self.assertNotIn("<0>", bandeau_defilant(items))

    def test_aucun_bandeau_si_aucune_breve(self):
        self.assertEqual(bandeau_defilant([]), "")


if __name__ == "__main__":
    unittest.main(verbosity=2)
