"""Empreintes des archives : publication et parcours de vérification."""
from hashlib import sha256
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch, MagicMock
import importlib.util
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "sites/openclaw-france"
SPEC = importlib.util.spec_from_file_location("deploy_hub", ROOT / "outils/deployer_openclaw.py")
DEPLOY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(DEPLOY)
KITS = ("kit-openclaw", "kit-hermes")


class HubIntegriteTest(unittest.TestCase):
    def test_manifeste_publie_correspond_aux_deux_archives(self):
        lines = (SITE / "dl/SHA256SUMS.txt").read_text().splitlines()
        self.assertEqual(len(lines), len(KITS))
        for line, kit in zip(lines, KITS):
            self.assertRegex(line, r"^[0-9a-f]{64}  kit-(openclaw|hermes)\.zip$")
            self.assertEqual(line, sha256((SITE / "dl" / (kit + ".zip")).read_bytes()).hexdigest() + "  " + kit + ".zip")

    def test_deploiement_regenere_et_envoie_les_empreintes_des_zips(self):
        with TemporaryDirectory() as tmp:
            source = Path(tmp)
            for kit in KITS:
                folder = source / "dl" / kit
                folder.mkdir(parents=True)
                (folder / "README.md").write_text("Fixture de test " + kit)
            ftp = MagicMock()
            uploads = []
            ftp.storbinary.side_effect = lambda cmd, fh, **kw: uploads.append((cmd, fh.read()))
            with patch.object(DEPLOY, "SOURCE", source), patch.object(DEPLOY.ftplib, "FTP", return_value=ftp), patch.object(DEPLOY, "mot_de_passe", return_value="test-only"):
                self.assertEqual(DEPLOY.main(), 0)
                first = (source / "dl/SHA256SUMS.txt").read_text()
                for kit in KITS:
                    self.assertIn(sha256((source / "dl" / (kit + ".zip")).read_bytes()).hexdigest(), first)
                self.assertIn(("STOR SHA256SUMS.txt", first.encode()), uploads)
                (source / "dl/kit-hermes/README.md").write_text("Contenu de test modifié")
                self.assertEqual(DEPLOY.main(), 0)
                second = (source / "dl/SHA256SUMS.txt").read_text()
                self.assertNotEqual(first, second)
                self.assertIn(sha256((source / "dl/kit-hermes.zip").read_bytes()).hexdigest(), second)

    def test_une_archive_manquante_empeche_un_manifeste_incomplet(self):
        with TemporaryDirectory() as tmp:
            source = Path(tmp)
            (source / "dl").mkdir()
            (source / "dl/kit-openclaw.zip").write_bytes(b"fixture")
            with patch.object(DEPLOY, "SOURCE", source):
                with self.assertRaises(FileNotFoundError):
                    DEPLOY.preparer_empreintes()
            self.assertFalse((source / "dl/SHA256SUMS.txt").exists())

    def test_parcours_lisible_sans_execution_automatique(self):
        for slug in ("openclaw", "hermes"):
            with self.subTest(page=slug):
                html = (SITE / slug / "index.html").read_text()
                hero = html.split("</section>", 1)[0]
                self.assertIn('href="#verifier-zip"', hero)
                self.assertEqual(html.count('id="verifier-zip"'), 1)
                match = re.search(r'<details[^>]*id="verifier-zip"[^>]*>(.*?)</details>', html, re.S)
                self.assertIsNotNone(match)
                block = match.group(1)
                self.assertIn('href="/dl/SHA256SUMS.txt"', block)
                for command in ("shasum -a 256", "sha256sum", "Get-FileHash -Algorithm SHA256"):
                    self.assertIn(command + " kit-" + slug + ".zip", block)
                for text in ("64 caractères", "majuscules", "ne lance aucun script", "pas une signature", "innocuité", "même site"):
                    self.assertIn(text, block)
                self.assertNotRegex(block, r"<(script|form|iframe)\b")


if __name__ == "__main__":
    unittest.main()
