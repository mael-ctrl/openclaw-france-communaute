"""OpenClaw : du kit au premier message, sans installation promise par le ZIP."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

SITE = Path(__file__).resolve().parents[1] / "sites" / "openclaw-france"

class Document(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.tags, self.text = [], []
        self.feed(html)
    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))
    def handle_data(self, text):
        self.text.append(text)
    def texte(self):
        return " ".join(" ".join(self.text).split())

class OpenClawInstallationTest(unittest.TestCase):
    def setUp(self):
        self.html = (SITE / "openclaw/index.html").read_text(encoding="utf-8")

    def test_limite_avant_boutons_et_parcours_accessible(self):
        hero = re.search(r'<section class="heros">(.*?)</section>', self.html, re.S).group(1)
        note = re.search(r'<p id="avant-installation">(.*?)</p>', hero, re.S)
        self.assertIsNotNone(note)
        self.assertIn("ne configure pas ta machine", Document(note.group(1)).texte())
        self.assertLess(hero.index("avant-installation"), hero.index("actions"))
        self.assertIn("#installation", [a.get("href") for t, a in Document(note.group(1)).tags if t == "a"])
        doc = Document(self.html)
        self.assertEqual(sum(a.get("id") == "installation" for t, a in doc.tags), 1)
        section = next(a for t, a in doc.tags if t == "section" and a.get("id") == "installation")
        self.assertEqual(section["aria-labelledby"], "titre-installation")
        self.assertEqual(sum(a.get("id") == "titre-installation" for t, a in doc.tags), 1)

    def test_etapes_configuration_et_premiere_reponse_sans_melange_de_methodes(self):
        section = re.search(r'<section id="installation"[^>]*>(.*?)</section>', self.html, re.S)
        self.assertIsNotNone(section)
        self.assertNotIn("<div></div>", section.group(1), "Les cartes ne doivent pas repousser le texte dans la colonne des numéros")
        doc = Document(section.group(1))
        text = doc.texte()
        for phrase in ("installateur officiel", "fournisseur compatible", "configuration privée", "Installation classique", "openclaw gateway status", "openclaw dashboard", "Docker", "texte fictif", "réponse sans erreur", "avant de brancher tes messageries", "pas une installation testée"):
            self.assertIn(phrase, text)
        links = [a.get("href") for t, a in doc.tags if t == "a"]
        for href in ("#prerequis", "#budget", "#depannage", "#securite-sauvegardes", "/dl/kit-openclaw/GUIDE.md", "https://docs.openclaw.ai/start/getting-started", "https://docs.openclaw.ai/install/docker"):
            self.assertIn(href, links)
        self.assertIn(("time", {"datetime": "2026-11-03"}), doc.tags)
        self.assertEqual(sum(t == "div" and a.get("class") == "etape" for t, a in doc.tags), 3)

    def test_texte_et_metadata_sans_delai_ni_prerequis_automatiques_promis(self):
        doc = Document(self.html)
        text = doc.texte()
        for phrase in ("~30 min", "Trois étapes, et", "Installation automatique des pré-requis"):
            self.assertNotIn(phrase, text)
        self.assertIn("Lance l’installateur officiel", text)
        for name in ("description", "og:description", "twitter:description"):
            meta = next(a for t, a in doc.tags if t == "meta" and name in (a.get("name"), a.get("property")))
            self.assertIn("kit gratuit", meta["content"])
            self.assertIn("premier message", meta["content"])

if __name__ == "__main__":
    unittest.main()
