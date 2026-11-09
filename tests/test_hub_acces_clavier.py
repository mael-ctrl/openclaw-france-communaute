"""Accès direct natif au contenu, avant les liens de navigation répétés."""
from html.parser import HTMLParser
from pathlib import Path
import unittest

SITE = Path(__file__).resolve().parents[1] / "sites" / "openclaw-france"
ROUTES = ("index.html", "openclaw/index.html", "hermes/index.html", "gratuit/index.html",
          "temoignages/index.html", "cgv/index.html", "guides/demarrer-openclaw-hermes/index.html")

class Balises(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.tags = []
        self.feed(html)
    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

class HubAccesClavierTest(unittest.TestCase):
    def test_premier_lien_vers_le_contenu_sans_javascript(self):
        for route in ROUTES:
            with self.subTest(route=route):
                tags = Balises((SITE / route).read_text()).tags
                liens = [a for t, a in tags if t == "a"]
                self.assertEqual(liens[0].get("href"), "#contenu")
                self.assertNotIn("onclick", liens[0])
                self.assertNotIn("tabindex", liens[0])
                self.assertTrue(set(liens[0].get("class", "").split()) & {"skip-link", "skip-guide"})

    def test_cible_main_unique_et_focusable_sans_tabulation_supplementaire(self):
        for route in ROUTES:
            with self.subTest(route=route):
                tags = Balises((SITE / route).read_text()).tags
                cibles = [(t, a) for t, a in tags if a.get("id") == "contenu"]
                self.assertEqual(len(cibles), 1)
                tag, attrs = cibles[0]
                self.assertEqual(tag, "main")
                self.assertEqual(attrs.get("tabindex"), "-1")
                self.assertNotIn("aria-hidden", attrs)

    def test_lien_visible_au_focus_sans_masquer_le_contenu(self):
        css = (SITE / "static/style.css").read_text()
        self.assertRegex(css, r"\.skip-link\s*\{[^}]*position:fixed")
        self.assertRegex(css, r"\.skip-link:focus\s*\{[^}]*transform:translateY\(0\)")
        self.assertRegex(css, r"#contenu\s*\{[^}]*scroll-margin-top:80px")
        self.assertNotRegex(css, r"\.skip-link\s*\{[^}]*(?:display:none|visibility:hidden)")

if __name__ == "__main__":
    unittest.main()
