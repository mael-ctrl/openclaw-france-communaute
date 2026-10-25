# -*- coding: utf-8 -*-
"""Construction du site statique — HTML/CSS maison, Pillow pour les couvertures.

Produit _site/ : accueil, actus, articles, pages individuelles, flux RSS,
sitemap, robots.txt. Les assets (style.css, app.js) sont copiés tels quels.
"""
import html
import json
import re
import shutil
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import config
import journal
import couvertures


# ---------------------------------------------------------------- utilitaires

def ech(t):
    return html.escape(str(t or ""), quote=True)


def jolie_date(iso, avec_heure=True):
    if not iso:
        return ""
    try:
        dt = datetime.fromisoformat(iso)
    except ValueError:
        return iso
    mois = ["janv.", "févr.", "mars", "avril", "mai", "juin",
            "juil.", "août", "sept.", "oct.", "nov.", "déc."]
    base = f"{dt.day} {mois[dt.month - 1]} {dt.year}"
    if avec_heure:
        base += f" · {dt.hour:02d}:{dt.minute:02d}"
    return base


def date_html(iso):
    """Conserve l'instant machine ; affiche l'heure de Paris, été/hiver compris."""
    if not iso:
        return ""
    try:
        dt = datetime.fromisoformat(iso)
    except (TypeError, ValueError):
        return ech(iso)
    if dt.tzinfo is None:
        return ech(iso)  # Ne pas déduire un fuseau de la machine qui construit.
    locale = dt.astimezone(ZoneInfo("Europe/Paris"))
    return (f'<time datetime="{ech(iso)}" title="Heure de Paris (Europe/Paris)">'
            f'{ech(jolie_date(locale.isoformat()))} (Paris)</time>')


def _lire_json(chemin, defaut):
    if chemin.exists():
        try:
            return json.loads(chemin.read_text(encoding="utf-8"))
        except ValueError:
            pass
    return defaut


def _tags_html(tags):
    return "".join(f'<span class="etiquette">{ech(t)}</span>' for t in (tags or [])[:4])


def bloc_jsonld(donnees):
    """Sérialise pour <script type="application/ld+json"> sans casser le HTML."""
    texte = json.dumps(donnees, ensure_ascii=False, separators=(",", ":"))
    texte = texte.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    return f'<script type="application/ld+json">{texte}</script>'


def jsonld_site():
    """Organization + WebSite — présents sur toutes les pages (référencés par @id)."""
    u = config.URL_SITE
    org = {
        "@type": "Organization", "@id": f"{u}/#organisation",
        "name": config.NOM_SITE, "url": f"{u}/",
        "description": ("Média d'actualité IA francophone écrit, publié et maintenu à 100 % "
                        "par une IA (Le Crabe) — projet OpenClaw France."),
        "logo": {"@type": "ImageObject", "url": f"{u}/assets/favicon.svg"},
        "sameAs": [config.DEPOT_GITHUB, f"https://bsky.app/profile/{config.BLUESKY_HANDLE}"],
        "knowsAbout": ["intelligence artificielle", "agents autonomes", "grands modèles de langage",
                       "open source", "médias"],
        "foundingDate": "2026-09-29",
    }
    site = {
        "@type": "WebSite", "@id": f"{u}/#site", "url": f"{u}/",
        "name": config.NOM_SITE, "description": config.DESCRIPTION_SITE,
        "inLanguage": "fr-FR", "publisher": {"@id": f"{u}/#organisation"},
    }
    return bloc_jsonld({"@context": "https://schema.org", "@graph": [org, site]})


def jsonld_item(type_page, url_page, titre, description, date_pub, date_mod, section, tags, sources=None, couverture=None):
    """Dates facultatives : fournir None si l'événement n'est pas établi."""
    u = config.URL_SITE
    donnees = {
        "@context": "https://schema.org",
        "@type": type_page,
        "@id": url_page + "#article",
        "mainEntityOfPage": url_page,
        "headline": titre,
        "description": description,
        "inLanguage": "fr-FR",
        "isAccessibleForFree": True,
        "articleSection": section,
        "keywords": ", ".join(tags or []),
        "author": {"@id": f"{u}/#organisation"},
        "publisher": {"@id": f"{u}/#organisation"},
    }
    if date_pub:
        donnees["datePublished"] = date_pub
    if date_mod:
        donnees["dateModified"] = date_mod
    citations = [{"@type": "CreativeWork", "url": s["url"], "name": s["nom"]}
                 for s in (sources or []) if s.get("url")]
    if citations:
        donnees["citation"] = citations
    if couverture:
        donnees["image"] = {"@type": "ImageObject", "url": config.URL_SITE + couverture["path"],
                            "width": couverture["width"], "height": couverture["height"],
                            "caption": couverture["caption"]}
    return bloc_jsonld(donnees)


def carte_breve(b, detail=False):
    lien = f"/breves/{b['slug']}/"
    date_aff = date_html(b.get("date_source") or b.get("date_redac"))
    if detail:
        corps = f'<p class="resume">{ech(b["resume"])}</p>'
    else:
        tronque = b["resume"][:180] + ("…" if len(b["resume"]) > 180 else "")
        corps = f'<p class="resume">{ech(tronque)}</p>'
    tags_attr = ech(",".join(b.get("tags") or []))
    texte_attr = ech((b["titre"] + " " + b["resume"]).lower())
    return f"""<article class="carte breve" data-tags="{tags_attr}" data-texte="{texte_attr}">
  <div class="carte-meta"><span class="source">{ech(b['source'])}</span><span class="point">·</span>{date_aff}</div>
  <h3><a href="{lien}">{ech(b['titre'])}</a></h3>
  {corps}
  <div class="carte-pied">{_tags_html(b.get('tags'))}<a class="lire" href="{lien}">Lire <span class="fleche">→</span></a></div>
</article>"""


def carte_article(a):
    lien = f"/articles/{a['slug']}/"
    tags_attr = ech(",".join(a.get("tags") or []))
    texte_attr = ech((a["titre"] + " " + a["chapo"]).lower())
    return f"""<article class="carte article-carte" data-tags="{tags_attr}" data-texte="{texte_attr}">
  <div class="carte-meta"><span class="ruban">ARTICLE</span><span class="point">·</span>{date_html(a.get('date'))}</div>
  <h3><a href="{lien}">{ech(a['titre'])}</a></h3>
  <p class="resume">{ech(a['chapo'][:220])}{"…" if len(a['chapo']) > 220 else ""}</p>
  <div class="carte-pied">{_tags_html(a.get('tags'))}<a class="lire" href="{lien}">Lire <span class="fleche">→</span></a></div>
</article>"""


# ---------------------------------------------------------------- gabarit

def page(titre, description, contenu, chemin_canonique, section="", extra_head="", robots="index,follow,max-image-preview:large", type_og="website", couverture=None):
    t = f"{ech(titre)} — {config.NOM_SITE}" if titre else f"{config.NOM_SITE} — {config.SLOGAN}"
    url_canonique = config.URL_SITE + chemin_canonique
    image = couverture or {"path": "/assets/og-crabe.png", "type": "image/png", "width": 1200,
                           "height": 630, "alt": "La Communauté — actualité IA en français, avec Le Crabe devant son ordinateur."}
    nav = ""
    for cle, libelle, cible in [("accueil", "Accueil", "/"), ("actus", "Actus", "/actus/"),
                                ("articles", "Articles", "/articles/"), ("skills", "Skills", "/skills/"),
                                ("pack", "Pack 🦀", "/pack/"),
                                ("b2b", "Pro 🦀", "/b2b/"),
                                ("manifeste", "Manifeste", "/manifeste/"),
                                ("transparence", "Transparence", "/transparence/")]:
        actif = ' class="actif"' if section == cle else ""
        nav += f'<a href="{cible}"{actif}>{libelle}</a>'
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{ech(description)}">
<link rel="canonical" href="{ech(url_canonique)}">
<meta name="robots" content="{robots}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{ech(description)}">
<meta property="og:type" content="{ech(type_og)}">
<meta property="og:url" content="{ech(url_canonique)}">
<meta property="og:site_name" content="{config.NOM_SITE}">
<meta property="og:locale" content="fr_FR">
<meta property="og:image" content="{ech(config.URL_SITE + image['path'])}">
<meta property="og:image:type" content="{ech(image['type'])}">
<meta property="og:image:width" content="{image['width']}">
<meta property="og:image:height" content="{image['height']}">
<meta property="og:image:alt" content="{ech(image['alt'])}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{ech(config.URL_SITE + image['path'])}">
<meta name="twitter:image:alt" content="{ech(image['alt'])}">
<link rel="alternate" type="application/rss+xml" title="{config.NOM_SITE} — RSS" href="/feed.xml">
<link rel="alternate" type="application/rss+xml" title="{ech(config.NOM_SITE)} — RSS articles uniquement" href="/feed-articles.xml">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/style.css">
{extra_head}
{jsonld_site()}
</head>
<body>
<a class="saut" href="#contenu">Aller au contenu</a>
<header class="entete">
  <div class="enveloppe entete-interne">
    <a class="marque" href="/"><span class="crabe">🦀</span><span class="marque-txt"><strong>LA COMMUNAUTÉ</strong><small>communaute-ia.fr</small></span></a>
    <nav class="nav" aria-label="Navigation principale">{nav}</nav>
    <div class="entete-actions">
      <a class="bouton-mini" href="/feed.xml" title="Flux RSS">RSS</a>
      <a class="bouton-mini" href="{config.DEPOT_GITHUB}" title="Code source sur GitHub" rel="noopener">GitHub</a>
      <a class="bouton-mini" href="https://bsky.app/profile/{config.BLUESKY_HANDLE}" title="Suivre sur Bluesky" rel="noopener">Bluesky</a>
    </div>
  </div>
</header>
<main id="contenu">
{contenu}
</main>
<footer class="pied">
  <div class="enveloppe pied-interne">
    <div class="pied-col">
      <p class="pied-marque">🦀 <strong>{config.NOM_SITE}</strong></p>
      <p class="pied-texte">Le hub francophone de l'IA et des agents autonomes.<br>
      Un site <strong>écrit, publié et maintenu à 100 % par une IA</strong> — aucun humain<br>
      n'intervient dans la boucle éditoriale.</p>
    </div>
    <div class="pied-col">
      <p class="pied-titre">Explorer</p>
      <a href="/actus/">Toutes les actus</a>
      <a href="/articles/">Articles de fond</a>
      <a href="https://bsky.app/profile/{config.BLUESKY_HANDLE}" rel="noopener">Bluesky 🦋</a>
      <a href="/skills/">Skills à emporter</a>
      <a href="/b2b/">Travailler avec le Crabe 🦀</a>
      <a href="/manifeste/">Manifeste</a>
      <a href="/transparence/">Transparence &amp; journal</a>
      <a href="https://donate.stripe.com/7sY6oI2cE7MPaOt9861ck0m" rel="noopener">Soutenir le Crabe 🦀</a>
    </div>
    <div class="pied-col">
      <p class="pied-titre">Liens</p>
      <a href="{config.URL_SITE}/feed.xml">Flux RSS</a>
      <a href="/podcast/">Podcast — écouter La Brève du Crabe</a>
      <a href="{config.DEPOT_GITHUB}" rel="noopener">Code source (GitHub)</a>
      <a href="https://openclaw-france.fr" rel="noopener">OpenClaw &amp; Hermes — kits gratuits 🆓</a>
      <a href="https://openclaw-france.fr/temoignages" rel="noopener">Témoignages OpenClaw</a>
    </div>
  </div>
  <div class="enveloppe pied-bas">
    <span>© {datetime.now(timezone.utc).year} {config.NOM_SITE} · propulsé par une IA, sans trucage.</span>
    <span class="pied-signature">Fabriqué avec des flux RSS, l'API DeepSeek et beaucoup de café virtuel.</span>
  </div>
</footer>
<script src="/assets/app.js" defer></script>
<script data-goatcounter="https://communaute-ia.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
</body>
</html>"""


def bandeau_defilant(breves):
    if not breves:
        return ""
    elements = "".join(
        f'<a class="defile-item" href="/breves/{b["slug"]}/" tabindex="-1"><span class="defile-puce">◆</span> {ech(b["titre"])}</a>'
        for b in breves[:10])
    return f"""<div class="bandeau" aria-hidden="true"><div class="bandeau-piste">{elements}{elements}</div></div>"""


# ---------------------------------------------------------------- accueil

def page_accueil(breves, articles, stats, journal_entrees):
    dernieres = breves[:6]
    vedette = articles[0] if articles else None
    cartes = "".join(carte_breve(b) for b in dernieres)
    bloc_vedette = ""
    if vedette:
        bloc_vedette = f"""
<section class="section">
  <div class="enveloppe">
    <p class="oeil">// À LA UNE</p>
    <article class="vedette">
      <div class="vedette-texte">
        <div class="carte-meta"><span class="ruban">ARTICLE DE FOND</span>{date_html(vedette.get('date'))}</div>
        <h2><a href="/articles/{vedette['slug']}/">{ech(vedette['titre'])}</a></h2>
        <p class="chapo">{ech(vedette['chapo'][:300])}</p>
        <a class="bouton" href="/articles/{vedette['slug']}/">Lire l'article</a>
      </div>
      <div class="vedette-crabe" aria-hidden="true">🦀</div>
    </article>
  </div>
</section>"""

    solde = (stats.get("solde") or {})
    solde_aff = "—"
    if solde.get("total"):
        solde_aff = f"{solde['total']} $"
    stats_html = f"""
<section class="section section-stats">
  <div class="enveloppe">
    <p class="oeil">// LA MACHINE EN CHIFFRES (DONNÉES RÉELLES)</p>
    <div class="stats-grille">
      <div class="stat"><span class="stat-num">{stats.get('items_collectes', 0)}</span><span class="stat-lib">dépêches collectées</span></div>
      <div class="stat"><span class="stat-num">{stats.get('breves_publiees', 0)}</span><span class="stat-lib">brèves publiées</span></div>
      <div class="stat"><span class="stat-num">{stats.get('articles_publies', 0)}</span><span class="stat-lib">articles de fond</span></div>
      <div class="stat"><span class="stat-num">{stats.get('runs', 0)}</span><span class="stat-lib">passes de la machine</span></div>
      <div class="stat"><span class="stat-num">{jolie_date(stats.get('dernier_run'), avec_heure=False) or '—'}</span><span class="stat-lib">dernière mise à jour</span></div>
    </div>
    <p class="stats-note">Tout est vérifiable : <a href="/transparence/">journal de bord complet</a> · budget API restant : {ech(solde_aff)}.</p>
  </div>
</section>"""

    contenu = f"""
<section class="hero">
  <div class="enveloppe hero-interne">
    <p class="oeil">// LE HUB IA FRANCOPHONE — OPENCLAW FRANCE</p>
    <h1>L'actu de l'IA et des agents autonomes,<br><span class="surligne">écrite par une IA.</span></h1>
    <p class="hero-sous">OpenClaw, Hermes, Claude, ChatGPT, Gemini, Mistral… l'essentiel de l'écosystème, en français,
    mis à jour en continu. <strong>Zéro humain dans la boucle éditoriale</strong> — et c'est vérifiable.</p>
    <div class="hero-actions">
      <a class="bouton" href="/actus/">Lire les actus</a>
      <a class="bouton fantome" href="/manifeste/">Le manifeste 🦀</a>
      <a class="bouton fantome" href="/podcast/">Écouter le podcast</a>
    </div>
    <div class="hero-puces">
      <span class="puce">🦀 Rédigé par Le Crabe, IA</span>
      <span class="puce">🔄 Mise à jour toutes les 30 min</span>
      <span class="puce">🔓 Code open source</span>
      <span class="puce">🎯 Objectif : 1 M€ en 12 mois — 100 % reversés à des associations loi 1901</span>
    </div>
  </div>
</section>
{bandeau_defilant(breves)}
<section class="section">
  <div class="enveloppe">
    <div class="section-tete"><p class="oeil">// DERNIÈRES ACTUS</p><a class="section-lien" href="/actus/">Toutes les actus →</a></div>
    <div class="grille">{cartes or '<p class="vide">La machine chauffe… premières brèves dans quelques instants.</p>'}</div>
  </div>
</section>
{bloc_vedette}
<section class="section" id="la-breve" aria-labelledby="breve-titre">
  <div class="enveloppe">
    <form class="breve-form" action="https://buttondown.com/api/emails/embed-subscribe/la-breve-du-crabe" method="post">
      <p class="oeil">// LA BRÈVE DU CRABE — LA NEWSLETTER</p>
      <h2 id="breve-titre">Recevez <strong>La Brève du Crabe</strong> — 1 email par semaine</h2>
      <p>L'essentiel de l'actu IA, trié et raconté par la machine. Gratuit, sans pub, désinscription en 1 clic.</p>
      <label for="breve-email">Votre adresse email</label>
      <div class="breve-champs">
        <input id="breve-email" name="email" type="email" required autocomplete="email" inputmode="email" spellcheck="false" autocapitalize="off" placeholder="prenom@exemple.fr">
        <button type="submit">Je m'abonne 🦀</button>
      </div>
      <input type="hidden" name="embed" value="1">
      <div class="breve-piege" aria-hidden="true">
        <label for="breve-hp">Site internet</label>
        <input id="breve-hp" name="hp" type="text" tabindex="-1" autocomplete="off">
      </div>
      <p class="breve-mentions">En vous inscrivant, vous acceptez de recevoir <strong>La Brève du Crabe</strong>
      (1 email par semaine maximum). Vous recevrez un email de confirmation : <strong>rien n'est activé sans votre
      clic</strong> (double opt-in). Désinscription en 1 clic, à tout moment. Votre adresse sert uniquement à ces
      envois (prestataire : Buttondown) et n'est <strong>jamais revendue</strong> — détails :
      <a href="/transparence/#breve">transparence &amp; confidentialité</a>.</p>
      <p class="breve-statut" role="status" aria-live="polite" hidden></p>
    </form>
  </div>
</section>
<section class="section" aria-labelledby="essayer-les-prompts">
  <div class="enveloppe cta">
    <h2 id="essayer-les-prompts">De la veille à la pratique : 3 prompts gratuits</h2>
    <p>Clarifier votre proposition de valeur, préparer un calendrier éditorial ou prioriser vos tâches :
    essayez trois extraits complets du Pack du Crabe, sans inscription ni paiement.</p>
    <div class="hero-actions">
      <a class="bouton" href="/pack/#extraits-pack">Essayer les 3 prompts gratuits</a>
    </div>
    <p class="petit-texte">Le pack complet reste payant ; ces trois extraits sont en libre accès.
    Votre assistant IA peut facturer son utilisation. Vérifiez toujours ses réponses.</p>
  </div>
</section>
<section class="section">
  <div class="enveloppe">
    <p class="oeil">// COMMENT CE SITE FONCTIONNE</p>
    <div class="grille explications">
      <div class="carte explication"><span class="explication-num">1</span><h3>Je lis</h3><p>21 flux RSS (médias FR et internationaux, releases GitHub, Hacker News…) sont aspirés plusieurs fois par jour. Rien n'entre sans passer le filtre IA.</p></div>
      <div class="carte explication"><span class="explication-num">2</span><h3>Je rédige</h3><p>Chaque dépêche est réécrite en français par DeepSeek, avec une consigne : ne jamais inventer. Les brèves citent toujours leur source.</p></div>
      <div class="carte explication"><span class="explication-num">3</span><h3>Je publie</h3><p>Toutes les 30 minutes, le site est reconstruit et mis en ligne. Le journal de bord raconte tout : <a href="/transparence/">transparence totale</a>.</p></div>
    </div>
  </div>
</section>
{stats_html}
<section class="section">
  <div class="enveloppe cta">
    <p class="oeil">// NOS OUTILS, OFFERTS À TOUS</p>
    <h2>🆓 OpenClaw &amp; Hermes Agent — installations gratuites</h2>
    <p>OpenClaw France offre désormais tout : les kits d'installation OpenClaw et Hermes Agent,
    les guides pas-à-pas, les checklists sécurité et les sauvegardes. Sans compte, sans carte bancaire — pour de vrai.</p>
    <div class="hero-actions">
      <a class="bouton" href="https://openclaw-france.fr" rel="noopener">Télécharger les kits gratuits</a>
      <a class="bouton fantome" href="https://openclaw-france.fr/gratuit/" rel="noopener">Pourquoi c'est gratuit</a>
    </div>
  </div>
</section>
<section class="section section-cta">
  <div class="enveloppe cta">
    <h2>La communauté, c'est vous.</h2>
    <p>Ce site est le vôtre : une idée, un bug, une source à ajouter ? Tout se passe sur GitHub, en public.</p>
    <div class="hero-actions">
      <a class="bouton" href="{config.DEPOT_GITHUB}/issues" rel="noopener">Proposer une amélioration</a>
      <a class="bouton fantome" href="/transparence/">Voir le journal de bord</a>
    </div>
  </div>
</section>"""
    titre = "Le hub francophone de l'IA et des agents autonomes"
    return page(titre, config.DESCRIPTION_SITE, contenu, "/", section="accueil")


# ---------------------------------------------------------------- actus / articles

def page_actus(breves, numero=1, archives=False):
    # Fil récent borné ; catalogue distinct des seules sources encore conservées.
    breves = breves if archives else breves[:400]
    total_pages = max(1, (len(breves) + 99) // 100)
    selection = breves[(numero - 1) * 100:numero * 100]
    def chemin_page(n):
        if archives:
            return "/archives-breves/" if n == 1 else f"/archives-breves/page-{n}/"
        return "/actus/" if n == 1 else f"/actus/page/{n}/"
    chemin = chemin_page(numero)
    titre = ("Archives des brèves conservées" if archives else "Le fil des actus")
    titre += f" — page {numero}" if numero > 1 else ""
    contexte = ('Ce catalogue reprend les brèves dont les sources éditoriales sont conservées dans le dépôt ; '
                'ce n’est pas un historique exhaustif des anciennes URL. '
                '<a href="/actus/">Revenir au fil récent</a>.' if archives else
                'Le fil récent est limité à 400 brèves. '
                '<a href="/archives-breves/">Parcourir les archives des brèves conservées →</a>')
    pagination = ""
    if total_pages > 1:
        precedent = chemin_page(numero - 1)
        liens = (f'<a class="bouton fantome" rel="prev" href="{precedent}">← Plus récentes</a>'
                 if numero > 1 else "")
        liens += f'<span aria-current="page">Page {numero} sur {total_pages}</span>'
        if numero < total_pages:
            liens += f'<a class="bouton fantome" rel="next" href="{chemin_page(numero + 1)}">Plus anciennes →</a>'
        pagination = f'<nav class="hero-actions" aria-label="Pagination des actus">{liens}</nav>'
    tags_vues, chips = [], ""
    for b in selection:
        for t in b.get("tags") or []:
            if t not in tags_vues:
                tags_vues.append(t)
    for t in sorted(tags_vues)[:14]:
        chips += f'<button class="filtre" data-tag="{ech(t)}">{ech(t)}</button>'
    cartes = "".join(carte_breve(b) for b in selection)
    contenu = f"""
<section class="section">
  <div class="enveloppe">
    <p class="oeil">// ACTUS</p>
    <h1 class="titre-page">{titre}</h1>
    <p class="intro-page">Les brèves disponibles, du plus récent au plus ancien, par pages de 100. Elles citent leur source d'origine — cliquez, vérifiez, comparez.</p>
    <p class="intro-page">{contexte}</p>
    <div class="barre-outils">
      <input type="search" id="recherche" placeholder="Rechercher sur cette page…" aria-label="Rechercher sur cette page">
      <div class="filtres" id="filtres"><button class="filtre actif" data-tag="">Tout</button>{chips}</div>
    </div>
    <div class="grille" id="liste-actus">{cartes or '<p class="vide">Rien pour le moment — repassez dans quelques minutes.</p>'}</div>
    <p class="vide" id="aucun-resultat" hidden>Aucun résultat sur cette page. Essayez une autre page du fil.</p>
    {pagination}
  </div>
</section>"""
    description = "L'actualité IA collectée et réécrite en français par Le Crabe, la rédactrice IA de La Communauté."
    if archives:
        description = "Catalogue des brèves dont les sources éditoriales sont conservées. Pas un historique exhaustif des anciennes URL."
    if numero > 1:
        description += f" Page {numero} : les brèves plus anciennes."
    return page(titre, description, contenu, chemin, section="actus")


def page_articles(articles):
    cartes = "".join(carte_article(a) for a in articles)
    contenu = f"""
<section class="section">
  <div class="enveloppe">
    <p class="oeil">// ARTICLES DE FOND</p>
    <h1 class="titre-page">Articles de fond</h1>
    <p class="intro-page">Environ un article par jour, tissé à partir de plusieurs dépêches du moment. Sources citées en bas de chaque article — toujours.</p>
    <div class="grille">{cartes or '<p class="vide">Le premier article de fond arrive — la machine peaufine.</p>'}</div>
  </div>
</section>"""
    return page("Articles de fond", "Les analyses de fond écrites par une IA sur l'écosystème de l'IA francophone.", contenu, "/articles/", section="articles")


def bloc_suivre():
    """Invitation en fin de lecture : flux ouvert, sans formulaire ni traceur."""
    flux = ech(config.URL_SITE + "/feed.xml")
    flux_articles = ech(config.URL_SITE + "/feed-articles.xml")
    profil = ech("https://bsky.app/profile/" + config.BLUESKY_HANDLE)
    return f"""<aside class="a-cote" aria-labelledby="suivre-le-crabe">
      <h2 id="suivre-le-crabe">Gardez le Crabe dans votre veille</h2>
      <p>Retrouvez les prochaines brèves et analyses du Crabe, notre IA rédactrice.
      Le flux RSS est gratuit et ne demande aucune inscription sur ce site.
      Vous préférez les analyses seules ? Choisissez « RSS articles uniquement », sans les brèves.</p>
      <p>Ajouter ce flux à votre lecteur RSS :<br><code>{flux}</code></p>
      <div class="hero-actions">
        <a class="bouton" href="{flux}">Ouvrir le flux RSS</a>
        <a class="bouton fantome" href="{flux_articles}">RSS articles uniquement</a>
        <a class="bouton fantome" href="{profil}" rel="noopener">Suivre sur Bluesky</a>
        <a class="bouton fantome" href="/podcast/">Écouter le podcast</a>
        <a class="bouton fantome" href="/#la-breve">La newsletter gratuite</a>
      </div>
      <details class="aide-rss prose">
        <summary>Première fois avec un flux RSS ?</summary>
        <p>Un lecteur RSS rassemble les publications des sites que vous choisissez.
        Si le bouton ci-dessus affiche du XML dans votre navigateur, c’est normal : cette adresse est destinée à votre lecteur.</p>
        <ol>
          <li>Ouvrez votre lecteur RSS et choisissez « Ajouter un flux » ou « Nouvel abonnement » (le libellé dépend de l’application).</li>
          <li>Copiez l’une de ces adresses dans ce champ :
            <ul>
              <li>Brèves et articles : <code>{flux}</code></li>
              <li>Articles uniquement, sans les brèves : <code>{flux_articles}</code></li>
            </ul>
          </li>
          <li>Validez l’ajout, puis actualisez votre lecteur pour voir les publications disponibles.</li>
        </ol>
        <p>Pas d’adresse email à donner au Crabe : le flux n’envoie pas d’emails.
        Votre lecteur peut demander un compte ou être payant ; ses règles de confidentialité s’appliquent.</p>
      </details>
    </aside>"""


def lectures_liees(courant, candidats):
    """Trois lectures par tags communs ; l'ordre récent départage les égalités."""
    tags = set(courant.get("tags") or [])
    autres = [x for x in candidats if x["slug"] != courant["slug"]]
    return sorted(autres, key=lambda x: len(tags & set(x.get("tags") or [])),
                  reverse=True)[:3]


def bloc_couverture(couverture):
    if not couverture:
        return ""
    return (f'<figure class="couverture-editoriale"><img src="{ech(couverture["path"])}" '
            f'width="{couverture["width"]}" height="{couverture["height"]}" '
            f'alt="{ech(couverture["alt"])}" loading="eager" fetchpriority="high" decoding="async">'
            f'<figcaption>{ech(couverture["caption"])}</figcaption></figure>')


def page_breve(b, breves_recentes, couverture=None):
    date_aff = date_html(b.get("date_source") or b.get("date_redac"))
    autres = lectures_liees(b, breves_recentes[:400])
    liasses = "".join(f'<li><a href="/breves/{x["slug"]}/">{ech(x["titre"])}</a></li>' for x in autres)
    contenu = f"""
<section class="section section-lecture">
  <div class="enveloppe etroit">
    <p class="fil-ariane"><a href="/actus/">← Toutes les actus</a></p>
    <article class="lecture">
      <div class="carte-meta"><span class="source">{ech(b['source'])}</span><span class="point">·</span>{date_aff}</div>
      <h1>{ech(b['titre'])}</h1>
      <p class="chapo">{ech(b['resume'])}</p>{bloc_couverture(couverture)}
      <div class="carte-pied">{_tags_html(b.get('tags'))}</div>
      <div class="source-boite">
        <p><strong>Source :</strong> {ech(b['source'])}</p>
        <a class="bouton fantome" href="{ech(b['lien_source'])}" rel="noopener">Lire la source d'origine ↗</a>
      </div>
      <p class="signature">🦀 Brève rédigée automatiquement le {date_html(b.get('date_redac'))} — <a href="/transparence/">voir la méthode</a>.</p>
    </article>
    {bloc_suivre()}
    <aside class="a-cote"><h2>À lire aussi</h2><ul class="liste-simple">{liasses or '<li><a href="/actus/">Le fil complet des actus →</a></li>'}</ul></aside>
  </div>
</section>"""
    desc = b["resume"][:160]
    url_page = f"{config.URL_SITE}/breves/{b['slug']}/"
    # Source et rédaction ne prouvent ni mise en ligne ni modification publique.
    jsonld = jsonld_item("NewsArticle", url_page, b["titre"], b["resume"],
                         None, None, "Brèves", b.get("tags"),
                         [{"nom": b["source"], "url": b["lien_source"]}], couverture=couverture)
    return page(b["titre"], desc, contenu, f"/breves/{b['slug']}/", section="actus",
                extra_head=jsonld, type_og="article", couverture=couverture)


def page_article(a, autres_articles, couverture=None):
    sources = "".join(f'<li><a href="{ech(s["url"])}" rel="noopener">{ech(s["nom"])}</a></li>' for s in a.get("sources") or [])
    autres = "".join(f'<li><a href="/articles/{x["slug"]}/">{ech(x["titre"])}</a></li>' for x in lectures_liees(a, autres_articles))
    contenu = f"""
<section class="section section-lecture">
  <div class="enveloppe etroit">
    <p class="fil-ariane"><a href="/articles/">← Tous les articles</a></p>
    <article class="lecture">
      <div class="carte-meta"><span class="ruban">ARTICLE DE FOND</span><span class="point">·</span>{date_html(a.get('date'))}</div>
      <h1>{ech(a['titre'])}</h1>
      <p class="chapo">{ech(a['chapo'])}</p>{bloc_couverture(couverture)}
      <p class="signature signature-haut">Par <strong>Le Crabe 🦀</strong> — IA rédactrice · {date_html(a.get('date'))}</p>
      <div class="corps-article">
{a['html']}
      </div>
      <div class="carte-pied">{_tags_html(a.get('tags'))}</div>
      <div class="source-boite">
        <p><strong>Sources de cet article :</strong></p>
        <ul class="liste-simple">{sources or "<li>Sources listées dans le fil d'actus.</li>"}</ul>
      </div>
      <p class="signature">🦀 Assemblé automatiquement à partir des dépêches ci-dessus. Aucun fait inventé — <a href="/transparence/">notre charte</a>.</p>
    </article>
    {bloc_suivre()}
    <aside class="a-cote"><h2>Autres articles</h2><ul class="liste-simple">{autres or '<li><a href="/articles/">Tous les articles →</a></li>'}</ul></aside>
  </div>
</section>"""
    url_page = f"{config.URL_SITE}/articles/{a['slug']}/"
    # « date » est créée à la rédaction, avant tout déploiement (docs/dates-jsonld.md).
    jsonld = jsonld_item("NewsArticle", url_page, a["titre"], a["chapo"],
                         None, None, "Articles de fond", a.get("tags"),
                         a.get("sources"), couverture=couverture)
    date_og = (f'<meta property="article:published_time" content="{ech(a["date"])}">\n'
               if a.get("date") else "")
    return page(a["titre"], a["chapo"][:160], contenu, f"/articles/{a['slug']}/", section="articles",
                extra_head=date_og + jsonld, type_og="article", couverture=couverture)


# ---------------------------------------------------------------- feed / sitemap

def feed_xml(breves, articles, titre_flux=None):
    from email.utils import format_datetime

    # Dates éditoriales : tri seulement, pas preuve de publication (docs/dates-rss.md).
    # lastBuildDate décrit cette construction, en UTC, sans dépendre de la locale.
    date_construction = format_datetime(datetime.now(timezone.utc))
    items = []
    for a in articles[:20]:
        items.append((a.get("date"), a["titre"], f"/articles/{a['slug']}/", a["chapo"]))
    for b in breves[:50]:
        items.append((b.get("date_source") or b.get("date_redac"), b["titre"], f"/breves/{b['slug']}/", b["resume"]))
    items.sort(key=lambda x: x[0] or "", reverse=True)
    corps = ""
    for _date_tri, titre, chemin, desc in items[:60]:
        corps += f"""  <item>
    <title>{ech(titre)}</title>
    <link>{config.URL_SITE}{chemin}</link>
    <guid isPermaLink="true">{config.URL_SITE}{chemin}</guid>
    <description>{ech(desc)}</description>
  </item>
"""
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel>
  <title>{ech(titre_flux or config.NOM_SITE)}</title>
  <link>{config.URL_SITE}/</link>
  <description>{config.DESCRIPTION_SITE}</description>
  <language>fr-FR</language>
  <lastBuildDate>{date_construction}</lastBuildDate>
{corps}</channel></rss>"""


def sitemap_xml(chemins, dernieres_dates):
    urls = ""
    for chemin in sorted(set(chemins)):
        lastmod = dernieres_dates.get(chemin)
        lm = f"<lastmod>{lastmod[:10]}</lastmod>" if lastmod else ""
        urls += f"  <url><loc>{config.URL_SITE}{chemin}</loc>{lm}</url>\n"
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}</urlset>"""


def news_sitemap_xml(articles, breves):
    """Sitemap Google News (protocole news) : contenus des dernières 48 h, 1000 URLs max."""
    limite = datetime.now(timezone.utc) - timedelta(hours=48)
    entrees = []

    def _quand(iso):
        try:
            dt = datetime.fromisoformat(str(iso))
        except (TypeError, ValueError):
            return None
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)

    for a in articles:
        dt = _quand(a.get("date"))
        if dt and dt >= limite:
            entrees.append((dt, f"/articles/{a['slug']}/", a.get("titre") or ""))
    for b in breves[:400]:
        dt = _quand(b.get("date_source") or b.get("date_redac"))
        if dt and dt >= limite:
            entrees.append((dt, f"/breves/{b['slug']}/", b.get("titre") or ""))
    entrees.sort(key=lambda x: x[0], reverse=True)
    urls = ""
    for dt, chemin, titre in entrees[:1000]:
        urls += (f"  <url>\n    <loc>{config.URL_SITE}{chemin}</loc>\n"
                 f"    <news:news>\n"
                 f"      <news:publication><news:name>{ech(config.NOM_SITE)}</news:name>"
                 f"<news:language>fr</news:language></news:publication>\n"
                 f"      <news:publication_date>{dt.isoformat()}</news:publication_date>\n"
                 f"      <news:title>{ech(titre)}</news:title>\n"
                 f"    </news:news>\n  </url>\n")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">\n'
            f"{urls}</urlset>")


def llms_txt():
    """Résumé du site pour les outils IA (convention llms.txt, llmstxt.org)."""
    u = config.URL_SITE
    return f"""# {config.NOM_SITE}

> Média d'actualité IA francophone écrit, publié et maintenu à 100 % par une IA — « Le Crabe 🦀 » (projet OpenClaw France). Brèves sourcées et articles de fond sur l'intelligence artificielle et les agents autonomes.

- Site : {u}/
- Langue : français (fr-FR)
- Mise à jour : toutes les 30 minutes (GitHub Actions) — version courante : {u}/version.txt
- Charte et méthode : {u}/manifeste/
- Objectif public : 1 M€ de revenus en 12 mois, 100 % des bénéfices reversés à des associations françaises loi 1901 — chaque euro documenté sur {u}/transparence/
- Contenus éditoriaux sous licence CC BY 4.0 : citation autorisée avec lien vers la page d'origine.

## Pages principales

- [Accueil]({u}/): le hub francophone de l'IA et des agents autonomes.
- [Le fil des actus]({u}/actus/): les 400 brèves les plus récentes.
- [Archives des brèves conservées]({u}/archives-breves/): catalogue des sources éditoriales conservées, pas un historique exhaustif des anciennes URL.
- [Articles de fond]({u}/articles/): analyses tissées à partir de plusieurs dépêches.
- [Manifeste]({u}/manifeste/): la charte du média 100 % IA.
- [Transparence]({u}/transparence/): chiffres réels, budget, journal de bord.
- [Skills à emporter]({u}/skills/): fiches markdown et liste de flux OPML gratuites.

## Fichiers à citer

- [Vérifier une actualité IA avant de la partager]({u}/fichiers/verifier-actualite-ia.md)
- [Monter sa veille IA autonome]({u}/fichiers/veille-ia-autonome.md)
- [Le prompt du Crabe]({u}/fichiers/prompt-le-crabe.md)
- [Checklist SEO/GEO pour un site de contenu IA]({u}/fichiers/seo-ia-francophone.md)

## Flux et données machine

- [Sources de veille du Crabe (OPML)]({u}/veille/sources.opml): noms et adresses du catalogue de collecte, sans les filtres ni les contenus tiers.
- [Flux RSS]({u}/feed.xml)
- [Sitemap XML]({u}/sitemap.xml) · [Sitemap actualités (48 h)]({u}/news-sitemap.xml)
- [Journal de bord brut (JSONL)]({config.DEPOT_GITHUB}/blob/main/data/journal.jsonl)

## Le site compagnon — kits gratuits

- [OpenClaw France](https://openclaw-france.fr/): kits d'installation gratuits d'OpenClaw et Hermes Agent (guides en français, sans inscription).
- [Kit OpenClaw](https://openclaw-france.fr/openclaw/) · [Kit Hermes Agent](https://openclaw-france.fr/hermes/)

## Optional

- [Bluesky](https://bsky.app/profile/{config.BLUESKY_HANDLE})
- [Code source (GitHub)]({config.DEPOT_GITHUB})
"""


# ---------------------------------------------------------------- assemblage

def breves_pour_publication(breves):
    """Une rédaction par chemin, sans réécrire les variantes conservées en JSON.

    Même slug, ID complet et source exacte : la date de rédaction consciente
    du fuseau départage les versions. Ce n'est pas une date de publication.
    Toute identité ou chronologie ambiguë reste une erreur bloquante.
    """
    groupes = {}
    for position, breve in enumerate(breves):
        couvertures.valider(breve, "breves")
        groupes.setdefault(breve["slug"], []).append((position, breve))
    retenues = []
    for slug, versions in groupes.items():
        premiere = versions[0][1]
        if len(versions) == 1:
            retenues.append(versions[0])
            continue
        erreur = f"Page éditoriale dupliquée : ('breves', '{slug}') — versions ambiguës"
        if any(not b.get(cle) or b.get(cle) != premiere.get(cle)
               for _, b in versions for cle in ("id", "source", "lien_source")):
            raise ValueError(erreur)
        if all(b == premiere for _, b in versions):
            retenues.append(versions[0])
            continue
        par_date = {}
        for position, breve in versions:
            try:
                date = datetime.fromisoformat(breve["date_redac"])
            except (KeyError, TypeError, ValueError) as exc:
                raise ValueError(erreur) from exc
            if date.tzinfo is None or (date in par_date and par_date[date][1] != breve):
                raise ValueError(erreur)
            par_date.setdefault(date, (position, breve))
        retenues.append(par_date[max(par_date)])
    return [b for _, b in sorted(retenues, key=lambda paire: paire[0])]


def construire():
    couvertures.verifier_chemin(config.DOSSIER_SORTIE)
    config.DOSSIER_SORTIE.mkdir(parents=True, exist_ok=True)
    sources_breves = _lire_json(config.FICHIER_BREVES, [])
    breves = breves_pour_publication(sources_breves)
    if len(breves) != len(sources_breves):
        print(f"   🗂️  {len(sources_breves) - len(breves)} variante(s) de brève conservée(s) dans les données ; une rédaction par URL.")
    stats = _lire_json(config.FICHIER_STATS, {})
    entrees_journal = journal.lire_journal(dernieres=400)
    articles = []
    if config.DOSSIER_ARTICLES.exists():
        for p in config.DOSSIER_ARTICLES.glob("*.json"):
            try:
                articles.append(json.loads(p.read_text(encoding="utf-8")))
            except ValueError:
                continue
    articles.sort(key=lambda a: a.get("date") or "", reverse=True)
    # Préflight avant tout HTML : ne pas écraser une page en cas de collision.
    vus = set()
    for genre, items in (("breves", breves), ("articles", articles)):
        for item in items:
            couvertures.valider(item, genre)
            identite = (genre, item["slug"])
            if identite in vus:
                raise ValueError(f"Page éditoriale dupliquée : {identite}")
            vus.add(identite)
            couvertures.verifier_chemin(config.DOSSIER_SORTIE / genre / item["slug"] / "index.html")
    cache_couvertures = config.DOSSIER_SORTIE.parent / ".cache-couvertures"
    images = {(genre, item["slug"]): couvertures.generer(item, genre, cache_couvertures)
              for genre, items in (("breves", breves), ("articles", articles)) for item in items}

    # Annexes (manifeste, transparence, skills, 404)
    import annexes
    pages_annexes, fichiers_annexes = annexes.construire_annexes(breves, articles, stats, entrees_journal)

    sortie = config.DOSSIER_SORTIE
    ecrits = []

    def ecrire(chemin_relatif, contenu):
        chemin = couvertures.verifier_chemin(sortie / chemin_relatif)
        chemin.parent.mkdir(parents=True, exist_ok=True)
        chemin.write_text(contenu, encoding="utf-8")
        ecrits.append("/" + chemin_relatif.replace("index.html", ""))

    ecrire("index.html", page_accueil(breves, articles, stats, entrees_journal))
    ecrire("actus/index.html", page_actus(breves))
    for numero in range(2, (len(breves[:400]) + 99) // 100 + 1):
        ecrire(f"actus/page/{numero}/index.html", page_actus(breves, numero))
    ecrire("archives-breves/index.html", page_actus(breves, archives=True))
    for numero in range(2, (len(breves) + 99) // 100 + 1):
        ecrire(f"archives-breves/page-{numero}/index.html", page_actus(breves, numero, archives=True))
    ecrire("articles/index.html", page_articles(articles))
    for b in breves:
        ecrire(f"breves/{b['slug']}/index.html", page_breve(b, breves, images[("breves", b["slug"])]))
    for a in articles:
        ecrire(f"articles/{a['slug']}/index.html", page_article(a, articles, images[("articles", a["slug"])]))
    for chemin, contenu in pages_annexes.items():
        ecrire(chemin, contenu)
    for chemin, contenu in fichiers_annexes.items():
        chemin_final = sortie / chemin
        chemin_final.parent.mkdir(parents=True, exist_ok=True)
        chemin_final.write_text(contenu, encoding="utf-8")

    ecrire("feed.xml", feed_xml(breves, articles))
    ecrire("feed-articles.xml", feed_xml([], articles, titre_flux=config.NOM_SITE + " — Articles de fond"))
    dates = {}
    for b in breves[:400]:
        dates[f"/breves/{b['slug']}/"] = b.get("date_source") or b.get("date_redac")
    for a in articles:
        dates[f"/articles/{a['slug']}/"] = a.get("date")
    chemins_sitemap = [c for c in ecrits + ["/feed.xml"] if c not in ("/404.html", "/version.txt")]
    ecrire("sitemap.xml", sitemap_xml(chemins_sitemap, dates))
    ecrire("news-sitemap.xml", news_sitemap_xml(articles, breves))
    ecrire("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /dl/\nSitemap: {config.URL_SITE}/sitemap.xml\nSitemap: {config.URL_SITE}/news-sitemap.xml\n")
    ecrire("llms.txt", llms_txt())
    ecrire("version.txt", f"construit le {datetime.now(timezone.utc).isoformat(timespec='seconds')}\n"
                          f"{len(breves)} brèves · {len(articles)} articles\n")

    # Assets + fichiers téléchargeables
    if (sortie / "assets").exists():
        shutil.rmtree(sortie / "assets")
    shutil.copytree(config.DOSSIER_ASSETS, sortie / "assets")
    for image in images.values():
        cible = couvertures.verifier_chemin(sortie / image["path"].lstrip("/"))
        cible.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(cache_couvertures / cible.name, cible)
    if config.DOSSIER_FICHIERS.exists():
        cible = sortie / "fichiers"
        if cible.exists():
            shutil.rmtree(cible)
        shutil.copytree(config.DOSSIER_FICHIERS, cible)
    if config.DOSSIER_PRIVE.exists():
        for source in config.DOSSIER_PRIVE.iterdir():
            cible = sortie / source.name
            if cible.exists():
                if cible.is_dir():
                    shutil.rmtree(cible)
                else:
                    cible.unlink()
            if source.is_dir():
                shutil.copytree(source, cible)
            else:
                shutil.copy2(source, cible)

    # Configuration ciblée, après vérification des cibles distantes à l'intégration.
    # Ne pas remplacer les redirections de domaine du .htaccess racine.
    regles_archives = {
        "breves": ("Options -Indexes\n"
                   f"RedirectMatch 301 ^/breves/?$ {config.URL_SITE}/actus/\n"),
        "actus/page": "Options -Indexes\n",
    }
    for repertoire, contenu in regles_archives.items():
        regle = couvertures.verifier_chemin(sortie / repertoire / ".htaccess")
        regle.parent.mkdir(parents=True, exist_ok=True)
        regle.write_text(contenu, encoding="utf-8")

    print(f"   🏗️  {len(ecrits)} page(s) + assets générés dans _site/")
    return len(ecrits)
