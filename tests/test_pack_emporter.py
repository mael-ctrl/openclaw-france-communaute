"""Les fichiers d'essai contiennent seulement les trois extraits publics."""
import json
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'engine'))
import annexes
import config

JSON_PATH = 'pack/extraits/3-prompts-gratuits.json'
MD_PATH = 'pack/extraits/3-prompts-gratuits.md'


class PackEmporterTest(unittest.TestCase):
    def test_selection_invalide_refusee_sans_anciens_extraits_ni_promesse(self):
        source = json.loads((config.DOSSIER_PRIVE / 'dl' / 'pack-du-crabe-100-prompts.json').read_text())
        trois = [p for p in source if p['id'] in (5, 13, 61)]
        with TemporaryDirectory() as dossier, patch.object(config, 'DOSSIER_PRIVE', Path(dossier)):
            fichier = Path(dossier) / 'dl' / 'pack-du-crabe-100-prompts.json'
            fichier.parent.mkdir()
            for valeur in (None, '{invalide', [], {}, trois[:-1], trois + [trois[0]],
                           [dict(p, id=float(p['id'])) for p in trois],
                           [dict(p, prompt=' ') for p in trois]):
                with self.subTest(valeur=valeur):
                    if valeur is None:
                        fichier.unlink(missing_ok=True)
                    else:
                        fichier.write_text(valeur if isinstance(valeur, str) else json.dumps(valeur))
                    self.assertEqual(annexes.donnees_extraits_pack(), [])
                    self.assertNotIn('pack-extraits-fichiers', annexes.page_pack())
                    sorties = annexes.fichiers_extraits_pack()
                    self.assertEqual(json.loads(sorties[JSON_PATH]), [])
                    self.assertEqual(sorties[MD_PATH], '')

    def test_fichiers_generes_depuis_les_trois_extraits_publics(self):
        source = json.loads((config.DOSSIER_PRIVE / 'dl' / 'pack-du-crabe-100-prompts.json').read_text())
        attendus = [{k: p[k] for k in ('id', 'titre', 'categorie', 'prompt')}
                    for ident in (5, 13, 61) for p in source if p['id'] == ident]
        pages, fichiers = annexes.construire_annexes([], [], {}, [])
        self.assertIn(JSON_PATH, fichiers)
        self.assertIn(MD_PATH, fichiers)
        self.assertEqual(json.loads(fichiers[JSON_PATH]), attendus)
        for p in attendus:
            self.assertIn(p['prompt'], fichiers[MD_PATH])
        for p in source:
            if p['id'] not in (5, 13, 61):
                self.assertNotIn(p['prompt'], fichiers[MD_PATH])
        self.assertIn('rédigés par une IA', fichiers[MD_PATH])
        self.assertIn('https://communaute-ia.fr/pack/', fichiers[MD_PATH])
        self.assertNotIn('/dl/', fichiers[MD_PATH])
        for path in (MD_PATH, JSON_PATH):
            self.assertIn(f'href="/{path}" download', pages['pack/index.html'])
            self.assertNotIn(path, pages['pack/merci/index.html'])
        self.assertIn('Seulement les trois extraits gratuits', pages['pack/index.html'])
        self.assertIn('pas d’import universel', pages['pack/index.html'])
        self.assertEqual(fichiers, annexes.construire_annexes([], [], {}, [])[1])


if __name__ == '__main__':
    unittest.main()
