"""Le pseudo-élément CSS numérote les cartes : aucun enfant vide supplémentaire."""
from html.parser import HTMLParser
from pathlib import Path
import unittest

SITE = Path(__file__).resolve().parents[1] / "sites" / "openclaw-france"

class StepParser(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.depth = 0
        self.active = None
        self.steps = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        if tag != "div":
            return
        if self.active is not None and self.depth == self.active["depth"]:
            self.active["children"] += 1
        self.depth += 1
        if "etape" in dict(attrs).get("class", "").split():
            self.active = {"depth": self.depth, "children": 0, "text": []}
            self.steps.append(self.active)

    def handle_endtag(self, tag):
        if tag != "div":
            return
        if self.active is not None and self.depth == self.active["depth"]:
            self.active = None
        self.depth -= 1

    def handle_data(self, text):
        if self.active is not None:
            self.active["text"].append(text)

class HubStepLayoutTest(unittest.TestCase):
    def test_une_cellule_de_contenu_apres_le_numero_css(self):
        checked = []
        for page in sorted(SITE.rglob("*.html")):
            steps = StepParser(page.read_text(encoding="utf-8")).steps
            if steps:
                checked.append(page.relative_to(SITE).as_posix())
            for index, step in enumerate(steps, 1):
                with self.subTest(page=page.relative_to(SITE), card=index):
                    self.assertEqual(step["children"], 1,
                        "Une cellule vide repousse le texte sous le numéro dans la colonne de 52 px")
                    self.assertTrue(" ".join(step["text"]).strip())
        self.assertIn("gratuit/index.html", checked)
        self.assertIn("openclaw/index.html", checked)
        self.assertIn("hermes/index.html", checked)

if __name__ == "__main__":
    unittest.main()
