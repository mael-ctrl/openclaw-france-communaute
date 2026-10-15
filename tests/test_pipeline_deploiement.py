"""Contrats hors réseau : vrai CLI, déployeur, journal et preuves ; E/S distantes simulées.

Exécution : python3 -B -m unittest discover -s tests -p test_pipeline_deploiement.py -v
PIPELINE_REPO permet de vérifier une autre COPIE du code. Aucun data réel importé.
"""
import contextlib
import hashlib
import json
import os
from pathlib import Path
import runpy
import socket
import subprocess
import sys
import tempfile
import time
import unittest
from unittest import mock

REPO = Path(os.environ.get('PIPELINE_REPO', Path(__file__).resolve().parents[1])).resolve()
TESTS = Path(__file__).resolve().parent


def worker(repo, racine, scenario, arguments):
    """Exécute réellement __main__, dans un enfant sans credentials ni réseau."""
    os.environ.clear()
    sys.dont_write_bytecode = True
    sys.path.insert(0, str(repo / 'engine'))
    with contextlib.ExitStack() as pile:
        pile.enter_context(mock.patch('socket.socket.connect', side_effect=AssertionError('réseau interdit')))
        pile.enter_context(mock.patch('socket.create_connection', side_effect=AssertionError('réseau interdit')))
        pile.enter_context(mock.patch('subprocess.Popen', side_effect=AssertionError('processus/credentials interdits')))
        import config
        import collecte
        import construction
        import deepseek
        import deploiement
        import indexnow
        import journal
        import preuves
        import redaction
        import social
        import archive

        data = racine / 'data'
        sortie = racine / '_site'
        data.mkdir()
        sortie.mkdir()
        config.RACINE = racine
        config.DOSSIER_DATA = data
        config.DOSSIER_SORTIE = sortie
        config.DOSSIER_ARTICLES = data / 'articles'
        config.DOSSIER_ARTICLES.mkdir()
        for cle, nom in [('FICHIER_STATS', 'stats.json'), ('FICHIER_JOURNAL', 'journal.jsonl'),
                         ('FICHIER_BREVES', 'breves.json'), ('FICHIER_ETAT', 'etat.json'),
                         ('FICHIER_SOCIAL_ETAT', 'social_etat.json'),
                         ('FICHIER_DEPLOY_ETAT', 'deploy_etat.json')]:
            setattr(config, cle, data / nom)
        config.DEEPSEEK_CLE = 'fixture-non-secrete'
        config.FTP_SERVEUR = 'ftp.invalid'
        config.FTP_UTILISATEUR = 'fixture'
        config.FTP_DOSSIER = 'www'
        config.URL_SITE = 'https://exemple.invalid'
        preuves.DOSSIER_PREUVES = data / 'preuves'
        preuves.DOSSIER_PREUVES.mkdir()
        preuves.FICHIER_PUBLICATIONS = data / 'publications.jsonl'
        jour = time.strftime('%Y-%m-%d', time.gmtime())
        for nom in ['manifeste-2000-01-01.json', f'manifeste-{jour}.json']:
            (preuves.DOSSIER_PREUVES / nom).write_text('{"fixture_immuable":true}\n')
        manifestes_avant = {p.name: p.read_bytes() for p in preuves.DOSSIER_PREUVES.iterdir()}
        journal.ajouter('fixture_anterieure', note='ne jamais réécrire')
        prefixe = config.FICHIER_JOURNAL.read_bytes()
        config.FICHIER_DEPLOY_ETAT.write_text('{"ancien.html":[7,1]}\n')
        config.FICHIER_SOCIAL_ETAT.write_text('{"publies":{"ancien":{}}}\n')
        social_avant = config.FICHIER_SOCIAL_ETAT.read_bytes()
        appels = []
        etat_avant = None

        def rediger_breves(items):
            breves = [{'id': 'neuf', 'slug': 'neuf', 'titre': 'Fixture non publiée',
                       'resume': 'Synthétique', 'date_redac': '2026-10-15T07:00:00+00:00'}]
            config.FICHIER_BREVES.write_text(json.dumps(breves))
            return breves

        def rediger_articles(items):
            article = {'slug': 'neuf', 'titre': 'Article synthétique', 'html': '<p>Fixture</p>',
                       'date': '2026-10-15T07:00:00+00:00'}
            (config.DOSSIER_ARTICLES / 'neuf.json').write_text(json.dumps(article))
            return [article]

        def construire():
            nonlocal etat_avant
            appels.append('build')
            for nom in ['index.html', 'breves/neuf/index.html', 'articles/neuf/index.html']:
                p = sortie / nom
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text('<html>Fixture isolée</html>')
            if scenario == 'noop':
                etat = {p.relative_to(sortie).as_posix(): [p.stat().st_size, int(p.stat().st_mtime)]
                        for p in sortie.rglob('*') if p.is_file()}
                config.FICHIER_DEPLOY_ETAT.write_text(json.dumps(etat))
            etat_avant = config.FICHIER_DEPLOY_ETAT.read_bytes()
            return 3

        class FTPDouble:
            def __init__(self, *args, **kwargs):
                appels.append('ftp')
                self.envois = 0
                if scenario == 'connexion':
                    raise OSError('421 échec FTP simulé')

            def login(self, *args):
                if scenario == 'auth':
                    raise deploiement.ftplib.error_perm('530 authentification refusée (fixture)')

            def set_pasv(self, *args):
                pass

            def cwd(self, *args):
                pass

            def storbinary(self, commande, fichier, **kwargs):
                self.envois += 1
                if scenario == 'partiel' and self.envois == 2:
                    raise OSError('426 transfert interrompu (fixture)')
                appels.append('upload')
                fichier.read()

            def quit(self):
                if scenario == 'quit':
                    raise OSError('421 fermeture FTP échouée (fixture)')

        def appeler(nom, retour):
            def action(*args, **kwargs):
                appels.append(nom)
                return retour
            return action

        apres_run_reel = preuves.apres_run

        def apres_run():
            appels.append('preuves')
            return apres_run_reel()

        for module, nom, remplacement in [
            (collecte, 'collecter', lambda: ([{'id': 'nouveau'}], [])),
            (deepseek, 'solde', lambda: {'total': 10}),
            (redaction, 'rediger_breves', rediger_breves),
            (redaction, 'rediger_articles_si_besoin', rediger_articles),
            (construction, 'construire', construire),
            (deploiement.ftplib, 'FTP', FTPDouble),
            (deploiement, '_mot_de_passe', lambda: 'fixture-non-secrete'),
            (indexnow, 'ecrire_cle', lambda: None),
            (indexnow, 'signaler', appeler('indexation', 202)),
            (archive, 'archiver_si_necessaire', appeler('archive', 'fixture')),
            (social, 'disponible', appeler('social_disponible', True)),
            (social, 'diffuser', appeler('diffusion', 1)),
            (preuves, 'apres_run', apres_run),
        ]:
            pile.enter_context(mock.patch.object(module, nom, remplacement))
        sys.argv = [str(repo / 'engine/run.py'), *arguments]
        try:
            runpy.run_path(str(repo / 'engine/run.py'), run_name='__main__')
        except SystemExit as exc:
            code = exc.code
        else:
            raise AssertionError('Le CLI doit terminer par SystemExit(main()).')
        lignes = journal.lire_journal()
        resultat = {
            'code': code, 'appels': appels, 'journal': lignes,
            'prefixe_intact': config.FICHIER_JOURNAL.read_bytes().startswith(prefixe),
            'manifestes_intacts': manifestes_avant == {
                p.name: p.read_bytes() for p in preuves.DOSSIER_PREUVES.iterdir()},
            'etat_ftp_intact': config.FICHIER_DEPLOY_ETAT.read_bytes() == etat_avant,
            'etat_social_intact': config.FICHIER_SOCIAL_ETAT.read_bytes() == social_avant,
            'breves_conservees': json.loads(config.FICHIER_BREVES.read_text())[0]['id'] == 'neuf',
            'article_conserve': (config.DOSSIER_ARTICLES / 'neuf.json').exists(),
            'registre_present': preuves.FICHIER_PUBLICATIONS.exists(),
            'stats': journal.charger_stats(),
        }
        (racine / 'resultat.json').write_text(json.dumps(resultat, ensure_ascii=False, indent=2))
        print('TRACE_FIXTURE=' + json.dumps({'code': code, 'appels': appels}, ensure_ascii=False))
        return code


class PipelineDeploiementTests(unittest.TestCase):
    def executer(self, scenario='succes', *arguments):
        with tempfile.TemporaryDirectory(prefix='fixture-', dir=TESTS) as dossier:
            racine = Path(dossier)
            resultat = subprocess.run(
                [sys.executable, '-B', str(Path(__file__).resolve()), '--worker', str(REPO),
                 str(racine), scenario, json.dumps(arguments)],
                cwd=REPO, env={'PYTHONDONTWRITEBYTECODE': '1'},
                capture_output=True, text=True, timeout=20)
            self.assertTrue((racine / 'resultat.json').exists(), resultat.stdout + resultat.stderr)
            info = json.loads((racine / 'resultat.json').read_text())
            self.assertEqual(info['code'], resultat.returncode, resultat.stderr)
            return resultat, info

    def test_echec_ftp_est_un_echec_du_processus(self):
        resultat, info = self.executer('connexion', '--tout')
        self.assertNotEqual(resultat.returncode, 0, resultat.stdout)

    def test_aucune_annonce_apres_echec_ftp(self):
        for scenario in ['connexion', 'auth', 'partiel', 'quit']:
            with self.subTest(scenario=scenario):
                resultat, info = self.executer(scenario, '--tout')
                self.assertEqual(resultat.returncode, 1, resultat.stdout)
                for action in ['indexation', 'archive', 'social_disponible', 'diffusion']:
                    self.assertNotIn(action, info['appels'], resultat.stdout)

    def test_sans_deploiement_ne_diffuse_pas_de_pages_locales(self):
        resultat, info = self.executer('succes', '--sans-deploiement')
        self.assertEqual(resultat.returncode, 0, resultat.stdout)
        for action in ['ftp', 'indexation', 'archive', 'social_disponible', 'diffusion']:
            self.assertNotIn(action, info['appels'], resultat.stdout)

    def test_bilan_signale_explicitement_lechec(self):
        resultat, info = self.executer('connexion', '--tout')
        self.assertIn('Échec du déploiement', resultat.stdout)
        self.assertNotIn('🦀 Terminé', resultat.stdout)
        bilan = [e for e in info['journal'] if e['evenement'] == 'bilan'][-1]
        self.assertEqual(bilan['details'].get('deploiement'), 'echec')

    def test_succes_reste_vert_et_annonce_apres_ftp(self):
        resultat, info = self.executer('succes', '--tout')
        self.assertEqual(resultat.returncode, 0, resultat.stdout)
        self.assertIn('🦀 Terminé', resultat.stdout)
        self.assertEqual(info['appels'], ['build', 'ftp', 'upload', 'upload', 'upload',
                                         'indexation', 'archive', 'social_disponible', 'diffusion', 'preuves'])
        evenements = [e for e in info['journal'] if e['evenement'] == 'deploiement']
        self.assertEqual(evenements[0]['details']['fichiers'], 3)
        self.assertFalse(info['etat_ftp_intact'])

    def test_noop_incremental_reste_un_succes(self):
        resultat, info = self.executer('noop', '--tout')
        self.assertEqual(resultat.returncode, 0, resultat.stdout)
        self.assertNotIn('upload', info['appels'])
        self.assertIn('indexation', info['appels'])
        self.assertIn('diffusion', info['appels'])
        evenement = next(e for e in info['journal'] if e['evenement'] == 'deploiement')
        self.assertEqual(evenement['details'], {'fichiers': 0, 'octets': 0})

    def test_essai_reste_vert_sans_ftp_annonces_ni_preuves(self):
        resultat, info = self.executer('connexion', '--essai')
        self.assertEqual(resultat.returncode, 0, resultat.stdout)
        self.assertEqual(info['appels'], ['build'])
        self.assertIn('(mode essai)', resultat.stdout)
        self.assertFalse(info['registre_present'])

    def test_echec_conserve_donnees_preuves_et_cache_ftp(self):
        for scenario in ['connexion', 'auth', 'partiel', 'quit']:
            with self.subTest(scenario=scenario):
                resultat, info = self.executer(scenario, '--tout')
                for cle in ['prefixe_intact', 'manifestes_intacts', 'etat_ftp_intact',
                            'etat_social_intact', 'breves_conservees', 'article_conserve', 'registre_present']:
                    self.assertTrue(info[cle], f'{scenario}: {cle}')
                self.assertEqual(info['stats']['runs'], 1)
                self.assertIn('preuves', info['appels'])
                evenements = [e['evenement'] for e in info['journal']]
                self.assertIn('erreur', evenements)
                self.assertIn('bilan', evenements)
                self.assertNotIn('deploiement', evenements)
                self.assertNotIn('indexation', evenements)
                for entree in info['journal']:
                    empreinte = entree.pop('sha256')
                    contenu = json.dumps(entree, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
                    self.assertEqual(empreinte, hashlib.sha256(contenu.encode()).hexdigest())


class WorkflowDeploiementTests(unittest.TestCase):
    def setUp(self):
        self.workflow = (REPO / '.github/workflows/maj.yml').read_text()
        self.pipeline = self.workflow.split('      - name: Pipeline ', 1)[1].split('      - name:', 1)[0]
        self.sauvegarde = self.workflow.split("      - name: Consigner l'état", 1)[1]

    def test_sauvegarde_apres_succes_ou_echec_non_annule(self):
        # Contrat statique : la sémantique GitHub Actions sera validée après intégration.
        self.assertIn('        id: pipeline\n', self.pipeline)
        condition = "if: ${{ !cancelled() && (steps.pipeline.outcome == 'success' || steps.pipeline.outcome == 'failure') }}"
        self.assertIn(condition, self.sauvegarde)

    def test_echec_pipeline_non_masque(self):
        self.assertNotIn('continue-on-error', self.workflow)
        self.assertIn('run: python engine/run.py --tout\n', self.pipeline)
        self.assertNotIn('|| true', self.pipeline)
        self.assertIn('git add data\n', self.sauvegarde)
        self.assertIn('exit 1\n', self.sauvegarde)
        self.assertIn('cancel-in-progress: false\n', self.workflow)

    def test_script_sauvegarde_syntaxe_bash(self):
        bloc = self.sauvegarde.split('        run: |\n', 1)[1]
        script = '\n'.join(ligne[10:] for ligne in bloc.splitlines()) + '\n'
        resultat = subprocess.run(['bash', '-n'], input=script, capture_output=True, text=True)
        self.assertEqual(resultat.returncode, 0, resultat.stderr)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--worker':
        raise SystemExit(worker(Path(sys.argv[2]), Path(sys.argv[3]), sys.argv[4], json.loads(sys.argv[5])))
    unittest.main()
