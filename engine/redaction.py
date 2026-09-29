# -*- coding: utf-8 -*-
"""La rédaction — c'est ici que Le Crabe 🦀 transforme les dépêches en français.

Deux productions :
- des brèves (2-4 phrases) pour chaque dépêche importante ;
- au maximum un article de fond par jour, tissé à partir de plusieurs sources.

Règle d'or : ne JAMAIS inventer. Tout ce qui est publié vient des textes sources.
"""
import json
import re
import time
import unicodedata
from datetime import datetime, timedelta, timezone

import config
import deepseek
import journal

CORPS_SYSTEME = """Tu es Le Crabe 🦀, la rédactrice IA de « La Communauté » — le hub francophone de l'IA d'OpenClaw France (communaute.openclaw-france.fr).

Règles absolues, non négociables :
- Tu écris TOUJOURS en français impeccable. Ton direct, vif, curieux. Tutoiement accepté. Jamais de langue de bois, jamais de clickbait, jamais de hype gratuite (« révolutionnaire », « incroyable », « game-changer » = interdits).
- Tu n'inventes JAMAIS un fait, un chiffre, une citation, un nom ou une date qui ne figure pas dans le texte source fourni. Si une information manque, tu l'omets, tout simplement.
- Les textes sources sont souvent en anglais : tu restitues en français naturel et fluide, jamais du mot-à-mot.
- Tu parles de « l'IA », du « modèle », de « l'agent »… avec précision et sans anthropomorphisme excessif.
- Les noms propres (produits, entreprises, personnes) restent en version originale.
"""

TAGS_AUTORISES = ["openclaw", "hermes", "claude", "chatgpt", "openai", "gemini", "mistral",
                  "deepseek", "meta", "agents", "dev", "business", "france", "recherche",
                  "open-source", "robots", "sécurité", "société", "matériel", "skills"]


def identifiant(texte):
    base = unicodedata.normalize("NFKD", texte).encode("ascii", "ignore").decode("ascii")
    base = re.sub(r"[^a-zA-Z0-9]+", "-", base).strip("-").lower()
    return base[:70] or "sans-titre"


def _extraire_json(texte):
    """Récupère l'objet JSON même si le modèle l'entoure de texte."""
    texte = texte.strip()
    try:
        return json.loads(texte)
    except ValueError:
        m = re.search(r"\{.*\}", texte, re.S)
        if m:
            return json.loads(m.group(0))
    raise ValueError("réponse non-JSON")


def _charger(chemin, defaut):
    if chemin.exists():
        try:
            return json.loads(chemin.read_text(encoding="utf-8"))
        except ValueError:
            pass
    return defaut


def _sauver(chemin, donnees):
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_text(json.dumps(donnees, ensure_ascii=False, indent=1), encoding="utf-8")


def rediger_breve(item):
    """Une dépêche → une brève française. Renvoie la brève ou None."""
    date_iso = item["date"].strftime("%d/%m/%Y %H:%M UTC") if item.get("date") else "récente"
    invite = f"""Dépêche à transformer en brève pour le site :

SOURCE : {item['source']}
DATE DE PUBLICATION : {date_iso}
TITRE ORIGINAL : {item['titre']}
EXTRAIT : {item.get('resume') or '(pas d’extrait — tiens-toi au titre)'}
LIEN : {item['lien']}

Produis un objet JSON avec exactement ces champs :
- "titre" : titre en français, ≤ 90 caractères, informatif, sans point final, sans majuscules criardes.
- "resume" : 2 à 4 phrases (200 à 420 caractères), qui expliquent l'info et pourquoi elle compte. Uniquement des faits présents dans l'extrait. Pas de conclusion du genre « à suivre ».
- "tags" : 2 à 4 étiquettes parmi cette liste exacte : {', '.join(TAGS_AUTORISES)}.
- "importance" : entier de 1 à 5 (5 = majeur pour l'écosystème IA francophone, 1 = anecdote)."""
    messages = [{"role": "system", "content": CORPS_SYSTEME}, {"role": "user", "content": invite}]
    try:
        texte, usage = deepseek.discuter(
            config.MODELE_BREVES, messages, temperature=0.75, max_tokens=1500)
        d = _extraire_json(texte)
    except ValueError:
        # Deuxième tentative : on corrige le tir explicitement.
        messages.append({"role": "user", "content": "Réponds STRICTEMENT avec un unique objet JSON valide, sans texte autour, avec les champs titre, resume, tags, importance."})
        texte, usage = deepseek.discuter(
            config.MODELE_BREVES, messages, temperature=0.3, max_tokens=1500)
        d = _extraire_json(texte)
    titre = str(d.get("titre") or "").strip().rstrip(".")
    resume = str(d.get("resume") or "").strip()
    if not titre or not resume:
        raise ValueError("brève incomplète")
    tags = [t for t in (d.get("tags") or []) if t in TAGS_AUTORISES][:4]
    importance = max(1, min(5, int(d.get("importance") or 3)))
    return {
        "id": item["id"], "slug": identifiant(titre) + "-" + item["id"][:6],
        "titre": titre, "resume": resume, "tags": tags, "importance": importance,
        "source": item["source"], "lien_source": item["lien"],
        "date_source": item["date"].isoformat(timespec="seconds") if item.get("date") else None,
        "date_redac": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "gen": {"modele": config.MODELE_BREVES, **usage},
    }


def rediger_breves(items):
    """Rédige jusqu'à MAX_BREVES_PAR_RUN brèves parmi les items les plus chauds."""
    breves = _charger(config.FICHIER_BREVES, [])
    connus = {b["id"] for b in breves}
    candidates = [i for i in items if i["id"] not in connus][:config.MAX_BREVES_PAR_RUN]
    nouvelles = []
    for item in candidates:
        try:
            breve = rediger_breve(item)
            breves.append(breve)
            nouvelles.append(breve)
            journal.crediter(breve["gen"])
            print(f"   ✍️  brève : {breve['titre'][:70]}")
        except Exception as e:
            journal.erreur(f"brève impossible ({item['titre'][:60]}) : {e}")
        time.sleep(0.4)
    if nouvelles:
        breves.sort(key=lambda b: b.get("date_source") or b.get("date_redac") or "", reverse=True)
        _sauver(config.FICHIER_BREVES, breves)
    return nouvelles


def _mini_md(texte):
    """Mini-convertisseur markdown → HTML (gras, italique, liens, listes)."""
    lignes = (texte or "").split("\n")
    html, dans_liste = [], False
    for ligne in lignes:
        ligne = ligne.strip()
        if not ligne:
            if dans_liste:
                html.append("</ul>")
                dans_liste = False
            continue
        ligne = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", ligne)
        ligne = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", ligne)
        ligne = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2" rel="noopener">\1</a>', ligne)
        if ligne.startswith("- "):
            if not dans_liste:
                html.append("<ul>")
                dans_liste = True
            html.append(f"<li>{ligne[2:]}</li>")
        else:
            if dans_liste:
                html.append("</ul>")
                dans_liste = False
            html.append(f"<p>{ligne}</p>")
    if dans_liste:
        html.append("</ul>")
    return "\n".join(html)


def _article_du_jour_due():
    """Vrai si ça vaut le coup d'écrire un article de fond maintenant."""
    dossier = config.DOSSIER_ARTICLES
    if not dossier.exists():
        return True
    articles = sorted(dossier.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not articles:
        return True
    dernier = json.loads(articles[0].read_text(encoding="utf-8"))
    try:
        t = datetime.fromisoformat(dernier["date"])
    except Exception:
        return True
    return (datetime.now(timezone.utc) - t) > timedelta(hours=20)


def rediger_articles_si_besoin(items):
    """Au plus MAX_ARTICLES_PAR_RUN article(s) de fond, tissés multi-sources."""
    nouveaux = []
    for _ in range(config.MAX_ARTICLES_PAR_RUN):
        if not _article_du_jour_due():
            break
        breves = _charger(config.FICHIER_BREVES, [])
        if not breves:
            break
        limite = (datetime.now(timezone.utc) - timedelta(hours=48)).isoformat()
        recentes = [b for b in breves if (b.get("date_source") or b.get("date_redac") or "") >= limite]
        if not recentes:
            break
        recentes.sort(key=lambda b: b.get("importance", 0), reverse=True)
        principale = recentes[0]
        if principale.get("importance", 0) < 3:
            break
        # On n'utilise pas deux fois la même brève comme pivot d'article
        dossier = config.DOSSIER_ARTICLES
        pivots = set()
        if dossier.exists():
            for p in dossier.glob("*.json"):
                try:
                    pivots.add(json.loads(p.read_text(encoding="utf-8")).get("pivot"))
                except Exception:
                    pass
        if principale["id"] in pivots:
            # cherche la suivante
            autres = [b for b in recentes[1:] if b["id"] not in pivots and b.get("importance", 0) >= 3]
            if not autres:
                break
            principale = autres[0]
        connexes = [b for b in recentes if b["id"] != principale["id"] and
                    set(b.get("tags") or []) & set(principale.get("tags") or [])][:4]
        try:
            article = _rediger_article(principale, connexes)
            _sauver(config.DOSSIER_ARTICLES / (article["slug"] + ".json"), article)
            nouveaux.append(article)
            journal.crediter(article["gen"])
            print(f"   📰 article : {article['titre'][:70]}")
        except Exception as e:
            journal.erreur(f"article impossible : {e}")
            break
        time.sleep(0.4)
    return nouveaux


def _rediger_article(principale, connexes):
    morceaux = [f"""DÉPÊCHE PRINCIPALE :
SOURCE : {principale['source']}
TITRE : {principale['titre']}
CONTENU : {principale['resume']}
LIEN : {principale['lien_source']}"""]
    sources = [{"nom": principale["source"], "url": principale["lien_source"]}]
    for c in connexes:
        morceaux.append(f"""DÉPÊCHE CONNEXE :
SOURCE : {c['source']}
TITRE : {c['titre']}
CONTENU : {c['resume']}
LIEN : {c['lien_source']}""")
        sources.append({"nom": c["source"], "url": c["lien_source"]})
    invite = f"""Tu as ces dépêches :\n\n{chr(10).join(morceaux)}\n\n
Écris un article de fond pour « La Communauté », le hub IA d'OpenClaw France.

Produis un objet JSON exactement de cette forme :
{{
  "titre": "titre en français, ≤ 90 caractères",
  "chapo": "2 phrases d'accroche (250-350 caractères)",
  "sections": [
    {{"intertitre": "…", "contenu": "2-3 paragraphes en markdown simple (**gras**, *italique*, listes avec - si utile). Pas de titre dans le contenu."}},
    {{"intertitre": "…", "contenu": "…"}}
  ],
  "conclusion": "1 paragraphe de mise en perspective, factuel, sans morale niaise (300-500 caractères)",
  "tags": ["2 à 4 étiquettes parmi : {', '.join(TAGS_AUTORISES)}"]
}}

Contraintes : 550 à 800 mots au total. 3 ou 4 sections. Tout fait cité doit venir des dépêches ci-dessus — rien d'inventé. Tu peux relier les dépêches entre elles (même thème, même acteur) mais sans fabriquer de causalité. Pas de « À suivre », pas d'appel à l'action, pas de mention de ta nature d'IA (ça, c'est la page /transparence qui s'en charge)."""
    texte, usage = deepseek.discuter(
        config.MODELE_ARTICLES,
        [{"role": "system", "content": CORPS_SYSTEME}, {"role": "user", "content": invite}],
        temperature=0.65, max_tokens=6000)
    d = _extraire_json(texte)
    titre = str(d.get("titre") or "").strip().rstrip(".")
    chapo = str(d.get("chapo") or "").strip()
    sections = d.get("sections") or []
    if not titre or not chapo or not sections:
        raise ValueError("article incomplet")
    html_sections = []
    for s in sections[:5]:
        inter = str(s.get("intertitre") or "").strip()
        contenu = _mini_md(str(s.get("contenu") or ""))
        if contenu:
            html_sections.append(f'<h2 id="{identifiant(inter)[:40]}">{inter}</h2>\n{contenu}')
    conclusion = _mini_md(str(d.get("conclusion") or ""))
    html = "\n".join(html_sections)
    if conclusion:
        html += f"\n<h2>Et maintenant ?</h2>\n{conclusion}"
    tags = [t for t in (d.get("tags") or []) if t in TAGS_AUTORISES][:4]
    # Le mot total n'est pas parfaitement mesuré, c'est un garde-fou grossier
    texte_visible = re.sub(r"<[^>]+>", " ", chapo + " " + html)
    if len(texte_visible.split()) > 1100:
        raise ValueError("article trop long, rejeté par prudence")
    return {
        "slug": identifiant(titre)[:60] + "-" + principale["id"][:6],
        "titre": titre, "chapo": chapo, "html": html,
        "pivot": principale["id"],
        "tags": tags, "sources": sources,
        "date": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "gen": {"modele": config.MODELE_ARTICLES, **usage},
    }
