"""Contrats CLI hors réseau, données synthétiques signalées comme fixtures."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SHA = "8dba69997d4c355134d9b9d5287c7a377d219f8c"
GUARD = """
import sys, runpy
def deny(event, args):
    if event.startswith(('socket.', 'urllib.')) or event in ('subprocess.Popen', 'os.system'):
        raise RuntimeError('RESEAU_ET_PROCESSUS_INTERDITS')
sys.addaudithook(deny)
script = sys.argv.pop(1)
sys.argv[0] = script
runpy.run_path(script, run_name='__main__')
"""


def fixture(n=1, **changes):
    row = {
        "id": f"{n:016x}", "slug": f"actu-test-{n}",
        "titre": f"Titre de test {n}", "resume": "Résumé synthétique de test, pas une actualité.",
        "source": f"Source de test {n}", "lien_source": f"https://www.python.org/test/{n}/",
        "date_redac": "2026-10-15T07:00:00+00:00", "date_source": None,
        "importance": 1, "tags": [], "gen": {"modele": "fixture"},
    }
    row.update(changes)
    return row


class ComposeCLI(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="test-", dir=ROOT)
        self.addCleanup(self.tmp.cleanup)
        self.home = Path(self.tmp.name)
        self.input = self.home / "input.json"

    def run_cli(self, rows, *extra):
        self.input.write_text(json.dumps(rows, ensure_ascii=False), encoding="utf-8")
        return self.run_existing(*extra)

    def run_existing(self, *extra):
        return subprocess.run(
            [sys.executable, "-B", "-c", GUARD, str(ROOT / "outils/compose_breve.py"),
             "--input", str(self.input), "--date", "2026-10-15", "--sha", SHA, *extra],
            cwd=ROOT, capture_output=True, text=True, timeout=10,
        )

    def test_titre_date_sans_fausse_numerotation(self):
        result = self.run_cli([fixture()], '--date', '2026-10-17')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.splitlines()[0], '# La Brève du Crabe 🦀 — édition du 2026-10-17')

    def test_rend_un_brouillon_source_sans_reseau(self):
        result = self.run_cli([fixture()])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("# La Brève du Crabe 🦀", result.stdout)
        self.assertIn("BROUILLON LOCAL — NON ENVOYÉ", result.stdout)
        self.assertIn("2026-10-15", result.stdout)
        self.assertIn(SHA, result.stdout)
        self.assertIn("intelligence artificielle", result.stdout)
        self.assertIn("Reprise sourcée — non vérifiée indépendamment", result.stdout)
        self.assertIn("https://communaute-ia.fr/breves/actu-test-1/", result.stdout)
        self.assertIn("https://www.python.org/test/1/", result.stdout)
        self.assertIn("Source de test 1", result.stdout)
        self.assertEqual(result.stderr, "")

    def test_selection_bornee_dedoublonnee_et_deterministe(self):
        rows = [fixture(n, date_redac=f"2026-10-15T{n:02}:00:00+00:00") for n in range(1, 9)]
        rows += [fixture(9, titre="Titre de test 8", date_redac="2026-10-15T09:00:00+00:00")]
        rows += [fixture(10, lien_source=rows[-1]["lien_source"] + "#section", date_redac="2026-10-15T08:30:00+00:00")]
        rows += [fixture(11, source="Source de test 9", date_redac="2026-10-15T08:20:00+00:00")]
        rows += [fixture(12, date_redac="2026-10-16T00:00:00+00:00")]
        rows += [fixture(13, date_redac="2026-10-08T23:59:59+00:00")]
        a = self.run_cli(rows)
        b = self.run_cli(list(reversed(rows)))
        self.assertEqual(a.returncode, 0, a.stderr)
        self.assertEqual(a.stdout.count("\n## "), 5)
        # L'empreinte des OCTETS change si l'entrée est permutée ; pas le contenu sélectionné.
        content_a = [line for line in a.stdout.splitlines() if not line.startswith("SHA-256 du JSON")]
        content_b = [line for line in b.stdout.splitlines() if not line.startswith("SHA-256 du JSON")]
        self.assertEqual(content_a, content_b)
        self.assertEqual(b.stdout, self.run_existing().stdout)
        self.assertIn("## 1. Titre de test 8", a.stdout)
        self.assertIn("actu-test-9/", a.stdout)
        for n in (8, 10, 11, 12, 13):
            self.assertNotIn(f"/breves/actu-test-{n}/", a.stdout)

    def test_rejette_entrees_malformees_et_placeholders(self):
        cases = [None, {}, [None], [], [fixture(titre="")], [fixture(resume=12)],
                 [fixture(id="bad")], [fixture(slug="../secret")],
                 [fixture(titre="[À REMPLACER par la collecte réelle]")],
                 [fixture(resume="TODO écrire ce texte")], [fixture(source="{{ source }}")],
                 [fixture(date_redac="2026-10-15T07:00:00")],
                 [fixture(date_source="2026-02-30T00:00:00Z")],
                 [fixture(date_source=42)], [fixture(email="contact non autorisé")]]
        missing = fixture()
        del missing["lien_source"]
        cases.append([missing])
        for rows in cases:
            with self.subTest(rows=rows):
                result = self.run_cli(rows)
                self.assertEqual(result.returncode, 2, result.stderr)
                self.assertEqual(result.stdout, "")
                self.assertIn("Erreur :", result.stderr)
                self.assertNotIn("Traceback", result.stderr)

    def test_refuse_urls_non_publiques_ou_tracantes(self):
        bad = ["javascript:alert(1)", "file:///etc/passwd", "http://localhost/a",
               "https://127.0.0.1/a", "https://10.0.0.1/a", "https://[::1]/a",
               "https://intranet/a", "https://service.local/a", "https://example.com/a",
               "https://user:secret@www.python.org/a", "https://www.python.org:8443/a",
               "https://www.python.org/a?utm_source=breve", "https://www.python.org/a?gclid=123",
               "https://www.python.org/a>![](https://evil.org/a)",
               "https://www.python.org/a\nInjected", "https://2130706433/a",
               "https://www.python.org/%ZZ", "https://www.python.org/a%0d%0aX"]
        for index, url in enumerate(bad):
            with self.subTest(case=index):
                result = self.run_cli([fixture(lien_source=url)])
                self.assertEqual(result.returncode, 2, result.stderr)
                self.assertEqual(result.stdout, "")
                self.assertNotIn("Traceback", result.stderr)
        good = "https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.1%2Bcanary.20261015T070051Z"
        result = self.run_cli([fixture(lien_source=good)])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(f"<{good}>", result.stdout)

    def test_texte_naturel_ne_declenche_pas_un_placeholder(self):
        for title in ("L'IA va transformer la relation client sans la remplacer, selon Maddyness",
                      "Un outil aide à remplacer des tâches répétitives"):
            result = self.run_cli([fixture(titre=title)])
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn(title, result.stdout)
        for marker in ("[À COMPLÉTER]", "À REMPLACER", "[public cible]", "${titre}"):
            result = self.run_cli([fixture(resume=marker)])
            self.assertEqual(result.returncode, 2, result.stderr)

    def test_parametres_et_fenetre_explicites_bornes(self):
        rows = [fixture(1, date_redac="2026-10-16T01:30:00+02:00"),
                fixture(2, date_redac="2026-10-15T02:00:00+02:00"),
                fixture(3, date_redac="2026-10-15T01:59:59+02:00"),
                fixture(4, date_redac="2026-10-16T02:00:00+02:00")]
        result = self.run_cli(rows, "--limit", "2", "--days", "1")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.count("\n## "), 2)
        self.assertIn("actu-test-1/", result.stdout)
        self.assertIn("actu-test-2/", result.stdout)
        for options in (("--limit", "0"), ("--limit", "11"), ("--days", "0"), ("--days", "32"),
                        ("--date", "20261015"), ("--date", "2026-02-30"), ("--sha", "bad"),
                        ("--sha", " " + SHA), ("--date", "2025-01-01")):
            with self.subTest(options=options):
                result = self.run_cli([fixture()], *options)
                self.assertEqual(result.returncode, 2, result.stderr)
                self.assertEqual(result.stdout, "")
                self.assertNotIn("Traceback", result.stderr)

    def test_texte_rendu_inerte_sans_html_ni_pixel(self):
        row = fixture(titre="Titre <script>x</script>",
                      resume="![pixel](https://tracker.fr/p.gif)\n## Fausse section",
                      source="Source [piège](https://tracker.fr/)")
        result = self.run_cli([row])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("<script>", result.stdout)
        self.assertNotIn("![pixel]", result.stdout)
        self.assertIn(r"\!\[pixel\]", result.stdout)
        self.assertEqual(result.stdout.count("\n## "), 1)
        self.assertIn("&lt;script&gt;", result.stdout)
        for text in ("nul\x00texte", "fausse\u202eprésentation", "x" * 10001):
            result = self.run_cli([fixture(resume=text)])
            self.assertEqual(result.returncode, 2, result.stderr)
            self.assertEqual(result.stdout, "")

    def test_fichier_reproductible_trace_sans_ecrasement(self):
        import hashlib
        row = fixture(date_source="2026-10-14T12:34:56Z")
        target = self.home / "numero.md"
        result = self.run_cli([row], "--output", str(target))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "")
        text = target.read_text(encoding="utf-8")
        digest = hashlib.sha256(self.input.read_bytes()).hexdigest()
        self.assertIn(digest, text)
        self.assertIn(row["date_source"], text)
        self.assertIn("100 % des bénéfices", text)
        self.assertIn("aucun don réalisé", text)
        self.assertIn("D'après Source de test 1", text)
        self.assertEqual(self.run_existing().stdout, text)
        again = self.run_existing("--output", str(target))
        self.assertEqual(again.returncode, 2)
        self.assertEqual(target.read_text(encoding="utf-8"), text)
        result = self.run_existing("--expect-sha256", "0" * 64)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        result = self.run_existing("--expect-sha256", digest)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, text)

    def test_json_strict_et_lecture_bornee(self):
        payload = json.dumps([fixture()])
        cases = [payload.replace('"id":', '"id":"0000000000000009", "id":', 1),
                 payload.replace('"importance": 1', '"importance": NaN'),
                 payload + " garbage", "{" , b"\xff",
                 payload.replace('"fixture"', '"' + "x" * (8 * 1024 * 1024) + '"')]
        for index, raw in enumerate(cases):
            with self.subTest(case=index):
                self.input.write_bytes(raw.encode() if isinstance(raw, str) else raw)
                result = self.run_existing()
                self.assertEqual(result.returncode, 2, result.stderr)
                self.assertEqual(result.stdout, "")
                self.assertNotIn("Traceback", result.stderr)
        for changes in ({"importance": "1"}, {"tags": "agents"}, {"gen": []}):
            result = self.run_cli([fixture(**changes)])
            self.assertEqual(result.returncode, 2, result.stderr)
        for date in ("9999-12-31", "0001-01-01"):
            result = self.run_cli([fixture()], "--date", date)
            self.assertEqual(result.returncode, 2, result.stderr)
            self.assertNotIn("Traceback", result.stderr)

    def test_limite_des_pages_construites_par_le_moteur(self):
        rows = [fixture(n, date_redac="2026-09-01T00:00:00Z") for n in range(1, 401)]
        rows.append(fixture(401))
        result = self.run_cli(rows)
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertEqual(result.stdout, "")
        rows[399] = fixture(400)
        result = self.run_cli(rows)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("/breves/actu-test-400/", result.stdout)
        self.assertNotIn("/breves/actu-test-401/", result.stdout)

    def test_collision_de_page_refusee_comme_au_build(self):
        rows = [fixture(1), fixture(2, slug=fixture(1)['slug'])]
        result = self.run_cli(rows)
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertIn('Page éditoriale dupliquée', result.stderr)
        self.assertEqual(result.stdout, '')
        # Une collision hors périmètre n'empêche pas de construire les 400 pages.
        rows = [fixture(n) for n in range(1, 402)]
        rows[400]['slug'] = rows[0]['slug']
        result = self.run_cli(rows)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_identifiants_dedoublonnes(self):
        rows = [fixture(1), fixture(2, id=fixture(1)["id"])]
        result = self.run_cli(rows)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.count("\n## "), 1)

    def test_erreur_ne_cree_pas_de_fichier(self):
        target = self.home / "invalide.md"
        result = self.run_cli([fixture(titre="TODO")], "--output", str(target))
        self.assertEqual(result.returncode, 2)
        self.assertFalse(target.exists())
        self.input.unlink()
        result = self.run_existing()
        self.assertEqual(result.returncode, 2)
        self.assertNotIn("Traceback", result.stderr)

    def test_surface_strictement_locale(self):
        import ast
        tree = ast.parse((ROOT / "outils/compose_breve.py").read_text())
        allowed = {"argparse", "html", "hashlib", "json", "re", "sys", "unicodedata",
                   "pathlib", "datetime", "urllib.parse"}
        imports = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.update(item.name for item in node.names)
            if isinstance(node, ast.ImportFrom):
                imports.add(node.module)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                self.assertNotIn(node.func.id, {"eval", "exec", "__import__"})
        self.assertLessEqual(imports, allowed)
        for option in ("--send", "--smtp", "--contacts", "--subscribe", "--api-key"):
            result = self.run_cli([fixture()], option)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(result.stdout, "")
        missing_date = subprocess.run([sys.executable, "-B", str(ROOT / "outils/compose_breve.py"),
                                       "--input", str(self.input), "--sha", SHA],
                                      capture_output=True, text=True, timeout=10)
        self.assertEqual(missing_date.returncode, 2)
        self.assertEqual(missing_date.stdout, "")

    def test_selection_editoriale_explicite_sans_modifier_le_snapshot(self):
        rows = [fixture(1), fixture(2), fixture(3)]
        result = self.run_cli(rows, "--only-id", rows[1]['id'], "--only-id", rows[2]['id'])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.count("\n## "), 2)
        self.assertNotIn('/breves/actu-test-1/', result.stdout)
        self.assertIn('/breves/actu-test-2/', result.stdout)
        self.assertIn('/breves/actu-test-3/', result.stdout)
        self.assertIn('Sélection éditoriale explicite (IDs)', result.stdout)
        self.assertEqual(json.loads(self.input.read_text()), rows)
        # Une sélection explicite est exhaustive : pas de suppression silencieuse.
        for options in (("--only-id", "bad"), ("--only-id", "f" * 16),
                        ("--only-id", rows[0]['id'], "--only-id", rows[0]['id']),
                        ("--only-id", rows[0]['id'], "--only-id", rows[1]['id'], "--limit", "1")):
            result = self.run_cli(rows, *options)
            self.assertEqual(result.returncode, 2, result.stderr)
            self.assertEqual(result.stdout, '')
        for changes in ({'date_redac': '2026-09-01T00:00:00Z'},
                        {'date_redac': '2026-10-16T00:00:00Z'}):
            result = self.run_cli([fixture(**changes)], '--only-id', fixture()['id'])
            self.assertEqual(result.returncode, 2, result.stderr)
        rows = [fixture(n) for n in range(1, 402)]
        result = self.run_cli(rows, '--only-id', rows[-1]['id'])
        self.assertEqual(result.returncode, 2, result.stderr)
        for changes in ({'source': rows[0]['source']}, {'id': rows[0]['id']}):
            rows = [fixture(1), fixture(2, **changes)]
            options = ['--only-id', rows[0]['id']]
            if rows[1]['id'] != rows[0]['id']:
                options += ['--only-id', rows[1]['id']]
            result = self.run_cli(rows, *options)
            self.assertEqual(result.returncode, 2, result.stderr)

    def test_rejette_un_decalage_horaire_malforme_sans_le_normaliser(self):
        for stamp in ("2026-10-15T07:00:00+00:99", "2026-10-15T07:00:00-02:60"):
            result = self.run_cli([fixture(date_redac=stamp)])
            self.assertEqual(result.returncode, 2, result.stderr)
            self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
