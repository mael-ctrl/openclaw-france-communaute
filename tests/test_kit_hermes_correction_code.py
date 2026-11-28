"""Exercice de correction du kit : contrat documentaire et code réellement exécuté."""
from pathlib import Path
import os
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile

DL = Path(os.environ.get("KIT_HERMES_DL", Path(__file__).resolve().parents[1] / "sites/openclaw-france/dl"))
DOCS = "https://hermes-agent.nousresearch.com/docs/"

class KitHermesCorrectionCodeTest(unittest.TestCase):
    def setUp(self):
        self.raw = (DL / "kit-hermes/demarrage.md").read_text()
        self.code_section = self.raw.split("### 3.", 1)[1].split("### 4.", 1)[0]
        self.section = " ".join(self.code_section.replace("\n> ", " ").replace("**", "").split())

    def test_perimetre_et_preservation_du_travail(self):
        for phrase in ("sans secrets", "Python 3", "hermes tools", "permissions techniques", "terminal", "panier.py", "test_panier.py", "sans modifier", "accord explicite", "sans commit", "sans push", "sans déploiement", "changements préexistants", "sans installation"):
            with self.subTest(phrase=phrase): self.assertTrue(phrase in self.section, phrase)

    def test_exercice_reproduit_echec_puis_reussite(self):
        blocks = re.findall(r"```python\n(.*?)```", self.code_section, re.S)
        self.assertEqual(len(blocks), 2, "Deux fichiers Python prêts à copier sont nécessaires")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            target = root / "panier.py"
            tests = root / "test_panier.py"
            target.write_text(blocks[0])
            tests.write_text(blocks[1])
            command = [sys.executable, "-B", "-m", "unittest", "-v", "test_panier.py"]
            red = subprocess.run(command, cwd=root, capture_output=True, text=True, timeout=20)
            self.assertEqual(red.returncode, 1, red.stdout + red.stderr)
            self.assertIn("Ran 2 tests", red.stderr)
            self.assertIn("FAILED (failures=1)", red.stderr)
            self.assertIn("AssertionError: 2 != 30", red.stderr)
            self.assertEqual(blocks[0].count("return len(prix)"), 1)
            target.write_text(blocks[0].replace("return len(prix)", "return sum(prix)"))
            green = subprocess.run(command, cwd=root, capture_output=True, text=True, timeout=20)
            self.assertEqual(green.returncode, 0, green.stdout + green.stderr)
            self.assertIn("Ran 2 tests", green.stderr)
            self.assertIn("OK", green.stderr)
            self.assertEqual(tests.read_text(), blocks[1])

    def test_preuves_et_limites_de_validation(self):
        for phrase in ("python3 -B -m unittest -v test_panier.py", "un échec", "diff", "code de sortie", "tests inchangés", "non exécuté", "pas un audit", "ne remplace pas", "modèle distant"):
            with self.subTest(phrase=phrase): self.assertTrue(phrase in self.section, phrase)
        self.assertNotIn("Il cherche, lit, modifie, relance les tests.", self.section)

    def test_sources_datees_et_archive_exacte(self):
        for source in (DOCS + "user-guide/features/tools#using-toolsets", DOCS + "user-guide/security#file-write-safety", "https://docs.python.org/3/library/unittest.html#command-line-interface"):
            self.assertTrue(source in self.section, source)
        self.assertIn("2026-11-28", self.section)
        with zipfile.ZipFile(DL / "kit-hermes.zip") as archive:
            self.assertIsNone(archive.testzip())
            self.assertEqual(archive.read("demarrage.md"), self.raw.encode())

if __name__ == "__main__":
    unittest.main()
