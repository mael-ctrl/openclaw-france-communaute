"""Filtre IA : l'auxiliaire français « ai » n'est pas le sigle anglais."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "engine"))

import collecte


class FiltreIATest(unittest.TestCase):
    def test_auxiliaire_francais_ne_declenche_pas_le_filtre(self):
        # Extraits du flux Frandroid constatés le 03/10/2026 : ces deux
        # dépêches hors IA passaient uniquement à cause du mot « ai ».
        textes = [
            "J’ai pris plein de photos avec le Xiaomi 18 Pro : "
            "est-il meilleur que l’iPhone 18 Pro ?",
            "Test Ninja Luxe Café Mini : la semi-automatique qui apprend "
            "à faire un espresso. J'ai confronté cette petite semi-automatique "
            "à mes machines du quotidien.",
            "Je n’ai pas aimé ce téléphone.",
            "Je n'ai pas aimé ce téléphone.",
            "Qu’ai-je photographié pendant ce voyage ?",
            "Qu'ai-je photographié pendant ce voyage ?",
            "Ai-je choisi le bon appareil photo ?",
        ]
        for texte in textes:
            with self.subTest(texte=texte):
                self.assertIsNone(collecte.MOTS_IA.search(texte))

    def test_vrais_signaux_ia_restent_acceptes(self):
        textes = [
            "AI research news", "ai research news", "AI-powered tools",
            "L'AI transforme la recherche", "L’AI transforme la recherche",
            "J'ai testé ChatGPT", "Je n’ai pas encore testé l’IA",
            "Ai-je besoin de Claude Code ?", "OpenClaw et Hermes",
            "Un LLM open source", "L'intelligence artificielle en France",
        ]
        for texte in textes:
            with self.subTest(texte=texte):
                self.assertIsNotNone(collecte.MOTS_IA.search(texte))

    def test_collecte_rejette_auxiliaire_sans_bloquer_sources_specialisees(self):
        # La vraie boucle collecte/filtre/dédup écrit uniquement dans ce dossier
        # temporaire ; seul le téléchargement réseau est remplacé.
        with tempfile.TemporaryDirectory() as dossier:
            data = Path(dossier)
            sources = data / "sources.json"
            sources.write_text(json.dumps([{"nom": "Test"}]), encoding="utf-8")
            items = [
                {"titre": "J’ai photographié mon café", "filtre_ia": True},
                {"titre": "J'ai testé ChatGPT", "filtre_ia": True},
                {"titre": "J’ai photographié mon café", "filtre_ia": False},
            ]
            for n, item in enumerate(items):
                item.update(lien=f"https://example.org/{n}", resume="", date=None,
                            source="Test", langue="fr", priorite=3)
            with patch.multiple(collecte.config, FICHIER_SOURCES=sources,
                                FICHIER_ETAT=data / "etat.json", DOSSIER_DATA=data), \
                    patch.object(collecte, "telecharger_flux", return_value=items):
                gardes, _ = collecte.collecter(verbeux=False)
                self.assertEqual([i["lien"] for i in gardes],
                                 ["https://example.org/1", "https://example.org/2"])
                self.assertEqual(collecte.collecter(verbeux=False)[0], [])
                self.assertEqual(len(collecte.charger_etat()["vus"]), 3)


if __name__ == "__main__":
    unittest.main()
