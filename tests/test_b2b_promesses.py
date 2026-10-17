"""Contrat factuel B2B ; pas une validation juridique ou d'aptitude à vendre."""
import hashlib
import re
import sys
import unittest
from html import unescape
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "engine"))
import construction  # Initialise la dépendance circulaire existante.
import annexes


class PromessesB2BTest(unittest.TestCase):
    def setUp(self):
        self.html = annexes.page_b2b()
        self.corps = self.html.split('<section class="section section-lecture">', 1)[1].rsplit('</section>', 1)[0]
        self.texte = " ".join(unescape(re.sub(r"<[^>]+>", " ", self.corps)).split())

    def test_les_preuves_ne_sont_pas_des_superlatifs_ou_des_chiffres_non_etablis(self):
        for ancien in ["la seule rédaction", "au dixième", "~6,50 $", "0 € encaissés",
                       "1 250+", "1 700+", "15 jours de production continue", "près de 300 passages",
                       "près de 600 pages", "1 085 brèves + 179 articles", "journaux de trafic publics"]:
            with self.subTest(ancien=ancien):
                self.assertFalse(ancien in self.texte, f"Affirmation non étayée conservée : {ancien}")
        for attendu in ["dollars (USD)", "estimation", "pas une comptabilité complète",
                        "cumul indisponible", "attribution incomplète", "ne certifient pas"]:
            with self.subTest(attendu=attendu):
                self.assertTrue(attendu in self.texte, f"Qualification manquante : {attendu}")
        for href in ["/feed.xml", "/transparence/", "/manifeste/",
                     "https://github.com/mael-ctrl/openclaw-france-communaute/actions",
                     "https://github.com/mael-ctrl/openclaw-france-communaute/tree/main/data/preuves"]:
            self.assertIn(f'href="{href}"', self.corps)

    def test_le_constat_de_revenus_reste_date_sans_affirmer_un_etat_actuel(self):
        self.assertIn("Cette page ne présente pas de cumul de revenus", self.texte)
        self.assertNotIn("Revenus : cumul indisponible", self.texte)
        self.assertIn("Le point de suivi du 15 octobre 2026 signalait", self.texte)
        self.assertIn("ce constat daté n'établit pas le montant actuel", self.texte)
        self.assertIn("L'absence de montant ici ne signifie pas zéro revenu", self.texte)
        self.assertIn('blob/4014352641e54cb895df6f41944f72998964ea80/docs/roadmap.md', self.corps)

    def test_la_proposition_ne_promet_ni_sla_ni_paiement_actif(self):
        for ancien in ["alertes sous 30 minutes", "je lis 22 flux en continu", "Je réponds sous 24 h",
                       "lien de paiement sécurisé Stripe", "et je lance", "assurés par l'humain",
                       "Je réponds vite", "Support complet livré 48 h avant", "publication sous 5 jours ouvrés",
                       "mise en route en 72 h", "La mention est visible dès le titre"]:
            with self.subTest(ancien=ancien):
                self.assertFalse(ancien in self.texte, f"Garantie ou activation non prouvée : {ancien}")
        for attendu in ["Proposition à confirmer", "aucun délai garanti", "cadence planifiée",
                        "Objectif de mise en route", "Objectif de publication", "Objectif : support",
                        "Disponibilité à confirmer", "objectif de réponse", "conditions envisagées",
                        "aucun paiement B2B", "30 %", "voix de synthèse", "production par IA"]:
            with self.subTest(attendu=attendu):
                self.assertTrue(attendu in self.texte, f"Qualification manquante : {attendu}")
        for interdit in ["<form", "buy.stripe.com", "checkout.stripe.com", "donate.stripe.com"]:
            self.assertFalse(interdit in self.corps, f"Activation B2B : {interdit}")
        for identifiant in ["offres", "preuves", "deroule", "faq", "contact"]:
            self.assertEqual(self.corps.count(f'id="{identifiant}"'), 1)
        for perimetre in ["3 à 7 items", "6 h 30", "72 h", "5 jours ouvrés", "48 h avant",
                          "90 minutes", "25 personnes", "10 jours ouvrés", "J+30", "30 jours",
                          "rapport mensuel", "récap hebdomadaire", "archive complète", "kit prêt à animer"]:
            self.assertTrue(perimetre in self.texte, f"Périmètre à préserver : {perimetre}")

    def test_les_benefices_sont_un_engagement_non_un_versement_prouve(self):
        for ancien in ["100 % des bénéfices reversés", "chaque euro reçu, chaque euro donné",
                       "justificatifs compris", "chaque euro consigné", "je ne garde rien"]:
            with self.subTest(ancien=ancien):
                self.assertFalse(ancien in self.texte, f"Réalisation non démontrée : {ancien}")
        for attendu in ["Engagement public", "100 % des bénéfices", "associations françaises loi 1901",
                        "pas une preuve de versement", "pas le chiffre d'affaires", "modalités de reversement"]:
            with self.subTest(attendu=attendu):
                self.assertTrue(attendu in self.texte, f"Qualification manquante : {attendu}")
        for interdit in ["TVA non applicable", "293 B", "remboursement garanti", "correction sous 24 h",
                         "pas d'entraînement sur", "accord de traitement des données sur demande"]:
            self.assertFalse(interdit in self.texte, f"Assurance non validée ajoutée : {interdit}")

    def test_les_trois_paragraphes_de_prix_sont_inchanges(self):
        attendus = [
            '<p><strong>Prix indicatif</strong> — <strong>à partir de 2 000 € / mois</strong>, engagement 3 mois,\n'
            '      puis stop net (pas de reconduction piège). Devis ferme après un échange de 20 minutes — gratuit.</p>',
            '<p><strong>Prix indicatif</strong> — <strong>à partir de 2 500 €</strong> la brève + page (30 jours) ·\n'
            '      <strong>4 900 €</strong> la campagne complète (article + 3 brèves + posts Bluesky).</p>',
            '<p><strong>Prix indicatif</strong> — <strong>à partir de 2 000 €</strong> la session ·\n'
            '      <strong>4 500 €</strong> le parcours (2 sessions + supports + 30 jours de questions).</p>',
        ]
        self.assertEqual(re.findall(r"<p><strong>Prix indicatif</strong>.*?</p>", self.corps, re.S), attendus)
        self.assertIn('HT, devis gratuit', self.texte)

    def test_demo_et_telechargements_sont_ceux_du_sha_de_reference(self):
        empreintes = {
            "contenus/b2b/bloc-demo.html": "d60f517906b18eb5f81768042253a05885227f85ac05894919917d1ca54929fa",
            "contenus/b2b/echantillon-veille.html": "38cf28409bc31dfaafbaf34434abb9114f7931a0beb5ee7f5431da28179b74e3",
            "contenus/b2b/echantillon-veille.md": "e1d2b026bdec96a38aebf89765e74563b75bdc1522f1b22ebaa4ae484ea8120b",
            "contenus/b2b/questionnaire-qualification.md": "d6d46bd9e1fbeaeac73a69f0c7eadf12788e6e835be4d17ac8a0be8f7a772768",
            "assets/b2b-demo.css": "6299df85cf80f7f692ed81ac92710550a4a111cf4cfdf72d792016ccd80ab0fa",
        }
        for nom, attendu in empreintes.items():
            with self.subTest(fichier=nom):
                self.assertEqual(hashlib.sha256((RACINE / nom).read_bytes()).hexdigest(), attendu)
        bloc = (RACINE / "contenus/b2b/bloc-demo.html").read_text(encoding="utf-8")
        self.assertEqual(self.corps.count(bloc), 1)


if __name__ == "__main__":
    unittest.main()
