"""Les lectures liées privilégient les sujets communs, sans appel à une IA."""
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))
import construction


class LecturesLiees(HTMLParser):
    def __init__(self, document):
        super().__init__()
        self.dans_bloc = False
        self.liens = []
        self.feed(document)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "aside":
            self.dans_bloc = attrs.get("class") == "a-cote" and not attrs.get("aria-labelledby")
        if self.dans_bloc and tag == "a":
            self.liens.append(attrs["href"])

    def handle_endtag(self, tag):
        if tag == "aside":
            self.dans_bloc = False


def contenu(slug, tags=None):
    return {"slug": slug, "titre": "Sujet " + slug, "resume": "Résumé.",
            "chapo": "Introduction.", "html": "<p>Analyse sourcée.</p>",
            "source": "Source de test", "lien_source": "https://example.org/",
            "date_redac": "2026-10-07T10:00:00+00:00",
            "date": "2026-10-07T10:00:00+00:00", "tags": tags}


class LecturesLieesTest(unittest.TestCase):
    def test_breve_ne_recommande_pas_une_page_hors_du_perimetre_construit(self):
        courant = contenu("courant", ["hermes"])
        candidats = [courant] + [contenu(f"recent-{i}", ["dev"]) for i in range(399)]
        candidats.append(contenu("non-construite", ["hermes"]))
        liens = LecturesLiees(construction.page_breve(courant, candidats)).liens
        self.assertNotIn("/breves/non-construite/", liens)
        self.assertEqual(liens, [f"/breves/recent-{i}/" for i in range(3)])

    def test_sans_tags_ou_sans_sujet_commun_garde_les_plus_recents(self):
        for tags in (None, [], ["inconnu"]):
            with self.subTest(tags=tags):
                courant = contenu("courant", tags)
                candidats = [courant, contenu("recent"), contenu("suivant", []),
                             contenu("ancien", ["dev"]), contenu("dernier")]
                avant = list(candidats)
                self.assertEqual([x["slug"] for x in construction.lectures_liees(courant, candidats)],
                                 ["recent", "suivant", "ancien"])
                self.assertEqual(candidats, avant, "Ne pas modifier l'ordre du registre")

    def test_egalite_de_tags_conserve_l_ordre_des_candidats(self):
        courant = contenu("courant", ["agents"])
        candidats = [contenu(slug, ["agents"]) for slug in ("recent", "suivant", "ancien", "dernier")]
        self.assertEqual([x["slug"] for x in construction.lectures_liees(courant, candidats)],
                         ["recent", "suivant", "ancien"])

    def test_liste_vide_et_auto_recommandation_ne_creent_aucun_lien(self):
        courant = contenu("courant", ["agents"])
        self.assertEqual(construction.lectures_liees(courant, []), [])
        self.assertEqual(construction.lectures_liees(courant, [courant]), [])
        self.assertEqual(construction.lectures_liees(courant, [courant, contenu("autre")]),
                         [contenu("autre")])

    def test_titres_des_lectures_liees_restent_echappes(self):
        courant = contenu("courant", ["agents"])
        autre = contenu("autre", ["agents"])
        autre["titre"] = '<script>alert("test")</script> & IA'
        for rendre in (construction.page_breve, construction.page_article):
            document = rendre(courant, [courant, autre])
            self.assertIn('&lt;script&gt;alert(&quot;test&quot;)&lt;/script&gt; &amp; IA', document)
            self.assertNotIn('<script>alert("test")</script>', document)

    def test_pages_privilegient_les_tags_communs_a_la_seule_recence(self):
        courant = contenu("courant", ["hermes", "agents"])
        candidats = [courant, contenu("recent", ["matériel"]),
                     contenu("partiel", ["agents"]), contenu("hors-sujet", ["business"]),
                     contenu("proche", ["hermes", "agents"])]
        for famille, rendre in (("breves", construction.page_breve),
                                ("articles", construction.page_article)):
            with self.subTest(famille=famille):
                liens = LecturesLiees(rendre(courant, candidats)).liens
                self.assertEqual(liens, [f"/{famille}/{slug}/"
                                         for slug in ("proche", "partiel", "recent")])


if __name__ == "__main__":
    unittest.main()
