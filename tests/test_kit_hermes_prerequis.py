"""Prérequis Hermes consultables avant exécution, dans le kit et le ZIP."""
from pathlib import Path
import re
import unittest
import zipfile

SITE = Path(__file__).resolve().parents[1] / "sites" / "openclaw-france"
DOCS = "https://hermes-agent.nousresearch.com/docs/getting-started/"


class KitHermesPrerequisTest(unittest.TestCase):
    def test_prerequis_systemes_et_reserve_intel(self):
        for name in ("GUIDE.md", "README.md"):
            with self.subTest(name=name):
                text = (SITE / "dl/kit-hermes" / name).read_text()
                for word in ("Bash", "WSL2", "PowerShell", "Apple Silicon", "Mac Intel",
                             "x86_64", "arm64", "Git", "curl", "tar", "SHA-256",
                             "bibliothèques système", "divergent", "compatibilité non garantie",
                             "2026-10-16", "pas une installation testée"):
                    self.assertIn(word, text)
                self.assertIn("pas dans PowerShell", text)
                self.assertNotIn("fonctionne aussi via", text)
                self.assertNotIn("les Mac Intel passent", text)

    def test_lecture_avant_script_et_budget_sans_garantie(self):
        readme = (SITE / "dl/kit-hermes/README.md").read_text()
        self.assertLess(readme.index("## Prérequis"), readme.index("## Démarrage rapide"))
        self.assertNotIn("Ou lancez directement", readme)
        guide = (SITE / "dl/kit-hermes/GUIDE.md").read_text()
        before = guide.split("## 2. Avant de commencer", 1)[1].split("## 3.", 1)[0]
        for word in ("libatomic", "compilateur", "64 000", "modèle", "hébergement", "payants", "plafond"):
            self.assertIn(word, before)
        for obsolete in ("C’est tout", "C\'est tout", "~5 €/mois", "rabais appliqué", "zéro surcoût"):
            self.assertNotIn(obsolete, before)

    def test_sources_et_page_coherentes(self):
        for name in ("GUIDE.md", "README.md"):
            text = (SITE / "dl/kit-hermes" / name).read_text()
            for suffix in ("installation#prerequisites", "platform-support", "installation#windows-native"):
                self.assertIn(DOCS + suffix, text)
        page = (SITE / "hermes/index.html").read_text()
        section = re.search(r'<section id="prerequis"[^>]*>(.*?)</section>', page, re.S).group(1)
        self.assertIn('datetime="2026-10-16"', section)
        self.assertIn("prérequis du guide", section)
        self.assertIn("script", section)
        self.assertNotIn("plus anciennes", section)
        self.assertIn("compatibilité non garantie", section)

    def test_archive_exacte_et_sans_secret(self):
        root = SITE / "dl/kit-hermes"
        expected = {p.relative_to(root).as_posix(): p.read_bytes()
                    for p in root.rglob("*") if p.is_file()}
        with zipfile.ZipFile(SITE / "dl/kit-hermes.zip") as archive:
            self.assertIsNone(archive.testzip())
            self.assertEqual(set(archive.namelist()), set(expected))
            self.assertEqual(len(archive.namelist()), len(expected))
            self.assertNotIn(".env", archive.namelist())
            for name, content in expected.items():
                self.assertEqual(archive.read(name), content, name)


if __name__ == "__main__":
    unittest.main()
