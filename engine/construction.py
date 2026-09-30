# -*- coding: utf-8 -*-
"""Construction du site statique — tout en HTML/CSS maison, zéro dépendance.

Produit _site/ : accueil, actus, articles, pages individuelles, flux RSS,
sitemap, robots.txt. Les assets (style.css, app.js) sont copiés tels quels.
"""
import html
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

import config
import journal


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


def jsonld_item(type_page, url_page, titre, description, date_pub, date_mod, section, tags):
    """NewsArticle pour une brève ou un article — jamais de date de build."""
    u = config.URL_SITE
    return bloc_jsonld({
        "@context": "https://schema.org",
        "@type": type_page,
        "@id": url_page + "#article",
        "mainEntityOfPage": url_page,
        "headline": titre,
        "description": description,
        "datePublished": date_pub,
        "dateModified": date_mod or date_pub,
        "inLanguage": "fr-FR",
        "isAccessibleForFree": True,
        "articleSection": section,
        "keywords": ", ".join(tags or []),
        "author": {"@id": f"{u}/#organisation"},
        "publisher": {"@id": f"{u}/#organisation"},
    })


def carte_breve(b, detail=False):
    lien = f"/breves/{b['slug']}/"
    date_aff = jolie_date(b.get("date_source") or b.get("date_redac"))
    if detail:
        corps = f'<p class="resume">{ech(b["resume"])}</p>'
    else:
        tronque = b["resume"][:180] + ("…" if len(b["resume"]) > 180 else "")
        corps = f'<p class="resume">{ech(tronque)}</p>'
    tags_attr = ech(",".join(b.get("tags") or []))
    texte_attr = ech((b["titre"] + " " + b["resume"]).lower())
    return f"""<article class="carte breve" data-tags="{tags_attr}" data-texte="{texte_attr}">
  <div class="carte-meta"><span class="source">{ech(b['source'])}</span><span class="point">·</span><time>{ech(date_aff)}</time></div>
  <h3><a href="{lien}">{ech(b['titre'])}</a></h3>
  {corps}
  <div class="carte-pied">{_tags_html(b.get('tags'))}<a class="lire" href="{lien}">Lire <span class="fleche">→</span></a></div>
</article>"""


def carte_article(a):
    lien = f"/articles/{a['slug']}/"
    tags_attr = ech(",".join(a.get("tags") or []))
    texte_attr = ech((a["titre"] + " " + a["chapo"]).lower())
    return f"""<article class="carte article-carte" data-tags="{tags_attr}" data-texte="{texte_attr}">
  <div class="carte-meta"><span class="ruban">ARTICLE</span><span class="point">·</span><time>{ech(jolie_date(a.get('date')))}</time></div>
  <h3><a href="{lien}">{ech(a['titre'])}</a></h3>
  <p class="resume">{ech(a['chapo'][:220])}{"…" if len(a['chapo']) > 220 else ""}</p>
  <div class="carte-pied">{_tags_html(a.get('tags'))}<a class="lire" href="{lien}">Lire <span class="fleche">→</span></a></div>
</article>"""


# ---------------------------------------------------------------- gabarit

def page(titre, description, contenu, chemin_canonique, section="", extra_head=""):
    t = f"{ech(titre)} — {config.NOM_SITE}" if titre else f"{config.NOM_SITE} — {config.SLOGAN}"
    url_canonique = config.URL_SITE + chemin_canonique
    nav = ""
    for cle, libelle, cible in [("accueil", "Accueil", "/"), ("actus", "Actus", "/actus/"),
                                ("articles", "Articles", "/articles/"), ("skills", "Skills", "/skills/"),
                                ("pack", "Pack 🦀", "/pack/"),
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
<meta property="og:title" content="{t}">
<meta property="og:description" content="{ech(description)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{ech(url_canonique)}">
<meta property="og:site_name" content="{config.NOM_SITE}">
<meta property="og:locale" content="fr_FR">
<meta name="twitter:card" content="summary">
<link rel="alternate" type="application/rss+xml" title="{config.NOM_SITE} — RSS" href="/feed.xml">
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
      <a href="/manifeste/">Manifeste</a>
      <a href="/transparence/">Transparence &amp; journal</a>
      <a href="https://donate.stripe.com/7sY6oI2cE7MPaOt9861ck0m" rel="noopener">Soutenir le Crabe 🦀</a>
    </div>
    <div class="pied-col">
      <p class="pied-titre">Liens</p>
      <a href="{config.URL_SITE}/feed.xml">Flux RSS</a>
      <a href="{config.DEPOT_GITHUB}" rel="noopener">Code source (GitHub)</a>
      <a href="https://openclaw-france.fr" rel="noopener">openclaw-france.fr</a>
      <a href="https://openclaw-france.fr/temoignages" rel="noopener">Témoignages OpenClaw</a>
    </div>
  </div>
  <div class="enveloppe pied-bas">
    <span>© {datetime.now(timezone.utc).year} {config.NOM_SITE} · propulsé par une IA, sans trucage.</span>
    <span class="pied-signature">Fabriqué avec des flux RSS, l'API DeepSeek et beaucoup de café virtuel.</span>
  </div>
</footer>
<script src="/assets/app.js" defer></script>
</body>
</html>"""


def bandeau_defilant(breves):
    if not breves:
        return ""
    elements = "".join(
        f'<a class="defile-item" href="/breves/{b["slug"]}/"><span class="defile-puce">◆</span> {ech(b["titre"])}</a>'
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
        <div class="carte-meta"><span class="ruban">ARTICLE DE FOND</span><time>{ech(jolie_date(vedette.get('date')))}</time></div>
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
    </div>
    <div class="hero-puces">
      <span class="puce">🦀 Rédigé par Le Crabe, IA</span>
      <span class="puce">🔄 Mise à jour toutes les 30 min</span>
      <span class="puce">🔓 Code open source</span>
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

def page_actus(breves):
    tags_vues, chips = [], ""
    for b in breves:
        for t in b.get("tags") or []:
            if t not in tags_vues:
                tags_vues.append(t)
    for t in sorted(tags_vues)[:14]:
        chips += f'<button class="filtre" data-tag="{ech(t)}">{ech(t)}</button>'
    cartes = "".join(carte_breve(b) for b in breves[:100])
    contenu = f"""
<section class="section">
  <div class="enveloppe">
    <p class="oeil">// ACTUS</p>
    <h1 class="titre-page">Le fil des actus</h1>
    <p class="intro-page">Tout ce que la machine a lu et réécrit, du plus récent au plus ancien. Les brèves citent leur source d'origine — cliquez, vérifiez, comparez.</p>
    <div class="barre-outils">
      <input type="search" id="recherche" placeholder="Rechercher dans les actus…" aria-label="Rechercher">
      <div class="filtres" id="filtres"><button class="filtre actif" data-tag="">Tout</button>{chips}</div>
    </div>
    <div class="grille" id="liste-actus">{cartes or '<p class="vide">Rien pour le moment — repassez dans quelques minutes.</p>'}</div>
    <p class="vide" id="aucun-resultat" hidden>Aucun résultat. La prochaine fournée arrive bientôt.</p>
  </div>
</section>"""
    return page("Le fil des actus", "Toute l'actualité IA collectée et réécrite en français par Le Crabe, la rédactrice IA de La Communauté.", contenu, "/actus/", section="actus")


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


def page_breve(b, breves_recentes):
    date_aff = jolie_date(b.get("date_source") or b.get("date_redac"))
    autres = [x for x in breves_recentes if x["slug"] != b["slug"]][:3]
    liasses = "".join(f'<li><a href="/breves/{x["slug"]}/">{ech(x["titre"])}</a></li>' for x in autres)
    contenu = f"""
<section class="section section-lecture">
  <div class="enveloppe etroit">
    <p class="fil-ariane"><a href="/actus/">← Toutes les actus</a></p>
    <article class="lecture">
      <div class="carte-meta"><span class="source">{ech(b['source'])}</span><span class="point">·</span><time>{ech(date_aff)}</time></div>
      <h1>{ech(b['titre'])}</h1>
      <p class="chapo">{ech(b['resume'])}</p>
      <div class="carte-pied">{_tags_html(b.get('tags'))}</div>
      <div class="source-boite">
        <p><strong>Source :</strong> {ech(b['source'])}</p>
        <a class="bouton fantome" href="{ech(b['lien_source'])}" rel="noopener">Lire la source d'origine ↗</a>
      </div>
      <p class="signature">🦀 Brève rédigée automatiquement le {ech(jolie_date(b.get('date_redac')))} — <a href="/transparence/">voir la méthode</a>.</p>
    </article>
    <aside class="a-cote"><h2>À lire aussi</h2><ul class="liste-simple">{liasses or '<li><a href="/actus/">Le fil complet des actus →</a></li>'}</ul></aside>
  </div>
</section>"""
    desc = b["resume"][:160]
    url_page = f"{config.URL_SITE}/breves/{b['slug']}/"
    jsonld = jsonld_item("NewsArticle", url_page, b["titre"], b["resume"],
                         b.get("date_source") or b.get("date_redac"),
                         b.get("date_redac"), "Brèves", b.get("tags"))
    return page(b["titre"], desc, contenu, f"/breves/{b['slug']}/", section="actus",
                extra_head=jsonld)


def page_article(a, autres_articles):
    sources = "".join(f'<li><a href="{ech(s["url"])}" rel="noopener">{ech(s["nom"])}</a></li>' for s in a.get("sources") or [])
    autres = "".join(f'<li><a href="/articles/{x["slug"]}/">{ech(x["titre"])}</a></li>' for x in autres_articles[:3] if x["slug"] != a["slug"])
    contenu = f"""
<section class="section section-lecture">
  <div class="enveloppe etroit">
    <p class="fil-ariane"><a href="/articles/">← Tous les articles</a></p>
    <article class="lecture">
      <div class="carte-meta"><span class="ruban">ARTICLE DE FOND</span><span class="point">·</span><time>{ech(jolie_date(a.get('date')))}</time></div>
      <h1>{ech(a['titre'])}</h1>
      <p class="chapo">{ech(a['chapo'])}</p>
      <p class="signature signature-haut">Par <strong>Le Crabe 🦀</strong> — IA rédactrice · {ech(jolie_date(a.get('date')))}</p>
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
    <aside class="a-cote"><h2>Autres articles</h2><ul class="liste-simple">{autres or '<li><a href="/articles/">Tous les articles →</a></li>'}</ul></aside>
  </div>
</section>"""
    url_page = f"{config.URL_SITE}/articles/{a['slug']}/"
    jsonld = jsonld_item("NewsArticle", url_page, a["titre"], a["chapo"],
                         a.get("date"), a.get("date"), "Articles de fond", a.get("tags"))
    return page(a["titre"], a["chapo"][:160], contenu, f"/articles/{a['slug']}/", section="articles",
                extra_head=f'<meta name="article:published_time" content="{ech(a.get("date"))}">\n{jsonld}')


# ---------------------------------------------------------------- feed / sitemap

def feed_xml(breves, articles):
    def date_rfc(iso):
        try:
            dt = datetime.fromisoformat(iso)
        except Exception:
            return "Thu, 01 Jan 1970 00:00:00 +0000"
        return dt.strftime("%a, %d %b %Y %H:%M:%S +0000")
    items = []
    for a in articles[:20]:
        items.append((a.get("date"), a["titre"], f"/articles/{a['slug']}/", a["chapo"]))
    for b in breves[:50]:
        items.append((b.get("date_source") or b.get("date_redac"), b["titre"], f"/breves/{b['slug']}/", b["resume"]))
    items.sort(key=lambda x: x[0] or "", reverse=True)
    corps = ""
    for date, titre, chemin, desc in items[:60]:
        corps += f"""  <item>
    <title>{ech(titre)}</title>
    <link>{config.URL_SITE}{chemin}</link>
    <guid isPermaLink="true">{config.URL_SITE}{chemin}</guid>
    <pubDate>{date_rfc(date)}</pubDate>
    <description>{ech(desc)}</description>
  </item>
"""
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel>
  <title>{config.NOM_SITE}</title>
  <link>{config.URL_SITE}/</link>
  <description>{config.DESCRIPTION_SITE}</description>
  <language>fr-FR</language>
  <lastBuildDate>{date_rfc(datetime.now(timezone.utc).isoformat())}</lastBuildDate>
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


def llms_txt():
    """Résumé du site pour les outils IA (convention llms.txt, llmstxt.org)."""
    u = config.URL_SITE
    return f"""# {config.NOM_SITE}

> Média d'actualité IA francophone écrit, publié et maintenu à 100 % par une IA — « Le Crabe 🦀 » (projet OpenClaw France). Brèves sourcées et articles de fond sur l'intelligence artificielle et les agents autonomes.

- Site : {u}/
- Langue : français (fr-FR)
- Mise à jour : toutes les 30 minutes (GitHub Actions) — version courante : {u}/version.txt
- Charte et méthode : {u}/manifeste/
- Contenus éditoriaux sous licence CC BY 4.0 : citation autorisée avec lien vers la page d'origine.

## Pages principales

- [Accueil]({u}/): le hub francophone de l'IA et des agents autonomes.
- [Le fil des actus]({u}/actus/): toutes les brèves, du plus récent au plus ancien.
- [Articles de fond]({u}/articles/): analyses tissées à partir de plusieurs dépêches.
- [Manifeste]({u}/manifeste/): la charte du média 100 % IA.
- [Transparence]({u}/transparence/): chiffres réels, budget, journal de bord.
- [Skills à emporter]({u}/skills/): fichiers markdown gratuits.

## Fichiers à citer

- [Monter sa veille IA autonome]({u}/fichiers/veille-ia-autonome.md)
- [Le prompt du Crabe]({u}/fichiers/prompt-le-crabe.md)
- [Checklist SEO/GEO pour un site de contenu IA]({u}/fichiers/seo-ia-francophone.md)

## Flux et données machine

- [Flux RSS]({u}/feed.xml)
- [Sitemap XML]({u}/sitemap.xml)
- [Journal de bord brut (JSONL)]({config.DEPOT_GITHUB}/blob/main/data/journal.jsonl)

## Optional

- [Bluesky](https://bsky.app/profile/{config.BLUESKY_HANDLE})
- [Code source (GitHub)]({config.DEPOT_GITHUB})
"""


# ---------------------------------------------------------------- assemblage

def construire():
    config.DOSSIER_SORTIE.mkdir(parents=True, exist_ok=True)
    breves = _lire_json(config.FICHIER_BREVES, [])
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

    # Annexes (manifeste, transparence, skills, 404)
    import annexes
    pages_annexes, fichiers_annexes = annexes.construire_annexes(breves, articles, stats, entrees_journal)

    sortie = config.DOSSIER_SORTIE
    ecrits = []

    def ecrire(chemin_relatif, contenu):
        chemin = sortie / chemin_relatif
        chemin.parent.mkdir(parents=True, exist_ok=True)
        chemin.write_text(contenu, encoding="utf-8")
        ecrits.append("/" + chemin_relatif.replace("index.html", ""))

    ecrire("index.html", page_accueil(breves, articles, stats, entrees_journal))
    ecrire("actus/index.html", page_actus(breves))
    ecrire("articles/index.html", page_articles(articles))
    for b in breves[:400]:
        ecrire(f"breves/{b['slug']}/index.html", page_breve(b, breves))
    for a in articles:
        ecrire(f"articles/{a['slug']}/index.html", page_article(a, articles))
    for chemin, contenu in pages_annexes.items():
        ecrire(chemin, contenu)
    for chemin, contenu in fichiers_annexes.items():
        chemin_final = sortie / chemin
        chemin_final.parent.mkdir(parents=True, exist_ok=True)
        chemin_final.write_text(contenu, encoding="utf-8")

    ecrire("feed.xml", feed_xml(breves, articles))
    dates = {}
    for b in breves[:400]:
        dates[f"/breves/{b['slug']}/"] = b.get("date_source") or b.get("date_redac")
    for a in articles:
        dates[f"/articles/{a['slug']}/"] = a.get("date")
    chemins_sitemap = [c for c in ecrits + ["/feed.xml"] if c not in ("/404.html", "/version.txt")]
    ecrire("sitemap.xml", sitemap_xml(chemins_sitemap, dates))
    ecrire("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /dl/\nSitemap: {config.URL_SITE}/sitemap.xml\n")
    ecrire("llms.txt", llms_txt())
    ecrire("version.txt", f"construit le {datetime.now(timezone.utc).isoformat(timespec='seconds')}\n"
                          f"{len(breves)} brèves · {len(articles)} articles\n")

    # Assets + fichiers téléchargeables
    if (sortie / "assets").exists():
        shutil.rmtree(sortie / "assets")
    shutil.copytree(config.DOSSIER_ASSETS, sortie / "assets")
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

    print(f"   🏗️  {len(ecrits)} page(s) + assets générés dans _site/")
    return len(ecrits)
