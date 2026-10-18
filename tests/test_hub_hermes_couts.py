"""Budget Hermes : distinguer le kit gratuit des services et de la machine."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

SITE = Path(__file__).resolve().parents[1] / "sites" / "openclaw-france"
COUTS = "/guides/demarrer-openclaw-hermes/#couts"
SOURCE = "https://hermes-agent.nousresearch.com/docs/getting-started/quickstart#2-choose-a-provider"


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


class HermesCoutsTest(unittest.TestCase):
    def setUp(self):
        self.html = (SITE / "hermes/index.html").read_text(encoding="utf-8")
        self.faqs = re.findall(r'<details\b[^>]*>(.*?)</details>', self.html, re.S)

    def test_budget_visible_avant_boutons_et_ancre_unique(self):
        hero = re.search(r'<section class="heros">(.*?)</section>', self.html, re.S).group(1)
        avant = hero.split('<div class="actions">', 1)[0]
        doc = Document(avant)
        text = " ".join(doc.text)
        for mot in ("Kit et guides : 0 €.", "modèle IA", "outils", "hébergement", "payants"):
            self.assertIn(mot, text)
        self.assertIn("#budget", [a.get("href") for t, a in doc.tags if t == "a"])
        self.assertEqual(sum(a.get("id") == "budget" for _, a in Document(self.html).tags), 1)

    def test_budget_sans_promesse_de_cout_universel(self):
        faq = next(f for f in self.faqs if "Ça coûte combien, au total ?" in f)
        doc = Document(faq)
        text = " ".join(" ".join(doc.text).split())
        for mot in ("kit", "0 €", "API", "abonnement", "modèle local", "outils", "matériel", "électricité", "limite de dépense", "fournisseur"):
            self.assertIn(mot, text)
        for promesse in ("centimes par jour", "usage normal", "quelques euros par mois"):
            self.assertNotIn(promesse, self.html)
        links = [a.get("href") for t, a in doc.tags if t == "a"]
        self.assertIn(COUTS, links)
        self.assertIn(SOURCE, links)
        self.assertIn(("time", {"datetime": "2026-10-18"}), doc.tags)
        guide = Document((SITE / "guides/demarrer-openclaw-hermes/index.html").read_text())
        self.assertEqual(sum(a.get("id") == "couts" for _, a in guide.tags), 1)

    def test_hebergement_conditionnel_partenaire_signale_sans_prix_invente(self):
        faq = next(f for f in self.faqs if "Je peux le faire tourner 24 h/24 ?" in f)
        doc = Document(faq)
        text = " ".join(" ".join(doc.text).split())
        for mot in ("machine compatible", "allumée", "connectée", "ressources", "tarifs", "lien partenaire", "obligatoire"):
            self.assertIn(mot, text)
        self.assertNotIn("€/mois", faq)
        self.assertNotIn("rabais inclus", faq)
        liens = [a for t, a in doc.tags if t == "a" and "hostinger.com" in a.get("href", "")]
        self.assertEqual(len(liens), 1)
        self.assertEqual(liens[0]["href"], "https://www.hostinger.com/fr?REFERRALCODE=FGUOPENCL2M5")
        self.assertTrue({"sponsored", "noopener"}.issubset(set(liens[0].get("rel", "").split())))


if __name__ == "__main__":
    unittest.main()
