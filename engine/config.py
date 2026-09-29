# -*- coding: utf-8 -*-
"""Configuration centrale de La Communauté — le site 100 % IA d'OpenClaw France.

Tout est surchargeable par variables d'environnement pour que le même code
tourne en local (Mac de Maël) et dans GitHub Actions.
"""
import os
from pathlib import Path

# --- Chemins ---
RACINE = Path(__file__).resolve().parent.parent
DOSSIER_DATA = RACINE / "data"
DOSSIER_SORTIE = RACINE / "_site"
DOSSIER_ASSETS = RACINE / "assets"
DOSSIER_FICHIERS = RACINE / "contenus" / "fichiers"

# --- Identité du site ---
NOM_SITE = "La Communauté"
SLOGAN = "Le hub francophone de l'IA et des agents autonomes"
DESCRIPTION_SITE = ("L'actualité de l'IA en français — OpenClaw, Hermes, Claude, ChatGPT, "
                    "Gemini, Mistral, DeepSeek… Écrite, publiée et maintenue à 100 % par une IA.")
URL_SITE = os.environ.get("URL_SITE", "https://communaute.openclaw-france.fr").rstrip("/")
DEPOT_GITHUB = os.environ.get("DEPOT_GITHUB", "https://github.com/mael-ctrl/openclaw-france-communaute")
REDACTEUR = "Le Crabe"
EMOJI_REDACTEUR = "🦀"

# --- DeepSeek ---
DEEPSEEK_CLE = os.environ.get("DEEPSEEK_API_KEY", "")
DEEPSEEK_URL = "https://api.deepseek.com"
MODELE_BREVES = os.environ.get("MODELE_BREVES", "deepseek-flash")
MODELE_ARTICLES = os.environ.get("MODELE_ARTICLES", "deepseek-flash")

# --- Cadence / garde-fous ---
MAX_BREVES_PAR_RUN = int(os.environ.get("MAX_BREVES_PAR_RUN", "6"))
MAX_ITEMS_PAR_RUN = int(os.environ.get("MAX_ITEMS_PAR_RUN", "40"))
MAX_ARTICLES_PAR_RUN = int(os.environ.get("MAX_ARTICLES_PAR_RUN", "1"))
FENETRE_JOURS = int(os.environ.get("FENETRE_JOURS", "3"))  # fraîcheur max des items traités
FICHIER_ETAT = DOSSIER_DATA / "etat.json"
FICHIER_BREVES = DOSSIER_DATA / "breves.json"
FICHIER_JOURNAL = DOSSIER_DATA / "journal.jsonl"
FICHIER_STATS = DOSSIER_DATA / "stats.json"
DOSSIER_ARTICLES = DOSSIER_DATA / "articles"
FICHIER_DEPLOY_ETAT = DOSSIER_DATA / "deploy_etat.json"
FICHIER_SOURCES = DOSSIER_DATA / "sources.json"

# --- FTP (OVH mutualisé jownmvu? non : zyqezjy — dossier Communaute) ---
FTP_SERVEUR = os.environ.get("FTP_SERVEUR", "ftp.cluster029.hosting.ovh.net")
FTP_UTILISATEUR = os.environ.get("FTP_UTILISATEUR", "zyqezjy-reelsvault")
FTP_MOT_DE_PASSE = os.environ.get("FTP_MOT_DE_PASSE", "")
FTP_DOSSIER = os.environ.get("FTP_DOSSIER", "Communaute")

# --- Divers ---
HTTP_UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
           "(KHTML, like Gecko) Chrome/126.0 Safari/537.36 LeCrabeBot/1.0")
