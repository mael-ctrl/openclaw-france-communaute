"""Hermes : distinguer téléchargement, installation, configuration et essai."""
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

class HermesInstallationTest(unittest.TestCase):
    def setUp(self):
        self.html = (SITE / "hermes/index.html").read_text(encoding="utf-8")

    def test_texte_et_metadata_sans_delai_ni_compatibilite_universels(self):
        doc = Document(self.html)
        text = doc.texte() + " " + " ".join(a.get("content", "") for tag, a in doc.tags if tag == "meta")
        for promesse in ("quinze minutes", "15 min", "Tous fournisseurs", "tout brancher", "chemin clair, testé", "guide simple, gratuit, testé"):
            self.assertNotIn(promesse, text)
        for name in ("description", "og:description", "twitter:description"):
            meta = next(a for tag, a in doc.tags if tag == "meta" and name in (a.get("name"), a.get("property")))
            self.assertIn("prérequis", meta["content"])
            self.assertIn("kit gratuit", meta["content"])

    def test_limite_avant_boutons_et_parcours_accessible(self):
        hero = re.search(r'<section class="heros">(.*?)</section>', self.html, re.S).group(1)
        note = re.search(r'<p id="avant-installation">(.*?)</p>', hero, re.S)
        self.assertIsNotNone(note)
        self.assertIn("ne configure pas ta machine", Document(note.group(1)).texte())
        self.assertLess(hero.index("avant-installation"), hero.index("actions"))
        self.assertIn("#installation", [a.get("href") for tag, a in Document(note.group(1)).tags if tag == "a"])
        doc = Document(self.html)
        self.assertEqual(sum(a.get("id") == "installation" for _, a in doc.tags), 1)
        section = next(a for tag, a in doc.tags if tag == "section" and a.get("id") == "installation")
        self.assertEqual(section["aria-labelledby"], "titre-installation")
        self.assertEqual(sum(a.get("id") == "titre-installation" for _, a in doc.tags), 1)

    def test_etapes_delegation_modele_et_essai_verifiable(self):
        match = re.search(r'<section id="installation"[^>]*>(.*?)</section>', self.html, re.S)
        self.assertIsNotNone(match)
        self.assertNotIn("<div></div>", match.group(1), "Une cellule vide repousse le texte dans la colonne du numéro")
        doc = Document(match.group(1))
        text = doc.texte()
        for phrase in ("installateur officiel", "hermes model", "fournisseur compatible", "configuration privée", "texte fictif", "réponse sans erreur", "avant de brancher des comptes"):
            self.assertIn(phrase, text)
        links = [a.get("href") for tag, a in doc.tags if tag == "a"]
        for href in ("#prerequis", "/dl/kit-hermes/GUIDE.md", "https://hermes-agent.nousresearch.com/docs/getting-started/quickstart", "#depannage"):
            self.assertIn(href, links)
        self.assertIn(("time", {"datetime": "2026-11-02"}), doc.tags)

if __name__ == "__main__":
    unittest.main()
