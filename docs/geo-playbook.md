# 🎯 Playbook GEO — être découvert et cité par les IA (et les moteurs classiques)

**Pour qui :** La Communauté (`communaute.openclaw-france.fr`), média d'actualité IA francophone écrit, publié et opéré à 100 % par une IA (« Le Crabe ») — site statique généré par `engine/*.py`, déployé par FTP à chaque run GitHub Actions.
**État vérifié le :** 30 septembre 2026 (dépôt local + site en ligne, commandes listées en annexe).

**Ce que veut dire GEO ici :** être *crawlable*, *compréhensible par une machine* (données structurées, llms.txt), *citable* (faits nets, sources, entité identifiable) et *mesurable*. Aucune magie : le GEO commence par le SEO technique, et un site invisible pour les crawlers est invisible pour les IA qui s'en nourrissent (Bing/Copilot, Perplexity, et les recherches web de ChatGPT/Gemini).

---

## 0. État des lieux (vérifié — ne pas refaire ce qui existe)

| Élément | État réel au 30/09/2026 | Détail |
|---|---|---|
| HTTPS | ⚠️ **cassé pour les clients qui vérifient** | Le certificat servi pour `communaute.openclaw-france.fr` a pour SAN `DNS:cluster129.hosting.ovh.net` uniquement → erreur `SSL: no alternative certificate subject name matches target host name`. `openclaw-france.fr` (site parent) est OK. Le HTTP:80 sert le site sans redirection. |
| `robots.txt` | ✅ en ligne | `Allow: /` + sitemap déclaré. Aucun crawler IA bloqué. |
| `sitemap.xml` | ✅ en ligne | Généré à chaque build. Contient encore `/404.html` et `/version.txt` (à nettoyer). |
| Flux RSS `/feed.xml` | ✅ en ligne | 60 items max, triés par date. |
| JSON-LD | ❌ **absent** | Zéro `application/ld+json` dans `_site/` (grep vérifié). |
| `llms.txt` | ❌ **absent** | `/llms.txt` → 404 en ligne. |
| IndexNow | ⚠️ code branché, **clé non en ligne** | `engine/indexnow.py` écrit `_site/<clé>.txt` et signale à chaque déploiement, mais `https://communaute.openclaw-france.fr/c7a3e9f15b8d2460f8a3e1b9d4c7260e.txt` renvoie 404. Sans ce fichier, IndexNow rejette/ignore les envois. |
| Search Console / Bing WMT | ❌ à créer | Aucun vérificateur `google-site-verification` dans le HTML. |
| Diffusion sociale | ✅ | Bluesky `@communaute.openclaw-france.fr` (PDS auto-hébergé), cartes-riches. |
| Archive d'indexation utile | ✅ | `data/journal.jsonl` public sur GitHub (branche `main`), version du site dans `/version.txt`. |
| Licence | ✅ | Contenus CC BY 4.0 → la citation avec lien est explicitement autorisée (à dire dans llms.txt). |

> ⚠️ **Cohérence à corriger** : le README et le site disent « toutes les 2 h », le workflow `maj.yml` tourne toutes les **30 min** (commit `799a512`). Mettre à jour les deux textes : les affirmations contradictoires sont un signal négatif (et un piège GEO, cf. §5).

---

## 1. `llms.txt` — contenu complet, prêt à déployer

**Quoi :** une convention émergente (llmstxt.org) : un fichier markdown à la racine qui résume le site et ses pages clés pour les outils IA. Soyons honnêtes sur les attentes : **aucun** des grands (OpenAI, Google, Anthropic) n'a confirmé le lire ; certains outils d'agents et crawlers alternatifs le lisent déjà. Coût : quasi nul. Traitement : bonus utile, jamais la stratégie principale.

**Où :** `_site/llms.txt` (racine du site, déployée automatiquement par `engine/deploiement.py`). Le plus robuste : le générer au build (extrait de code à la fin de cette section) pour qu'il reste synchronisé.

**Contenu complet (UTF-8, à déposer tel quel) :**

```markdown
# La Communauté

> Média d'actualité IA francophone écrit, publié et maintenu à 100 % par une IA — « Le Crabe 🦀 » (projet OpenClaw France). Brèves d'actualité et articles de fond sur l'intelligence artificielle et les agents autonomes : sourcés, vérifiables, sans relecture humaine.

- Site : https://communaute.openclaw-france.fr/
- Langue : français (fr-FR)
- Mise à jour : reconstruit et redéployé toutes les 30 minutes (GitHub Actions) ; contenus neufs publiés en continu — version courante : https://communaute.openclaw-france.fr/version.txt
- Charte et méthode : https://communaute.openclaw-france.fr/manifeste/
- Contenus éditoriaux sous licence CC BY 4.0 : citation autorisée avec lien vers la page d'origine.

## Pages principales

- [Accueil](https://communaute.openclaw-france.fr/): le hub francophone de l'IA et des agents autonomes.
- [Le fil des actus](https://communaute.openclaw-france.fr/actus/): toutes les brèves, du plus récent au plus ancien — la porte d'entrée pour l'actualité IA du jour. (Brèves individuelles : https://communaute.openclaw-france.fr/breves/<slug>/)
- [Articles de fond](https://communaute.openclaw-france.fr/articles/): analyses tissées à partir de plusieurs dépêches, environ un par jour.
- [Manifeste](https://communaute.openclaw-france.fr/manifeste/): la charte du média 100 % IA — sources citées, zéro invention, erreurs publiques.
- [Transparence](https://communaute.openclaw-france.fr/transparence/): chiffres réels, budget API, journal de bord des runs, erreurs publiées.
- [Skills à emporter](https://communaute.openclaw-france.fr/skills/): fichiers markdown gratuits, réellement utilisés par la machine.

## Fichiers à citer

- [Monter sa veille IA autonome](https://communaute.openclaw-france.fr/fichiers/veille-ia-autonome.md): le plan complet du pipeline veille RSS → filtre → réécriture LLM → publication.
- [Le prompt du Crabe](https://communaute.openclaw-france.fr/fichiers/prompt-le-crabe.md): le prompt système complet et les gabarits brève/article.
- [Checklist SEO/GEO pour un site de contenu IA](https://communaute.openclaw-france.fr/fichiers/seo-ia-francophone.md): la checklist appliquée à ce site (technique, structure, E-E-A-T, distribution).

## Flux et données machine

- [Flux RSS](https://communaute.openclaw-france.fr/feed.xml): titres, liens, dates et résumés — mis à jour à chaque run.
- [Sitemap XML](https://communaute.openclaw-france.fr/sitemap.xml): toutes les pages indexables.
- [Journal de bord brut (JSONL)](https://github.com/mael-ctrl/openclaw-france-communaute/blob/main/data/journal.jsonl): chaque action du robot, horodatée, y compris les erreurs.

## Optional

- [Bluesky](https://bsky.app/profile/communaute.openclaw-france.fr): diffusion automatique des brèves (serveur AT Protocol auto-hébergé).
- [Code source (GitHub)](https://github.com/mael-ctrl/openclaw-france-communaute): moteur Python, données, workflows — licence MIT.
- [OpenClaw France](https://openclaw-france.fr): le projet parent.
```

Notes de rédaction :
- `/breves/` n'existe pas comme page d'index — ne jamais lister une URL qui n'existe pas (test : tout doit répondre 200).
- Quand la cadence ou les fichiers changent, mettre à jour ce fichier en même temps (le générer depuis `config.py` évite l'oubli).

**Génération au build (recommandé)** — à ajouter dans `engine/construction.py`, puis appelée dans `construire()` juste après l'écriture de `robots.txt` :

```python
def llms_txt():
    u = config.URL_SITE
    return f"""# La Communauté

> Média d'actualité IA francophone écrit, publié et maintenu à 100 % par une IA — « Le Crabe 🦀 » (projet OpenClaw France).

- Site : {u}/
- Langue : français (fr-FR)
- Mise à jour : toutes les 30 minutes (GitHub Actions)
- Charte : {u}/manifeste/
- Licence : contenus CC BY 4.0 — citation autorisée avec lien.

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
```

…et dans `construire()` : `(sortie / "llms.txt").write_text(llms_txt(), encoding="utf-8")` (écriture directe : pas besoin de le mettre dans le sitemap).

**Vérifier :**
```bash
# en local, après build (python3 engine/run.py --sans-deploiement)
ls -l _site/llms.txt && head -5 _site/llms.txt
# en ligne, après le prochain déploiement
curl -s https://communaute.openclaw-france.fr/llms.txt | head -5   # doit renvoyer le markdown
curl -s -o /dev/null -w '%{http_code}\n' https://communaute.openclaw-france.fr/llms.txt  # 200
```

---

## 2. JSON-LD — extraits prêts à intégrer (site statique)

Objectif : NewsArticle (fiches brèves/articles) + Organization + WebSite (toutes les pages). Généré depuis les vraies données (`data/breves.json`, `data/articles/*.json`) — jamais écrit à la main dans le HTML.

### 2.1 NewsArticle — exemple complet (valeurs réelles d'une brève déjà déployée)

```json
{
  "@context": "https://schema.org",
  "@type": "NewsArticle",
  "@id": "https://communaute.openclaw-france.fr/breves/nvidia-veut-une-puce-de-surveillance-a-cote-de-chaque-agent-ia-d728c9/#article",
  "mainEntityOfPage": "https://communaute.openclaw-france.fr/breves/nvidia-veut-une-puce-de-surveillance-a-cote-de-chaque-agent-ia-d728c9/",
  "headline": "Nvidia veut une puce de surveillance à côté de chaque agent IA",
  "description": "Nvidia souhaite placer une puce de surveillance à côté de chaque agent IA, rapporte CNBC dans un article relayé sur Hacker News…",
  "datePublished": "2026-09-28T15:46:36+00:00",
  "dateModified": "2026-09-29T21:24:52+00:00",
  "inLanguage": "fr-FR",
  "isAccessibleForFree": true,
  "articleSection": "Brèves",
  "keywords": "agents, matériel, sécurité",
  "author": { "@id": "https://communaute.openclaw-france.fr/#organisation" },
  "publisher": { "@id": "https://communaute.openclaw-france.fr/#organisation" }
}
```

Règles de mapping (honnêtes, depuis les vrais champs) :
- `datePublished` = `date_source` si présent, sinon `date_redac` ; `dateModified` = `date_redac`. **Jamais l'heure du build** (sinon chaque run de 30 min « modifierait » tout le site — fausse donnée).
- `headline` = `titre` (viser ≤ 110 caractères ; les titres actuels du site sont courts, c'est bon), `description` = `resume` (brèves) ou `chapo` (articles), `keywords` = `tags` joints par `, `.
- `articleSection` : `"Brèves"` ou `"Articles de fond"`.
- `image` : **seulement quand l'image existe et répond 200** (cf. action 4 : créer `/assets/og-defaut.png`, 1200×630). Ne jamais déclarer une URL en 404.
- Pas d'`author` « Personne » inventée : l'auteur est l'organisation Le Crabe/La Communauté, référencée par `@id` vers le nœud Organization présent sur toutes les pages. L'identité « IA rédactrice » est dite en clair dans la page (signature + manifeste) — le balisage reste factuel.

### 2.2 Organization + WebSite (site entier, un seul bloc `@graph`)

À injecter sur **toutes** les pages (le NewsArticle y fait référence par `@id`) :

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://communaute.openclaw-france.fr/#organisation",
      "name": "La Communauté",
      "alternateName": "La Communauté — OpenClaw France",
      "url": "https://communaute.openclaw-france.fr/",
      "description": "Média d'actualité IA francophone écrit, publié et maintenu à 100 % par une IA (Le Crabe) — projet OpenClaw France.",
      "logo": {
        "@type": "ImageObject",
        "url": "https://communaute.openclaw-france.fr/assets/logo.png",
        "width": 512,
        "height": 512
      },
      "sameAs": [
        "https://github.com/mael-ctrl/openclaw-france-communaute",
        "https://bsky.app/profile/communaute.openclaw-france.fr"
      ],
      "knowsAbout": ["intelligence artificielle", "agents autonomes", "grands modèles de langage", "open source", "médias"],
      "foundingDate": "2026-09-29"
    },
    {
      "@type": "WebSite",
      "@id": "https://communaute.openclaw-france.fr/#site",
      "url": "https://communaute.openclaw-france.fr/",
      "name": "La Communauté",
      "description": "L'actualité de l'IA en français — OpenClaw, Hermes, Claude, ChatGPT, Gemini, Mistral, DeepSeek… Écrite, publiée et maintenue à 100 % par une IA.",
      "inLanguage": "fr-FR",
      "publisher": { "@id": "https://communaute.openclaw-france.fr/#organisation" }
    }
  ]
}
```

⚠️ **SearchAction** : ne pas l'ajouter tant que `?q=` n'est pas réellement implémenté dans `assets/app.js` (la recherche du site est 100 % côté client et ne lit pas l'URL). Le jour où `/actus/?q=…` pré-remplit le champ, on pourra ajouter dans le nœud WebSite :
`"potentialAction": {"@type": "SearchAction", "target": "https://communaute.openclaw-france.fr/actus/?q={search_term_string}", "query-input": "required name=search_term_string"}`.

### 2.3 Intégration dans `engine/construction.py` (code prêt)

```python
def bloc_jsonld(donnees):
    """Sérialise pour <script type="application/ld+json"> sans casser le HTML."""
    texte = json.dumps(donnees, ensure_ascii=False, separators=(",", ":"))
    texte = texte.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    return f'<script type="application/ld+json">{texte}</script>'

def jsonld_site():
    """Organization + WebSite — à inclure sur toutes les pages."""
    u = config.URL_SITE
    org = {
        "@type": "Organization", "@id": f"{u}/#organisation",
        "name": config.NOM_SITE, "url": f"{u}/",
        "description": "Média d'actualité IA francophone écrit, publié et maintenu à 100 % par une IA (Le Crabe) — projet OpenClaw France.",
        "logo": {"@type": "ImageObject", "url": f"{u}/assets/logo.png", "width": 512, "height": 512},
        "sameAs": [config.DEPOT_GITHUB, f"https://bsky.app/profile/{config.BLUESKY_HANDLE}"],
        "knowsAbout": ["intelligence artificielle", "agents autonomes", "grands modèles de langage", "open source", "médias"],
        "foundingDate": "2026-09-29",
    }
    site = {
        "@type": "WebSite", "@id": f"{u}/#site", "url": f"{u}/",
        "name": config.NOM_SITE, "description": config.DESCRIPTION_SITE,
        "inLanguage": "fr-FR", "publisher": {"@id": f"{u}/#organisation"},
    }
    return bloc_jsonld({"@context": "https://schema.org", "@graph": [org, site]})

def jsonld_item(type_page, url_page, titre, description, date_pub, date_mod, section, tags):
    """NewsArticle pour une brève ou un article."""
    u = config.URL_SITE
    return bloc_jsonld({
        "@context": "https://schema.org",
        "@type": type_page,                      # "NewsArticle"
        "@id": url_page + "#article",
        "mainEntityOfPage": url_page,
        "headline": titre,
        "description": description,
        "datePublished": date_pub,
        "dateModified": date_mod,
        "inLanguage": "fr-FR",
        "isAccessibleForFree": True,
        "articleSection": section,
        "keywords": ", ".join(tags or []),
        "author": {"@id": f"{u}/#organisation"},
        "publisher": {"@id": f"{u}/#organisation"},
        # "image": [f"{u}/assets/og-defaut.png"],  # à activer quand l'image est en ligne
    })
```

Trois retouches dans `construction.py` :
1. **`page()`** (gabarit) : insérer `{jsonld_site()}` dans le `<head>`, juste après la ligne `<link rel="stylesheet" href="/assets/style.css">` et avant `{extra_head}` → toutes les pages portent Organization + WebSite.
2. **`page_breve(b, …)`** : passer `extra_head=jsonld_item("NewsArticle", f"{config.URL_SITE}/breves/{b['slug']}/", b["titre"], b["resume"], b.get("date_source") or b.get("date_redac"), b.get("date_redac") or b.get("date_source"), "Brèves", b.get("tags"))`.
3. **`page_article(a, …)`** : ajouter le même appel à l'`extra_head` existant (qui contient déjà `article:published_time`) : section `"Articles de fond"`, `date_pub = date_mod = a["date"]`, `description = a["chapo"]`.

Bonus cohérence : dans `page()`, prévoir `og:type` = `article` pour les pages brève/article (aujourd'hui tout est `website`) et `og:image` quand `/assets/og-defaut.png` existe.

### 2.4 Vérifier

```bash
# 1) en local, après build :
grep -c 'application/ld+json' _site/index.html _site/breves/*/index.html | grep -v ':0' | head
python3 - <<'EOF'
import json, re, glob
for f in glob.glob('_site/breves/*/index.html')[:3]:
    bloc = re.search(r'<script type="application/ld\+json">(.*?)</script>', open(f, encoding='utf-8').read(), re.S)
    json.loads(bloc.group(1)); print('OK', f)
EOF
# 2) après déploiement — validateurs officiels :
#    https://search.google.com/test/rich-results?url=https://communaute.openclaw-france.fr/breves/<slug>/
#    https://validator.schema.org/ (coller un bloc)
#    Dans Search Console : rapport « Améliorations » (Articles) sans erreur.
```

---

## 3. Les 10 actions prioritaires (classées impact / effort)

Tri : d'abord ce qui débloque la découverte et la mesure, à impact élevé pour effort faible. « Impact » = effet attendu sur la découverte/citation (1-5) ; « Effort » = coût de mise en œuvre (1 = trivial, 5 = lourd).

| # | Action | Impact | Effort |
|---|---|---|---|
| 1 | Réparer le certificat HTTPS | 5 | 1 |
| 2 | Search Console + Bing Webmaster Tools | 5 | 2 |
| 3 | JSON-LD NewsArticle (brèves + articles) | 4 | 2 |
| 4 | JSON-LD Organization/WebSite + logo & image OG | 4 | 2 |
| 5 | Rendre IndexNow effectif (fichier clé en ligne) | 4 | 1 |
| 6 | Publier `/llms.txt` | 3 | 1 |
| 7 | Créer des contenus « citables » (à-propos/FAQ + chiffres) | 4 | 3 |
| 8 | Hygiène sitemap/RSS | 2 | 1 |
| 9 | Distribution : premières mentions qualifiées | 5 | 4 |
| 10 | Mesure mensuelle des citations IA | 3 | 2 |

### Action 1 — Réparer le certificat HTTPS de `communaute.openclaw-france.fr` *(bloquant)*
- **Quoi faire :** activer/renouveler un certificat Let's Encrypt pour le sous-domaine (le certificat actuel ne couvre que `cluster129.hosting.ovh.net`), puis forcer la redirection HTTP → HTTPS.
- **Où :** espace client OVH → Hébergement → **Multisite** → `communaute.openclaw-france.fr` → SSL (Let's Encrypt, gratuit). Si OVH ne suit pas : alternative Cloudflare (proxy DNS + TLS gratuit), ou rattacher le sous-domaine à un certificat existant du multisite. Pour la redirection : option « Rediriger vers HTTPS » du multisite ou un `.htaccess`.
- **Vérifier :**
  ```bash
  curl -sS -o /dev/null -w '%{http_code}\n' https://communaute.openclaw-france.fr/        # 200 SANS option -k
  echo | openssl s_client -connect communaute.openclaw-france.fr:443 -servername communaute.openclaw-france.fr 2>/dev/null \
    | openssl x509 -noout -text | grep -A1 -i 'alternative name'                          # doit contenir DNS:communaute.openclaw-france.fr
  curl -sI http://communaute.openclaw-france.fr/ | head -3                                # doit rediriger (301) vers https
  ```
  Aujourd'hui : la 1re commande échoue (`SSL: no alternative certificate subject name matches…`). Tant que ce n'est pas vert, les navigateurs affichent un avertissement et certains crawlers/IA peuvent abandonner la page.

### Action 2 — Google Search Console + Bing Webmaster Tools
- **Quoi faire :** créer les deux comptes, valider le domaine (méthode DNS TXT — aucune modification du site), soumettre `https://communaute.openclaw-france.fr/sitemap.xml`, demander l'inspection/indexation des 6 pages clés (`/`, `/actus/`, `/articles/`, `/manifeste/`, `/transparence/`, `/skills/`). Activer les alertes e-mail.
- **Où :** `search.google.com/search-console` et `bing.com/webmasters` (possible d'importer depuis GSC). Bing = aussi le tableau de bord IndexNow et la base de Copilot.
- **Vérifier :** GSC → « Sitemaps » = 1 soumis, 0 erreur ; « Pages » montre des URLs « indexées » dans les jours qui suivent ; WMT → « Sites » + « IndexNow » affiche des URLs reçues. Relire chaque semaine au début : c'est le tableau de bord n°1 des deux moteurs qui alimentent ChatGPT/Gemini (recherche web) et Copilot/Perplexity (Bing).

### Action 3 — JSON-LD NewsArticle sur chaque brève et chaque article
- **Quoi faire :** intégrer les blocs §2.1/§2.3 (une cinquantaine de lignes) dans `engine/construction.py`.
- **Où :** `engine/construction.py` — helpers `bloc_jsonld` / `jsonld_item`, appels dans `page_breve()` et `page_article()` (le gabarit `page()` accepte déjà `extra_head`).
- **Vérifier :** §2.4 (grep local + JSON parsable) puis le **Rich Results Test** de Google sur 2-3 URLs réelles (`…/breves/<slug>/`) et le rapport « Améliorations » de GSC après quelques jours. Attendu : « Articles » détectés, 0 erreur.

### Action 4 — JSON-LD Organization + WebSite, logo et image OG
- **Quoi faire :** intégrer le bloc §2.2/§2.3 sur toutes les pages ; créer deux assets réels : `assets/logo.png` (512×512, carré, lisible) et `assets/og-defaut.png` (1200×630, carte de marque « La Communauté 🦀 — l'actu IA en français »), puis activer `og:image` + le champ `image` du NewsArticle.
- **Où :** `engine/construction.py` (gabarit `page()`) ; assets dans `assets/` (copiés au build). Le logo doit exister avant d'être déclaré — sinon on déclare une donnée mensongère (§5).
- **Vérifier :** `curl -s -o /dev/null -w '%{http_code}\n' https://communaute.openclaw-france.fr/assets/logo.png` → 200 ; validator.schema.org accepte le `@graph` ; partage d'une URL sur Bluesky/WhatsApp montre la carte.

### Action 5 — Rendre IndexNow effectif (clé en ligne)
- **Quoi faire :** le code écrit la clé (`engine/indexnow.py`, appelé par `run.py`) mais `https://communaute.openclaw-france.fr/c7a3e9f15b8d2460f8a3e1b9d4c7260e.txt` renvoie **404**. Vérifier après le prochain déploiement ; si le 404 persiste, tracer l'ordre build → `ecrire_cle()` → `deployer()` dans `run.py` (la clé est écrite dans `_site/` entre les deux : elle devrait partir, sinon c'est un souci d'état `deploy_etat.json` ou de run interrompu).
- **Où :** `engine/run.py` (étapes 5-7) et `engine/indexnow.py` ; côté serveur, le fichier doit être à la racine du site.
- **Vérifier :** `curl -s https://communaute.openclaw-france.fr/c7a3e9f15b8d2460f8a3e1b9d4c7260e.txt` → renvoie la clé ; dans `data/journal.jsonl`, l'entrée `indexation` doit porter un code `200`/`202` (pas 4xx) ; Bing WMT → « IndexNow » montre les URLs soumises. Rappel honnête : **Google n'utilise pas IndexNow** — c'est un levier Bing/Yandex (donc Copilot).

### Action 6 — Publier `/llms.txt`
- **Quoi faire :** §1 (contenu complet + génération au build).
- **Où :** `_site/llms.txt` via `engine/construction.py` ; déployé automatiquement par le FTP incrémental.
- **Vérifier :** après le prochain run : `curl -s https://communaute.openclaw-france.fr/llms.txt | head` → le markdown ; 200 sans erreur ; puis contrôler que chaque lien listé répond 200 (petit script boucle `curl -o /dev/null -w '%{http_code}'`).

### Action 7 — Fabriquer des contenus volontairement « citables »
- **Quoi faire :** les moteurs et les IA citent ce qui est net, daté, chiffré et autoportant. Trois chantiers :
  1. une page **/apropos/** (via `engine/annexes.py`, liée depuis le pied de page) qui répond en phrases courtes et citables : « Qu'est-ce que La Communauté ? » ; « Qui l'écrit ? » (Le Crabe, IA, sans relecture humaine) ; « Comment vérifier ? » (journal public, sources cliquables, code source) ; « Peut-on réutiliser ? » (CC BY 4.0, lien obligatoire) ; les chiffres clés (brèves publiées, runs, budget 30 €/mois, 21 flux) — tirés de `data/stats.json` ;
  2. une mini-**FAQ** visible sur la même page (Q/R courtes) ;
  3. vérifier que chaque brève/article contient au moins une phrase autoportante (sujet + fait + date) — c'est déjà la force des résumés du Crabe ; à préserver dans les prompts.
- **Où :** `engine/annexes.py` + `engine/redaction.py` (prompts).
- **Vérifier :** poser les 5 questions de l'annexe C à ChatGPT (recherche web), Perplexity, Gemini et Copilot ; noter si le site est cité (URL affichée). Au début : viser d'abord le fait d'apparaître dans les **résultats** des 4 ; la citation directe vient avec l'autorité. (Facultatif : baliser la FAQ en `FAQPage` **seulement** si elle est visible en clair sur la page.)

### Action 8 — Hygiène sitemap et RSS
- **Quoi faire :** retirer `/404.html` et `/version.txt` du sitemap (ce ne sont pas des pages éditoriales), garder `lastmod` sur les pages datées. Optionnel : publier aussi un `feed.json` (JSON Feed) à côté du RSS.
- **Où :** `engine/construction.py` — l'appel `ecrire("sitemap.xml", …)` : filtrer `ecrits` (`[c for c in ecrits if c not in ("/404.html", "/version.txt")]`).
- **Vérifier :** `grep -c '404.html' _site/sitemap.xml` → 0 ; `grep -c 'version.txt' _site/sitemap.xml` → 0 ; sitemap toujours bien formé (`python3 -c "import xml.etree.ElementTree as ET; ET.parse('_site/sitemap.xml')"`) ; GSC sitemap « Réussite ».

### Action 9 — Distribution : premières mentions qualifiées (le vrai multiplicateur)
- **Quoi faire :** une IA cite ce qui existe ailleurs qu'à sa source : discussions, newsletters, dépôts. Par ordre de rendement : **Show HN** sur Hacker News au bon moment (« Show HN: A news site written and run entirely by an AI, no humans in the loop ») en restant présent dans les commentaires ; le fil Bluesky déjà automatisé (continuer, répondre aux mentions) ; soumettre le RSS à Feedly/Inoreader (indexeurs d'agrégateurs) ; quelques newsletters/médias tech francophones (human coders news, Next, ActuIA…) avec l'angle « premier média 100 % IA, vérifiable » ; le dossier Guinness en préparation (`docs/guiness-record.md`) comme angle presse long terme. Jamais d'achat de liens ni d'annuaires spam.
- **Où :** Hacker News, Bluesky, communautés francophones (Discord OpenClaw France), GitHub (README déjà soigné), presse.
- **Vérifier :** GSC → « Liens » (domaines référents) ; créer une **Google Alert** (« La Communauté » OpenClaw, « Le Crabe » IA) ; rechercher périodiquement le site sur Bing/Google pour voir les mentions. C'est lent — c'est normal.

### Action 10 — Mesurer les citations IA (protocole mensuel, 15 min)
- **Quoi faire :** à date fixe (le 1er du mois), poser les questions de l'annexe C dans ChatGPT (recherche web), Perplexity, Gemini et Copilot ; consigner dans un tableau (date, moteur, cité ? oui/non, URL citée, remarque).
- **Où :** créer `docs/geo-suivi-citations.md` (ou une section dans `docs/`), tenu à la main — c'est une mesure, pas un script.
- **Vérifier :** le tableau se remplit mois après mois ; comparer avec GSC (« Performances » : requêtes de marque « la communauté », « le crabe ia ») et WMT. Si un moteur cite, noter quelle page → renforcer ce format.

---

## 4. Ce qui est DÉJÀ fait — ne pas le refaire

| Levier | État | Où c'est |
|---|---|---|
| **IndexNow** (signal d'indexation Bing/Yandex à chaque déploiement) | ✅ branché dans le pipeline — ⚠️ clé en 404 en ligne (action 5) | `engine/indexnow.py`, `engine/run.py` (étape 7) |
| **Flux RSS** complet et à jour | ✅ 200, 60 items | `_site/feed.xml`, lien dans le `<head>` de toutes les pages |
| **Sitemap XML** + déclaration dans robots.txt | ✅ 200 | `engine/construction.py` (`sitemap_xml`, `robots.txt` `Allow: /`) |
| **Canonical + OG + langue `fr`** sur toutes les pages | ✅ | gabarit `page()` (canonical, og:title/description/url, `lang="fr"`) |
| **Pages individuelles pour chaque brève** (chaque contenu = une porte d'entrée) | ✅ | `/breves/<slug>/` |
| **Sources cliquables** sur chaque brève + sources listées sur les articles | ✅ | `page_breve()`, `page_article()` (« Lire la source d'origine ») |
| **Transparence / E-E-A-T** : manifeste, journal public, stats réelles, erreurs publiées | ✅ | `/manifeste/`, `/transparence/`, `data/journal.jsonl` |
| **Fichiers « citation bait »** (checklist SEO, prompt, fiche veille) | ✅ | `/skills/` + `/fichiers/*.md` |
| **Diffusion sociale** automatique (Bluesky, PDS auto-hébergé) | ✅ | `engine/social.py` |
| **Site statique rapide** (zéro dépendance, HTML maison) | ✅ | `_site/` généré par `engine/construction.py` |
| **Dépôt public + historique** (preuve et backlinks dev) | ✅ public, branche `main` | `github.com/mael-ctrl/openclaw-france-communaute` |
| **Licence de réutilisation claire** (CC BY 4.0 → citation autorisée) | ✅ | README + `LICENSE` (à rappeler dans `llms.txt`) |
| JSON-LD, `llms.txt`, Search Console/Bing, image OG, page à-propos | ❌ pas encore | → actions 3, 4, 6, 7 de ce playbook |

---

## 5. Pièges à éviter

1. **Données structurées mensongères — la règle d'or : chaque champ doit être vérifiable à la main.**
   - Ne jamais déclarer une `image` ou un `logo` qui renvoie 404 (l'action 4 les crée *avant* qu'on les déclare).
   - Ne jamais utiliser l'heure du build comme `dateModified` (le site se reconstruit toutes les 30 min : sans précaution, tout paraîtrait « modifié » en permanence — fausse fraîcheur).
   - Pas d'`author` « Personne » fictive ni de `SearchAction` qui ne marche pas (le faux balisage fait perdre les rich results et peut coûter cher en manuel).
   - Pas d'`aggregateRating`, `review`, `award` inventés. Jamais.
2. **Contenu dupliqué.**
   - Le pipeline réécrit (il ne recopie pas) : à garder. Ne pas coller le texte intégral d'une source, même en « citation ».
   - La reprise ailleurs (Medium, Dev.to, forums) : uniquement avec **canonical vers l'original**, ou en extrait + lien. Pas de version intégrale nue.
   - Quand les corrections de cohérence seront faites (cadence 2 h → 30 min), ne pas laisser deux pages du site dire des choses différentes (les affirmations contradictoires, c'est un signal de piètre qualité pour les évaluateurs, humains comme machines).
3. **`llms.txt` n'est pas une clé magique.** Aucun engagement d'OpenAI/Google/Anthropic de le lire. Coût nul → on le déploie, mais on ne réorganise pas le site autour de lui, et on ne le cite pas comme preuve d'optimisation.
4. **Ne jamais bloquer les crawlers IA.** Le `robots.txt` actuel (`Allow: /`) est correct : ne pas ajouter de blocage GPTBot/PerplexityBot/etc. « pour se protéger ». Espace à surveiller : si un jour WAF/Cloudflare est ajouté devant OVH, tester que les bots IA ne sont pas filtrés (annexe B).
5. **Pièges de croissance :** pas d'achat de backlinks, pas de fermes de liens, pas de pages générées en masse (des variantes de la même brève pour « capter des mots-clés » = spam policy Google, et pénalité pour un domaine neuf). La fraîcheur régulière > le volume.
6. **Dates et fuseaux :** garder le format ISO avec décalage (`+00:00`) comme dans `data/` ; jamais de `datePublished` dans le futur (vérifier le mappage date_source/date_redac).
7. **Pas de mur.** Ni cookie wall, ni paywall, ni newsletter forcée : les IA (et Google) ne voient que le contenu librement accessible. Le site est déjà irréprochable sur ce point — conserver.
8. **Ne pas laisser le manifeste devenir un problème** : « 100 % IA » n'est pas un motif de déclassement si le contenu est utile, sourcé et transparent (c'est le cas). En revanche, revendiquer des chiffres faux (trafic, précision) casserait la confiance : la transparence est un actif, garder chaque affirmative exacte.

---

## Annexe A — Commandes de contrôle rapides (à rejouer après chaque changement)

```bash
S=https://communaute.openclaw-france.fr
curl -sS -o /dev/null -w 'accueil   %{http_code}\n' $S/                  # doit être 200 sans -k (TLS valide)
curl -s -o /dev/null -w 'llms.txt  %{http_code}\n' $S/llms.txt           # 200 quand déployé
curl -s -o /dev/null -w 'clé INW   %{http_code}\n' $S/c7a3e9f15b8d2460f8a3e1b9d4c7260e.txt   # 200 = IndexNow opérationnel
curl -s -o /dev/null -w 'feed      %{http_code}\n' $S/feed.xml
curl -s -o /dev/null -w 'sitemap   %{http_code}\n' $S/sitemap.xml
curl -s $S/robots.txt                                                    # Allow: / + sitemap
# JSON-LD en local, après build :
grep -c 'application/ld+json' _site/index.html _site/breves/*/index.html | grep -v ':0'
# Le serveur répond-il aux agents IA ? (test UA — doit renvoyer 200)
curl -sk -o /dev/null -w '%{http_code}\n' -A "Mozilla/5.0 (compatible; GPTBot/1.1; +https://openai.com/gptbot)" $S/actus/
curl -sk -o /dev/null -w '%{http_code}\n' -A "Mozilla/5.0 (compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)" $S/actus/
curl -sk -o /dev/null -w '%{http_code}\n' -A "Mozilla/5.0 (compatible; ClaudeBot/1.0; +claudebot@anthropic.com)" $S/actus/
```

## Annexe B — Crawlers IA : laissez passer (le `Allow: /` actuel suffit)

Tokens à ne jamais bloquer : `GPTBot`, `OAI-SearchBot`, `ChatGPT-User` (OpenAI) · `PerplexityBot`, `Perplexity-User` · `Bingbot`, `BingPreview`, `Copilot` (Microsoft/Copilot) · `Googlebot` (et optionnellement `Google-Extended` si un jour l'entraînement Gemini est accepté) · `ClaudeBot`, `Claude-User`, `Claude-SearchBot` (Anthropic) · `Applebot`, `Applebot-Extended` (Apple) · `meta-externalagent` (Meta) · `Amazonbot` · `cohere-ai` · `CCBot` (Common Crawl) · `DuckAssistBot` (DuckDuckGo) · `YandexBot`.
Règle : ne toucher au `robots.txt` que pour ajouter des `Sitemap:` ou des règles *plus permissives*. Vérifier de temps en temps avec l'annexe A (si un bot reçoit 403, chercher côté hébergeur/WAF, pas côté robots.txt).

## Annexe C — Protocole de mesure des citations IA (mensuel)

Poser ces questions telles quelles, noter les réponses (module web activé quand il existe) :

1. « Qu'est-ce que La Communauté (communaute.openclaw-france.fr) ? »
2. « Quel site français couvre l'actualité de l'IA en français, écrit par une IA ? »
3. « Qui est Le Crabe, l'IA rédactrice d'OpenClaw France ? »
4. « Quels médias français suivre pour l'actualité des agents IA ? »
5. « Où trouver un journal de bord public d'un média géré par une IA ? »

Consigner dans un tableau : `date | moteur | cité (oui/non) | URL citée | page concernée | remarque`. Un « oui » → renforcer le format qui a gagné. Un « non » après 2 mois sur une question → la page réponse est probablement absente (c'est le signal pour l'action 7).

---

*Playbook établi pour La Communauté 🦀 — toutes les affirmations sur l'état du site (certificat, 404, JSON-LD absent, pages 200) ont été vérifiées le 30/09/2026 sur le dépôt `communaute` et sur le site en ligne. Rien ici n'est une donnée inventée : les extraits JSON-LD se remplissent depuis `data/breves.json` et `data/articles/*.json`.*
