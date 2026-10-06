"""Les brèves déjà publiées restent accessibles depuis le fil, sans JavaScript."""
import json
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))
import config
import construction


class LiensActus(HTMLParser):
    def __init__(self, document):
        super().__init__()
        self.liens = []
        self.canoniques = []
        self.feed(document)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a":
            self.liens.append(attrs)
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canoniques.append(attrs["href"])


def breves_test(nombre):
    return [{"slug": f"breve-{i}", "titre": f"Brève IA {i}", "resume": "Résumé.",
             "source": "Source de test", "lien_source": "https://example.org/",
             "date_redac": "2026-10-06T10:00:00+00:00", "tags": ["IA"]}
            for i in range(nombre)]


class PaginationActusTest(unittest.TestCase):
    def test_premiere_page_donne_acces_aux_breves_plus_anciennes(self):
        document = construction.page_actus(breves_test(101))
        liens = LiensActus(document)
        suivants = [a["href"] for a in liens.liens if a.get("rel") == "next"]
        self.assertEqual(suivants, ["/actus/page/2/"],
                         "Le fil doit donner accès aux brèves au-delà des 100 premières")
        self.assertFalse(any(a.get("rel") == "prev" for a in liens.liens))
        self.assertEqual(liens.canoniques, [config.URL_SITE + "/actus/"])
        self.assertIn('aria-label="Pagination des actus"', document)
        self.assertIn("Page 1 sur 2", document)
        self.assertEqual({a["href"] for a in liens.liens if a["href"].startswith("/breves/")},
                         {f"/breves/breve-{i}/" for i in range(100)})

    def test_fil_vide_ou_court_ne_propose_pas_de_page_inexistante(self):
        for nombre in (0, 1, 100):
            with self.subTest(nombre=nombre):
                document = construction.page_actus(breves_test(nombre))
                self.assertNotIn('aria-label="Pagination des actus"', document)
                self.assertEqual(LiensActus(document).canoniques, [config.URL_SITE + "/actus/"])

    def test_derniere_page_incomplete_ne_duplique_pas_la_precedente(self):
        breves = breves_test(201)
        breves[-1]["tags"] = ["Tag final"]
        document = construction.page_actus(breves, 3)
        liens = LiensActus(document)
        self.assertEqual({a["href"] for a in liens.liens if a["href"].startswith("/breves/")},
                         {"/breves/breve-200/"})
        self.assertEqual([a["href"] for a in liens.liens if a.get("rel") == "prev"],
                         ["/actus/page/2/"])
        self.assertFalse(any(a.get("rel") == "next" for a in liens.liens))
        self.assertIn('data-tag="Tag final"', document)
        self.assertNotIn('data-tag="IA"', document)

    def test_build_relie_les_400_breves_sans_doublon_et_indexe_les_archives(self):
        with tempfile.TemporaryDirectory() as dossier:
            racine = Path(dossier)
            source = racine / "breves.json"
            source.write_text(json.dumps(breves_test(401)), encoding="utf-8")
            sortie = racine / "site"
            with patch.object(config, "FICHIER_BREVES", source), \
                    patch.object(config, "DOSSIER_SORTIE", sortie):
                construction.construire()
            chemins = ["/actus/", "/actus/page/2/", "/actus/page/3/", "/actus/page/4/"]
            groupes = []
            for numero, chemin in enumerate(chemins, 1):
                fichier = sortie / chemin.lstrip("/") / "index.html"
                self.assertTrue(fichier.is_file(), f"Archive absente : {chemin}")
                document = fichier.read_text(encoding="utf-8")
                liens = LiensActus(document)
                self.assertEqual(liens.canoniques, [config.URL_SITE + chemin])
                self.assertIn(f"Page {numero} sur 4", document)
                self.assertIn("Rechercher sur cette page", document)
                if numero > 1:
                    self.assertIn(f"Le fil des actus — page {numero}", document)
                self.assertEqual([a["href"] for a in liens.liens if a.get("rel") == "prev"],
                                 [chemins[numero - 2]] if numero > 1 else [])
                self.assertEqual([a["href"] for a in liens.liens if a.get("rel") == "next"],
                                 [chemins[numero]] if numero < 4 else [])
                groupe = {a["href"] for a in liens.liens if a["href"].startswith("/breves/")}
                self.assertEqual(groupe, {f"/breves/breve-{i}/" for i in range((numero - 1) * 100, numero * 100)})
                for cible in groupe:
                    self.assertTrue((sortie / cible.lstrip("/") / "index.html").is_file())
                groupes.append(groupe)
            self.assertEqual(len(set.union(*groupes)), 400)
            self.assertFalse((sortie / "actus/page/1").exists())
            self.assertFalse((sortie / "actus/page/5").exists())
            sitemap = ET.parse(sortie / "sitemap.xml")
            urls = {n.text for n in sitemap.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")}
            self.assertTrue({config.URL_SITE + c for c in chemins} <= urls)


if __name__ == "__main__":
    unittest.main()
