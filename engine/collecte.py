# -*- coding: utf-8 -*-
"""Collecte des flux RSS/Atom — stdlib uniquement.

- lit data/sources.json
- télécharge chaque flux (tolérant : un flux mort n'arrête rien)
- déduplique via data/etat.json (les items déjà vus sont ignorés)
- pré-filtre IA pour les médias généralistes (mots-clés)
"""
import hashlib
import html
import json
import re
import time
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime

import config
import reseau

MOTS_IA = re.compile(
    r"\b(ia|ai|intelligence artificielle|artificial intelligence|chatgpt|openai|claude|"
    r"anthropic|gemini|google deepmind|mistral|deepseek|llm|large language|agent|agents|"
    r"agentique|agentic|machine learning|apprentissage|nvidia|copilot|groq|openrouter|"
    r"hugging ?face|meta ai|llama|gpt|modèle|model|prompt|chatbot|robot|automatisation|"
    r"openclaw|hermes|claude ?code|codex|cursor|midjourney|stable diffusion|sora|veo)\b",
    re.IGNORECASE)


def _nettoyer(texte, maxi=800):
    if not texte:
        return ""
    texte = re.sub(r"<br\s*/?>", " ", texte, flags=re.IGNORECASE)
    texte = re.sub(r"<[^>]+>", " ", texte)
    texte = html.unescape(texte)
    texte = re.sub(r"\s+", " ", texte).strip()
    return texte[:maxi]


def _date_depuis_item(item, ns):
    """Récupère la date de publication la plus fiable possible."""
    for balise in ("pubDate", "published", "updated", "date"):
        for prefixe in ("", "{http://www.w3.org/2005/Atom}"):
            el = item.find(prefixe + balise)
            if el is not None and el.text:
                brut = el.text.strip()
                try:
                    if "T" in brut or "-" in brut[:5]:
                        dt = datetime.fromisoformat(brut.replace("Z", "+00:00"))
                    else:
                        dt = parsedate_to_datetime(brut)
                    if dt.tzinfo is None:
                        dt = dt.replace(tzinfo=timezone.utc)
                    return dt.astimezone(timezone.utc)
                except Exception:
                    continue
    return None


def _lien_depuis_item(item, ns):
    for prefixe in ("", "{http://www.w3.org/2005/Atom}"):
        el = item.find(prefixe + "link")
        if el is not None:
            if el.text and el.text.strip().startswith("http"):
                return el.text.strip()
            if el.get("href"):
                return el.get("href").strip()
        el = item.find(prefixe + "link[@rel='alternate']")
        if el is not None and el.get("href"):
            return el.get("href").strip()
    # Atom avec plusieurs <link>
    for ln in item.findall("{http://www.w3.org/2005/Atom}link"):
        if ln.get("rel", "alternate") == "alternate" and ln.get("href"):
            return ln.get("href").strip()
    for ln in item.findall("link"):
        if ln.get("href"):
            return ln.get("href").strip()
    return ""


def _texte_enfant(item, noms):
    for nom in noms:
        for prefixe in ("", "{http://www.w3.org/2005/Atom}"):
            el = item.find(prefixe + nom)
            if el is not None and (el.text or "").strip():
                return el.text.strip()
    return ""


def telecharger_flux(source):
    """Renvoie la liste d'items bruts d'un flux (peut lever une exception)."""
    req = urllib.request.Request(source["url"], headers={"User-Agent": config.HTTP_UA,
                                                         "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, */*"})
    with urllib.request.urlopen(req, timeout=30, context=reseau.contexte()) as r:
        brut = r.read()
    # Les feeds XML peuvent arriver avec un BOM ou du bruit en tête
    racine = ET.fromstring(brut)
    ns = {"atom": "http://www.w3.org/2005/Atom",
          "content": "http://purl.org/rss/1.0/modules/content/"}
    items = racine.findall(".//item") or racine.findall(".//atom:entry", ns)
    resultats = []
    for item in items[:25]:
        titre = _nettoyer(_texte_enfant(item, ["title"]), 300)
        lien = _lien_depuis_item(item, ns)
        if not titre or not lien:
            continue
        resume = _nettoyer(_texte_enfant(item, ["description", "summary",
                                                "{http://purl.org/rss/1.0/modules/content/}encoded",
                                                "content"]), 900)
        date = _date_depuis_item(item, ns)
        resultats.append({"titre": titre, "lien": lien, "resume": resume, "date": date,
                          "source": source["nom"], "langue": source.get("langue", "fr"),
                          "priorite": source.get("priorite", 3),
                          "filtre_ia": source.get("filtre_ia", False)})
    return resultats


def _identifiant(item):
    base = (item["lien"] or "") + "|" + item["titre"]
    return hashlib.sha1(base.encode("utf-8")).hexdigest()[:16]


def charger_etat():
    if config.FICHIER_ETAT.exists():
        try:
            etat = json.loads(config.FICHIER_ETAT.read_text(encoding="utf-8"))
            etat.setdefault("vus", {})
            return etat
        except ValueError:
            pass
    return {"vus": {}}


def sauver_etat(etat):
    config.DOSSIER_DATA.mkdir(parents=True, exist_ok=True)
    # On purge les "vus" de plus de 45 jours pour ne pas gonfler le fichier
    limite = (datetime.now(timezone.utc) - timedelta(days=45)).isoformat()
    etat["vus"] = {k: v for k, v in etat["vus"].items() if v > limite}
    config.FICHIER_ETAT.write_text(json.dumps(etat, ensure_ascii=False, indent=0),
                                   encoding="utf-8")


def collecter(verbeux=True):
    """Point d'entrée : renvoie (items_neufs, rapport)."""
    sources = json.loads(config.FICHIER_SOURCES.read_text(encoding="utf-8"))
    etat = charger_etat()
    maintenant = datetime.now(timezone.utc)
    limite_fraicheur = maintenant - timedelta(days=config.FENETRE_JOURS)

    neufs, rapport = [], []
    for source in sources:
        try:
            items = telecharger_flux(source)
            gardes = 0
            for item in items:
                ident = _identifiant(item)
                if ident in etat["vus"]:
                    continue
                if item["date"] and item["date"] < limite_fraicheur:
                    etat["vus"][ident] = maintenant.isoformat(timespec="seconds")
                    continue
                if item.get("filtre_ia"):
                    cible = item["titre"] + " " + (item["resume"] or "")
                    if not MOTS_IA.search(cible):
                        etat["vus"][ident] = maintenant.isoformat(timespec="seconds")
                        continue
                item["id"] = ident
                neufs.append(item)
                gardes += 1
            rapport.append(f"{source['nom']}: {gardes} neuf(s)")
        except Exception as e:
            rapport.append(f"{source['nom']}: ÉCHEC ({str(e)[:80]})")
            time.sleep(0.3)

    # Les plus récents d'abord ; à date égale, la priorité décide
    neufs.sort(key=lambda x: (x["date"] or datetime(1970, 1, 1, tzinfo=timezone.utc),
                              x.get("priorite", 3)), reverse=True)
    neufs = neufs[:config.MAX_ITEMS_PAR_RUN]
    for item in neufs:
        etat["vus"][item["id"]] = maintenant.isoformat(timespec="seconds")
    sauver_etat(etat)
    if verbeux:
        for ligne in rapport:
            print("   ·", ligne)
    return neufs, rapport
