"""Les trois ressources exécutables ont des URL liées à leurs octets."""
import hashlib
import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "engine"))
import config
import construction


class AssetsVersionnesTests(unittest.TestCase):
    def module(self):
        self.assertIsNotNone(importlib.util.find_spec("assets_versionnes"),
                             "Gestion des assets versionnés absente")
        import assets_versionnes
        return assets_versionnes

    def test_url_app_depend_des_octets_et_change_si_source_change(self):
        module = self.module()
        with tempfile.TemporaryDirectory() as tmp:
            assets = Path(tmp)
            (assets / "style.css").write_bytes((config.DOSSIER_ASSETS / "style.css").read_bytes())
            source = assets / "app.js"
            with patch.object(config, "DOSSIER_ASSETS", assets):
                for data in (b"console.log('v1');\n", b"console.log('v2');\n"):
                    source.write_bytes(data)
                    attendu = "/assets/versionnes/app." + hashlib.sha256(data).hexdigest() + ".js"
                    self.assertEqual(module.url("app.js"), attendu)
                    self.assertIn('src="' + attendu + '" defer',
                                  construction.page("Test", "Test", "", "/test/"))

    def test_build_publie_les_trois_fichiers_exacts_mtime_stable(self):
        module = self.module()
        import annexes
        with tempfile.TemporaryDirectory() as tmp:
            racine = Path(tmp)
            breves = racine / "breves.json"
            breves.write_text("[]")
            sorties = []
            for nom_sortie in ("site1", "site2"):
                sortie = racine / nom_sortie
                with patch.object(config, "DOSSIER_SORTIE", sortie), \
                        patch.object(config, "FICHIER_BREVES", breves), \
                        patch.object(config, "DOSSIER_ARTICLES", racine / "articles"):
                    construction.construire()
                identites = {}
                for nom in ("app.js", "pack-copie.js", "b2b-demo.css"):
                    url = module.url(nom)
                    fichier = sortie / url.lstrip("/")
                    self.assertTrue(fichier.is_file(), f"Référence sans destination : {url}")
                    data = (config.DOSSIER_ASSETS / nom).read_bytes()
                    self.assertEqual(fichier.read_bytes(), data)
                    self.assertEqual((sortie / "assets" / nom).read_bytes(), data)
                    identites[url] = (hashlib.sha256(data).hexdigest(), fichier.stat().st_mtime_ns)
                sorties.append(identites)
                self.assertIn(module.url("pack-copie.js"), (sortie / "pack/index.html").read_text())
                self.assertIn(module.url("b2b-demo.css"), (sortie / "b2b/index.html").read_text())
                self.assertNotIn("<script", (sortie / "podcast/index.html").read_text())
                self.assertNotIn("/assets/versionnes/", (sortie / "sitemap.xml").read_text())
            self.assertEqual(sorties[0], sorties[1])

    def test_refuse_sources_hors_liste_symboliques_ou_absentes(self):
        module = self.module()
        with tempfile.TemporaryDirectory() as tmp:
            assets = Path(tmp) / "assets"
            assets.mkdir()
            secret = Path(tmp) / "hors-perimetre.js"
            secret.write_bytes(b"non public")
            with patch.object(config, "DOSSIER_ASSETS", assets):
                for nom in ("../hors-perimetre.js", str(secret), "style.css", "inconnu.js"):
                    with self.subTest(nom=nom), self.assertRaises(ValueError):
                        module.url(nom)
                with self.assertRaises(FileNotFoundError):
                    module.url("app.js")
                (assets / "app.js").symlink_to(secret)
                with self.assertRaises(ValueError):
                    module.url("app.js")

    def test_politique_cache_bornee_aux_noms_versionnes_et_statuts_succes(self):
        import re
        regle = ROOT / "assets/versionnes/.htaccess"
        self.assertTrue(regle.is_file(), "Politique de cache absente")
        texte = regle.read_text()
        self.assertIn("Options -Indexes", texte)
        self.assertIn("<IfModule mod_headers.c>", texte)
        motif = re.search(r'<FilesMatch "([^"]+)">', texte).group(1)
        for nom in ("app", "pack-copie", "b2b-demo"):
            suffixe = ".css" if nom == "b2b-demo" else ".js"
            self.assertIsNotNone(re.fullmatch(motif, nom + "." + "a" * 64 + suffixe))
        for nom in ("app.js", "style.css", "inconnu." + "a" * 64 + ".js",
                    "app." + "a" * 63 + ".js", "app." + "A" * 64 + ".js",
                    "app." + "a" * 64 + ".css", "b2b-demo." + "a" * 64 + ".js",
                    "pack-copie." + "a" * 64 + ".js.bak", "podcast.mp3"):
            self.assertIsNone(re.fullmatch(motif, nom), nom)
        condition = '"expr=%{REQUEST_STATUS} == 200 || %{REQUEST_STATUS} == 206 || %{REQUEST_STATUS} == 304"'
        self.assertEqual([s.strip() for s in texte.splitlines() if s.strip().startswith("Header ")], [
            'Header set Cache-Control "public, max-age=31536000, immutable" ' + condition,
            'Header unset Expires ' + condition,
        ])


if __name__ == "__main__":
    unittest.main()
