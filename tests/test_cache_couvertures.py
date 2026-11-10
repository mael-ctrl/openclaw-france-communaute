"""Cache long limité aux couvertures adressées par empreinte, jamais aux erreurs."""
from pathlib import Path
import re
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "engine"))
import config
import construction

REGLE = ROOT / "assets/couvertures/.htaccess"


class CacheCouverturesTests(unittest.TestCase):
    def test_cache_long_reserve_aux_jpeg_adresses_par_empreinte(self):
        self.assertTrue(REGLE.is_file(), "Politique de cache des couvertures absente")
        texte = REGLE.read_text(encoding="utf-8")
        self.assertIn('<IfModule mod_headers.c>', texte)
        motif = re.search(r'<FilesMatch "([^"]+)">', texte).group(1)
        for nom in ["a" * 64 + ".jpg", "0123456789abcdef" * 4 + ".jpg"]:
            self.assertIsNotNone(re.search(motif, nom), nom)
        for nom in ["a" * 63 + ".jpg", "a" * 65 + ".jpg", "g" * 64 + ".jpg",
                    "A" * 64 + ".jpg", "cover.jpg", "index.html", "app.js",
                    "a" * 64 + ".jpg.bak", "a" * 64 + ".json"]:
            self.assertIsNone(re.search(motif, nom), nom)
        self.assertIn('public, max-age=31536000, immutable', texte)


    def test_erreurs_exclues_et_expiration_heritee_retiree(self):
        texte = REGLE.read_text(encoding="utf-8")
        condition = '"expr=%{REQUEST_STATUS} == 200 || %{REQUEST_STATUS} == 206 || %{REQUEST_STATUS} == 304"'
        directives = [ligne.strip() for ligne in texte.splitlines()
                      if ligne.strip().startswith("Header ")]
        self.assertEqual(directives, [
            'Header set Cache-Control "public, max-age=31536000, immutable" ' + condition,
            'Header unset Expires ' + condition,
        ])


    def test_deux_builds_copient_la_regle_sans_toucher_aux_politiques_voisines(self):
        with tempfile.TemporaryDirectory() as tmp:
            racine = Path(tmp)
            breves = racine / "breves.json"
            breves.write_text("[]", encoding="utf-8")
            sortie = racine / "site"
            sortie.mkdir()
            racine_avant = b"# Regle hebergeur a conserver\n"
            (sortie / ".htaccess").write_bytes(racine_avant)
            with patch.object(config, "DOSSIER_SORTIE", sortie), \
                    patch.object(config, "FICHIER_BREVES", breves), \
                    patch.object(config, "DOSSIER_ARTICLES", racine / "articles"):
                for _ in range(2):
                    construction.construire()
                    self.assertEqual((sortie / "assets/couvertures/.htaccess").read_bytes(),
                                     REGLE.read_bytes())
                    self.assertEqual((sortie / ".htaccess").read_bytes(), racine_avant)
                    for rel in (".htaccess", "app.js", "style.css",
                                "favicon.svg", "og-crabe.png"):
                        self.assertEqual((sortie / "assets" / rel).read_bytes(),
                                         (config.DOSSIER_ASSETS / rel).read_bytes())
                    self.assertEqual((sortie / "fichiers/.htaccess").read_bytes(),
                                     (config.DOSSIER_FICHIERS / ".htaccess").read_bytes())
                    self.assertEqual((sortie / "dl/.htaccess").read_bytes(),
                                     (config.DOSSIER_PRIVE / "dl/.htaccess").read_bytes())
                    self.assertNotIn(".htaccess", (sortie / "sitemap.xml").read_text())


if __name__ == "__main__":
    unittest.main()
