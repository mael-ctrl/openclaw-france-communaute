"""Guide sauvegardes : destinations et lancement shell, sans installer OpenClaw.

Le script du kit est réellement lancé dans un HOME temporaire. Les commandes
OpenClaw/Docker sont des doubles qui enregistrent leurs arguments : ces tests
ne prouvent ni la création d'une archive ni une restauration réelle.
"""
from pathlib import Path
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

SITE = Path(__file__).resolve().parents[1] / "sites/openclaw-france"


class KitOpenClawSauvegardesTest(unittest.TestCase):
    def section(self):
        text = (SITE / "dl/kit-openclaw/GUIDE.md").read_text()
        return text.split("## 5.", 1)[1].split("## 6.", 1)[0]

    def test_destinations_explicites_et_pas_de_liste_trompeuse(self):
        text = self.section()
        for expected in ('MODE=classique bash scripts/sauvegarde.sh',
                         'MODE=docker bash scripts/sauvegarde.sh',
                         '~/Backups/openclaw', 'DOSSIER_BACKUPS',
                         'sauvegardes/', 'MODE=auto'):
            self.assertIn(expected, text)
        self.assertNotIn('ls -lh sauvegardes/', text)
        self.assertIn('pas un essai de restauration', text)
        self.assertIn('2026-10-28', text)

    def test_journal_prepare_avant_cron_et_chemins_entre_guillemets(self):
        text = self.section()
        prep = 'mkdir -p "$HOME/Backups/openclaw-logs"'
        self.assertIn(prep, text)
        self.assertLess(text.index(prep), text.index('30 3 * * *'))
        commands = re.findall(r'^30 3 \* \* \* (.+)$', text, re.M)
        self.assertEqual(len(commands), 2)
        for mode, cmd in zip(('classique', 'docker'), commands):
            self.assertIn('MODE=' + mode + ' /bin/bash "', cmd)
            self.assertIn('>> "$HOME/Backups/openclaw-logs/sauvegarde.log" 2>&1', cmd)
        self.assertIn('une seule', text)
        self.assertIn('PATH', text)

    def run_documented_cron(self, mode):
        text = self.section()
        prep = re.search(r'```bash\n(mkdir -p "\$HOME/Backups/openclaw-logs".*?)```', text, re.S)
        self.assertIsNotNone(prep, 'préparation du dossier de journal absente')
        match = re.search(r'^30 3 \* \* \* (MODE=' + mode + r' .+)$', text, re.M)
        self.assertIsNotNone(match, 'commande cron explicite absente')
        with tempfile.TemporaryDirectory(prefix='kit-backup-guide-') as tmp:
            root = Path(tmp)
            home = root / 'home avec espaces'
            binaries = home / '.local/bin'
            binaries.mkdir(parents=True)
            kit = root / 'kit avec espaces'
            shutil.copytree(SITE / 'dl/kit-openclaw', kit)
            # Aucun binaire réel ni secret du compte n'est utilisé.
            recorder = ('#!' + sys.executable + '\nimport json, os, sys\n'
                        'from pathlib import Path\n'
                        'Path(os.environ["TEST_CALL"]).write_text(json.dumps(sys.argv[1:]))\n')
            for binary in ('openclaw', 'docker'):
                target = binaries / binary
                target.write_text(recorder)
                target.chmod(0o700)
            env = {'HOME': str(home), 'PATH': os.defpath, 'TMPDIR': str(root),
                   'TEST_CALL': str(root / 'call.json')}
            ready = subprocess.run(['/bin/sh', '-c', prep.group(1)], env=env,
                                   cwd=root, capture_output=True, text=True, timeout=15)
            self.assertEqual(ready.returncode, 0, ready.stderr)
            cmd = match.group(1).replace('/chemin/vers/kit-openclaw', str(kit))
            run = subprocess.run(['/bin/sh', '-c', cmd], env=env, cwd=root,
                                 capture_output=True, text=True, timeout=15)
            self.assertEqual(run.returncode, 0, run.stderr)
            args = json.loads((root / 'call.json').read_text())
            if mode == 'classique':
                self.assertEqual(args, ['backup', 'create', '--output',
                                       str(home / 'Backups/openclaw'), '--verify'])
                self.assertTrue((home / 'Backups/openclaw').is_dir())
            else:
                self.assertEqual(args, ['compose', 'run', '-T', '--rm', 'openclaw-cli',
                                       'backup', 'create', '--output',
                                       '/home/node/sauvegardes', '--verify'])
                self.assertTrue((kit / 'sauvegardes').is_dir())
            log = home / 'Backups/openclaw-logs/sauvegarde.log'
            self.assertIn('Méthode détectée : ' + mode, log.read_text())

    def test_lancement_cron_classique_home_et_kit_avec_espaces(self):
        self.run_documented_cron('classique')

    def test_lancement_cron_docker_home_et_kit_avec_espaces(self):
        self.run_documented_cron('docker')


if __name__ == '__main__':
    unittest.main()
