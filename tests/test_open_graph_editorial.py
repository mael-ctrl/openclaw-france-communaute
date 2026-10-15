"""Les pages éditoriales sont identifiées comme articles lors du partage."""
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "engine"))

import construction


class Metadonnees(HTMLParser):
    def __init__(self, contenu):
        super().__init__()
        self.metas = []
        self.feed(contenu)

    def handle_starttag(self, tag, attrs):
        if tag == "meta":
            self.metas.append(dict(attrs))

    def valeurs(self, propriete):
        return [m.get("content") for m in self.metas
                if m.get("property") == propriete]


class OpenGraphEditorialTest(unittest.TestCase):
    def test_breve_est_un_article_et_garde_sa_canonique(self):
        breve = {
            "slug": "essai-breve", "titre": "Brève & IA", "resume": "Résumé.",
            "source": "Source", "lien_source": "https://example.org/source",
            "date_redac": "2026-10-15T10:00:00+00:00", "tags": [],
        }
        meta = Metadonnees(construction.page_breve(breve, []))
        self.assertEqual(meta.valeurs("og:type"), ["article"])
        self.assertEqual(meta.valeurs("og:url"),
                         [construction.config.URL_SITE + "/breves/essai-breve/"])

    def test_article_est_un_article_avec_date_open_graph(self):
        article = {
            "slug": "essai-article", "titre": "Une analyse", "chapo": "Chapeau.",
            "html": "<p>Texte.</p>", "date": "2026-10-15T10:30:00+00:00",
            "tags": [], "sources": [],
        }
        meta = Metadonnees(construction.page_article(article, []))
        self.assertEqual(meta.valeurs("og:type"), ["article"])
        self.assertEqual(meta.valeurs("article:published_time"), [article["date"]])
        self.assertFalse(any(m.get("name") == "article:published_time" for m in meta.metas))
        self.assertEqual(meta.valeurs("og:url"),
                         [construction.config.URL_SITE + "/articles/essai-article/"])

    def test_article_sans_date_omet_la_propriete(self):
        for date in (None, ""):
            with self.subTest(date=date):
                article = {"slug": "sans-date", "titre": "Analyse", "chapo": "Texte.",
                           "html": "<p>Texte.</p>", "date": date}
                meta = Metadonnees(construction.page_article(article, []))
                self.assertEqual(meta.valeurs("og:type"), ["article"])
                self.assertEqual(meta.valeurs("article:published_time"), [])

    def test_pages_non_editoriales_gardent_website(self):
        pages = [construction.page_accueil([], [], {}, []),
                 construction.page_actus([]), construction.page_articles([]),
                 construction.page("Skills", "Fiches", "<p>Fiches.</p>", "/skills/"),
                 construction.page("404", "Introuvable", "", "/404.html", robots="noindex")]
        for contenu in pages:
            meta = Metadonnees(contenu)
            self.assertEqual(meta.valeurs("og:type"), ["website"])
            self.assertEqual(meta.valeurs("article:published_time"), [])

    def test_titre_et_chapo_echappes_sans_modifier_image(self):
        titre = 'Analyse "IA" </script><script>alert(1)</script> & 🦀'
        article = {"slug": "echappement", "titre": titre, "chapo": titre,
                   "html": "<p>Texte.</p>", "date": "2026-10-15T10:30:00+00:00"}
        contenu = construction.page_article(article, [])
        meta = Metadonnees(contenu)
        self.assertEqual(meta.valeurs("og:title"), [titre + " — " + construction.config.NOM_SITE])
        self.assertEqual(meta.valeurs("og:description"), [titre])
        self.assertNotIn("<script>alert(1)</script>", contenu)
        self.assertEqual(meta.valeurs("og:image"),
                         [construction.config.URL_SITE + "/assets/og-crabe.png"])


if __name__ == "__main__":
    unittest.main()
