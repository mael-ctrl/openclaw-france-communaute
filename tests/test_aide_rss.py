"""Un mode d'emploi RSS accessible sans script à la fin des lectures."""
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))
import config
import construction


class AideRSS(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.details = []
        self.summaries = 0
        self.codes = []
        self.in_code = False
        self.text = []
        self.forbidden = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        if tag == "details":
            self.details.append(dict(attrs))
        if tag == "summary":
            self.summaries += 1
        if tag == "code":
            self.in_code = True
            self.codes.append("")
        if tag in ("script", "form", "iframe", "input"):
            self.forbidden.append(tag)

    def handle_endtag(self, tag):
        if tag == "code":
            self.in_code = False

    def handle_data(self, data):
        self.text.append(data)
        if self.in_code:
            self.codes[-1] += data


class AideRSSTest(unittest.TestCase):
    def test_mode_emploi_natif_avec_les_deux_adresses_a_copier(self):
        html = construction.bloc_suivre()
        aide = AideRSS(html)
        self.assertEqual(len(aide.details), 1, "Il manque le mode d'emploi dépliable")
        self.assertNotIn("open", aide.details[0], "Le mode d'emploi est fermé au départ")
        self.assertEqual(aide.summaries, 1)
        self.assertEqual(aide.codes[-2:], [config.URL_SITE + "/feed.xml",
                                         config.URL_SITE + "/feed-articles.xml"])
        text = " ".join(aide.text)
        for phrase in ("Première fois avec un flux RSS ?", "Ajouter un flux",
                       "Copiez", "Validez", "XML", "n’envoie pas d’emails",
                       "confidentialité", "payant"):
            self.assertIn(phrase, text)
        self.assertEqual(aide.forbidden, [])
        self.assertNotIn("onclick", html)


if __name__ == "__main__":
    unittest.main()
