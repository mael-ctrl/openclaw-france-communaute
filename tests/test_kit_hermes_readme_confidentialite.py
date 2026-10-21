"""Le README résume les précautions déjà livrées dans le GUIDE."""
from pathlib import Path
import re
import unittest
import zipfile

DL = Path(__file__).resolve().parents[1] / 'sites/openclaw-france/dl'


class ReadmeConfidentialiteTest(unittest.TestCase):
    def test_zip_livre_le_readme_harmonise_et_les_cinq_sources_exactes(self):
        with zipfile.ZipFile(DL / 'kit-hermes.zip') as archive:
            expected = sorted(p.relative_to(DL / 'kit-hermes').as_posix()
                              for p in (DL / 'kit-hermes').rglob('*') if p.is_file())
            self.assertEqual(sorted(archive.namelist()), expected)
            self.assertEqual(len(archive.namelist()), len(set(archive.namelist())))
            self.assertIsNone(archive.testzip())
            for name in expected:
                with self.subTest(member=name):
                    self.assertEqual(archive.read(name), (DL / 'kit-hermes' / name).read_bytes())

    def test_precautions_avant_demarrage_sans_promesse_absolue(self):
        text = (DL / 'kit-hermes/README.md').read_text(encoding='utf-8')
        self.assertIn('## Confidentialité — avant le premier essai', text)
        self.assertLess(text.index('## Confidentialité'), text.index('## Démarrage rapide'))
        section = text.split('## Confidentialité', 1)[1].split('\n## ', 1)[0]
        for phrase in ('contexte', 'extraits de fichiers', 'outils connectés', 'modèles auxiliaires',
                       'fournisseurs de secours', 'droits minimaux', 'sans secrets', 'journaux',
                       'sauvegardes', '.env', 'contrôle réseau indépendant', 'GUIDE.md',
                       'pas un audit réseau', '2026-10-21'):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, section)
        for phrase in ('100 % en local, sans compte ni clé API', 'rien ne sort du tout', 'tout reste chez vous'):
            self.assertNotIn(phrase, text)
        self.assertIn('conditions de conservation', section)
        self.assertIn('modèle IA, les outils externes et l’hébergement peuvent être payants', text)


if __name__ == '__main__':
    unittest.main()
