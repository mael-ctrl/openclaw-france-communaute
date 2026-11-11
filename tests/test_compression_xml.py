"""Configuration racine préparée hors réseau, jamais remplacée par le build."""
import hashlib
import importlib.util
from pathlib import Path
import unittest
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "outils/compression_xml.py"
BASE = (b"RewriteEngine On\n"
        b"RewriteCond %{HTTP_HOST} ^www\\.communaute-ia\\.fr$ [NC]\n"
        b"RewriteRule ^(.*)$ https://communaute-ia.fr/$1 [R=301,L,QSA]\n")


class CompressionXMLTests(unittest.TestCase):
    def charger(self):
        self.assertTrue(MODULE.is_file(), "Préparateur de compression XML absent")
        spec = importlib.util.spec_from_file_location("compression_xml", MODULE)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_ajoute_seulement_les_mimes_xml_sans_changer_la_base(self):
        module = self.charger()
        candidate = module.preparer(BASE, hashlib.sha256(BASE).hexdigest())
        self.assertTrue(candidate.startswith(BASE + b"\n"))
        block = candidate[len(BASE):]
        self.assertIn(b"<IfModule mod_deflate.c>", block)
        self.assertIn(b"<IfModule mod_filter.c>", block)
        self.assertIn(b"AddOutputFilterByType DEFLATE application/xml text/xml application/rss+xml application/atom+xml text/x-opml", block)
        for forbidden in (b"Cache-Control", b"Header ", b"RewriteRule", b"SetOutputFilter", b"AddEncoding", b"text/html", b"image/jpeg", b"audio/mpeg"):
            self.assertNotIn(forbidden, block)


    def test_refuse_une_base_differente_ou_une_empreinte_malformee(self):
        module = self.charger()
        for digest in ("0" * 64, "", hashlib.sha256(BASE).hexdigest().upper()):
            with self.subTest(digest=digest), self.assertRaises(ValueError):
                module.preparer(BASE, digest)


    def test_idempotence_bloc_exact_et_refus_des_marqueurs_ambigus(self):
        module = self.charger()
        candidate = module.preparer(BASE, hashlib.sha256(BASE).hexdigest())
        self.assertEqual(module.preparer(candidate, hashlib.sha256(candidate).hexdigest()), candidate)
        for bad in (BASE + module.DEBUT, BASE + module.FIN,
                    candidate + module.BLOC,
                    candidate.replace(b"DEFLATE", b"OTHER"),
                    candidate.replace(b"XML v1", b"XML v2")):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                module.preparer(bad, hashlib.sha256(bad).hexdigest())
        # Des octets CRLF ou une dernière ligne sans LF ne sont pas normalisés.
        for original in (BASE.replace(b"\n", b"\r\n"), BASE.rstrip(b"\n")):
            self.assertTrue(module.preparer(original, hashlib.sha256(original).hexdigest()).startswith(original))


    def test_cli_ecrit_une_sortie_neuve_et_refuse_un_ecrasement(self):
        self.charger()
        with tempfile.TemporaryDirectory() as tmp:
            source, dest = Path(tmp) / "base.htaccess", Path(tmp) / "candidate.htaccess"
            source.write_bytes(BASE)
            command = [sys.executable, str(MODULE), str(source), str(dest),
                       "--sha256", hashlib.sha256(BASE).hexdigest()]
            result = subprocess.run(command, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(dest.is_file(), "Le CLI n'a pas créé le candidat")
            expected = self.charger().preparer(BASE, hashlib.sha256(BASE).hexdigest())
            self.assertEqual(dest.read_bytes(), expected)
            self.assertNotEqual(subprocess.run(command, capture_output=True).returncode, 0)
            self.assertEqual(dest.read_bytes(), expected)
            self.assertEqual(source.read_bytes(), BASE)
            refused = Path(tmp) / "refused.htaccess"
            command[3] = str(refused)
            command[-1] = "0" * 64
            self.assertNotEqual(subprocess.run(command, capture_output=True).returncode, 0)
            self.assertFalse(refused.exists())


    def test_compression_bornee_aux_extensions_xml_opml(self):
        import re
        module = self.charger()
        texte = module.BLOC.decode("ascii")
        match = re.search(r'<FilesMatch "([^"\n]+)">\s*<IfModule mod_deflate.c>', texte)
        self.assertIsNotNone(match, "Ne pas écraser les filtres hérités HTML/CSS/JS")
        for name in ("feed.xml", "news-sitemap.xml", "sources.opml"):
            self.assertIsNotNone(re.search(match.group(1), name))
        for name in ("index.html", "app.js", "style.css", "test.xml.jpg", "test.xml.bak", "test.mp3", "test.json"):
            self.assertIsNone(re.search(match.group(1), name))
        self.assertTrue(texte.endswith("</FilesMatch>\n" + module.FIN.decode()))


if __name__ == "__main__":
    unittest.main()
