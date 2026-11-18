"""Un export public n'a pas besoin d'un listing de répertoire."""
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))
import annexes
import config
import construction


class AutoindexVeilleTest(unittest.TestCase):
    def test_deux_builds_ferment_le_listing_sans_changer_export_ni_racine(self):
        attendu = annexes.sources_opml().encode("utf-8")
        with tempfile.TemporaryDirectory() as dossier:
            racine = Path(dossier)
            breves = racine / "breves.json"
            breves.write_text("[]", encoding="utf-8")
            sortie = racine / "site"
            sortie.mkdir()
            regle_racine = b"# hebergement existant\n"
            (sortie / ".htaccess").write_bytes(regle_racine)
            with patch.object(config, "DOSSIER_SORTIE", sortie), \
                    patch.object(config, "FICHIER_BREVES", breves), \
                    patch.object(config, "DOSSIER_ARTICLES", racine / "articles"):
                for passage in range(2):
                    construction.construire()
                    with self.subTest(passage=passage):
                        regle = sortie / "veille/.htaccess"
                        self.assertTrue(regle.is_file(), "Listing de /veille/ non désactivé")
                        self.assertEqual(regle.read_bytes(), b"Options -Indexes\n")
                        self.assertEqual((sortie / "veille/sources.opml").read_bytes(), attendu)
                        self.assertEqual((sortie / ".htaccess").read_bytes(), regle_racine)
                        self.assertFalse((sortie / "veille/index.html").exists())
                        self.assertNotIn(".htaccess", (sortie / "sitemap.xml").read_text())
                        self.assertNotIn("/veille/", (sortie / "sitemap.xml").read_text())
                        self.assertIn('href="/veille/sources.opml" download=',
                                      (sortie / "skills/index.html").read_text())
                        self.assertIn(config.URL_SITE + "/veille/sources.opml",
                                      (sortie / "llms.txt").read_text())
                        self.assertTrue((sortie / "podcast/feed.xml").is_file())
                        self.assertEqual((sortie / "assets/.htaccess").read_bytes(),
                                         (config.DOSSIER_ASSETS / ".htaccess").read_bytes())


if __name__ == "__main__":
    unittest.main()
