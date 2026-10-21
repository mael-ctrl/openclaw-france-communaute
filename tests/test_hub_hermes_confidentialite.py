"""Contrats documentaires : confidentialité Hermes, sans toucher au kit."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

SITE = Path(__file__).resolve().parents[1] / "sites" / "openclaw-france"


class Document(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.tags, self.text = [], []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

    def handle_data(self, data):
        self.text.append(data)


class HermesConfidentialiteTest(unittest.TestCase):
    def setUp(self):
        self.html = (SITE / "hermes/index.html").read_text(encoding="utf-8")

    def test_navigation_avant_telechargement_et_section_nommee(self):
        hero = re.search(r'<section class="heros">(.*?)</section>', self.html, re.S).group(1)
        avant = hero.split('<div class="actions">', 1)[0]
        self.assertIn('href="#confidentialite"', avant, "Lien confidentialité absent avant téléchargement")
        tags = Document(self.html).tags
        self.assertEqual(sum(a.get("id") == "confidentialite" for _, a in tags), 1)
        self.assertIn(("section", {"id": "confidentialite", "aria-labelledby": "titre-confidentialite", "style": "scroll-margin-top:88px"}), tags)
        self.assertEqual(sum(a.get("id") == "titre-confidentialite" for _, a in tags), 1)

    def test_cinq_cas_pratiques_sans_garantie_absolue(self):
        bloc = re.search(r'<section id="confidentialite"[^>]*>(.*?)</section>', self.html, re.S)
        self.assertIsNotNone(bloc, "Section confidentialité absente")
        faqs = re.findall(r'<details\b[^>]*>(.*?)</details>', bloc.group(1), re.S)
        self.assertEqual(len(faqs), 5, "Cinq cas de confidentialité attendus")
        exigences = [
            ("fournisseur distant", "contexte envoyé", "extraits de fichiers", "conditions"),
            ("modèle local", "outils connectés", "hors ligne", "recherche web"),
            ("droits minimums", "dossier dédié", "pas une barrière", "administrateur"),
            ("historique", "journaux", "sauvegardes", "clés API", "jetons", ".env"),
            ("diagnostic", "transmettre", "relis", "masquage automatique", "extrait"),
        ]
        for faq, mots in zip(faqs, exigences):
            texte = " ".join(" ".join(Document(faq).text).split())
            with self.subTest(cas=mots[0]):
                for mot in mots:
                    self.assertIn(mot, texte)
        for interdit in ("<script", "<form", "<pre", "<code", "100 % privé", "chiffré", "souverain", "aucune télémétrie", "effacement garanti"):
            self.assertNotIn(interdit, bloc.group(1))

    def test_renvoi_guide_corrige_sans_reserve_perimee(self):
        bloc = re.search(r'<section id="confidentialite"[^>]*>(.*?)</section>', self.html, re.S)
        self.assertIsNotNone(bloc)
        self.assertNotIn("rien ne sort du tout", bloc.group(1))
        self.assertNotIn("encore présente", bloc.group(1))
        self.assertIn('href="/dl/kit-hermes/GUIDE.md"', bloc.group(1))
        self.assertIn("modèles auxiliaires", bloc.group(1))
        self.assertIn("fournisseurs de secours", bloc.group(1))
        guide = (SITE / "dl/kit-hermes/GUIDE.md").read_text(encoding="utf-8")
        self.assertIn("Confidentialité : modèle local ne veut pas dire hors ligne", guide)
        self.assertNotIn("rien ne sort du tout", guide)

    def test_sources_datees_et_synthese_ia_independante(self):
        bloc = re.search(r'<section id="confidentialite"[^>]*>(.*?)</section>', self.html, re.S)
        self.assertIsNotNone(bloc, "Section confidentialité absente")
        doc = Document(bloc.group(1))
        links = [a["href"] for t, a in doc.tags if t == "a"]
        for chemin in ("user-guide/sessions", "user-guide/local-models", "user-guide/features/web-search", "guides/secure-hermes-on-a-work-machine", "reference/cli-commands"):
            self.assertIn("https://hermes-agent.nousresearch.com/docs/" + chemin, links)
        self.assertIn(("time", {"datetime": "2026-10-21"}), doc.tags)
        texte = " ".join(" ".join(doc.text).split())
        for mot in ("Le Crabe (IA)", "indépendante", "documentation officielle", "prévaut", "pas un audit"):
            self.assertIn(mot, texte)
        self.assertNotIn("target=", bloc.group(1))


if __name__ == "__main__":
    unittest.main()
