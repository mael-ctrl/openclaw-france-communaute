"""Parcours FTP relatif : conserver les dossiers communs sans changer les envois."""
import ftplib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))
import config
import deploiement


class ServeurFTP:
    def __init__(self, dossiers):
        self.dossiers = {tuple(p.split("/")) for p in dossiers}
        self.position = ()
        self.commandes = []
        self.envois = []
        self.refus = None

    def login(self, *args):
        pass

    def set_pasv(self, actif):
        assert actif is True

    def cwd(self, dossier):
        self.commandes.append(("CWD", dossier))
        if self.refus == ("CWD", dossier):
            raise ftplib.error_temp("450 refus de navigation")
        assert not dossier.startswith("/"), "chemin absolu interdit"
        cible = self.position[:-1] if dossier == ".." else self.position + (dossier,)
        if cible not in self.dossiers:
            raise ftplib.error_perm("550 dossier absent")
        self.position = cible

    def mkd(self, dossier):
        self.commandes.append(("MKD", dossier))
        if self.refus == ("MKD", dossier):
            raise ftplib.error_perm("550 creation refusee")
        self.dossiers.add(self.position + (dossier,))

    def storbinary(self, commande, fichier, **kwargs):
        if self.refus == ("STOR", commande):
            raise ftplib.error_temp("450 transfert refuse")
        assert commande.startswith("STOR ") and "/" not in commande[5:]
        assert kwargs == {"blocksize": 262144}
        self.envois.append(("/".join(self.position + (commande[5:],)), fichier.read()))

    def quit(self):
        self.commandes.append(("QUIT",))
        assert self.position == ("www",), "retour relatif a la base attendu"


class NavigationFTPTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.racine = Path(self.tmp.name)
        self.sortie = self.racine / "site"
        self.sortie.mkdir()
        self.etat = self.racine / "deploy.json"

    def fichier(self, chemin, corps=b"contenu"):
        p = self.sortie / chemin
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(corps)
        return p

    def deployer(self, ftp):
        with patch.multiple(config, DOSSIER_SORTIE=self.sortie,
                            FICHIER_DEPLOY_ETAT=self.etat, FTP_DOSSIER="www",
                            FTP_SERVEUR="test.invalid", FTP_UTILISATEUR="test"), \
             patch.object(deploiement, "_mot_de_passe", return_value="fictif"), \
             patch.object(deploiement.ftplib, "FTP", return_value=ftp):
            return deploiement.deployer(verbeux=False)

    def test_deux_fichiers_freres_ne_retraversent_pas_le_meme_dossier(self):
        self.fichier("assets/a.txt", b"A")
        self.fichier("assets/b.txt", b"BB")
        ftp = ServeurFTP(["www", "www/assets"])
        self.assertEqual(self.deployer(ftp), (2, 3))
        self.assertEqual(ftp.envois, [("www/assets/a.txt", b"A"),
                                      ("www/assets/b.txt", b"BB")])
        self.assertEqual(ftp.commandes, [("CWD", "www"), ("CWD", "assets"),
                                         ("CWD", ".."), ("QUIT",)])

    def test_racine_sous_dossiers_freres_unicode_et_creation(self):
        contenus = {".htaccess": b"Options -Indexes", "a/a.txt": b"a",
                    "a/b/c.txt": b"c", "a/b/d.txt": b"d", "a/e.txt": b"e",
                    "ab/f.txt": b"f", "index.html": b"index",
                    "z/été et espace.txt": b"utf8"}
        for chemin, corps in contenus.items():
            self.fichier(chemin, corps)
        ftp = ServeurFTP([])
        self.assertEqual(self.deployer(ftp), (len(contenus), sum(map(len, contenus.values()))))
        self.assertEqual(ftp.envois, [("www/" + p, contenus[p]) for p in sorted(contenus)])
        self.assertEqual([c[1] for c in ftp.commandes if c[0] == "MKD"],
                         ["www", "a", "b", "ab", "z"])
        etat = json.loads(self.etat.read_text())
        self.assertEqual(set(etat), set(contenus))
        for p in contenus:
            s = (self.sortie / p).stat()
            self.assertEqual(etat[p], [s.st_size, int(s.st_mtime)])

    def test_cache_ignore_sans_naviguer_et_conserve_les_anciennes_entrees(self):
        for p in ["a/1.txt", "a/2.txt", "b/3.txt", "z.txt"]:
            self.fichier(p, p.encode())
        etat = {p: [(self.sortie / p).stat().st_size,
                     int((self.sortie / p).stat().st_mtime)]
                for p in ["a/2.txt", "b/3.txt"]}
        etat["ancien.txt"] = [42, 0]
        self.etat.write_text(json.dumps(etat))
        ftp = ServeurFTP(["www", "www/a"])
        self.assertEqual(self.deployer(ftp)[0], 2)
        self.assertEqual([p for p, _ in ftp.envois], ["www/a/1.txt", "www/z.txt"])
        self.assertEqual(ftp.commandes, [("CWD", "www"), ("CWD", "a"),
                                         ("CWD", ".."), ("QUIT",)])
        self.assertEqual(json.loads(self.etat.read_text())["ancien.txt"], [42, 0])

    def test_second_passage_entierement_en_cache_ne_navigue_plus(self):
        self.fichier("a/b/c.txt")
        ftp = ServeurFTP(["www"])
        self.deployer(ftp)
        etat = self.etat.read_bytes()
        ftp2 = ServeurFTP(["www"])
        self.assertEqual(self.deployer(ftp2), (0, 0))
        self.assertEqual(ftp2.commandes, [("CWD", "www"), ("QUIT",)])
        self.assertEqual(self.etat.read_bytes(), etat)

    def test_sortie_vide(self):
        ftp = ServeurFTP(["www"])
        self.assertEqual(self.deployer(ftp), (0, 0))
        self.assertEqual(ftp.envois, [])

    def test_erreurs_navigation_creation_transfert_ne_valident_pas_le_cache(self):
        self.fichier("a/1.txt", b"1")
        self.fichier("a/2.txt", b"2")
        avant = b'{"ancien": [1, 2]}'
        for refus in [("CWD", "a"), ("MKD", "a"), ("STOR", "STOR 2.txt"),
                      ("CWD", "..")]:
            with self.subTest(refus=refus):
                self.etat.write_bytes(avant)
                ftp = ServeurFTP(["www"])
                ftp.refus = refus
                with self.assertRaises(ftplib.Error):
                    self.deployer(ftp)
                self.assertEqual(self.etat.read_bytes(), avant)
                self.assertNotIn(("QUIT",), ftp.commandes)

    def test_refus_quit_ne_valide_pas_le_cache(self):
        self.fichier("a/1.txt")
        avant = b'{}'
        self.etat.write_bytes(avant)
        ftp = ServeurFTP(["www", "www/a"])
        with patch.object(ftp, "quit", side_effect=ftplib.error_temp("450 quit")):
            with self.assertRaises(ftplib.error_temp):
                self.deployer(ftp)
        self.assertEqual(self.etat.read_bytes(), avant)

    def test_cache_json_invalide_retransmet_sans_changer_les_corps(self):
        self.etat.write_text("JSON invalide")
        self.fichier("a/b.txt", b"\x00\xffcontenu")
        ftp = ServeurFTP(["www", "www/a"])
        self.assertEqual(self.deployer(ftp), (1, 9))
        self.assertEqual(ftp.envois, [("www/a/b.txt", b"\x00\xffcontenu")])


if __name__ == "__main__":
    unittest.main()
