"""Démarrage : distinguer stockage, contexte envoyé et services connectés."""
from pathlib import Path
import os
import unittest

ROOT = Path(os.environ.get('P10_TREE', Path(__file__).resolve().parents[1]))
DL = ROOT / 'sites/openclaw-france/dl'
DOCS = 'https://hermes-agent.nousresearch.com/docs/'
TITLE = '## Confidentialité — avant de partager un dossier'


class DemarrageConfidentialiteTest(unittest.TestCase):
    def setUp(self):
        self.raw = (DL / 'kit-hermes/demarrage.md').read_text(encoding='utf-8')
        self.text = ' '.join(self.raw.split())

    def test_contexte_envoye_et_limites_avant_les_premiers_pas(self):
        self.assertIn(TITLE, self.raw)
        self.assertLess(self.raw.index(TITLE), self.raw.index('## Premiers pas'))
        section = self.text.split(TITLE, 1)[1].split('## Premiers pas', 1)[0]
        for phrase in ('fournisseur distant', 'contexte sélectionné', 'messages',
                       'mémoire', 'instructions de projet', 'résultats d’outils',
                       'extraits de fichiers', 'modèles auxiliaires', 'fournisseurs de secours',
                       'recherche web', 'MCP', 'messagerie', 'terminal',
                       'hermes tools', 'sans secrets', 'droits minimaux',
                       'contrôle réseau indépendant', 'conditions de conservation',
                       'pas un audit réseau', 'garantie juridique', '2026-11-24'):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, section)
        for source in ('user-guide/sessions', 'user-guide/features/context-files',
                       'user-guide/features/tools', 'user-guide/configuration#auxiliary-models',
                       'user-guide/features/fallback-providers'):
            self.assertIn(DOCS + source, section)

    def test_fichiers_memoire_et_historique_ne_sont_pas_confondus_avec_secret(self):
        self.assertNotIn('Hermes lit votre machine comme vous.', self.text)
        fichiers = self.text.split('### 1. Poser', 1)[1].split('### 2.', 1)[0]
        self.assertIn('permissions', fichiers)
        self.assertIn('contexte envoyé au modèle', fichiers)
        memory = self.text.split('### 6.', 1)[1].split('### 7.', 1)[0]
        for phrase in ('mémoire intégrée', '~/.hermes/memories/', 'profil',
                       'contexte du modèle', 'sans secrets'):
            self.assertIn(phrase, memory)
        section = self.text.split(TITLE, 1)[1].split('## Premiers pas', 1)[0]
        for phrase in ('~/.hermes/state.db', 'historique', 'résultats d’outils',
                       'journaux', 'exports', 'sauvegardes', 'effacement', '.env'):
            self.assertIn(phrase, section)
        self.assertIn(DOCS + 'user-guide/features/memory', memory)

    def test_zip_et_sommes_livrent_le_demarrage_corrige(self):
        import hashlib
        import zipfile
        with zipfile.ZipFile(DL / 'kit-hermes.zip') as archive:
            self.assertEqual(archive.read('demarrage.md'), self.raw.encode('utf-8'))
            self.assertIn(TITLE, archive.read('demarrage.md').decode('utf-8'))
            self.assertNotIn('Tout reste chez vous', archive.read('demarrage.md').decode('utf-8'))
        sums = (DL / 'SHA256SUMS.txt').read_text()
        self.assertIn(hashlib.sha256((DL / 'kit-hermes.zip').read_bytes()).hexdigest()
                      + '  kit-hermes.zip', sums)


if __name__ == '__main__':
    unittest.main()
