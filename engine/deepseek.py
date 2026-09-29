# -*- coding: utf-8 -*-
"""Client HTTP minimal pour l'API DeepSeek — zéro dépendance externe.

Utilisé par tous les étages de la rédaction : brèves, articles, éditos.
Chaque appel renvoie (texte, usage) avec usage = {"entree": n, "sortie": n}.
"""
import json
import time
import urllib.error
import urllib.request

import config
import reseau


def _poste(url, corps, cle, essais=3):
    donnees = json.dumps(corps).encode("utf-8")
    derniere = None
    for i in range(essais):
        try:
            req = urllib.request.Request(
                url, data=donnees, method="POST",
                headers={"Authorization": f"Bearer {cle}",
                         "Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=240, context=reseau.contexte()) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "ignore")[:400]
            derniere = RuntimeError(f"DeepSeek HTTP {e.code}: {detail}")
            if e.code in (429, 500, 502, 503) and i < essais - 1:
                time.sleep(6 * (i + 1))
                continue
            raise derniere
        except Exception as e:  # timeouts, réseau…
            derniere = e
            if i < essais - 1:
                time.sleep(5 * (i + 1))
                continue
            raise
    raise derniere or RuntimeError("DeepSeek : échec inconnu")


def discuter(modele, messages, json_force=True, temperature=0.7, max_tokens=4000):
    """Un tour de conversation. Renvoie (texte, usage)."""
    corps = {"model": modele, "messages": messages,
             "temperature": temperature, "max_tokens": max_tokens}
    if json_force:
        corps["response_format"] = {"type": "json_object"}
    d = _poste(config.DEEPSEEK_URL + "/chat/completions", corps, config.DEEPSEEK_CLE)
    choix = (d.get("choices") or [{}])[0]
    texte = ((choix.get("message") or {}).get("content") or "").strip()
    u = d.get("usage") or {}
    return texte, {"entree": int(u.get("prompt_tokens") or 0),
                   "sortie": int(u.get("completion_tokens") or 0)}


def solde():
    """Solde du compte DeepSeek (donnée réelle, affichée sur /transparence)."""
    try:
        req = urllib.request.Request(
            config.DEEPSEEK_URL + "/user/balance",
            headers={"Authorization": f"Bearer {config.DEEPSEEK_CLE}"})
        with urllib.request.urlopen(req, timeout=30, context=reseau.contexte()) as r:
            d = json.loads(r.read().decode("utf-8"))
        b = (d.get("balance_infos") or [{}])[0]
        return {"total": b.get("total_balance"), "devise": b.get("currency"),
                "disponible": bool(d.get("is_available"))}
    except Exception as e:
        return {"erreur": str(e)[:200]}
