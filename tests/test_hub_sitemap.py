"""Sitemap du hub : pages finales, canonicals et dates documentaires cohérentes."""
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
import unittest
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET

SITE = Path(__file__).resolve().parents[1] / "sites" / "openclaw-france"
ORIGIN = "https://openclaw-france.fr"
NS = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}


class PageMetadata(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.canonicals = []
        self.documentary_dates = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonicals.append(attrs.get("href"))
        if tag == "time" and attrs.get("datetime"):
            self.documentary_dates.append(date.fromisoformat(attrs["datetime"]))


class HubSitemapTest(unittest.TestCase):
    def setUp(self):
        self.entries = ET.parse(SITE / "sitemap.xml").getroot().findall("s:url", NS)

    def test_chaque_page_index_a_son_url_finale_unique(self):
        expected = {
            ORIGIN + "/" + (p.parent.relative_to(SITE).as_posix().strip(".") + "/").lstrip("/")
            for p in SITE.rglob("index.html")
        }
        urls = [entry.findtext("s:loc", namespaces=NS) for entry in self.entries]
        self.assertEqual(set(urls), expected)
        self.assertEqual(len(urls), len(set(urls)))
        for url in urls:
            with self.subTest(url=url):
                parsed = urlsplit(url)
                self.assertEqual(parsed.scheme, "https")
                self.assertEqual(parsed.netloc, "openclaw-france.fr")
                self.assertFalse(parsed.query or parsed.fragment)
                self.assertTrue(parsed.path.endswith("/"), "Pas de redirection de dossier dans le sitemap")

    def test_url_coherente_avec_la_canonical_existante(self):
        for entry in self.entries:
            url = entry.findtext("s:loc", namespaces=NS)
            page = SITE / urlsplit(url).path.strip("/") / "index.html"
            with self.subTest(url=url):
                meta = PageMetadata(page.read_text())
                if meta.canonicals:
                    self.assertEqual(meta.canonicals, [url])

    def test_lastmod_ne_precede_pas_les_controles_documentaires_affiches(self):
        for entry in self.entries:
            url = entry.findtext("s:loc", namespaces=NS)
            page = SITE / urlsplit(url).path.strip("/") / "index.html"
            with self.subTest(url=url):
                modified = date.fromisoformat(entry.findtext("s:lastmod", namespaces=NS))
                meta = PageMetadata(page.read_text())
                if meta.documentary_dates:
                    self.assertGreaterEqual(modified, max(meta.documentary_dates))


if __name__ == "__main__":
    unittest.main()
