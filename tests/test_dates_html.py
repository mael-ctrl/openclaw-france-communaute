"""Dates HTML lisibles, sans changement des instants éditoriaux stockés."""
import json
import re
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "engine"))
import construction


class Dates(HTMLParser):
    def __init__(self, contenu):
        super().__init__()
        self.dates = []
        self.courante = None
        self.feed(contenu)

    def handle_starttag(self, tag, attrs):
        if tag == "time":
            self.courante = {"attrs": dict(attrs), "texte": ""}
            self.dates.append(self.courante)

    def handle_data(self, data):
        if self.courante is not None:
            self.courante["texte"] += data

    def handle_endtag(self, tag):
        if tag == "time":
            self.courante = None


ARTICLE = {"slug": "essai", "titre": "Une analyse", "chapo": "Résumé.",
           "html": "<p>Corps intact.</p>", "date": "2026-10-16T11:15:03+00:00"}
BREVE = {"slug": "essai", "titre": "Une brève", "resume": "Résumé.",
         "source": "Source", "lien_source": "https://example.org/source",
         "date_source": "2026-10-15T22:30:00+00:00",
         "date_redac": "2026-10-16T11:15:03+00:00"}


class DatesHTMLTest(unittest.TestCase):
    def test_article_date_semantique_et_heure_de_paris(self):
        contenu = construction.page_article(ARTICLE, [])
        dates = Dates(contenu).dates
        self.assertEqual(dates[0]["attrs"].get("datetime"), ARTICLE["date"])
        self.assertEqual(dates[0]["texte"], "16 oct. 2026 · 13:15 (Paris)")
        self.assertIn("<p>Corps intact.</p>", contenu)
        news = [json.loads(s) for s in re.findall(
            r'<script type="application/ld\+json">(.*?)</script>', contenu)]
        news = next(s for s in news if s.get("@type") == "NewsArticle")
        self.assertEqual(news["datePublished"], ARTICLE["date"])
        self.assertEqual(news["dateModified"], ARTICLE["date"])

    def test_tous_les_emplacements_editoriaux_partagent_le_meme_rendu(self):
        for contenu, attendues in (
            (construction.carte_article(ARTICLE), [ARTICLE["date"]]),
            (construction.carte_breve(BREVE), [BREVE["date_source"]]),
            (construction.page_breve(BREVE, []), [BREVE["date_source"], BREVE["date_redac"]]),
            (construction.page_article(ARTICLE, []), [ARTICLE["date"], ARTICLE["date"]]),
            (construction.page_accueil([], [ARTICLE], {}, []), [ARTICLE["date"]]),
            (construction.carte_breve({**BREVE, "date_source": None}), [BREVE["date_redac"]]),
        ):
            with self.subTest(attendues=attendues, debut=contenu[:50]):
                dates = Dates(contenu).dates
                self.assertEqual([d["attrs"].get("datetime") for d in dates], attendues)
                self.assertTrue(all(d["texte"].endswith(" (Paris)") for d in dates))

    def test_ete_hiver_changement_de_jour_et_decalage_source(self):
        cas = [
            ("2026-01-15T23:30:00Z", "16 janv. 2026 · 00:30 (Paris)"),
            ("2026-07-15T23:30:00+00:00", "16 juil. 2026 · 01:30 (Paris)"),
            ("2026-10-25T00:30:00+00:00", "25 oct. 2026 · 02:30 (Paris)"),
            ("2026-10-25T01:30:00+00:00", "25 oct. 2026 · 02:30 (Paris)"),
            ("2026-10-16T05:00:00-04:00", "16 oct. 2026 · 11:00 (Paris)"),
        ]
        for iso, visible in cas:
            with self.subTest(iso=iso):
                date = Dates(construction.date_html(iso)).dates[0]
                self.assertEqual(date["attrs"]["datetime"], iso)
                self.assertEqual(date["texte"], visible)

    def test_breve_garde_les_dates_jsonld_et_le_lien_source(self):
        contenu = construction.page_breve(BREVE, [])
        news = next(json.loads(s) for s in re.findall(
            r'<script type="application/ld\+json">(.*?)</script>', contenu)
            if json.loads(s).get("@type") == "NewsArticle")
        self.assertEqual(news["datePublished"], BREVE["date_source"])
        self.assertEqual(news["dateModified"], BREVE["date_redac"])
        self.assertIn('href="https://example.org/source"', contenu)
        self.assertIn("16 oct. 2026 · 00:30 (Paris)", contenu)

    def test_dates_absentes_ne_creent_pas_de_balise_vide(self):
        for contenu in (construction.carte_article({**ARTICLE, "date": None}),
                        construction.page_article({**ARTICLE, "date": None}, []),
                        construction.page_breve({**BREVE, "date_source": None, "date_redac": None}, [])):
            self.assertEqual(Dates(contenu).dates, [])

    def test_date_inconnue_ou_invalide_ne_fabrique_pas_un_instant(self):
        for valeur in (None, "", 'date <script>alert(1)</script>',
                       "2026-02-30T10:00:00+00:00", "2026-10-16T10:00:00", "2026-10-16", 42):
            with self.subTest(valeur=valeur):
                rendu = construction.date_html(valeur)
                self.assertEqual(Dates(rendu).dates, [])
                self.assertNotIn("<script>", rendu)
                self.assertNotIn("(Paris)", rendu)
        self.assertEqual(construction.date_html(None), "")
        self.assertEqual(construction.date_html(""), "")


if __name__ == "__main__":
    unittest.main()
