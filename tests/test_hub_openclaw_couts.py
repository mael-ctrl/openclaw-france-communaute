"""OpenClaw : gratuité du kit, budget et lien partenaire sans promesses tarifaires."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

SITE = Path(__file__).resolve().parents[1] / "sites" / "openclaw-france"
PARTENAIRE = "https://www.hostinger.com/fr?REFERRALCODE=FGUOPENCL2M5"
COUTS = "/guides/demarrer-openclaw-hermes/#couts"


class Document(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.tags, self.text = [], []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

    def handle_data(self, data):
        self.text.append(data)


class OpenClawCoutsTest(unittest.TestCase):
    def setUp(self):
        self.html = (SITE / "openclaw/index.html").read_text(encoding="utf-8")

    def budget(self):
        section = re.search(r'<section id="budget"[^>]*>(.*?)</section>', self.html, re.S)
        self.assertIsNotNone(section, "Section budget absente")
        return Document(section.group(1))

    def test_couts_signales_avant_boutons_et_ancre_accessible(self):
        hero = re.search(r'<section class="heros">(.*?)</section>', self.html, re.S).group(1)
        avant = Document(hero.split('<div class="actions">', 1)[0])
        texte = " ".join(" ".join(avant.text).split())
        for repere in ("Kit et guides : 0 €.", "modèle IA", "hébergement", "payants"):
            self.assertIn(repere, texte)
        self.assertIn("#budget", [a.get("href") for t, a in avant.tags if t == "a"])
        tags = Document(self.html).tags
        sections = [a for t, a in tags if a.get("id") == "budget"]
        self.assertEqual(len(sections), 1)
        self.assertEqual(sections[0]["aria-labelledby"], "titre-budget")
        self.assertEqual(sum(a.get("id") == "titre-budget" for t, a in tags), 1)

    def test_budget_distingue_machine_modele_et_conditions_hebergement(self):
        doc = self.budget()
        texte = " ".join(" ".join(doc.text).split())
        for repere in ("machine compatible", "allumée", "connectée", "ressources", "modèle IA",
                       "limite de dépense", "tarifs", "renouvellement", "paiement initial", "taxes"):
            self.assertIn(repere, texte)
        liens = [a.get("href") for t, a in doc.tags if t == "a"]
        self.assertIn(COUTS, liens)
        self.assertIn("#prerequis", liens)
        guide = Document((SITE / "guides/demarrer-openclaw-hermes/index.html").read_text())
        self.assertEqual(sum(a.get("id") == "couts" for t, a in guide.tags), 1)
        self.assertEqual(sum(a.get("id") == "prerequis" for t, a in Document(self.html).tags), 1)

    def test_partenaire_facultatif_identique_sans_promesse_de_remise(self):
        doc = self.budget()
        texte = " ".join(" ".join(doc.text).split())
        for repere in ("lien partenaire", "facultatif", "autre hébergeur", "Aucun achat", "aucune remise"):
            self.assertIn(repere, texte)
        for promesse in ("€/mois", "rabais déjà appliqué", "rabais inclus", "zéro surcoût", "importe quel hébergeur", "En ligne en quelques minutes"):
            self.assertNotIn(promesse, self.html)
        liens = [a for t, a in doc.tags if t == "a" and "hostinger.com" in a.get("href", "")]
        self.assertEqual(len(liens), 2)
        for lien in liens:
            self.assertEqual(lien["href"], PARTENAIRE)
            self.assertEqual(lien["target"], "_blank")
            self.assertTrue({"sponsored", "noopener"}.issubset(set(lien.get("rel", "").split())))


if __name__ == "__main__":
    unittest.main()
