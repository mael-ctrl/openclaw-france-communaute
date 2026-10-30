"""L’accueil propose des kits à utiliser, pas une installation déjà effectuée."""
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

class AccueilInstallationTest(unittest.TestCase):
    def setUp(self):
        self.html = (SITE / "index.html").read_text(encoding="utf-8")

    def test_pas_de_garantie_installation_securite_delai(self):
        text = Document(self.html).texte()
        for promesse in ("Installés, sécurisés, à toi.", "installés et 100 % gratuits", "ça marche même si", "installé proprement, sécurisé, sauvegardé", "démarrer en quinze minutes", "Sauvegardes automatiques + mises à jour"):
            self.assertNotIn(promesse, text)
        self.assertIn("kits gratuits", re.search(r"<title>(.*?)</title>", self.html).group(1))

    def test_limite_avant_boutons_et_lien_securite_reel(self):
        hero = re.search(r"<section class=.heros.>(.*?)</section>", self.html, re.S).group(1)
        note = re.search(r"<p id=.avant-installation.>(.*?)</p>", hero, re.S)
        self.assertIsNotNone(note)
        self.assertIn("ne configure pas votre machine", Document(note.group(1)).texte())
        self.assertLess(hero.index("avant-installation"), hero.index("actions"))
        href = "/openclaw/#securite-sauvegardes"
        self.assertIn(href, [a.get("href") for tag, a in Document(note.group(1)).tags if tag == "a"])
        target = Document((SITE / "openclaw/index.html").read_text())
        self.assertEqual(sum(a.get("id") == "securite-sauvegardes" for _, a in target.tags), 1)

    def test_sauvegardes_a_planifier_et_prerequis_accessibles(self):
        doc = Document(self.html)
        self.assertIn("Script de sauvegarde à lancer ou à planifier", doc.texte())
        for href in ("/openclaw/#prerequis", "/hermes/#prerequis"):
            self.assertIn(href, [a.get("href") for tag, a in doc.tags if tag == "a"])
            target = Document((SITE / href.split("#")[0].strip("/") / "index.html").read_text())
            self.assertEqual(sum(a.get("id") == "prerequis" for _, a in target.tags), 1)

if __name__ == "__main__":
    unittest.main()
