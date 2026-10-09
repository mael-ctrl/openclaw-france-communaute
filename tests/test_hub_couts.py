"""La gratuité du kit ne promet pas un modèle ou un serveur offert."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

SITE = Path(__file__).resolve().parents[1] / "sites" / "openclaw-france"
COUTS = "/guides/demarrer-openclaw-hermes/#couts"


class Document(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.tags = []
        self.text = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

    def handle_data(self, data):
        self.text.append(data)


class HubCoutsTest(unittest.TestCase):
    def setUp(self):
        self.html = (SITE / "index.html").read_text(encoding="utf-8")

    def test_couts_signales_avant_les_boutons_des_kits(self):
        hero = re.search(r'<section class="heros">(.*?)</section>', self.html, re.S).group(1)
        avant_boutons = hero.split('<div class="actions">', 1)[0]
        text = " ".join(Document(avant_boutons).text)
        for repere in ("Kits et guides : 0 €.", "modèle IA", "hébergement", "payant"):
            self.assertIn(repere, text)
        self.assertIn(COUTS, [a.get("href") for t, a in Document(avant_boutons).tags if t == "a"])
        guide = Document((SITE / "guides/demarrer-openclaw-hermes/index.html").read_text())
        self.assertEqual(sum(a.get("id") == "couts" for _, a in guide.tags), 1)

    def test_faq_gratuite_distingue_kit_et_services(self):
        faq = re.findall(r'<details class="faq"[^>]*>(.*?)</details>', self.html, re.S)[0]
        text = " ".join(Document(faq).text)
        for repere in ("kits et guides", "modèle IA", "hébergement", "distincts"):
            self.assertIn(repere, text)
        self.assertIn(COUTS, faq)

    def test_faq_budget_sans_prix_hebergeur_non_verifie(self):
        faqs = re.findall(r'<details class="faq"[^>]*>(.*?)</details>', self.html, re.S)
        faq = next(f for f in faqs if "Il faut un serveur ?" in f)
        text = " ".join(Document(faq).text)
        for repere in ("machine compatible", "modèle IA", "fournisseur", "limite de dépense", "tarifs"):
            self.assertIn(repere, text)
        self.assertNotIn("€/mois", text)
        self.assertNotIn("rabais inclus", text)
        self.assertIn(COUTS, faq)
        partenaire = [a for t, a in Document(faq).tags if t == "a" and "hostinger.com" in a.get("href", "")]
        self.assertEqual(len(partenaire), 1)
        self.assertIn("sponsored", partenaire[0].get("rel", "").split())
        self.assertIn("lien partenaire", text)


if __name__ == "__main__":
    unittest.main()
