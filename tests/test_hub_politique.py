"""Contrats factuels du parcours gratuit, sans validation juridique globale."""
from pathlib import Path
import unittest

SITE = Path(__file__).resolve().parents[1] / "sites/openclaw-france"

def section(html, start, end):
    return html.split(start, 1)[1].split(end, 1)[0]

class HubPolitiqueTest(unittest.TestCase):
    def setUp(self):
        self.html = (SITE / "politique-de-confidentialite/index.html").read_text(encoding="utf-8")
        self.main = section(self.html, "<main>", "</main>")

    def test_parcours_gratuit_et_donnees_historiques_distincts(self):
        bloc = section(self.main, "<h2>2.", "<h3>2.2.")
        for texte in ("téléchargement direct", "sans compte", "sans formulaire", "sans paiement", "données historiques", "À VALIDER"):
            self.assertIn(texte, bloc)
        self.assertNotIn("collectée via la plateforme", bloc)
        self.assertNotIn("livraison du pack d'installation OpenClaw par email", self.main)
        self.assertNotIn("pour la livraison du produit acheté", self.main)

    def test_navigation_distingue_journaux_et_traceurs(self):
        nav = section(self.main, "<h3>2.2.", "<h3>2.3.")
        for texte in ("journaux", "adresse IP", "cache local", "Google Analytics", "code source examiné"):
            self.assertIn(texte, nav)
        self.assertNotIn("si vous acceptez les cookies", nav)
        cookies = section(self.main, "<h2>10.", "<h2>11.")
        self.assertIn("ne prouve pas", cookies)
        self.assertIn("À VALIDER", cookies)
        self.assertNotIn("Notre site utilise des cookies pour améliorer", cookies)

    def test_hebergement_et_retrait_des_anciennes_ressources(self):
        bloc = section(self.main, "<h2>5.", "<h2>6.")
        for texte in ("OVH", "Cloudflare", "retirés", "23 octobre 2026", "Tailwind", "Font Awesome", "Google Fonts"):
            self.assertIn(texte, bloc)
        self.assertNotIn("Qonto : pour le traitement sécurisé", bloc)
        self.assertNotIn("référencent un script Tailwind", bloc)
        for domaine in ("cdn.tailwindcss.com", "cdnjs.cloudflare.com", "fonts.googleapis.com"):
            self.assertNotIn(domaine, self.html)

    def test_perimetre_limite_et_liens_preserves(self):
        self.assertIn("Mise à jour technique : 24 octobre 2026", self.main)
        self.assertIn("clauses juridiques", self.main)
        self.assertIn("restent à valider", self.main)
        self.assertEqual(self.html.count('<link rel="canonical" href="https://openclaw-france.fr/politique-de-confidentialite/">'), 1)
        for href in ("/cgv", "/mentions-legales", "mailto:support@openclaw-france.fr", "https://www.cnil.fr"):
            self.assertIn('href="' + href + '"', self.html)
        self.assertNotIn("<form", self.html)

if __name__ == "__main__":
    unittest.main()
