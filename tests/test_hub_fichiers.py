"""Le parcours « Parcourir les fichiers » reste guidé et exhaustif."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest
from urllib.parse import urlsplit

SITE = Path(__file__).resolve().parents[1] / "sites" / "openclaw-france"


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


class HubFichiersTest(unittest.TestCase):
    def test_le_bouton_mene_a_un_catalogue_identifie_sans_javascript(self):
        for kit in ("openclaw", "hermes"):
            with self.subTest(kit=kit):
                html = (SITE / kit / "index.html").read_text(encoding="utf-8")
                hero = Document(html.split("</section>", 1)[0])
                buttons = [a for t, a in hero.tags if t == "a" and "btn-secondaire" in a.get("class", "")]
                self.assertEqual([a.get("href") for a in buttons], ["#fichiers"])
                document = Document(html)
                ids = [a["id"] for _, a in document.tags if "id" in a]
                self.assertEqual(len(ids), len(set(ids)))
                self.assertIn("titre-fichiers", ids)
                sections = [a for t, a in document.tags if t == "section" and a.get("id") == "fichiers"]
                self.assertEqual(len(sections), 1)
                self.assertEqual(sections[0].get("aria-labelledby"), "titre-fichiers")
                self.assertFalse(any(t in ("script", "form", "iframe") for t, _ in document.tags))

    def test_tous_les_fichiers_du_kit_sont_lies_avec_une_description(self):
        for kit in ("openclaw", "hermes"):
            with self.subTest(kit=kit):
                html = (SITE / kit / "index.html").read_text(encoding="utf-8")
                document = Document(html)
                links = [a["href"] for t, a in document.tags if t == "a" and a.get("class") == "fichier"]
                files = {"/" + p.relative_to(SITE).as_posix() for p in (SITE / "dl" / ("kit-" + kit)).rglob("*") if p.is_file()}
                self.assertEqual(set(links), files)
                self.assertEqual(len(links), len(files))
                cards = re.findall('<a class="fichier".*?</a>', html, re.S)
                self.assertEqual(len(cards), len(files))
                for card in cards:
                    self.assertRegex(card, r"<small>[^<]+</small>")
                for link in links:
                    self.assertTrue((SITE / urlsplit(link).path.lstrip("/")).is_file())
                self.assertTrue(all(not link.endswith("/.env") for link in links))

    def test_le_catalogue_indique_quoi_lire_avant_execution(self):
        for kit in ("openclaw", "hermes"):
            with self.subTest(kit=kit):
                html = (SITE / kit / "index.html").read_text(encoding="utf-8")
                section = re.search('<section id="fichiers"[^>]*>(.*?)</section>', html, re.S)
                self.assertIsNotNone(section)
                text = " ".join(Document(section.group(1)).text)
                for notice in ("README.md", "GUIDE.md", "avant de", "scripts", "sans compte", "clés API"):
                    self.assertIn(notice, text)


if __name__ == "__main__":
    unittest.main()
