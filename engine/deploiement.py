# -*- coding: utf-8 -*-
"""Déploiement vers l'hébergement OVH (FTP incrémental).

Le dossier distant visé est « www/ » à la racine de l'hébergement
communo.cluster131.hosting.ovh.net (serveur de communaute-ia.fr).

En local (Mac), le mot de passe FTP est lu dans le Trousseau macOS
(entrée « ovh-communo-ftp », compte « communo »).
Dans GitHub Actions, il vient des secrets du dépôt.
"""
import ftplib
import json
import subprocess
import sys

import config

SERVICE_TROUSSEAU = "ovh-communo-ftp"
COMPTE_TROUSSEAU = "communo"


def _mot_de_passe():
    if config.FTP_MOT_DE_PASSE:
        return config.FTP_MOT_DE_PASSE
    if sys.platform == "darwin":
        r = subprocess.run(["security", "find-generic-password",
                            "-s", SERVICE_TROUSSEAU, "-a", COMPTE_TROUSSEAU, "-w"],
                           capture_output=True, text=True)
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout.strip()
    raise RuntimeError("mot de passe FTP introuvable (ni variable d'environnement ni Trousseau)")


def deployer(verbeux=True):
    """Pousse _site/ vers le serveur. Renvoie (fichiers envoyés, octets)."""
    base = config.FTP_DOSSIER.strip("/")
    etat = {}
    if config.FICHIER_DEPLOY_ETAT.exists():
        try:
            etat = json.loads(config.FICHIER_DEPLOY_ETAT.read_text(encoding="utf-8"))
        except ValueError:
            etat = {}

    ftp = ftplib.FTP(config.FTP_SERVEUR, timeout=180)
    ftp.login(config.FTP_UTILISATEUR, _mot_de_passe())
    ftp.set_pasv(True)
    ftp.encoding = "utf-8"

    # On travaille en RELATIF depuis le dossier du site (validé sur cet hébergement :
    # le chemin absolu avec « / » trompe le serveur OVH).
    try:
        ftp.cwd(base)
    except ftplib.error_perm:
        ftp.mkd(base)
        ftp.cwd(base)

    envois, total_octets = 0, 0
    dossier_courant = []  # composants relatifs à la base, confirmés par CWD
    for fichier in sorted(config.DOSSIER_SORTIE.rglob("*")):
        if not fichier.is_file():
            continue
        relatif = fichier.relative_to(config.DOSSIER_SORTIE).as_posix()
        st = fichier.stat()
        empreinte = [st.st_size, int(st.st_mtime)]
        if etat.get(relatif) == empreinte:
            continue
        parties = relatif.split("/")
        cible = parties[:-1]
        commun = 0
        for actuel, attendu in zip(dossier_courant, cible):
            if actuel != attendu:
                break
            commun += 1
        while len(dossier_courant) > commun:
            ftp.cwd("..")
            dossier_courant.pop()
        for partie in cible[commun:]:
            try:
                ftp.cwd(partie)
            except ftplib.error_perm:
                ftp.mkd(partie)
                ftp.cwd(partie)
            dossier_courant.append(partie)
        with open(fichier, "rb") as fh:
            ftp.storbinary("STOR " + parties[-1], fh, blocksize=262144)
        etat[relatif] = empreinte
        envois += 1
        total_octets += st.st_size
        if verbeux:
            print(f"   ↑ {relatif} ({st.st_size} o)")
    while dossier_courant:
        ftp.cwd("..")
        dossier_courant.pop()
    ftp.quit()

    config.FICHIER_DEPLOY_ETAT.write_text(json.dumps(etat, ensure_ascii=False, indent=0),
                                          encoding="utf-8")
    return envois, total_octets
