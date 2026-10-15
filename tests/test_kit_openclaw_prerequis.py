"""Prérequis du kit OpenClaw cohérents en ligne et dans le ZIP."""
from pathlib import Path
import re
import unittest
import zipfile

SITE = Path(__file__).resolve().parents[1] / "sites" / "openclaw-france"


class KitOpenClawPrerequisTest(unittest.TestCase):
    def test_guide_et_readme_distinguent_les_chemins(self):
        for name in ("GUIDE.md", "README.md"):
            with self.subTest(name=name):
                text = (SITE / "dl/kit-openclaw" / name).read_text()
                for word in ("Bash", "curl", "WSL2", "PowerShell", "Node.js",
                             "24.16+", "26.1+", "Docker Compose v2", "6 Go",
                             "construction", "préconstruite", "SSH", "2026-10-15"):
                    self.assertIn(word, text)
                self.assertIn("pas dans PowerShell", text)
                self.assertIn("pas une installation testée", text)
                self.assertNotIn("Rien de particulier à préparer", text)
                self.assertNotIn("minimum constaté en pratique", text)

    def test_couts_et_acces_sans_promesse_non_verifiee(self):
        for name in ("GUIDE.md", "README.md"):
            with self.subTest(name=name):
                text = (SITE / "dl/kit-openclaw" / name).read_text()
                for word in ("modèle IA", "hébergement", "payants", "plafond"):
                    self.assertIn(word, text)
                for old in ("seul coût possible", "réutiliser tout seul", "~5–10", "~5-10",
                            "rabais déjà appliqué", "zéro surcoût"):
                    self.assertNotIn(old, text)

    def test_sources_datees_et_page_coherente(self):
        urls = ("https://docs.openclaw.ai/install", "https://docs.openclaw.ai/install/docker",
                "https://docs.openclaw.ai/platforms/windows")
        guide = (SITE / "dl/kit-openclaw/GUIDE.md").read_text()
        for url in urls:
            self.assertIn(url, guide)
        page = (SITE / "openclaw/index.html").read_text()
        prerequis = re.search(r'<section id="prerequis"[^>]*>(.*?)</section>', page, re.S).group(1)
        self.assertIn('datetime="2026-10-15"', prerequis)
        self.assertNotIn("plus anciennes", prerequis)
        self.assertIn("prérequis du guide", prerequis)
        self.assertIn("24.16+", prerequis)
        self.assertIn("26.1+", prerequis)
        self.assertIn("6 Go", prerequis)

    def test_archive_integrite_exhaustivite_et_contenu_exact(self):
        root = SITE / "dl/kit-openclaw"
        expected = {p.relative_to(root).as_posix(): p.read_bytes()
                    for p in root.rglob("*") if p.is_file()}
        with zipfile.ZipFile(SITE / "dl/kit-openclaw.zip") as archive:
            self.assertIsNone(archive.testzip())
            self.assertEqual(set(archive.namelist()), set(expected))
            self.assertEqual(len(archive.namelist()), len(expected))
            self.assertNotIn(".env", archive.namelist())
            for name, content in expected.items():
                self.assertEqual(archive.read(name), content, name)


if __name__ == "__main__":
    unittest.main()
