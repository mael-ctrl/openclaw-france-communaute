#!/usr/bin/env python3
"""Déploie sites/openclaw-france/ vers l'hébergement OVH « communo ».

Cible : dossier « openclaw-france/ » à la racine du FTP (racine web du futur
openclaw-france.fr). Même identité FTP que le moteur (Trousseau ovh-communo-ftp).
Usage : python3 outils/deployer_openclaw.py
"""
import ftplib
import pathlib
import subprocess
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
SOURCE = RACINE / "sites" / "openclaw-france"
BASE = "openclaw-france"
HOTE = "ftp.cluster131.hosting.ovh.net"
UTILISATEUR = "communo"
SERVICE_TROUSSEAU = "ovh-communo-ftp"
COMPTE_TROUSSEAU = "communo"


def mot_de_passe():
    r = subprocess.run(["security", "find-generic-password",
                        "-s", SERVICE_TROUSSEAU, "-a", COMPTE_TROUSSEAU, "-w"],
                       capture_output=True, text=True)
    if r.returncode == 0 and r.stdout.strip():
        return r.stdout.strip()
    raise RuntimeError("mot de passe FTP introuvable au Trousseau")


def main() -> int:
    ftp = ftplib.FTP(HOTE, timeout=120)
    ftp.login(UTILISATEUR, mot_de_passe())
    ftp.set_pasv(True)
    ftp.encoding = "utf-8"
    try:
        ftp.cwd(BASE)
    except ftplib.error_perm:
        ftp.mkd(BASE)
        ftp.cwd(BASE)

    envois = 0
    for fichier in sorted(SOURCE.rglob("*")):
        if not fichier.is_file():
            continue
        relatif = fichier.relative_to(SOURCE).as_posix()
        parties = relatif.split("/")
        if len(parties) > 1:
            for partie in parties[:-1]:
                try:
                    ftp.cwd(partie)
                except ftplib.error_perm:
                    ftp.mkd(partie)
                    ftp.cwd(partie)
            with open(fichier, "rb") as fh:
                ftp.storbinary("STOR " + parties[-1], fh, blocksize=262144)
            for _ in range(len(parties) - 1):
                ftp.cwd("..")
        else:
            with open(fichier, "rb") as fh:
                ftp.storbinary("STOR " + parties[0], fh, blocksize=262144)
        envois += 1
        print(f"   ↑ {relatif} ({fichier.stat().st_size} o)")
    ftp.quit()
    print(f"Terminé : {envois} fichier(s) envoyé(s) vers « {BASE}/ ».")
    return 0


if __name__ == "__main__":
    sys.exit(main())
