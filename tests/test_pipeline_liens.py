"""Garde avant FTP : vrai vérificateur et vrai journal, réseau interdit par le worker."""
import unittest
import test_pipeline_deploiement as pipeline


class PipelineLiensTests(unittest.TestCase):
    executer = pipeline.PipelineDeploiementTests.executer

    def test_bon_lien_scan_apres_build_et_cle_avant_ftp(self):
        resultat, info = self.executer('liens-bon', '--tout')
        self.assertEqual(resultat.returncode, 0, resultat.stdout)
        self.assertEqual(info['appels'][:4], ['build', 'cle_locale', 'liens', 'ftp'])
        self.assertEqual(info['appels'][-5:], ['indexation', 'archive', 'social_disponible', 'diffusion', 'preuves'])
        scan, = info['scans_liens']
        self.assertTrue(scan['build_intact'])
        r = scan['rapport']
        self.assertEqual(r['errors'], [])
        self.assertIs(r['complete'], True)
        self.assertEqual(r['stats']['checked'], 2)
        self.assertEqual(r['stats']['html_files'], 3)
        self.assertEqual(r['budgets'], {'files': 10000, 'bytes': 100000000, 'page_bytes': 2000000,
                                       'links': 200000, 'depth': 32})
        evenements = [e['evenement'] for e in info['journal']]
        self.assertLess(evenements.index('construction'), evenements.index('verification_liens'))
        self.assertLess(evenements.index('verification_liens'), evenements.index('deploiement'))

    def verifier_refus_reel(self, scenario, code):
        resultat, info = self.executer(scenario, '--tout')
        self.assertEqual(resultat.returncode, 1, resultat.stdout)
        self.assertEqual(info['appels'], ['build', 'liens', 'preuves'])
        self.assertNotIn('🦀 Terminé', resultat.stdout)
        scan, = info['scans_liens']
        self.assertTrue(scan['build_intact'])
        self.assertIn(code, [e['code'] for e in scan['rapport']['errors']])
        for cle in ['prefixe_intact', 'manifestes_intacts', 'etat_ftp_intact',
                    'etat_social_intact', 'breves_conservees', 'article_conserve', 'registre_present']:
            self.assertTrue(info[cle], cle)
        return scan['rapport']

    def test_fragment_absent_refuse(self):
        r = self.verifier_refus_reel('liens-fragment', 'missing_fragment')
        self.assertTrue(r['complete'])  # Complet ne signifie pas sans défaut.

    def test_quota_reel_refuse(self):
        r = self.verifier_refus_reel('liens-quota', 'budget_exceeded')
        self.assertFalse(r['complete'])
        self.assertIn('page_bytes', [e.get('dimension') for e in r['errors']])

    def test_symlink_reel_refuse(self):
        r = self.verifier_refus_reel('liens-symlink', 'symlink_refused')
        self.assertFalse(r['complete'])

    def test_build_sans_html_refuse(self):
        self.verifier_refus_reel('liens-sans-html', 'no_html')

    def test_essai_et_sans_deploiement_ne_scannent_ni_nannoncent(self):
        for mode in ['--essai', '--sans-deploiement']:
            with self.subTest(mode=mode):
                resultat, info = self.executer('liens-cible', mode)
                self.assertEqual(resultat.returncode, 0, resultat.stdout)
                self.assertEqual(info['scans_liens'], [])
                self.assertEqual(info['appels'], ['build'] if mode == '--essai' else ['build', 'preuves'])
                self.assertTrue(info['etat_ftp_intact'])

    def test_sans_redaction_conserve_garde_et_deploiement_si_bon(self):
        for scenario, attendu in [('liens-bon', 0), ('liens-cible', 1)]:
            with self.subTest(scenario=scenario):
                resultat, info = self.executer(scenario, '--sans-redaction')
                self.assertEqual(resultat.returncode, attendu, resultat.stdout)
                self.assertIn('liens', info['appels'])
                self.assertEqual('ftp' in info['appels'], attendu == 0)
                self.assertFalse(info['breves_conservees'])
                self.assertFalse(info['article_conserve'])
                self.assertEqual(info['stats']['breves_publiees'], 0)
                self.assertEqual(info['stats']['articles_publies'], 0)

    def test_url_site_non_qualifiable_refuse(self):
        for cas in ['vide', 'scheme', 'port', 'chemin', 'user', 'dns']:
            with self.subTest(cas=cas):
                resultat, info = self.executer('liens-url-' + cas, '--tout')
                self.assertEqual(resultat.returncode, 1, resultat.stdout)
                for action in ['ftp', 'indexation', 'archive', 'social_disponible', 'diffusion']:
                    self.assertNotIn(action, info['appels'])
                self.assertNotIn('🦀 Terminé', resultat.stdout)

    def test_diagnostic_incorrect_refuse(self):
        for scenario in ['schema', 'erreurs-null', 'compteur', 'vide', 'budget',
                         'hote', 'retour-null', 'exception']:
            with self.subTest(scenario=scenario):
                resultat, info = self.executer('liens-' + scenario, '--tout')
                self.assertEqual(resultat.returncode, 1, resultat.stdout)
                self.assertEqual(info['appels'], ['build', 'liens', 'preuves'])
                self.assertNotIn('🦀 Terminé', resultat.stdout)

    def test_diagnostic_tronque_ou_types_incorrects_refuse(self):
        for scenario in ['champ-absent', 'stats-incompletes', 'schema-bool', 'stats-bool', 'exemptions-null']:
            with self.subTest(scenario=scenario):
                resultat, info = self.executer('liens-' + scenario, '--tout')
                self.assertEqual(resultat.returncode, 1, resultat.stdout)
                self.assertEqual(info['appels'], ['build', 'liens', 'preuves'])

    def test_diagnostic_incomplet_sans_erreurs_refuse(self):
        resultat, info = self.executer('liens-incomplet', '--tout')
        self.assertEqual(resultat.returncode, 1, resultat.stdout)
        self.assertEqual(info['appels'], ['build', 'liens', 'preuves'])
        self.assertNotIn('🦀 Terminé', resultat.stdout)

    def test_cible_absente_refuse_avant_ftp_et_annonces(self):
        resultat, info = self.executer('liens-cible', '--tout')
        self.assertEqual(resultat.returncode, 1, resultat.stdout)
        for action in ['ftp', 'upload', 'indexation', 'archive', 'social_disponible', 'diffusion']:
            self.assertNotIn(action, info['appels'])
        self.assertNotIn('🦀 Terminé', resultat.stdout)
        self.assertIn('preuves', info['appels'])
        for cle in ['prefixe_intact', 'manifestes_intacts', 'etat_ftp_intact',
                    'etat_social_intact', 'breves_conservees', 'article_conserve', 'registre_present']:
            self.assertTrue(info[cle], cle)
        bilan = [e for e in info['journal'] if e['evenement'] == 'bilan'][-1]
        self.assertEqual(bilan['details'].get('deploiement'), 'echec')


if __name__ == '__main__':
    unittest.main()
