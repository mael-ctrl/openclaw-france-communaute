"""Contrat autonome statique : jamais de lancement de Hermes ou des scripts du kit."""
import os
from pathlib import Path
import unittest

ROOT=Path(os.environ.get('P10_TREE',Path(__file__).resolve().parents[1]))
DOC=ROOT/'sites/openclaw-france/dl/kit-hermes/demarrage.md'

class RepriseSessionTest(unittest.TestCase):
    def test_reprise_ciblee_et_portee(self):
        raw=DOC.read_text();s=' '.join(raw.split('5. **',1)[1].split('Sources officielles consultées',1)[0].split())
        for phrase in ('hermes -c','profil actif','terminal','répertoire','identifiant exact','hermes sessions list','hermes -r "recherche-x"','/title recherche-x','/sessions','historique','mémoire','ne relancez pas','2026-11-27','IA','version','aucune reprise utilisateur réelle','user-guide/sessions'):
            self.assertIn(phrase,s)
        self.assertNotIn('votre dernière session revient',s)

    def test_raccourcis_conditionnels_et_image_non_garantie(self):
        s=' '.join(DOC.read_text().split())
        for phrase in ('brouillon', 'champ vide', 'Windows Terminal', 'Ctrl+J', 'Alt+Entrée', 'CLI classique', 'presse-papiers', '/paste', 'pièce jointe', 'sans secrets'):
            self.assertIn(phrase,s)
        self.assertNotIn('Ctrl+V` colle une capture',s)
        self.assertNotIn('/help` liste toutes les commandes',s)

    def test_surface_gateway_et_commandes_non_universelles(self):
        s=' '.join(DOC.read_text().split())
        for phrase in ('compositeur classique', 'client du gateway', '`/stop`',
                       'détacher le client', 'si votre `/help` le propose',
                       'utilisez directement son ID'):
            self.assertIn(phrase,s)
        self.assertNotIn('Dans la **CLI classique**, `Ctrl+C`', s)
        self.assertNotIn('créer. Nommez-la avec `/title recherche-x`.', s)

if __name__=='__main__':unittest.main()
