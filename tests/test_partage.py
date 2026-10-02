"""Contrat des aperçus de partage — stdlib seule, sans API ni mutation de data/."""
import json
import struct
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "engine"))

import config
import construction


class Metadonnees(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.valeurs = {}
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        if tag == "meta":
            attrs = dict(attrs)
            cle = attrs.get("property") or attrs.get("name")
            self.valeurs.setdefault(cle, []).append(attrs.get("content"))


class ApercuPartageTest(unittest.TestCase):
    def test_pages_partageables_avec_banniere_deployee(self):
        breves = json.loads(config.FICHIER_BREVES.read_text(encoding="utf-8"))
        articles = [json.loads(p.read_text(encoding="utf-8"))
                    for p in config.DOSSIER_ARTICLES.glob("*.json")]
        pages = [construction.page("Titre & test", "Description", "", "/"),
                 construction.page_actus(breves)]
        pages += [construction.page_breve(b, breves) for b in breves]
        pages += [construction.page_article(a, articles) for a in articles]
        for html in pages:
            meta = Metadonnees(html).valeurs
            self.assertEqual(meta.get("og:image"),
                             [config.URL_SITE + "/assets/og-crabe.png"])
            self.assertEqual(meta.get("og:image:type"), ["image/png"])
            self.assertEqual(meta.get("og:image:width"), ["1200"])
            self.assertEqual(meta.get("og:image:height"), ["630"])
            self.assertEqual(meta.get("twitter:card"), ["summary_large_image"])
            self.assertEqual(meta.get("twitter:image"), meta["og:image"])
            self.assertEqual(meta.get("twitter:image:alt"), meta.get("og:image:alt"))
            self.assertTrue(meta.get("og:image:alt", [""])[0])
        image = (config.DOSSIER_ASSETS / "og-crabe.png").read_bytes()
        self.assertEqual(image[:8], b"\x89PNG\r\n\x1a\n")
        self.assertEqual(struct.unpack(">II", image[16:24]), (1200, 630))
        self.assertLess(len(image), 2_000_000)


if __name__ == "__main__":
    unittest.main()
