"""Un export OPML fidèle au catalogue configuré, sans copie manuelle."""
import json
from pathlib import Path
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))
import annexes
import config
import construction


class SourcesOPMLTest(unittest.TestCase):
    def test_export_fidele_aux_sources_et_aux_caracteres_xml(self):
        sources = [{"nom": 'IA & <recherche> "🦀"',
                    "url": "https://example.org/feed?q=AI+agent&points=80",
                    "langue": "fr", "priorite": 4, "filtre_ia": True}]
        with tempfile.TemporaryDirectory() as tmp:
            fichier = Path(tmp) / "sources.json"
            fichier.write_text(json.dumps(sources), encoding="utf-8")
            with patch.object(config, "FICHIER_SOURCES", fichier):
                _, fichiers = annexes.construire_annexes([], [], {}, [])
        self.assertIn("veille/sources.opml", fichiers,
                      "Le build doit offrir la liste des flux à importer")
        racine = ET.fromstring(fichiers["veille/sources.opml"])
        self.assertEqual(racine.tag, "opml")
        self.assertEqual(racine.get("version"), "2.0")
        self.assertTrue(racine.findtext("head/title"))
        flux = racine.findall(".//outline[@type='rss']")
        self.assertEqual(len(flux), 1)
        self.assertEqual(flux[0].attrib, {"type": "rss", "text": sources[0]["nom"],
                                         "xmlUrl": sources[0]["url"]})

    def test_telechargement_et_mode_emploi_sans_javascript_sur_skills(self):
        from html.parser import HTMLParser

        class Liens(HTMLParser):
            def __init__(self):
                super().__init__()
                self.liens = []

            def handle_starttag(self, tag, attrs):
                if tag == "a":
                    self.liens.append(dict(attrs))

        rendu = annexes.page_skills()
        parser = Liens()
        parser.feed(rendu)
        liens = [a for a in parser.liens if a.get("href") == "/veille/sources.opml"]
        self.assertEqual(len(liens), 1, "Un téléchargement OPML natif doit être proposé")
        self.assertIn("download", liens[0])
        self.assertIn("Importer", rendu)
        self.assertIn("ne reprend pas nos filtres", rendu)
        self.assertIn("disponibilité des flux tiers", rendu)
        self.assertIn("sans inscription", rendu)
        self.assertNotIn("<form", rendu)
        self.assertIn(config.URL_SITE + "/veille/sources.opml", construction.llms_txt())

    def test_build_exporte_exactement_le_catalogue_reel_hors_sitemap(self):
        sources = json.loads(config.FICHIER_SOURCES.read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmp:
            sortie = Path(tmp) / "site"
            with patch.object(config, "DOSSIER_SORTIE", sortie):
                construction.construire()
            cible = sortie / "veille/sources.opml"
            self.assertTrue(cible.is_file())
            flux = ET.parse(cible).findall(".//outline[@type='rss']")
            self.assertEqual([(f.get("text"), f.get("xmlUrl")) for f in flux],
                             [(s["nom"], s["url"]) for s in sources])
            self.assertEqual(cible.read_bytes(), annexes.sources_opml().encode("utf-8"))
            self.assertNotIn("sources.opml", (sortie / "sitemap.xml").read_text())
            self.assertTrue((sortie / "podcast/feed.xml").is_file())
            self.assertTrue((sortie / "b2b/echantillon-veille/echantillon-veille.md").is_file())
            for s in annexes.SKILLS:
                self.assertEqual((sortie / "fichiers" / s["fichier"]).read_bytes(),
                                 (config.DOSSIER_FICHIERS / s["fichier"]).read_bytes())

    def test_catalogue_vide_garde_un_groupe_et_export_deterministe(self):
        with tempfile.TemporaryDirectory() as tmp:
            fichier = Path(tmp) / "sources.json"
            fichier.write_text("[]", encoding="utf-8")
            with patch.object(config, "FICHIER_SOURCES", fichier):
                premier = annexes.sources_opml()
                self.assertEqual(premier, annexes.sources_opml())
        racine = ET.fromstring(premier)
        self.assertEqual(len(racine.findall("body/outline")), 1)
        self.assertEqual(racine.findall(".//outline[@type='rss']"), [])
        self.assertIsNone(racine.find("head/dateCreated"))

    def test_catalogue_corrompu_non_masque_par_un_export_vide(self):
        with tempfile.TemporaryDirectory() as tmp:
            fichier = Path(tmp) / "sources.json"
            fichier.write_text("{", encoding="utf-8")
            with patch.object(config, "FICHIER_SOURCES", fichier):
                with self.assertRaises(json.JSONDecodeError):
                    annexes.sources_opml()


if __name__ == "__main__":
    unittest.main()
