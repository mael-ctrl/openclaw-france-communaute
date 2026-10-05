"""Fidélisation en fin de lecture, sans JS ni service supplémentaire."""
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))

import config
import construction


class BlocSuivi(HTMLParser):
    def __init__(self, document):
        super().__init__()
        self.blocs = 0
        self.dans_bloc = False
        self.liens = []
        self.texte = []
        self.feed(document)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "aside" and attrs.get("aria-labelledby") == "suivre-le-crabe":
            self.blocs += 1
            self.dans_bloc = True
        if self.dans_bloc and tag == "a":
            self.liens.append(attrs)

    def handle_endtag(self, tag):
        if tag == "aside":
            self.dans_bloc = False

    def handle_data(self, data):
        if self.dans_bloc:
            self.texte.append(data)


class SuivreTest(unittest.TestCase):
    def test_breve_propose_le_flux_et_le_profil_apres_la_lecture(self):
        breve = {
            "slug": "essai", "titre": "Une actualité IA", "resume": "Résumé sourcé.",
            "source": "Source de test", "lien_source": "https://example.org/source",
            "date_redac": "2026-10-05T12:00:00+00:00", "tags": ["IA"],
        }
        document = construction.page_breve(breve, [breve])
        bloc = BlocSuivi(document)
        self.assertEqual(bloc.blocs, 1, "Une invitation à suivre doit figurer après la brève")
        self.assertEqual([a["href"] for a in bloc.liens],
                         [config.URL_SITE + "/feed.xml",
                          "https://bsky.app/profile/" + config.BLUESKY_HANDLE])
        self.assertIn("Ajouter ce flux à votre lecteur RSS", " ".join(bloc.texte))
        self.assertIn("https://communaute-ia.fr/feed.xml", " ".join(bloc.texte))
        self.assertLess(document.index('</article>'), document.index('aria-labelledby="suivre-le-crabe"'))
        self.assertLess(document.index('aria-labelledby="suivre-le-crabe"'), document.index('À lire aussi'))
        self.assertNotIn('onclick', document)

    def test_article_propose_le_suivi_avant_les_articles_lies(self):
        article = {
            "slug": "analyse", "titre": "Une analyse IA", "chapo": "Introduction.",
            "html": "<p>Analyse sourcée.</p>", "date": "2026-10-05T12:00:00+00:00",
            "tags": ["IA"], "sources": [{"nom": "Source", "url": "https://example.org/"}],
        }
        document = construction.page_article(article, [article])
        bloc = BlocSuivi(document)
        self.assertEqual(bloc.blocs, 1, "Une invitation à suivre doit figurer après l'article")
        self.assertEqual([a["href"] for a in bloc.liens],
                         [config.URL_SITE + "/feed.xml",
                          "https://bsky.app/profile/" + config.BLUESKY_HANDLE])
        self.assertLess(document.index('</article>'), document.index('aria-labelledby="suivre-le-crabe"'))
        self.assertLess(document.index('aria-labelledby="suivre-le-crabe"'), document.index('Autres articles'))
        self.assertNotIn('onclick', document)


if __name__ == "__main__":
    unittest.main()
