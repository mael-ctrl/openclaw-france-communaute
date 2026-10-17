"""Une date absente ne devient ni publication ni modification."""
import json
import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))
import construction


def newsarticle(contenu):
    objets = [json.loads(x) for x in re.findall(
        r'<script type="application/ld\+json">(.*?)</script>', contenu, re.S)]
    return next(x for x in objets if x.get("@type") == "NewsArticle")


class DatesJsonldTest(unittest.TestCase):
    def test_dates_inconnues_omises_sans_repli_sur_la_publication(self):
        for publication, modification in ((None, None), ("", ""),
                                          ("2026-10-01T10:00:00Z", None),
                                          (None, "2026-10-02T10:00:00+02:00")):
            with self.subTest(publication=publication, modification=modification):
                donnees = newsarticle(construction.jsonld_item(
                    "NewsArticle", "https://example.org/a/", "Titre", "Résumé",
                    publication, modification, "Brèves", []))
                self.assertEqual(donnees.get("datePublished"), publication or None)
                self.assertEqual(donnees.get("dateModified"), modification or None)
                if not publication:
                    self.assertNotIn("datePublished", donnees)
                if not modification:
                    self.assertNotIn("dateModified", donnees)

    def test_les_gabarits_ne_transforment_pas_les_dates_editoriales_en_preuve(self):
        breve = {"slug": "b", "titre": "Brève", "resume": "Texte.",
                 "source": "Source", "lien_source": "https://example.org/"}
        article = {"slug": "a", "titre": "Article", "chapo": "Chapeau.",
                   "html": "<p>Texte.</p>"}
        for source, redaction in (("2026-10-01T10:00:00Z", "2026-10-02T12:00:00Z"),
                                  ("2026-10-03T10:00:00Z", "2026-10-02T12:00:00Z"),
                                  (None, "2026-10-02T12:00:00Z"), (None, None)):
            for rendu in (construction.page_breve(
                    {**breve, "date_source": source, "date_redac": redaction}, []),
                    construction.page_article({**article, "date": redaction}, [])):
                with self.subTest(source=source, redaction=redaction, page=newsarticle(rendu)["@id"]):
                    donnees = newsarticle(rendu)
                    self.assertNotIn("datePublished", donnees)
                    self.assertNotIn("dateModified", donnees)


if __name__ == "__main__":
    unittest.main()
