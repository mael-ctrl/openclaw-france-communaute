"""L'accueil mène aux extraits gratuits, jamais directement au paiement."""
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))

import annexes
import construction


class Liens(HTMLParser):
    def __init__(self, document):
        super().__init__()
        self.liens = []
        self.ids = []
        self.feed(document)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a":
            self.liens.append(attrs)
        if attrs.get("id"):
            self.ids.append(attrs["id"])


class AccueilExtraitsTest(unittest.TestCase):
    def test_accueil_propose_un_essai_gratuit_avant_les_explications(self):
        document = construction.page_accueil([], [], {}, [])
        liens = Liens(document)
        essais = [a for a in liens.liens if a.get("href") == "/pack/#extraits-pack"]
        self.assertEqual(len(essais), 1, "Un accès direct aux extraits manque sur l'accueil")
        self.assertIn("bouton", essais[0].get("class", ""))
        self.assertIn("Essayer les 3 prompts gratuits", document)
        self.assertIn("sans inscription", document)
        self.assertIn("Le pack complet reste payant", document)
        self.assertLess(document.index('href="/pack/#extraits-pack"'),
                        document.index("// COMMENT CE SITE FONCTIONNE"))
        self.assertIn("extraits-pack", Liens(annexes.page_pack()).ids)
        self.assertNotIn("onclick", document)
        self.assertFalse(any("buy.stripe.com" in a.get("href", "") for a in liens.liens))


if __name__ == "__main__":
    unittest.main()
