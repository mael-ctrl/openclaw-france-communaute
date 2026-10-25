"""Les extraits publics reflètent exactement le livrable, sans ouvrir le pack entier."""
import html
import json
import re
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))

import annexes
import config


class PackExtraitsTest(unittest.TestCase):
    def test_aide_de_copie_chargee_uniquement_sur_la_boutique(self):
        script = '<script src="/assets/pack-copie.js" defer></script>'
        self.assertIn(script, annexes.page_pack())
        self.assertNotIn(script, annexes.page_skills())
        self.assertNotIn(script, annexes.page_pack_merci())

    def test_page_propose_trois_prompts_exacts_avant_le_paiement(self):
        livrable = json.loads((config.DOSSIER_PRIVE / "dl" /
                               "pack-du-crabe-100-prompts.json").read_text(encoding="utf-8"))
        attendus = [p for p in livrable if p["id"] in (5, 13, 61)]
        self.assertEqual(len(attendus), 3)
        document = annexes.page_pack()
        extraits = re.findall(r'<details class="extrait-pack" data-prompt-id="(\d+)">(.*?)</details>',
                              document, re.S)
        self.assertEqual([int(ident) for ident, _ in extraits], [5, 13, 61])
        for (_, bloc), prompt in zip(extraits, attendus):
            self.assertIn(html.escape(prompt["titre"], quote=True), bloc)
            self.assertIn(html.escape(prompt["categorie"], quote=True), bloc)
            texte = re.search(r'<pre[^>]*>(.*?)</pre>', bloc, re.S).group(1)
            self.assertEqual(html.unescape(texte), prompt["prompt"])
        self.assertIn('3 prompts à essayer avant d’acheter', document)
        self.assertIn('Remplace les champs entre crochets', document)
        self.assertIn('Vérifie les réponses', document)
        self.assertLess(document.index('id="extraits-pack"'), document.index('<h2 id="prix-pack">Combien</h2>'))
        self.assertIn('href="https://buy.stripe.com/9B628s2cE6IL09P8421ck0n"', document)
        self.assertIn('Acheter le pack — 14 €', document)
        self.assertIn('rel="canonical" href="https://communaute-ia.fr/pack/"', document)
        self.assertNotIn('href="/dl/', document)
        self.assertNotIn('<form', document)


    def test_livrable_absent_ou_incomplet_ne_promet_pas_de_faux_extraits(self):
        with TemporaryDirectory() as temporaire, patch.object(config, "DOSSIER_PRIVE", Path(temporaire)):
            fichier = Path(temporaire) / "dl" / "pack-du-crabe-100-prompts.json"
            for contenu in (None, "{invalide", "[]", '[{"id": 5}]'):
                with self.subTest(contenu=contenu):
                    if contenu is not None:
                        fichier.parent.mkdir(exist_ok=True)
                        fichier.write_text(contenu, encoding="utf-8")
                    try:
                        document = annexes.page_pack()
                    except (KeyError, TypeError) as erreur:
                        self.fail(f"Un aperçu indisponible ne doit pas casser la page : {erreur}")
                    self.assertNotIn('id="extraits-pack"', document)
                    self.assertIn('Acheter le pack — 14 €', document)

    def test_le_texte_du_livrable_est_echappe_et_non_interprete_comme_html(self):
        champs = {"titre": '<img src=x onerror="alert(1)">', "categorie": 'A & B',
                  "prompt": '</pre><script>alert("x")</script>\n[champ] & suite'}
        with TemporaryDirectory() as temporaire, patch.object(config, "DOSSIER_PRIVE", Path(temporaire)):
            fichier = Path(temporaire) / "dl" / "pack-du-crabe-100-prompts.json"
            fichier.parent.mkdir()
            fichier.write_text(json.dumps([dict(champs, id=i) for i in (5, 13, 61)]), encoding="utf-8")
            bloc = annexes.extraits_pack()
            for valeur in champs.values():
                self.assertIn(html.escape(valeur, quote=True), bloc)
            self.assertNotIn('<script>', bloc)
            self.assertNotIn('<img', bloc)


if __name__ == "__main__":
    unittest.main()
