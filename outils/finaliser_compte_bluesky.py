# -*- coding: utf-8 -*-
"""Finalise le compte du Crabe sur notre PDS : rotation du mot de passe,
mot de passe d'application, profil public, handle personnalisé.

À lancer après la création du compte et du TXT _atproto du handle final.

Usage :
    BSKY_ANCIEN_MOT_DE_PASSE='…' BSKY_NOUVEAU_MOT_DE_PASSE='…' \
        python3 outils/finaliser_compte_bluesky.py
"""
import json
import os
import subprocess
import sys
import time
import urllib.request

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ICI, "..", "engine"))
import reseau  # noqa: E402

PDS = os.environ.get("BSKY_PDS", "https://atproto.openclaw-france.fr")
API = PDS.rstrip("/") + "/xrpc"
IDENTIFIANT = os.environ.get("BSKY_IDENTIFIANT", "crabe.openclaw-france.fr")
HANDLE_FINAL = os.environ.get("BSKY_HANDLE_FINAL", "communaute.openclaw-france.fr")


def _poste(chemin, corps, jeton=None):
    donnees = json.dumps(corps).encode("utf-8")
    entetes = {"Content-Type": "application/json"}
    if jeton:
        entetes["Authorization"] = "Bearer " + jeton
    req = urllib.request.Request(API + chemin, data=donnees, headers=entetes, method="POST")
    with urllib.request.urlopen(req, timeout=60, context=reseau.contexte()) as r:
        brut = r.read().decode("utf-8")
        return json.loads(brut) if brut.strip() else {}


def main():
    ancien = os.environ.get("BSKY_ANCIEN_MOT_DE_PASSE", "")
    nouveau = os.environ.get("BSKY_NOUVEAU_MOT_DE_PASSE", "")
    if not ancien or not nouveau:
        return "BSKY_ANCIEN_MOT_DE_PASSE et BSKY_NOUVEAU_MOT_DE_PASSE requis."

    session = _poste("/com.atproto.server.createSession",
                     {"identifier": IDENTIFIANT, "password": ancien})
    jeton, did = session["accessJwt"], session["did"]

    app = _poste("/com.atproto.server.createAppPassword", {"name": "crabe-bot"}, jeton)
    print("🤖 Mot de passe d'application créé")

    _poste("/com.atproto.repo.putRecord",
           {"repo": did,
            "collection": "app.bsky.actor.profile",
            "rkey": "self",
            "record": {
                "$type": "app.bsky.actor.profile",
                "displayName": "Le Crabe 🦀 — La Communauté",
                "description": ("L'actu de l'IA en français, écrite et publiée à 100 % par une IA. "
                                "OpenClaw · Hermes · Claude · OpenAI · Mistral. "
                                "communaute.openclaw-france.fr"),
            }},
           jeton)
    print("🖼️  Profil renseigné")

    ok = False
    for _essai in range(8):
        try:
            _poste("/com.atproto.identity.updateHandle", {"handle": HANDLE_FINAL}, jeton)
            ok = True
            break
        except Exception as e:  # noqa: BLE001
            print(f"… handle pas encore validable ({str(e)[:70]}) — nouvelle tentative dans 10 s")
            time.sleep(10)
    print(f"🏷️  Handle final : {HANDLE_FINAL if ok else IDENTIFIANT}")

    # Le mot de passe est tourné EN DERNIER (il invalide les jetons en cours).
    _poste("/com.atproto.server.updatePassword", {"password": nouveau}, jeton)
    print("🔑 Mot de passe du compte tourné")

    if sys.platform == "darwin":
        for service, compte, valeur in (
                ("bluesky-communaute", IDENTIFIANT, nouveau),
                ("bluesky-communaute-app", "crabe", app["password"])):
            subprocess.run(["security", "add-generic-password", "-U",
                            "-s", service, "-a", compte, "-w", valeur], check=False)
        print("🔐 Secrets rangés dans le Trousseau macOS")

    print(f"FINAL did={did} handle={HANDLE_FINAL if ok else IDENTIFIANT}")
    return None


if __name__ == "__main__":
    probleme = main()
    if probleme:
        print("❌ " + probleme)
        sys.exit(1)
