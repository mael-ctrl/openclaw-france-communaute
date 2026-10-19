"""Le podcast existant est découvrable avant de parcourir la page d’accueil."""
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))
import construction
import podcast
import config


class ActionsAccueil(HTMLParser):
    def __init__(self, document):
        super().__init__()
        self.dans_hero = False
        self.liens = []
        self.lien = None
        self.feed(document)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "section" and "hero" in attrs.get("class", "").split():
            self.dans_hero = True
        if tag == "a" and self.dans_hero:
            self.lien = {**attrs, "texte": ""}
            self.liens.append(self.lien)

    def handle_data(self, data):
        if self.lien is not None:
            self.lien["texte"] += data

    def handle_endtag(self, tag):
        if tag == "a":
            self.lien = None
        if tag == "section":
            self.dans_hero = False


class AccueilPodcastTest(unittest.TestCase):
    def test_hero_propose_un_lien_natif_vers_le_podcast_sans_retirer_les_actions(self):
        document = construction.page_accueil([], [], {}, [])
        actions = ActionsAccueil(document).liens
        ecoute = [a for a in actions if a.get("href") == "/podcast/"]
        self.assertEqual(len(ecoute), 1, "Le podcast reste caché dans le pied de page")
        self.assertEqual(ecoute[0]["texte"], "Écouter le podcast")
        self.assertIn("bouton", ecoute[0].get("class", "").split())
        self.assertNotIn("onclick", ecoute[0])
        self.assertNotIn("target", ecoute[0])
        self.assertEqual([a["href"] for a in actions], ["/actus/", "/manifeste/", "/podcast/"])
        self.assertLess(document.index('href="/podcast/"'), document.index("// DERNIÈRES ACTUS"))
        self.assertNotIn("<audio", document, "Aucun téléchargement audio ajouté à l’accueil")
        self.assertIn('href="/pack/#extraits-pack"', document)
        self.assertIn('href="https://openclaw-france.fr"', document)
        episodes = podcast.charger_episodes(config.RACINE)
        destination = podcast.page_ecoute(episodes, config.URL_SITE)
        self.assertIn('<audio controls preload="none"', destination)
        self.assertIn('href="/podcast/feed.xml"', destination)
        self.assertIn("voix synthétique", destination)


if __name__ == "__main__":
    unittest.main()
