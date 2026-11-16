"""Le premier essai mène au dépannage pertinent, sans réinstallation aveugle."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

SITE = Path(__file__).resolve().parents[1] / "sites/openclaw-france"
ROUTE = "guides/demarrer-openclaw-hermes/index.html"

class Document(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.ids, self.links, self.text = [], [], []
        self.link = None
        self.feed(html)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "a":
            self.link = {"attrs": attrs, "text": ""}
            self.links.append(self.link)
    def handle_data(self, data):
        self.text.append(data)
        if self.link is not None:
            self.link["text"] += data
    def handle_endtag(self, tag):
        if tag == "a":
            self.link = None

class GuideDepannageTest(unittest.TestCase):
    def aide(self):
        html = (SITE / ROUTE).read_text()
        section = re.search(r'<section id="demarrer".*?</section>', html, re.S).group()
        aide = re.search(r'<p class="guide-note" id="aide-installation">.*?</p>', section, re.S)
        self.assertIsNotNone(aide, "Le parcours ne propose pas le dépannage après la première tâche")
        self.assertGreater(aide.start(), section.index("</ol>"))
        self.assertEqual(Document(html).ids.count("aide-installation"), 1)
        return Document(aide.group())

    def test_liens_natifs_explicites_apres_la_premiere_tache(self):
        links = self.aide().links
        self.assertEqual([(l["attrs"].get("href"), l["text"]) for l in links], [
            ("/openclaw/#depannage", "dépannage OpenClaw"),
            ("/hermes/#depannage", "dépannage Hermes Agent")])
        for link in links:
            for attr in ("onclick", "target", "aria-label", "tabindex"):
                self.assertNotIn(attr, link["attrs"])

    def test_cibles_de_depannage_existantes_et_uniques(self):
        for slug in ("openclaw", "hermes"):
            html = (SITE / slug / "index.html").read_text()
            self.assertEqual(Document(html).ids.count("depannage"), 1)
            self.assertRegex(html, r'<section id="depannage"[^>]*aria-labelledby="titre-depannage"')

    def test_orientation_et_garde_fous_preserves(self):
        text = " ".join(self.aide().text)
        for expected in ("passerelle", "accès distant", "authentification", "commande introuvable",
                         "modèle", "diagnostic", "avant de relancer un script",
                         "Ne supprimez pas votre configuration ou vos sauvegardes",
                         "masquez les clés API, jetons et données personnelles"):
            self.assertIn(expected, text)
        html = (SITE / ROUTE).read_text()
        self.assertIn("Aucun délai de réponse ni support individuel n’est garanti.", html)
        self.assertIn("https://github.com/mael-ctrl/openclaw-france-communaute/issues", html)

if __name__ == "__main__":
    unittest.main()
