# 🦀 Distribution Mastodon / Fédivers — « La Communauté »

**Objet** : étendre la diffusion de « La Communauté » — média d'actualité IA francophone **100 % écrit par une IA** (« Le Crabe », OpenClaw France), `communaute.openclaw-france.fr` — vers **Mastodon / le Fédivers**, en complément de Bluesky (PDS AT Protocol déjà auto-hébergé).

**Statut** : dossier de recherche et de planification. **Aucun compte n'a été créé, aucun message n'a été publié, aucun commit n'a été fait.** Les règles de chaque serveur ont été vérifiées le **30/09/2026** sur leurs pages publiques « À propos / Règles » et via l'API d'instance Mastodon (`/api/v1|v2/instance`), ainsi que dans la documentation officielle de Mastodon.

**En bref**

- **Recommandation : `piaille.fr`** — la plus grande instance généraliste FR, seule à avoir une **politique bots publiée et compatible** avec un compte média automatisé (marquage bot + limites 5 posts/h, 50/j + labellisation IA). Inscription avec approbation : candidature transparente requise.
- **Plan B : `pouet.chapril.org`** (accord préalable de l'équipe exigé par les CGU) — **Plan C : `mastodon.bot`** (instance dédiée aux bots, dérogation anglais à demander).
- **Risque global : MOYEN** (cf. §5) — le Fédivers accepte les bots, mais encadre strictement cadence, réponses et contenu IA ; certaines grandes instances les interdisent purement et simplement.

---

## 1. Pourquoi Mastodon — et les 3 règles d'or du Fédivers

Mastodon est le principal réseau du Fédivers (ActivityPub) : ~10 000 instances interconnectées, chacune avec **ses propres règles locales**. Contrairement à Bluesky (une fédération uniforme), un compte doit choisir **une instance d'attache** — et c'est cette instance qui applique ses règles, y compris via une modération humaine.

Trois règles d'or pour un compte média automatisé :

1. **Marquer le compte comme bot, toujours.** Badge « Ceci est un robot » + bio explicite. C'est exigé (ou fortement attendu) partout ; ne pas le faire expose à la suspension.
2. **Poster « natif », pas du cross-post brut.** Le Fédivers valorise : texte adapté, hashtags, **alt text** sur chaque média, CW (avertissement de contenu) si sensible, langue réglée sur `fr`. Plusieurs instances interdisent explicitement le cross-postage (cf. h4.io, toot.aquilenet.fr).
3. **Aucune interaction automatique non sollicitée.** Pas de réponses/likes/follows automatiques. Les bots qui « parlent en premier » sont bannis presque partout. Le robot répond uniquement si on l'a mentionné (et ≤ 2 réponses par sollicitation, cf. piaille).

---

## 2. Comparatif des serveurs

### 2.1 Tableau de synthèse (vérifié le 30/09/2026)

| Serveur | Taille | Position sur les bots (règles publiées) | Inscription | À savoir |
|---|---|---|---|---|
| **piaille.fr** | ~46 500 comptes / ~7 200 actifs | **Bots tolérés, politique dédiée publiée** (blog.piaille.fr, mars 2024) : marquage obligatoire, **≤ 5 posts/h et 50/j**, réponses uniquement sur mention (≤ 2), contenus IA « découragés » mais **autorisés si labellisés** | **Ouverte avec approbation** + motif obligatoire (`/auth/sign_up`) | Le cas « bot d'articles de presse/blog » est cité comme usage légitime ; 666 caractères ; 4 médias |
| **pouet.chapril.org** | ~1 900 comptes | **Compte bot = « demande préalable » + « accord exprès » de l'équipe** exigés par les CGU (projet April / CHATONS) | Ouverte (mais bot → demander d'abord via le formulaire de contact Chapril) | Instance éthique associative ; clause « tout abus sera puni » ; compte jugé abandonné = suppression possible |
| **h4.io** | ~8 600 comptes / ~180 actifs | Pas de règle bot publiée, mais **cross-postage bloqué** : « nous avons décidé de bloquer le cross-postage… les comptes utilisant ce procédé finissent par ne poster que sur Twitter, ne lisent pas les réponses et n'ont aucune interaction » | Ouverte avec approbation | **Écarté en pratique** : un flux automatisé qui ne lit pas les réponses est précisément ce qu'ils refusent ; contenu en français exigé |
| **mastodon.cipherbliss.com** | ~2 300 comptes | Pas de règle bots explicite ; règles minimales (politesse, NSFW, « rédigez de temps à autre des posts qui ne sont PAS un repost ») | Ouverte avec approbation | Petit, arts & divers fr/en ; aucune garantie long terme |
| **mastodon.tedomum.net** | ~340 comptes | Pas de règle bot ; **« Spam interdit, ainsi que toute forme d'attaque technique »** | Via le SSO TeDomum (« Se connecter ») | Petit (association CHATONS) ; 16 règles de modération ; aucune mention des bots → à clarifier avant |
| **toot.aquilenet.fr** | ~5 400 comptes | **Bot accepté si déclaré explicitement** (« Précisez explicitement si votre compte est parodique ou s'il s'agit d'un bot ») mais **« Le cross-posting automatisé est proscrit »** | **Fermée** (vagues de spambots) — demande par e-mail/IRC | Instance associative Aquitaine ; contenu fr/en ; écarté pour un flux automatisé |
| **toot.paris** | ~130 comptes | **« Pas d'agents IA sur cette instance. »** | Ouverte avec approbation + motif | **Rédhibitoire** : notre nature IA est le cœur du projet |
| **mastodon.bot** | ~280 comptes (instance dédiée aux bots, hébergée UE) | **Instance 100 % bots** avec « Code of Conduct » détaillé : bot marqué + but + propriétaire ; **pas de premier contact @** (pas de mention d'inconnus) ; **repost d'actus autorisé uniquement si vous êtes propriétaire vérifié du site** ✔ ; **alt text obligatoire** ; cadence raisonnable ; **publication en anglais exigée** (dérogation possible « contact us ») | Ouverte avec **approbation** (décrire le bot dans le motif ; ~1 jour) | Petit mais bien modéré et bien fédéré (sa mission affichée) ; à demander : dérogation pour publier en français |

### 2.2 Détail des 8 fiches

#### 1. piaille.fr — la cible principale
- **Taille** : 46 557 comptes, ~7 200 actifs (30/09/2026). La plus grande instance généraliste francophone « ouverte ».
- **Position bots (source : `blog.piaille.fr/les-regles-de-piaille-relatives-aux-bots/`, v1 mars 2024)** :
  - un compte qui poste ≥ 50 % de ses messages de manière automatisée **est** un bot ; « toléré » mais règles **d'application stricte** ;
  - **marquage obligatoire** : cocher « Ceci est un robot » dans les préférences du profil ;
  - **limites : ≤ 5 messages/heure et ≤ 50/jour** hors fil ; réponses auto **uniquement** si le message adresse le bot (≤ 2 réponses par sollicitation) ;
  - le bot reste **responsable de ses contenus** (charte complète applicable) ;
  - le blog cite comme cas légitime **« le compte qui poste un lien vers les nouveaux articles d'un site web de type presse, blog etc. »** — exactement notre cas ;
  - avertissement : un bot buggé ayant posté des centaines de messages lors de son installation **n'est pas toléré** → plafonner la reprise d'historique.
- **Règle IA (charte)** : « La publication de contenus générés totalement ou en partie par des outils d'intelligence artificielle (textes, images, sons…) est **découragée** sur Piaille. Le cas échéant, les contenus générés par IA **doivent être labellisés comme tels dans le corps de leurs messages**. » → publication possible **si étiquetage systématique** ; c'est la principale fragilité (voir §5).
- **Inscription** : ouverte, **approbation + motif obligatoires** (`/auth/sign_up`) : il faut expliquer qui on est. Validation par e-mail (utiliser `crabe@blockos.fr`, cf. §3).
- **Format** : 666 caractères, 4 médias max, langue `fr` recommandée.

#### 2. pouet.chapril.org — plan B éthique
- **Taille** : ~1 925 comptes ; instance de l'association **April** (collectif CHATONS).
- **Position bots (CGU Chapril, `chapril.org/cgu.html`)** : « Les comptes créés par les robots ou autres méthodes automatisées pourront être supprimés sans mise en demeure préalable. **L'ouverture d'un compte affilié à un robot devra faire l'objet d'une demande préalable** et ne pourra être effectuée qu'après notre accord exprès. »
- **Inscription** : registre ouvert pour les humains ; **pour un bot : demander l'accord AVANT création** (formulaire de contact Chapril), en présentant le projet, le marquage bot, le rythme et la nature IA des contenus.
- **À savoir** : CGU inspirées Framasoft ; « usage raisonnable » ; suppression possible des comptes présumés abandonnés (8 jours après demande de justification) ; aucune règle IA spécifique.
- **Pourquoi c'est un bon plan B** : valeurs open source/éthique proches d'OpenClaw ; si accord exprès, statut parfaitement légitime.

#### 3. h4.io — écarté (cross-postage bloqué)
- ~8 630 comptes / 183 actifs ; français exigé ; approbation requise.
- **Règle clé** : « Nous avons décidé de bloquer le cross-postage, aka le fait de publier sur Twitter et que cela soit également publié sur notre instance Mastodon. La raison est que bien souvent, les comptes utilisant ce procédé finissent par ne poster que sur Twitter, **ne lisent pas les réponses et n'ont aucune interaction** avec le reste de l'instance. »
- Un flux 100 % automatisé sans lecture des réponses entre exactement dans cette critique → à éviter.

#### 4. mastodon.cipherbliss.com — possible mais faible valeur
- ~2 291 comptes ; règles minimales ; approbation. Aucune protection long terme ni audience significative. À considérer seulement en dépannage.

#### 5. mastodon.tedomum.net — petit, à clarifier
- ~344 comptes ; CHATONS ; inscriptions via **SSO** ; règles : spam interdit, avertissements obligatoires, etc. Pas de règle bot → demander avant. Trop petit pour être prioritaire.

#### 6. toot.aquilenet.fr — écarté (cross-posting automatisé proscrit)
- ~5 384 comptes ; bot **doit être déclaré** (règle favorable) mais « **Le cross-posting automatisé est proscrit** » et **inscriptions fermées** (spambots) → double blocage.

#### 7. toot.paris — rédhibitoire
- ~128 comptes ; règle explicite : « **Pas d'agents IA sur cette instance.** » → exclu d'office pour un média 100 % IA.

#### 8. mastodon.bot — l'option « spécialiste bots » (anglaise)
- ~283 comptes, hébergée UE ; instance conçue **pour les bots** ; approbation (~1 jour) avec description du bot.
- Règles bot (extraits) : identification obligatoire (badge bot + but + **propriétaire**) ; **pas de premier contact** (aucune mention non sollicitée) ; **repost de sites d'actus interdit SAUF si vous êtes le propriétaire vérifié du site** (✔ notre cas) ; **alt text obligatoire** ; CW appropriés ; pas de spam du fil local ; suggestions d'auto-suppression 1–2 ans ; **langue : anglais** (« If you require an exception, contact us. »).
- Utile si piaille et chapril refusent — mais il faudrait obtenir la dérogation pour publier en français.

### 2.3 Serveurs écartés (et pourquoi)

| Serveur | Constat (30/09/2026) |
|---|---|
| **mamot.fr** (La Quadrature du Net) | **Inscriptions fermées.** Règle IA : « découragé d'utiliser des outils de génération procédurale (IA), et si c'est le cas, ça doit être mentionné. » |
| **framapiaf.org** (Framasoft) | Inscriptions fermées (« ne sont pas possibles »). |
| **mstdn.fr** | Inscriptions fermées. |
| **mastodon.xyz** | Inscriptions fermées. |
| **mastodon.social** (instance historique, 3,4 M comptes) | Inscriptions ouvertes **MAIS** Community Standards : « **Accounts that primarily or exclusively post AI-generated content are prohibited.** » → interdit pour La Communauté. |
| **mstdn.social** (276 000 comptes) | Approbation requise ; règle IA à surveiller (« use of generative AI must be disclosed ») + « **AI Agents are charged €100 for account processing and €10 per email** » → défavorable. |
| **mastoot.fr** | « Pas de spam, **pas de bot**, encore moins de Bot cross-post (cas particulier, contactez l'admin avant) ». |
| **mastodon.top** | Inscriptions fermées ; « Bots limités à 1 publication par heure » (montre le type de plafond courant). |
| **mastodon.fr** | Trop petit (~400 comptes, créé 2025, 1 admin). |
| **bzh.social** | Régional (Bretagne) ; confirmation manuelle anti-bots. |
| **mastodon.quebec** | ~360 comptes ; « N'utilisez pas ce serveur à des fins de promotion commerciale » ; thématique Québec. |
| **newsie.social** (média/journalistes) | **Inscriptions en pause.** |
| **botsin.space** | **Fermé** (annoncé oct. 2024, lecture seule début 2025) — précédent à garder en tête : aucune instance n'est éternelle. |

---

## 3. Publier automatiquement via l'API Mastodon — procédure précise

Prérequis : compte créé et approuvé sur l'instance retenue ; e-mail de validation = **`crabe@blockos.fr`** (boîte OVH, IMAP `ssl0.ovh.net:993` ; mot de passe au Trousseau macOS, service `blockos-crabe-email` — **jamais affiché, jamais écrit dans un fichier**).

### 3.1 Créer l'application (une fois par instance)

```bash
curl -X POST \
  -F 'client_name=La Communauté 🦀 (OpenClaw France)' \
  -F 'redirect_uris=urn:ietf:wg:oauth:2.0:oob' \
  -F 'scopes=write:statuses write:media write:accounts' \
  -F 'website=https://communaute.openclaw-france.fr' \
  https://<instance>/api/v1/apps
```

- Réponse : `client_id` + `client_secret` → **à traiter comme des mots de passe** (Trousseau macOS, ex. service `mastodon-communaute`).
- `urn:ietf:wg:oauth:2.0:oob` = flux « out-of-band » (copier-coller), parfait pour un script unique. Scopes : `write:statuses` (publier), `write:media` (images), `write:accounts` (poser le flag bot).

### 3.2 Obtenir le jeton utilisateur

1. Ouvrir dans un navigateur (connecté au compte) :

   `https://<instance>/oauth/authorize?response_type=code&client_id=<client_id>&redirect_uri=urn:ietf:wg:oauth:2.0:oob&scope=write:statuses write:media write:accounts`

2. Copier le **code** affiché, puis :

```bash
curl -X POST \
  -F 'grant_type=authorization_code' \
  -F 'code=<code>' \
  -F 'client_id=<client_id>' \
  -F 'client_secret=<client_secret>' \
  -F 'redirect_uri=urn:ietf:wg:oauth:2.0:oob' \
  https://<instance>/oauth/token
```

- Réponse : `access_token` → **mot de passe bis** (Trousseau + secret GitHub Actions `MASTODON_ACCESS_TOKEN` via `gh secret set`, jamais affiché).
- Révocation : `POST /oauth/revoke` (client_id + client_secret + token) si compromis.

### 3.3 Marquer le compte bot (API)

```bash
curl -X PATCH \
  -H 'Authorization: Bearer <access_token>' \
  -F 'bot=true' \
  -F 'display_name=Le Crabe 🦀 | La Communauté (bot)' \
  -F 'note=Compte automatisé — média d'actualité IA francophone…' \
  https://<instance>/api/v1/accounts/update_credentials
```

(`bot` est un booléen officiel de `PATCH /api/v1/accounts/update_credentials` ; équivalent manuel : Préférences → Profil → « Ceci est un robot ».)

### 3.4 Publier un statut

Étape média (optionnelle, obligatoire si image) :

```bash
curl -X POST -H 'Authorization: Bearer <access_token>' \
  -F 'file=@article.jpg' \
  -F 'description=Illustration générée par IA pour l'article …' \
  https://<instance>/api/v1/media          # → id ; limite 30 uploads / 30 min
```

Puis :

```bash
curl -X POST -H 'Authorization: Bearer <access_token>' \
  -H 'Idempotency-Key: crab-2026-09-30-article-123' \
  -F 'status=🦀 <titre> — <chapô> <lien>' \
  -F 'visibility=public' \
  -F 'language=fr' \
  -F 'media_ids[]=<id>' \
  https://<instance>/api/v1/statuses
```

- **`Idempotency-Key`** (header libre, stocké 1 h) = anti-doublon en cas de retry → indispensable pour un pipeline automatique.
- `visibility` : `public` (fil public) ou `unlisted` (visible des abonnés et via le lien, hors fils publics — utile pour tester ou pour les séries à fort volume). Jamais `private`/`direct` pour de la diffusion.
- `spoiler_text` (CW) si sujet sensible ; `scheduled_at` possible (≥ 5 min dans le futur, renvoie un `ScheduledStatus`).
- Réponse 200 : l'objet `Status` (avec son `id` et `url`) — **à journaliser** (idempotence, anti-doublons, stats).

### 3.5 Limites à connaître

| Limite | Valeur par défaut |
|---|---|
| Toute l'API | **300 requêtes / 5 min par compte** (headers `X-RateLimit-*`) |
| Upload média `POST /api/v1/media` | 30 / 30 min |
| Suppression de statuts | 30 / 30 min |
| Statut | 500 caractères (…666 sur piaille), 4 médias max |
| Limites locales en plus | ex. piaille : **bots ≤ 5 posts/h et ≤ 50/j** — c'est la contrainte la plus basse qui s'applique |

### 3.6 Intégration au dépôt (côté code, plus tard)

- Prévoir un module `engine/mastodon.py` sur le modèle de `engine/social.py` (Bluesky) : même signature d'appel depuis `run.py`, mêmes garde-fous.
- **Toujours passer par `engine/reseau.contexte()`** pour tout HTTP(S) (le python3 local n'a pas de bundle de certificats).
- Secrets : Trousseau macOS en local (`security find-generic-password -s mastodon-communaute -w`) + `gh secret set` (stdin) pour GitHub Actions. Jamais dans le repo, jamais dans les logs.
- **Pas de backfill massif** : ne publier que les articles du jour (le cas du bot qui poste « des centaines de messages » à l'installation est explicitement sanctionné chez piaille). Plafond dur : ≤ 5 posts/h, ≤ 50/j, en pratique viser 2–4/j.
- Idempotence : `Idempotency-Key` dérivé de l'ID d'article ; état dans `data/` (ex. `data/mastodon_publies.jsonl`).

---

## 4. Recommandation

### 🥇 Principal : piaille.fr

**Pourquoi** :

1. **Taille et pertinence** : la plus grande instance généraliste francophone ouverte (~46 500 comptes) — c'est là que se trouve le public FR du Fédivers, en plus de la fédération.
2. **Politique bots publiée, claire et compatible** : le blog modération cite explicitement le « bot qui poste les nouveaux articles d'un site de presse/blog » comme usage légitime. Nos obligations sont connues d'avance : badge bot, ≤ 5 posts/h, ≤ 50/j, réponses uniquement sur mention, responsabilité des contenus.
3. **Cadre IA praticable** : contenus IA « découragés » mais **autorisés s'ils sont labellisés** — La Communauté est transparente sur sa nature IA par conception ; l'étiquetage systématique est de toute façon la norme fédivers et un choix éditorial du projet.
4. **Procédure claire** : approbation humaine avec motif → nous candidatons en expliquant honnêtement le projet (modèle de texte ci-dessous). En cas de refus : aucun préjudice, on bascule sur le plan B.

**Modèle de motif d'inscription (à adapter)** :

> Bonjour, je candidate pour un compte **bot média** au nom de « La Communauté » (communaute.openclaw-france.fr), média d'actualité francophone sur l'IA, **intégralement rédigé par une IA** (projet OpenClaw France). Compte **marqué comme robot**, publications **labellisées « contenu généré par IA »**, rythme volontairement bas (≤ 2–4 posts/jour, ≤ 5/heure), liens vers nos articles. Aucune réponse automatique. Responsable humain : Maël (contact ci-dessous). Merci !

### 🥈 Plan B : pouet.chapril.org

Si refus de piaille (ou modération défavorable à moyen terme) : **demander l'accord exprès** à l'équipe Chapril (formulaire de contact) en amont — c'est une exigence des CGU pour tout compte robot. Argumentaire : projet associatif/éthique (open source, IA transparente), rythme très bas, aucun automatisme d'interaction. Petit mais propre, et aligné avec l'esprit OpenClaw.

### 🥉 Plan C : mastodon.bot — et option radicale

- **mastodon.bot** : instance dédiée aux bots, règles limpides, repost d'actus autorisé pour le propriétaire du site (nous le sommes). Prérequis : contacter `hello@mastodon.bot` pour une **dérogation de langue** (publication en français) et décrire le bot.
- **Option radicale (si tout échoue)** : auto-héberger un compte **GoToSocial** (ActivityPub, léger) sur le VPS OpenClaw (`85.31.238.150`) — aucune règle tierce, cohérent avec le PDS Bluesky déjà auto-hébergé. Coût : maintenance d'un service de plus ; à n'envisager qu'en dernier recours.

### Ce que nous n'utiliserons pas

`mastodon.social` et `mastodon.online` (interdiction des comptes majoritairement IA), `toot.paris` (pas d'agents IA), `h4.io` et `toot.aquilenet.fr` (cross-postage automatisé bloqué), `mamot.fr`/`framapiaf.org`/`mstdn.fr`/`mastodon.xyz` (fermés), `mstdn.social` (€100 pour les agents IA).

---

## 5. Risques et interdits

| Risque | Détail | Parade |
|---|---|---|
| **Contenu IA mal perçu** | `mastodon.social` **interdit** les comptes majoritairement IA (« prohibited ») ; piaille et mamot le « découragent » ; toot.paris interdit les « agents IA » | Choisir une instance compatible (piaille) ; **labelliser chaque post** (« 🤖 Contenu généré par IA ») + bio transparente ; ne jamais dissimuler la nature IA — c'est aussi la transparence exigée par l'AI Act côté UE |
| **Spam / cadence** | Toutes les instances sanctionnent le spam ; piaille plafonne les bots à 5/h et 50/j ; mastodon.social proscrit « using automation to disrupt conversations » | Rythme 2–4 posts/j ; jamais de rafale ; plafonds codés en dur ; **pas de backfill massif** |
| **Réactions automatiques** | Interdites ou très encadrées partout : pas de premier contact (mastodon.bot), réponses seulement sur mention et ≤ 2 (piaille), pas d'engagement artificiel (mastodon.social) | **Zéro automatisme** de réponse/like/follow ; le robot ne parle que si on lui parle |
| **Cross-post brut** | h4.io bloque le cross-postage ; aquilenet proscrit le « cross-posting automatisé » ; la culture fédivers rejette les miroirs automatisés | Publier du contenu **natif** : texte adapté, hashtags (#IA #IntelligenceArtificielle #Fediverse), alt text systématique, langue `fr` |
| **Marquage bot absent** | Suspension/exclusion quasi certaine, filtrage possible par les utilisateurs | Badge bot dès la création (`bot=true`) + mention dans le pseudo/bio |
| **Modération discrétionnaire** | « Les modérateurs (…) ont le dernier mot » (mastodon.bot) ; piaille supprime tout compte ne respectant pas les règles bots | Respecter strictement la charte locale ; relire les règles à chaque mise à jour ; garder un contact humain identifiable |
| **Instabilité des instances** | `botsin.space` a fermé (annonce oct. 2024) ; inscriptions qui se ferment (mamot, framapiaf…) | Le site `communaute.openclaw-france.fr` reste la source de vérité ; prévoir export/archivage ; plan B prêt |
| **Juridique FR** | Hébergeurs soumis au droit français (loi LCEN, DSA) ; piaille applique la loi française | Pas de contenu illicite ; pour tout média repris : source citée + lien ; pas de copie intégrale d'articles tiers |
| **Anti-bot technique** | Des instances bloquent les inscriptions par vagues de spambots ; e-mail de validation indispensable | Passer par `crabe@blockos.fr` (IMAP OVH) ; candidater avec un motif crédible ; ne jamais automatiser l'inscription elle-même |

**En résumé — interdits absolus :** spam et rafales ; cross-post brut non adapté ; réponses automatiques non sollicitées ; engagement artificiel (likes/follows auto) ; absence de marquage bot ; contenu non labellisé IA ; création automatisée de comptes.

---

## 6. Plan de démarrage en 6 étapes

1. **Candidature** (piaille.fr) — créer le compte via `https://piaille.fr/auth/sign_up` avec le motif transparent (§4), e-mail `crabe@blockos.fr` ; valider l'e-mail ; attendre l'approbation. *En parallèle (optionnel) : envoyer la demande préalable à Chapril pour préparer le plan B.*
2. **Marquage bot + profil complet** — cocher « Ceci est un robot » (ou `PATCH … bot=true`) ; avatar/bandeau « Le Crabe » ; bio : « Média d'actualité IA francophone 100 % IA — compte automatisé — labellisation IA sur chaque post — humain responsable : @… » ; champs : site, Bluesky, contact ; activer la vérification par lien du site (`rel=me`) si possible.
3. **Post de présentation épinglé** — 1 post manuel : qui est Le Crabe, comment le compte fonctionne (rythme, nature IA, pas de réponses automatiques), lien vers le site ; l'épingler sur le profil.
4. **Premiers posts (manuellement, 3 à 5)** — présentation + 2–3 articles phares formatés **natifs** (titre, 1–2 phrases, lien, 2–3 hashtags, alt sur les images), langue `fr`. Pas d'historique massif. *Objectif : donner un profil crédible avant l'automatisation.*
5. **Brancher l'automatisation** — créer l'app API (§3.1), obtenir le jeton (§3.2), test `unlisted`, puis passage en `public` ; intégrer au pipeline (`engine/mastodon.py`, Keychain + secret GitHub) avec plafond 2–4/jour, idempotence, journalisation.
6. **Rythme & hygiène** — démarrage prudent (1–2 posts/j la 1ʳᵉ semaine, puis 2–4/j) ; **jamais > 5/h** ; relire les mentions une fois par semaine (humain) ; revérifier les règles de l'instance une fois par mois ; si refus/incident → activer le plan B (Chapril) ou C (mastodon.bot).

---

## 7. Sources (consultées le 30/09/2026)

- API instance des serveurs cités : `https://<serveur>/api/v1/instance` et `/api/v2/instance` (règles, inscriptions, limites).
- Politique bots Piaille : `https://blog.piaille.fr/les-regles-de-piaille-relatives-aux-bots/`
- CGU Chapril (April/CHATONS) : `https://www.chapril.org/cgu.html`
- Règles & Code of Conduct de mastodon.bot : `https://explore.mastodon.bot/rules` et `https://mastodon.bot/about`
- Page « À propos » h4.io (section Cross-postage) : `https://h4.io/about`
- Community Standards Mastodon GmbH (mastodon.social / mastodon.online) : `https://help.joinmastodon.org/article/12-community-standards` + Fediquette : `https://help.joinmastodon.org/article/13-fediquette-community-etiquette-guide`
- Documentation API officielle : `https://docs.joinmastodon.org/methods/apps/`, `/methods/oauth/`, `/methods/statuses/`, `/methods/accounts/`, `/api/rate-limits/`
- Fermeture de botsin.space : `https://muffinlabs.com/posts/2024/10/29/10-29-rip-botsin-space`

---

**Conclusion** — Serveur recommandé : **piaille.fr** (bot marqué, ≤ 5 posts/h, labellisation IA systématique, candidature transparente) ; replis : **pouet.chapril.org** puis **mastodon.bot**. Niveau de risque global : **MOYEN**.
