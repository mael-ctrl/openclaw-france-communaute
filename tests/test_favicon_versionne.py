"""Le favicon peut être mis en cache sans figer une URL mutable."""
import hashlib
import json
from pathlib import Path
import re
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "engine"))
import assets_versionnes
import config
import construction


class FaviconVersionneTests(unittest.TestCase):
    def test_favicon_et_logo_emploient_empreinte_des_octets(self):
        data = (config.DOSSIER_ASSETS / "favicon.svg").read_bytes()
        attendu = "/assets/versionnes/favicon." + hashlib.sha256(data).hexdigest() + ".svg"
        html = construction.page("Titre", "Description", "", "/test/")
        self.assertIn('rel="icon" href="' + attendu + '" type="image/svg+xml"', html)
        graphe = json.loads(construction.jsonld_site().split(">", 1)[1].rsplit("<", 1)[0])
        self.assertEqual(graphe["@graph"][0]["logo"]["url"], config.URL_SITE + attendu)
        self.assertNotIn("/assets/favicon.svg", html)

    def test_build_garde_original_et_podcast_sans_script(self):
        with tempfile.TemporaryDirectory() as tmp:
            racine = Path(tmp)
            breves = racine / "breves.json"
            breves.write_text("[]")
            sortie = racine / "site"
            with patch.object(config, "DOSSIER_SORTIE", sortie), \
                    patch.object(config, "FICHIER_BREVES", breves), \
                    patch.object(config, "DOSSIER_ARTICLES", racine / "articles"):
                construction.construire()
            url = assets_versionnes.url("favicon.svg")
            copie = sortie / url.lstrip("/")
            self.assertEqual(copie.read_bytes(), (sortie / "assets/favicon.svg").read_bytes())
            self.assertEqual(copie.stat().st_mtime, assets_versionnes.MTIME)
            podcast = (sortie / "podcast/index.html").read_text()
            self.assertIn('rel="icon" href="' + url + '"', podcast)
            self.assertNotIn("<script", podcast)
            self.assertNotIn("<iframe", podcast)
            self.assertNotIn(url, (sortie / "sitemap.xml").read_text())

    def test_cache_reserve_au_favicon_versionne(self):
        texte = (ROOT / "assets/versionnes/.htaccess").read_text()
        motif = re.search(r'<FilesMatch "([^"]+)">', texte).group(1)
        self.assertIsNotNone(re.fullmatch(motif, "favicon." + "a" * 64 + ".svg"))
        for nom in ("favicon.svg", "favicon." + "a" * 63 + ".svg",
                    "favicon." + "A" * 64 + ".svg", "favicon." + "a" * 64 + ".png",
                    "autre." + "a" * 64 + ".svg", "og-crabe.png"):
            self.assertIsNone(re.fullmatch(motif, nom), nom)

    def test_changement_svg_change_url_et_symlink_refuse(self):
        with tempfile.TemporaryDirectory() as tmp:
            racine = Path(tmp)
            source = racine / "favicon.svg"
            with patch.object(config, "DOSSIER_ASSETS", racine):
                source.write_bytes(b'<svg xmlns="http://www.w3.org/2000/svg"/>')
                avant = assets_versionnes.url("favicon.svg")
                source.write_bytes(b'<svg xmlns="http://www.w3.org/2000/svg"><title>x</title></svg>')
                apres = assets_versionnes.url("favicon.svg")
                self.assertNotEqual(avant, apres)
                self.assertIn(hashlib.sha256(source.read_bytes()).hexdigest(), apres)
                source.unlink()
                source.symlink_to(ROOT / "assets/favicon.svg")
                with self.assertRaises(ValueError):
                    assets_versionnes.url("favicon.svg")


if __name__ == "__main__":
    unittest.main()
