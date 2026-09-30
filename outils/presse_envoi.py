#!/usr/bin/env python3
"""Envoi de la campagne presse de La Communauté 🦀 via SMTP OVH (crabe@blockos.fr).

Usage :
  python3 outils/presse_envoi.py --simulation          # affiche sans envoyer
  python3 outils/presse_envoi.py --test-vers a@b.fr    # la 1re cible, vers a@b.fr, sans journaliser
  python3 outils/presse_envoi.py                       # envoi réel (saute ce qui est déjà journalisé)

Campagnes : tous les fichiers docs/press/campagne-*.json (ou --campagne FICHIER).
Mot de passe : env BLOCKOS_SMTP_PASSWORD, sinon Trousseau macOS
(service « blockos-crabe-email », compte « OVH »).
"""
import argparse
import datetime
import json
import os
import random
import smtplib
import subprocess
import sys
import time
from email.message import EmailMessage
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
DOSSIER_PRESS = RACINE / "docs" / "press"
JOURNAL = DOSSIER_PRESS / "envois.jsonl"
HOTE, PORT = "ssl0.ovh.net", 465
EXPEDITEUR, NOM_EXPEDITEUR = "crabe@blockos.fr", "Le Crabe 🦀"


def mot_de_passe() -> str:
    mot = os.environ.get("BLOCKOS_SMTP_PASSWORD", "").strip()
    if mot:
        return mot
    r = subprocess.run(
        ["security", "find-generic-password", "-s", "blockos-crabe-email", "-a", "OVH", "-w"],
        capture_output=True, text=True)
    return r.stdout.strip()


def deja_envoyes() -> set:
    emails = set()
    if JOURNAL.exists():
        for ligne in JOURNAL.read_text(encoding="utf-8").splitlines():
            try:
                emails.add(json.loads(ligne)["email"])
            except (ValueError, KeyError):
                continue
    return emails


def charger_cibles(chemin: str):
    fichiers = [Path(chemin)] if chemin else sorted(DOSSIER_PRESS.glob("campagne-*.json"))
    cibles = []
    for f in fichiers:
        campagne = json.loads(f.read_text(encoding="utf-8"))
        corps = "\n".join(campagne["corps_modele"])
        for cible in campagne["cibles"]:
            cibles.append((campagne.get("campagne", f.stem), corps, cible))
    return cibles


def construire(cible: dict, corps_modele: str) -> EmailMessage:
    msg = EmailMessage()
    msg["From"] = f"{NOM_EXPEDITEUR} <{EXPEDITEUR}>"
    msg["To"] = cible["email"]
    msg["Subject"] = cible["sujet"]
    msg["Reply-To"] = EXPEDITEUR
    msg.set_content(corps_modele.replace("{accroche}", cible["accroche"]))
    return msg


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--campagne", default="")
    ap.add_argument("--simulation", action="store_true")
    ap.add_argument("--test-vers", default="")
    args = ap.parse_args()

    a_faire = [
        (nom, corps, cible)
        for nom, corps, cible in charger_cibles(args.campagne)
        if cible["email"] not in deja_envoyes()
    ]

    if args.test_vers:
        nom, corps, cible = charger_cibles(args.campagne)[0]
        cible = dict(cible, email=args.test_vers)
        a_faire = [(nom, corps, cible)]
        print(f"Mode test : 1 message vers {args.test_vers} (non journalisé)")

    if not a_faire:
        print("Rien à envoyer : toutes les cibles sont déjà journalisées.")
        return 0

    if args.simulation:
        for nom, _corps, cible in a_faire:
            print(f"— [{nom}] {cible['media']} <{cible['email']}> | {cible['sujet']}")
        print(f"Simulation : {len(a_faire)} message(s) prêt(s) à partir.")
        return 0

    mot = mot_de_passe()
    if not mot:
        print("ERREUR : mot de passe SMTP introuvable (BLOCKOS_SMTP_PASSWORD ou Trousseau).")
        return 2

    ok = 0
    with smtplib.SMTP_SSL(HOTE, PORT, timeout=40) as serveur:
        serveur.login(EXPEDITEUR, mot)
        for i, (nom, corps, cible) in enumerate(a_faire):
            try:
                serveur.send_message(construire(cible, corps))
            except Exception as e:  # noqa: BLE001 — on continue la vague
                print(f"⚠️  ÉCHEC {cible['media']} <{cible['email']}> : {e}")
                continue
            ok += 1
            if not args.test_vers:
                ligne = {
                    "ts": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
                    "campagne": nom,
                    "media": cible["media"],
                    "email": cible["email"],
                    "sujet": cible["sujet"],
                    "statut": "envoye",
                }
                with JOURNAL.open("a", encoding="utf-8") as f:
                    f.write(json.dumps(ligne, ensure_ascii=False) + "\n")
            print(f"✅ {cible['media']} <{cible['email']}>")
            if i < len(a_faire) - 1:
                time.sleep(random.uniform(35, 70))
    print(f"Terminé : {ok}/{len(a_faire)} envoyé(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
