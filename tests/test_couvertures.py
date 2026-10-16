"""Contrat local des couvertures : aucune requête réseau."""
import importlib
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path
from contextlib import contextmanager
from html.parser import HTMLParser
from unittest.mock import patch

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "engine"))

BREVE = {"slug": "puces--essai", "titre": "Des GPU pour les modèles locaux",
         "resume": "Un résumé.", "tags": ["matériel"], "source": "Source & exemple",
         "lien_source": "https://example.org/a?x=1&y=2", "date_redac": "2026-10-15T09:00:00Z"}
ARTICLE = {"slug": "analyse", "titre": "Des agents & des outils", "chapo": "Le chapeau.",
           "html": "<p>Texte <strong>original</strong>.</p>", "date": "2026-10-15T10:00:00Z",
           "tags": ["agents"], "sources": [{"nom": "Source", "url": "https://example.org/a"}]}


class HTML(HTMLParser):
    def __init__(self, texte):
        super().__init__()
        self.metas, self.images = [], []
        self.feed(texte)
        self.news = [x for x in (json.loads(s) for s in re.findall(
            r'<script type="application/ld\+json">(.*?)</script>', texte, re.S))
            if x.get("@type") == "NewsArticle"]

    def handle_starttag(self, tag, attrs):
        if tag == "meta":
            self.metas.append(dict(attrs))
        elif tag == "img":
            self.images.append(dict(attrs))

    def meta(self, cle):
        return [m["content"] for m in self.metas if m.get("name", m.get("property")) == cle]


@contextmanager
def build_isole(breves, articles):
    import construction as con
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "articles").mkdir()
        (root / "assets").mkdir()
        (root / "breves.json").write_text(json.dumps(breves))
        for i, a in enumerate(articles):
            (root / "articles" / f"{i}.json").write_text(json.dumps(a))
        with patch.multiple(con.config, DOSSIER_SORTIE=root / "site",
                            FICHIER_BREVES=root / "breves.json", DOSSIER_ARTICLES=root / "articles",
                            DOSSIER_ASSETS=root / "assets", DOSSIER_FICHIERS=root / "absent",
                            DOSSIER_PRIVE=root / "absent", FICHIER_STATS=root / "stats.json",
                            FICHIER_JOURNAL=root / "journal.jsonl"):
            yield con, root


class CouverturesTest(unittest.TestCase):
    def moteur(self):
        self.assertIsNotNone(importlib.util.find_spec("couvertures"),
                             "Le générateur de couvertures manque")
        return importlib.import_module("couvertures")

    def test_jpeg_local_dimensions_et_budget(self):
        c = self.moteur()
        with tempfile.TemporaryDirectory() as tmp:
            info = c.generer(BREVE, "breves", Path(tmp))
            fichier = Path(tmp) / Path(info["path"]).name
            with Image.open(fichier) as image:
                image.load()
                self.assertEqual(image.format, "JPEG")
                self.assertEqual(image.size, (1280, 720))
            self.assertLess(fichier.stat().st_size, 120_000)
            self.assertEqual(info["bytes"], fichier.stat().st_size)
            self.assertEqual(info["theme"], "materiel")
            self.assertIn("Illustration générée", info["caption"])

    def test_cache_stable_repare_et_invalide_par_contenu(self):
        c = self.moteur()
        with tempfile.TemporaryDirectory() as tmp:
            cache = Path(tmp)
            premier = c.generer(BREVE, "breves", cache)
            fichier = cache / Path(premier["path"]).name
            octets, mtime = fichier.read_bytes(), fichier.stat().st_mtime_ns
            second = c.generer(BREVE, "breves", cache)
            self.assertEqual(premier, second)
            self.assertEqual(fichier.stat().st_mtime_ns, mtime, "Le cache doit éviter une écriture")
            fichier.write_bytes(b"JPEG tronque")
            self.assertEqual(c.generer(BREVE, "breves", cache), premier)
            self.assertEqual(fichier.read_bytes(), octets)
            autre = c.generer(dict(BREVE, titre="Un autre GPU"), "breves", cache)
            self.assertNotEqual(autre["path"], premier["path"])
            self.assertNotEqual(autre["sha256"], premier["sha256"])
            neuf = cache / "neuf"
            self.assertEqual(c.generer(BREVE, "breves", neuf), premier)
            self.assertEqual((neuf / fichier.name).read_bytes(), octets)

    def test_cache_froid_preserve_empreinte_du_deployeur(self):
        """Un runner neuf ne doit pas réenvoyer tous les JPEG immuables."""
        import time
        c = self.moteur()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            premier = c.generer(BREVE, "breves", root / "premier")
            time.sleep(1.1)  # le déployeur compare des secondes entières
            second = c.generer(BREVE, "breves", root / "second")
            self.assertEqual(premier, second)
            a = (root / "premier" / Path(premier["path"]).name).stat()
            b = (root / "second" / Path(second["path"]).name).stat()
            self.assertEqual((a.st_size, int(a.st_mtime)), (b.st_size, int(b.st_mtime)),
                             "Un cache cloud neuf change l'empreinte FTP taille/mtime")

    def test_themes_et_repli_declares_sans_texte_raster(self):
        c = self.moteur()
        cas = [("Faille de sécurité et données", "securite"),
               ("Des agents coordonnent leurs outils", "agents"),
               ("Un robot industriel", "robotique"),
               ("Un modèle de langage", "modeles"),
               ("Un sujet sans thème reconnu", "generique")]
        with tempfile.TemporaryDirectory() as tmp:
            empreintes = set()
            for titre, theme in cas:
                info = c.generer(dict(BREVE, titre=titre, tags=[]), "breves", Path(tmp))
                self.assertEqual(info["theme"], theme)
                self.assertIn("pas une photographie", info["caption"])
                empreintes.add(info["sha256"])
                if theme == "generique":
                    self.assertIn("générique", info["caption"])
            self.assertEqual(len(empreintes), len(cas))

    def test_chemins_non_surs_rejetes_et_genres_distincts(self):
        c = self.moteur()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for slug in ("../sortie", "/absolu", "x/y", "x\\y", "x%2fy", "", ".", "A"):
                with self.subTest(slug=slug), self.assertRaises(ValueError):
                    c.generer(dict(BREVE, slug=slug), "breves", root / "cache")
            with self.assertRaises(ValueError):
                c.generer(BREVE, "../articles", root / "cache")
            b = c.generer(BREVE, "breves", root / "cache")
            a = c.generer(BREVE, "articles", root / "cache")
            self.assertNotEqual(b["path"], a["path"])
            (root / "lien").symlink_to(root / "cache", target_is_directory=True)
            with self.assertRaises(ValueError):
                c.generer(BREVE, "breves", root / "lien")
            cible = root / "cache" / Path(b["path"]).name
            cible.unlink()
            temoin = root / "temoin"
            temoin.write_bytes(b"ne pas toucher")
            cible.symlink_to(temoin)
            with self.assertRaises(ValueError):
                c.generer(BREVE, "breves", root / "cache")
            self.assertEqual(temoin.read_bytes(), b"ne pas toucher")

    def test_build_html_og_twitter_jsonld_coherents_preserve_contenu(self):
        with build_isole([BREVE], [ARTICLE]) as (con, root):
            anciens = {"breves": con.page_breve(BREVE, [BREVE]),
                       "articles": con.page_article(ARTICLE, [ARTICLE])}
            con.construire()
            for genre, item in (("breves", BREVE), ("articles", ARTICLE)):
                texte = (root / "site" / genre / item["slug"] / "index.html").read_text()
                html = HTML(texte)
                self.assertEqual(len(html.images), 1, "La page éditoriale doit afficher sa couverture")
                image = html.images[0]
                url = con.config.URL_SITE + image["src"]
                self.assertEqual(html.meta("og:image"), [url])
                self.assertEqual(html.meta("twitter:image"), [url])
                self.assertEqual(html.meta("og:type"), ["article"])
                self.assertEqual(html.meta("og:image:type"), ["image/jpeg"])
                self.assertEqual(html.meta("og:image:width"), ["1280"])
                self.assertEqual(html.meta("og:image:height"), ["720"])
                self.assertEqual((image["width"], image["height"]), ("1280", "720"))
                self.assertNotEqual(image.get("loading"), "lazy")
                self.assertEqual(image["fetchpriority"], "high")
                self.assertEqual(html.news[0]["image"]["url"], url)
                self.assertEqual(html.news[0]["image"]["width"], 1280)
                self.assertEqual(html.news[0]["image"]["height"], 720)
                self.assertTrue((root / "site" / image["src"].lstrip("/")).is_file())
                self.assertIn("Illustration générée", texte)
                news = dict(html.news[0]); news.pop("image")
                self.assertEqual(news, HTML(anciens[genre]).news[0])
                sans_figure = re.sub(r'<figure class="couverture-editoriale">.*?</figure>', "", texte, flags=re.S)
                self.assertEqual(sans_figure.split("<body>")[1], anciens[genre].split("<body>")[1])
            for fichier in ("index.html", "actus/index.html", "articles/index.html", "404.html", "b2b/index.html"):
                page = HTML((root / "site" / fichier).read_text())
                self.assertEqual(page.meta("og:type"), ["website"])
                self.assertEqual(page.meta("og:image"), [con.config.URL_SITE + "/assets/og-crabe.png"])
                self.assertFalse(page.news)

    def test_build_refuse_collisions_avant_pages_et_liens_symboliques(self):
        for breves, articles in (([BREVE, dict(BREVE, titre="Autre")], []), ([], [ARTICLE, ARTICLE])):
            with build_isole(breves, articles) as (con, root):
                with self.assertRaises(ValueError):
                    con.construire()
                self.assertFalse(list((root / "site").rglob("*.html")))
        with build_isole([BREVE], []) as (con, root):
            cible = root / "site" / "breves" / BREVE["slug"]
            cible.parent.mkdir(parents=True)
            (root / "interdit").mkdir()
            cible.symlink_to(root / "interdit", target_is_directory=True)
            with self.assertRaises(ValueError):
                con.construire()
            self.assertFalse(list((root / "interdit").iterdir()))

    def test_metadonnees_cache_corrompues_regenerees(self):
        c = self.moteur()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            info = c.generer(BREVE, "breves", root)
            meta = (root / Path(info["path"]).name).with_suffix(".json")
            meta.write_text(json.dumps(dict(info, width=1, alt="alt corrompu")))
            self.assertEqual(c.generer(BREVE, "breves", root), info)

    def test_build_borne_400_tous_articles_et_reexecution(self):
        import hashlib
        breves = [dict(BREVE, slug=f"breve-{i}") for i in range(401)]
        articles = [dict(ARTICLE, slug=f"article-{i}") for i in range(3)]
        with build_isole(breves, articles) as (con, root):
            con.construire()
            sortie = root / "site"
            images = list((sortie / "assets/couvertures").glob("*.jpg"))
            self.assertEqual(len(images), 403)
            self.assertEqual(len(list((sortie / "breves").glob("*/index.html"))), 400)
            self.assertEqual(len(list((sortie / "articles").glob("*/index.html"))), 3)
            self.assertFalse((sortie / "breves/breve-400").exists())
            avant = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in images}
            for p in list((sortie / "breves").glob("*/index.html")) + list((sortie / "articles").glob("*/index.html")):
                page = HTML(p.read_text())
                self.assertEqual(len(page.images), 1)
                self.assertEqual(page.meta("og:image"), [page.news[0]["image"]["url"]])
            con.construire()
            self.assertEqual(avant, {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in images})

    def test_styles_reservent_ratio_sans_debordement(self):
        css = (ROOT / "assets/style.css").read_text()
        self.assertRegex(css, r"\.couverture-editoriale img\s*\{[^}]*width:\s*100%;[^}]*height:\s*auto;")

    def test_cache_separe_versions_encodeur(self):
        c = self.moteur()
        with tempfile.TemporaryDirectory() as tmp:
            info = c.generer(BREVE, "breves", Path(tmp))
            with patch.object(c.features, "version_feature", return_value="version-test-differente"):
                autre = c.generer(BREVE, "breves", Path(tmp))
            self.assertNotEqual(info["path"], autre["path"])


if __name__ == "__main__":
    unittest.main()
