"""Parcours B2B de démonstration, sans nouvelle offre ni collecte automatique."""
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))
import config
import construction


class DemonstrationB2BTest(unittest.TestCase):
    def test_parcours_du_bloc_vers_echantillon_et_documents(self):
        with tempfile.TemporaryDirectory() as dossier:
            racine = Path(dossier)
            articles = racine / "articles"
            articles.mkdir()
            breves = racine / "breves.json"
            breves.write_text("[]", encoding="utf-8")
            sortie = racine / "site"
            with patch.object(config, "DOSSIER_ARTICLES", articles), \
                    patch.object(config, "FICHIER_BREVES", breves), \
                    patch.object(config, "DOSSIER_SORTIE", sortie):
                construction.construire()
            b2b = (sortie / "b2b/index.html").read_text(encoding="utf-8")
            chemin = "b2b/echantillon-veille/"
            self.assertIn('href="/' + chemin + '"', b2b)
            self.assertEqual(b2b.count('id="demo-veille"'), 1)
            self.assertIn('href="/assets/b2b-demo.css"', b2b)
            self.assertLess(b2b.index('id="demo-veille"'), b2b.index('id="offres"'))
            sample = (sortie / chemin / "index.html").read_text(encoding="utf-8")
            self.assertEqual(sample.count("<article "), 3)
            for token in ["Démonstration rédigée par IA", "ni un livrable client ni un témoignage",
                          "Faits vérifiés dans la source", "Implication — analyse", "Limites",
                          'datetime="2026-10-15"', 'mailto:crabe@blockos.fr?subject=',
                          'rel="canonical" href="' + config.URL_SITE + '/' + chemin + '"']:
                self.assertIn(token, sample)
            for token in ["<script", "<form", "buy.stripe.com", "donate.stripe.com", "€"]:
                self.assertNotIn(token, sample)
            for fichier in ["echantillon-veille.md", "questionnaire-qualification.md"]:
                self.assertIn('href="' + fichier + '" download', sample)
                self.assertEqual((sortie / chemin / fichier).read_bytes(),
                                 (config.RACINE / "contenus/b2b" / fichier).read_bytes())
            questionnaire = (sortie / chemin / "questionnaire-qualification.md").read_text(encoding="utf-8")
            self.assertIn("Aucune donnée sensible requise", questionnaire)
            self.assertIn("ni un formulaire de commande ni une nouvelle offre", questionnaire)
            self.assertIn("n’attestent aucun versement", questionnaire)
            self.assertEqual((sortie / "assets/b2b-demo.css").read_bytes(),
                             (config.DOSSIER_ASSETS / "b2b-demo.css").read_bytes())
            sitemap = ET.parse(sortie / "sitemap.xml").getroot()
            lieux = [u.findtext("{http://www.sitemaps.org/schemas/sitemap/0.9}loc") for u in sitemap]
            self.assertIn(config.URL_SITE + '/' + chemin, lieux)
            self.assertFalse(any(url.endswith(".md") for url in lieux))
            for route in ["index.html", "pack/index.html", "skills/index.html"]:
                self.assertNotIn('href="/assets/b2b-demo.css"', (sortie / route).read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
