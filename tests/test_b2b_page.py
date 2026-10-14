"""La page B2B « Travailler avec le Crabe » : en ligne, liée, déclarée."""
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))
import config
import construction


class PageB2BTest(unittest.TestCase):
    def test_la_page_existe_dans_le_build_et_contient_les_offres(self):
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
            page = (sortie / "b2b" / "index.html").read_text(encoding="utf-8")
            self.assertIn("Travailler avec le Crabe", page)
            self.assertIn("2 000 €", page)
            self.assertIn("4 900 €", page)
            self.assertIn("mailto:crabe@blockos.fr", page)
            self.assertIn("loi 1901", page)
            self.assertIn("<details>", page)  # FAQ sans JS
            sitemap = ET.parse(sortie / "sitemap.xml").getroot()
            lieux = [u.findtext("{http://www.sitemaps.org/schemas/sitemap/0.9}loc") for u in sitemap]
            self.assertIn(config.URL_SITE + "/b2b/", lieux)

    def test_lien_dans_la_navigation_et_le_pied(self):
        html = construction.page("T", "D", "<p>x</p>", "/")
        self.assertIn('href="/b2b/"', html)
        self.assertIn("Pro 🦀", html)
        self.assertIn("Travailler avec le Crabe", html)


if __name__ == "__main__":
    unittest.main()
