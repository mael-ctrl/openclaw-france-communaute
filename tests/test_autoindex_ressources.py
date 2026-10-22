"""Les ressources restent lisibles, leurs dossiers ne sont plus listables."""
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))
import config
import construction


class AutoindexRessourcesTest(unittest.TestCase):
    def test_regles_copiees_apres_deux_builds_sans_alterer_les_fichiers(self):
        sources = {"assets": config.DOSSIER_ASSETS,
                   "fichiers": config.DOSSIER_FICHIERS,
                   "dl": config.DOSSIER_PRIVE / "dl"}
        with tempfile.TemporaryDirectory() as tmp:
            racine = Path(tmp)
            breves = racine / "breves.json"
            breves.write_text("[]", encoding="utf-8")
            sortie = racine / "site"
            sortie.mkdir()
            regle_racine = b"# configuration hebergeur existante\n"
            (sortie / ".htaccess").write_bytes(regle_racine)
            with patch.object(config, "DOSSIER_SORTIE", sortie), \
                    patch.object(config, "FICHIER_BREVES", breves), \
                    patch.object(config, "DOSSIER_ARTICLES", racine / "articles"):
                for passage in range(2):
                    construction.construire()
                    for dossier, source in sources.items():
                        with self.subTest(passage=passage, dossier=dossier):
                            cible = sortie / dossier / ".htaccess"
                            self.assertTrue(cible.is_file(), f"Listing non desactive : {dossier}")
                            # Retirer seulement Indexes : ni authentification,
                            # ni blocage de fichier, ni redirection ou CORS global.
                            self.assertEqual(cible.read_bytes(), b"Options -Indexes\n")
                            for fichier in source.rglob("*"):
                                if fichier.is_file():
                                    self.assertEqual(
                                        (sortie / dossier / fichier.relative_to(source)).read_bytes(),
                                        fichier.read_bytes(), str(fichier))
                    self.assertEqual((sortie / ".htaccess").read_bytes(), regle_racine)
                    self.assertNotIn(".htaccess", (sortie / "sitemap.xml").read_text())
                    self.assertIn("Disallow: /dl/", (sortie / "robots.txt").read_text())
                    self.assertTrue((sortie / "podcast/feed.xml").is_file())
                    self.assertTrue((sortie / "veille/sources.opml").is_file())
                    self.assertIn("RedirectMatch 301 ^/breves/?$", (sortie / "breves/.htaccess").read_text())


if __name__ == "__main__":
    unittest.main()
