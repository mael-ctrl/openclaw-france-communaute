"""Usages 4 et 7 : parcours documentaire, jamais exécution de Hermes."""
import os
from pathlib import Path
import unittest

ROOT = Path(os.environ.get('P10_TREE', Path(__file__).resolve().parents[1]))
DOC = ROOT / 'sites/openclaw-france/dl/kit-hermes/demarrage.md'

class GitSkillsTest(unittest.TestCase):
    def section(self, n):
        return ' '.join(DOC.read_text().split('### '+str(n)+'.',1)[1].split('### '+str(n+1)+'.',1)[0].replace('> ', '').split())

    def test_git_disponibilite_et_autorisations(self):
        s=self.section(4)
        for phrase in ('hermes skills list', 'hermes skills browse', '/github-pr-workflow',
                       '`github`', 'pas une commande intégrée', 'profil actif',
                       'Git', '`gh`', 'authentification', 'droits minimaux',
                       'copie de test', 'sans secrets', 'sans commit', 'sans push',
                       'sans création de PR', 'accord explicite', 'publication',
                       'diff', 'tests', 'ne donne aucun droit', 'n’est pas un mode lecture seule', '2026-11-25',
                       'https://hermes-agent.nousresearch.com/docs/user-guide/features/skills'):
            self.assertIn(phrase,s)
        self.assertNotIn('crée une PR propre pour la refonte',s)

    def test_learn_relecture_portee_et_confiance(self):
        s=self.section(7)
        for phrase in ('/learn', 'SKILL.md', 'skill_manage', 'profil actif',
                       'sans secrets', 'ne publie rien', 'nom réellement créé',
                       'hermes skills list', 'permissions', 'confiance',
                       'scripts', 'approbation', '2026-11-25',
                       'https://hermes-agent.nousresearch.com/docs/reference/slash-commands'):
            self.assertIn(phrase,s)
        self.assertRegex(s,r'(?i)relisez')
        self.assertNotIn('recharge la procédure partout',s)
        self.assertNotIn('/publier-un-article',s)
        self.assertNotIn('nouveau brouillon, relire, publier',s)

if __name__=='__main__':
    unittest.main()
