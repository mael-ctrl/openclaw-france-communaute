"""Les sources visibles restent identiques dans les données structurées."""
import json
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "engine"))

import construction


class DonneesStructurees(HTMLParser):
    def __init__(self, contenu):
        super().__init__()
        self.blocs = []
        self.script = None
        self.feed(contenu)

    def handle_starttag(self, tag, attrs):
        if tag == "script" and dict(attrs).get("type") == "application/ld+json":
            self.script = ""

    def handle_data(self, data):
        if self.script is not None:
            self.script += data

    def handle_endtag(self, tag):
        if tag == "script" and self.script is not None:
            self.blocs.append(json.loads(self.script))
            self.script = None


def newsarticle(contenu):
    return next(b for b in DonneesStructurees(contenu).blocs
                if b.get("@type") == "NewsArticle")


class CitationsJsonldTest(unittest.TestCase):
    def test_breve_declare_la_source_deja_visible(self):
        breve = {
            "slug": "test-source", "titre": "Une brève", "resume": "Résumé sourcé.",
            "source": "Média & recherche", "lien_source": "https://example.org/article?a=1&b=2",
            "date_redac": "2026-10-08T10:00:00+00:00", "tags": ["agents"],
        }
        contenu = construction.page_breve(breve, [breve])
        self.assertIn('href="https://example.org/article?a=1&amp;b=2"', contenu)
        donnees = newsarticle(contenu)
        self.assertEqual(donnees.get("citation"), [{
            "@type": "CreativeWork", "url": breve["lien_source"], "name": breve["source"],
        }])
        self.assertEqual(donnees["datePublished"], breve["date_redac"])
        self.assertEqual(donnees["dateModified"], breve["date_redac"])

    def test_article_declare_toutes_les_sources_visibles(self):
        sources = [
            {"nom": "Publication originale", "url": "https://example.org/original"},
            {"nom": "Média & analyse", "url": "https://example.net/analyse?q=ia&lang=fr"},
        ]
        article = {
            "slug": "analyse", "titre": "Analyse", "chapo": "Deux sources.",
            "html": "<p>Texte.</p>", "date": "2026-10-08T11:00:00+00:00",
            "sources": sources, "tags": [],
        }
        contenu = construction.page_article(article, [article])
        for source in sources:
            self.assertIn('href="' + construction.ech(source["url"]) + '"', contenu)
        donnees = newsarticle(contenu)
        self.assertEqual(donnees.get("citation"), [
            {"@type": "CreativeWork", "url": s["url"], "name": s["nom"]} for s in sources
        ])
        self.assertEqual(donnees["datePublished"], article["date"])
        self.assertEqual(donnees["dateModified"], article["date"])

    def test_aucune_citation_inventee_si_source_absente(self):
        for sources in (None, [], [{"nom": "Source sans lien", "url": ""}]):
            with self.subTest(sources=sources):
                contenu = construction.jsonld_item(
                    "NewsArticle", "https://example.org/article/", "Titre", "Résumé",
                    "2026-10-08T10:00:00+00:00", None, "Brèves", [], sources)
                self.assertNotIn("citation", newsarticle(contenu))

    def test_caracteres_speciaux_ne_ferment_pas_le_script(self):
        nom = 'Média "IA" </script><script>alert(1)</script> & recherche 🦀'
        url = "https://example.org/article?texte=%3Cscript%3E&lang=fr"
        contenu = construction.jsonld_item(
            "NewsArticle", "https://example.org/article/", "Titre", "Résumé",
            "2026-10-08T10:00:00+00:00", None, "Brèves", [],
            [{"nom": nom, "url": url}])
        self.assertEqual(contenu.count("</script>"), 1)
        self.assertNotIn("<script>alert(1)", contenu)
        self.assertEqual(newsarticle(contenu)["citation"], [
            {"@type": "CreativeWork", "url": url, "name": nom}
        ])

    def test_sources_reelles_du_perimetre_construit(self):
        import config
        breves = json.loads(config.FICHIER_BREVES.read_text(encoding="utf-8"))[:400]
        articles = [json.loads(p.read_text(encoding="utf-8"))
                    for p in config.DOSSIER_ARTICLES.glob("*.json")]
        for b in breves:
            with self.subTest(breve=b["slug"]):
                citations = newsarticle(construction.page_breve(b, breves))["citation"]
                self.assertEqual(citations, [{"@type": "CreativeWork",
                                              "url": b["lien_source"], "name": b["source"]}])
        for a in articles:
            with self.subTest(article=a["slug"]):
                citations = newsarticle(construction.page_article(a, articles)).get("citation", [])
                self.assertEqual(citations, [
                    {"@type": "CreativeWork", "url": s["url"], "name": s["nom"]}
                    for s in (a.get("sources") or []) if s.get("url")])


if __name__ == "__main__":
    unittest.main()
