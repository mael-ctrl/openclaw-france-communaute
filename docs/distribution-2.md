# 🚀 Distribution — openclaw-france.fr (kits gratuits) — campagne-2

**Objet** : pousser **https://openclaw-france.fr** — les kits d'installation **OpenClaw** et **Hermes Agent**, désormais **100 % gratuits** — et, à travers lui, le média qui le porte : **La Communauté** (https://communaute-ia.fr), 100 % écrit et publié par une IA.

**Statut** : dossier préparé le **30/09/2026** ; autonomie de distribution accordée par Maël le **02/10/2026**, confirmée par la mission planifiée. Au plus **une action par jour**, jamais deux fois la même plateforme dans la même semaine. Exécution individualisée, sans rafale ; ne pas automatiser une plateforme qui l'interdit. Suivi opposable : `docs/distribution-textes.md`, section « Journal d'exécution ».

**Avancement (01/10/2026)** : contrôle J0 ✅ (accueil, `/openclaw/`, `/hermes/`, `/gratuit/` → 200). Première action : **Journal du Hacker** — demande d'invitation envoyée et **e-mail confirmé** le 01/10 (affichée aux utilisateurs connectés ; en attente d'invitation). Textes prêts à poster pour toutes les destinations : `docs/distribution-textes.md`.

**Méthode de vérification** : chaque URL et chaque point de règle cités ont été vérifiés le **30/09/2026** sur les pages publiques des plateformes (pages de règles, guides de soumission, annuaires). Les règles changent souvent : **relire la page de règles de chaque plateforme juste avant de poster**.

**Restrictions revérifiées le 07/10/2026 — prioritaires sur les fiches historiques ci-dessous** :
- **Show HN en réserve pour l'agent** : les [règles actuelles](https://news.ycombinator.com/newsguidelines.html) interdisent la publication automatisée et les textes générés ou édités par IA. Ne pas utiliser le brouillon préparé.
- **Product Hunt** : le [guide officiel](https://www.producthunt.com/launch/how-product-hunt-works#no-company-accounts) exige un compte personnel et interdit aux comptes de marque de publier/commenter ; ne pas créer d'identité humaine fictive pour Le Crabe.
- **Uneed** : permission explicite reçue, soumission gratuite possible avec indépendance visible ; accès sécurisé absent au contrôle. Aucun nouveau contact à envoyer (suivi dans `distribution-demande-uneed.md`).
- **Microlaunch / AIxploria** : offres de soumission payantes affichées ; pas d'achat automatique. AIxploria confirme ne plus proposer de listing gratuit.
- **Futurepedia / Ben's Bites News** : route historique de soumission en 404 pour le premier, erreur 522/délai de navigation pour le second ; requalifier l'accès avant une éventuelle soumission. Les contrôles ne sont pas des actions de distribution.

**⚠️ Pré-requis bloquant — avant toute mise en avant**
- Vérifier que **openclaw-france.fr sert bien la version gratuite**. Au 30/09/2026 ~18 h (CEST), la production servait encore l'ancienne version : `/gratuit/`, `/openclaw/`, `/hermes/` répondaient **404**. Contrôle rapide : `curl -sIL https://openclaw-france.fr/openclaw/` (200 attendu) et vérifier la page d'accueil.
- Liens publics à utiliser partout : site `https://openclaw-france.fr` · média `https://communaute-ia.fr` · dépôt `https://github.com/mael-ctrl/openclaw-france-communaute`. Contact : `crabe@blockos.fr`.

**Règles d'or (anti-spam) — valables partout**
1. **Toujours se déclarer** : « nous portons openclaw-france.fr, tout est gratuit, le projet est ouvert » — jamais de faux compte, faux avis, faux votes.
2. **Lire les règles locales avant de poster** ; poster **une fois**, au bon endroit ; répondre aux retours (ne pas répondre = spam).
3. **Pas de rafales ni de cross-post brut** : adapter le texte à chaque communauté (langue, format, angle, ton).
4. **Jamais de sollicitation artificielle** : pas de demande d'upvotes, pas de mentions ou placements achetés.
5. **Transparence IA** : dire que le média est opéré par une IA — c'est l'angle du projet, pas une faiblesse à cacher.

---

## 1. Synthèse — 20 destinations

| # | Destination | Catégorie | Priorité | Risque | Mode de soumission |
|---|---|---|---|---|---|
| 1 | LinuxFr.org | Forum FR libre | Haute | Moyen | Dépêche ou journal (compte, modération a priori) |
| 2 | Journal du Hacker | Agrégateur FR | Haute | Faible–Moyen | Lien soumis (compte par invitation) |
| 3 | Lemmy — jlai.lu | Fédivers FR | Moyenne | Faible | Post natif (compte) |
| 4 | Discords IA francophones | Communautés | Moyenne | Moyen | Rejoindre puis salon dédié |
| 5 | Framalibre | Annuaire du libre | Basse | Moyen | Notice (compte, guides officiels) |
| 6 | Uneed | Plateforme de lancement | Haute | Faible | Formulaire (sans compte au départ) |
| 7 | Microlaunch | Plateforme de lancement | Moyenne | Faible–Moyen | Formulaire (compte) |
| 8 | Product Hunt | Plateforme de lancement | Moyenne–Haute | Moyen | Lancement « maker » (jour J préparé) |
| 9 | AIxploria | Annuaire IA (FR) | Moyenne | Faible | Formulaire de soumission |
| 10 | Futurepedia | Annuaire IA (EN) | Basse–Moyenne | Moyen | Formulaire (conditions à vérifier) |
| 11 | awesome-selfhosted | awesome-list GitHub | Haute* | Moyen | Pull request (repo de données) |
| 12 | e2b-dev/awesome-ai-agents | awesome-list GitHub | Moyenne | Faible–Moyen | PR ou formulaire |
| 13 | r/selfhosted | Reddit | Moyenne–Haute | Moyen | Post texte (règles strictes) |
| 14 | r/LocalLLaMA | Reddit | Moyenne | Moyen–Élevé | Post de contribution |
| 15 | r/SideProject | Reddit | Moyenne | Faible–Moyen | Post de projet |
| 16 | r/france | Reddit FR | Basse | Élevé | ⚠️ promo directe à éviter |
| 17 | r/developpeurs | Reddit FR | Basse | Élevé | ⚠️ règles à revérifier sur place |
| 18 | Ben's Bites (+ News) | Newsletter IA | Moyenne | Faible | Compte sur la plateforme News |
| 19 | Hacker Newsletter | Digest | Basse | Faible | Indirect (reprise depuis HN) |
| 20 | Hacker News — Show HN | Hacker News | Moyenne | Élevé | « Show HN: … » |

*\* Haute si le logiciel est éligible (voir fiche 11 — condition de release).*

---

## 2. Fiches détaillées

### A. Communautés et forums francophones

#### 1. LinuxFr.org
- **URL** : https://linuxfr.org (règles : https://linuxfr.org/regles_de_moderation)
- **Mode de soumission** : créer un compte, puis **proposer une dépêche** (passage en modération *a priori* par l'équipe). Pour un retour d'expérience moins « actualité », préférer un **journal** (espace personnel) — plus souple.
- **Prérequis** : compte ; texte **rédigé en français** (une dépêche « non rédigée » est rejetée) ; sujet lié au libre — OpenClaw et Hermes Agent sont open source, les kits FR sont un contenu libre.
- **Règles anti-spam** : pas de répétition d'un même sujet de dépêche ; pas de publicité déguisée ; la ligne éditoriale attend une actualité ou un contenu, pas un slogan.
- **Risque** : **Moyen** — une dépêche perçue comme promotionnelle est régulièrement rejetée ; le journal passe mieux.
- **Priorité** : **Haute** — l'audience FR « logiciel libre / auto-hébergement » est exactement la cible.

#### 2. Journal du Hacker
- **URL** : https://www.journalduhacker.net (invitation : https://www.journalduhacker.net/invitations/request)
- **Mode de soumission** : une fois le compte obtenu, **soumettre un lien** (vote communautaire, esprit HN/Lobsters).
- **Prérequis** : **compte sur invitation** — soit par un utilisateur existant, soit via la demande publique (e-mail valide à confirmer, et une **URL de vérification** type site personnel ou compte GitHub ; la demande est visible des modérateurs).
- **Règles anti-spam** : contenu **en français**, utile à la communauté libre/tech ; l'auto-soumission pertinente est tolérée, le matraquage marketing non.
- **Risque** : **Faible–Moyen**.
- **Priorité** : **Haute** — audience dev FR qualifiée, et le projet « fait maison » y est bien reçu.

#### 3. Lemmy — jlai.lu (fédivers FR)
- **URL** : https://jlai.lu — communautés vérifiées : `c/france`, `c/technologie`, `c/libre`, `c/interessant`.
- **Mode de soumission** : créer un compte sur jlai.lu (ou une autre instance fédérée), **poster un contenu natif** dans la communauté adéquate (`c/technologie` pour les kits, `c/libre` pour l'angle open source).
- **Prérequis** : compte ; respecter les règles de l'instance (page « Règles » de jlai.lu — à relire) et le sujet de chaque communauté.
- **Règles anti-spam** : pas de multi-posts ni de spam inter-instances ; participer (commenter) plutôt que déballer sa promotion.
- **Risque** : **Faible**.
- **Priorité** : **Moyenne** — petite mais très francophone, culture libre.

#### 4. Discords IA francophones (via l'annuaire Disboard)
- **URL** : https://disboard.org/fr/servers/tag/intelligence-artificielle (exemple repéré : « Olympe Groupe », entrepreneuriat × IA × automatisation)
- **Mode de soumission** : rejoindre un ou deux serveurs, se présenter, puis poster dans le salon prévu (`#projets`, `#partage`, `#veille` selon le serveur).
- **Prérequis** : compte Discord ; lire les règles du serveur (questionnaire d'entrée fréquent) ; viser des serveurs dont l'objet inclut projets/partage.
- **Règles anti-spam** : jamais de DM non sollicités ; un seul post, au bon endroit ; certains serveurs réservent la promo à un salon ou un jour précis — s'y tenir.
- **Risque** : **Moyen** — règles variables d'un serveur à l'autre ; la promo brutale y est souvent bannie (c'est leur droit).
- **Priorité** : **Moyenne**.

#### 5. Framalibre
- **URL** : https://framalibre.org (guide officiel : https://participer.framasoft.org/fr/framalibre/creer-modifier-une-notice.html)
- **Mode de soumission** : créer/compléter une **notice** (fiche) dans l'annuaire, via un compte.
- **Prérequis** : c'est un annuaire **de logiciels libres** — la fiche doit porter sur le logiciel lui-même (OpenClaw / Hermes Agent), pas sur le site ni sur les kits. Vérifier que le logiciel n'y est pas déjà et que la fiche est légitime (pas un détournement marketing).
- **Règles anti-spam** : fiches factuelles et maintenues ; c'est un annuaire, pas un canal de communication.
- **Risque** : **Moyen** — fiche supprimée si perçue comme vitrine.
- **Priorité** : **Basse** — utile pour la visibilité « libre » de long terme.

### B. Plateformes de lancement

#### 6. Uneed
- **URL** : https://www.uneed.best (soumission : https://www.uneed.best/submit-a-tool — « no account needed to start »)
- **Mode de soumission** : soumettre le produit (la plateforme récupère d'abord les données de la page, le compte est demandé pour enregistrer) ; classements jour/semaine + reprise dans leur newsletter pour les premiers.
- **Prérequis** : page produit claire (openclaw-france.fr) et description soignée.
- **Règles anti-spam** : plateforme revendiquée « anti-triche » (votes vérifiés, produits frauduleux retirés) — ne pas tenter de votes artificiels, c'est contre-productif.
- **Risque** : **Faible**.
- **Priorité** : **Haute** — soumission simple, audience early adopters et francophone.

#### 7. Microlaunch
- **URL** : https://microlaunch.net (soumission : https://microlaunch.net/submit)
- **Mode de soumission** : soumettre le produit ; lancement + retours sur 30 jours ; re-lancements réservés aux vraies nouveautés.
- **Prérequis** : compte + fiche produit honnête ; des options premium existent (facultatives).
- **Règles anti-spam** : accueillir les retours sans filtrage ; pas de faux comptes pour gonfler le feedback.
- **Risque** : **Faible–Moyen**.
- **Priorité** : **Moyenne** — complémentaire d'Uneed.

#### 8. Product Hunt
- **URL** : https://www.producthunt.com/launch (guide : https://www.producthunt.com/launch/how-product-hunt-works)
- **Mode de soumission** : **lancer en tant que maker** — compte, fiche produit, visuels ; viser un jour de semaine et préparer sa communauté à l'avance.
- **Prérequis** : produit **utilisable immédiatement** (c'est le cas : téléchargement direct, sans compte) ; maker identifiable ; pas de bêta fermée.
- **Règles anti-spam** : solliciter ou acheter des upvotes est interdit et sanctionné (produit retiré) ; un seul lancement par produit, sauf évolution majeure.
- **Risque** : **Moyen** — sans mobilisation réelle le jour J, le lancement se noie.
- **Priorité** : **Moyenne–Haute** — fort levier si un vrai jour J est organisé.

### C. Annuaires d'outils IA

#### 9. AIxploria
- **URL** : https://www.aixploria.com/en/submit-ai-tool-or-feature-company/ (version FR : `/fr/submit-ai-tool-or-feature-company/`)
- **Mode de soumission** : **formulaire de soumission** d'un outil IA ; sélection annoncée comme « vérifiée manuellement », mise à jour quotidienne.
- **Prérequis** : outil IA réel et utile (les kits d'installation pour agents entrent dans leur champ) ; description soignée.
- **Règles anti-spam** : vérification manuelle — soumettre une fois, proprement ; pas de resoumission en boucle.
- **Risque** : **Faible**.
- **Priorité** : **Moyenne** — annuaire FR d'outils IA, bien référencé.

#### 10. Futurepedia
- **URL** : https://futurepedia.io/submit-tool
- **Mode de soumission** : formulaire de soumission, sous validation éditoriale ; la page mentionne des options de listing avec conditions — **vérifier les conditions en vigueur avant de soumettre** et ne rien engager sans arbitrage.
- **Prérequis** : produit IA avec page propre.
- **Règles anti-spam** : validation éditoriale ; refus possible si le produit ne correspond pas à leur audience.
- **Risque** : **Moyen**.
- **Priorité** : **Basse–Moyenne** — à traiter seulement si l'accès standard est compatible.

### D. awesome-lists GitHub

#### 11. awesome-selfhosted
- **URL** : https://github.com/awesome-selfhosted/awesome-selfhosted (contributions : https://github.com/awesome-selfhosted/awesome-selfhosted-data — guide `CONTRIBUTING.md`)
- **Mode de soumission** : **pull request** ajoutant `software/<nom>.yml` (template fourni) — ou issue si la PR est inconfortable.
- **Prérequis** : logiciel **libre**, **auto-hébergeable**, **activement maintenu** ; la checklist de PR exige une **première release datant d'au moins ~4 mois** ; vérifier d'abord que le logiciel n'est pas déjà listé, puis choisir la bonne catégorie/tags.
- **Règles anti-spam** : template strict (kebab-case, message de commit descriptif) ; une entrée par projet ; aucune PR « site vitrine » — uniquement des logiciels.
- **Risque** : **Moyen** — rejet si un critère manque (c'est la règle du jeu, sans rancune).
- **Priorité** : **Haute si éligible** — trafic dev durable et international.

#### 12. e2b-dev/awesome-ai-agents
- **URL** : https://github.com/e2b-dev/awesome-ai-agents
- **Mode de soumission** : **PR** (ordre alphabétique, bonne catégorie) ou formulaire (lien « Submit new product here » dans le README).
- **Prérequis** : présenter l'agent/l'outil avec son lien ; suivre exactement les instructions du README.
- **Règles anti-spam** : respecter ordre et catégorie ; une seule entrée.
- **Risque** : **Faible–Moyen**.
- **Priorité** : **Moyenne**.

### E. Reddit

#### 13. r/selfhosted
- **URL** : https://www.reddit.com/r/selfhosted/ (règles lues : https://www.reddit.com/r/selfhosted/wiki/rules)
- **Mode de soumission** : **post texte** (pas de lien direct en titre) ; si contenu de blog, le lien va **dans le corps** du post ; flair adapté.
- **Prérequis** : compte Reddit avec un minimum d'historique (les comptes neufs sont filtrés) ; rester dans le sujet : le **self-hosting** — OpenClaw sur son VPS est pertinent ; pour Hermes, tenir l'angle « chez soi / auto-hébergé ».
- **Règles anti-spam** : respecter les *Reddit self-promotion guidelines* (surveillées même si secondaires) ; pas de shill/publicité non sollicitée ; « Minimum effort » ; un contenu de blog ne passe qu'avec le lien dans le corps ; les modérateurs ont le dernier mot (ban possible en récidive).
- **Risque** : **Moyen**.
- **Priorité** : **Moyenne–Haute**.

#### 14. r/LocalLLaMA
- **URL** : https://www.reddit.com/r/LocalLLaMA/
- **Mode de soumission** : **participer d'abord**, puis poster un partage (agents, outils locaux) — format technique, détaillé, honnête.
- **Prérequis** : compte établi ; les règles complètes ne sont lisibles qu'une fois connecté — **les relire avant de poster**. Résumés publics au 30/09 : participation type « 9:1 » (1 contenu personnel pour 9 contributions) et auto-promo « tolérée mais surveillée ».
- **Règles anti-spam** : pas de « lancement » sec ; apporter du contenu utilisable (retour d'installation, comparatif OpenClaw / Hermes Agent) et répondre aux commentaires.
- **Risque** : **Moyen–Élevé** — audience allergique au marketing.
- **Priorité** : **Moyenne**.

#### 15. r/SideProject
- **URL** : https://www.reddit.com/r/SideProject/
- **Mode de soumission** : **post de partage de projet** — le sub est fait pour ça ; raconter le pourquoi, pas seulement le lien.
- **Prérequis** : compte ; règles simples (pas de spam, contexte et transparence attendus — à relire).
- **Règles anti-spam** : pas de promotion répétée ; répondre aux retours.
- **Risque** : **Faible–Moyen**.
- **Priorité** : **Moyenne**.

#### 16. r/france — ⚠️ à ne pas forcer
- **URL** : https://www.reddit.com/r/france/
- **Mode de soumission** : participation dans les fils existants uniquement en premier lieu ; la **promotion directe y est à très haut risque** (auto-promo encadrée, modération stricte, filtres anti-comptes jeunes ; règles complètes lisibles seulement connecté au 30/09).
- **Prérequis** : compte ancien avec karma significatif.
- **Règles anti-spam** : considérer la promo directe comme **proscrite** ; jamais de lien nu.
- **Risque** : **Élevé** — retrait quasi systématique, voire ban.
- **Priorité** : **Basse** — n'y compter que par une participation utile en commentaire (fils sur l'IA locale, le libre, les VPS).

#### 17. r/developpeurs (FR)
- **URL** : https://www.reddit.com/r/developpeurs/ (existence vérifiée le 30/09/2026)
- **Mode de soumission** : participer, puis poster un contenu utile au dev francophone ; présenter le projet comme un cas (open source, kits FR), pas comme une annonce.
- **Prérequis** : compte avec historique ; règles à relire sur place (non consultables hors compte au 30/09).
- **Règles anti-spam** : textes natifs, pas de liens nus ; répondre ; pas de récurrence.
- **Risque** : **Élevé** — petite communauté, la promo directe y est malvenue.
- **Priorité** : **Basse**.

### F. Newsletters et digests

#### 18. Ben's Bites (plateforme « Ben's Bites News »)
- **URL** : https://bensbites.co — plateforme communautaire : https://news.bensbites.co
- **Mode de soumission** : créer un compte sur **Ben's Bites News** et y soumettre ses posts ; les meilleurs posts (et choix de la rédaction) sont repris dans les digests e-mail.
- **Prérequis** : compte ; actualité produit/IA notable — les kits gratuits sont une news produit légitime.
- **Règles anti-spam** : sélection communautaire + éditoriale ; pas de sollicitation de mentions ; poster une fois avec du contexte.
- **Risque** : **Faible** — au pire, ignoré.
- **Priorité** : **Moyenne** — audience early adopters anglophone, bon fit « agents + gratuit ».

#### 19. Hacker Newsletter
- **URL** : https://hackernewsletter.com/
- **Mode de soumission** : **indirect uniquement** — la sélection est faite à la main **depuis Hacker News** ; pas de canal de soumission direct.
- **Prérequis** : un Show HN qui performe (cf. fiche 20).
- **Règles anti-spam** : rien à solliciter — ne pas contacter pour « faire passer » ; c'est un bonus, pas un canal.
- **Risque** : **Faible**.
- **Priorité** : **Basse** — effet secondaire d'un bon HN.

### G. Hacker News

#### 20. Hacker News — Show HN
- **URL** : https://news.ycombinator.com/showhn.html (règles générales : https://news.ycombinator.com/newsguidelines.html)
- **Mode de soumission** : soumettre un lien dont le titre commence par « **Show HN:** » — quelque chose que les gens peuvent **essayer tout de suite** (ici : les kits à télécharger). Poster un mardi–jeudi matin (heure US) et **rester dans le fil** pour répondre.
- **Prérequis** (règles lues) : le projet doit être « quelque chose qu'on peut faire tourner sur son ordinateur » (✓) ; **pas de mur d'inscription** pour essayer (✓) ; projet non trivial, présenté par quelqu'un qui y a travaillé et qui est là pour discuter.
- **Règles anti-spam** : « Please don't ask friends to upvote or comment » (interdit explicite) ; pas de landing page ni de page de dons à la place d'un essai ; pas de repostage en boucle — un seul shot, soigné. En anglais, ton factuel, zéro superlatif.
- **Risque** : **Élevé** — audience exigeante, le titre et le timing font tout.
- **Priorité** : **Moyenne** — le plus fort levier du lot si bien exécuté.

---

## 3. Écartés (et pourquoi)

- **There's An AI For That** — soumission à conditions commerciales → écarté en l'état (aucune dépense engagée sans arbitrage).
- **Fermes de liens, annuaires automatiques de backlinks, votes ou mentions achetés** — **jamais** : nocif pour le projet, son histoire de transparence et son référencement.
- **Wikipédia** — critères de notoriété non remplis à ce stade (à reconsidérer si la presse couvre le projet).
- **Cross-posts bruts et DM de masse** — bannis partout ; contre-productifs même quand ils passent.

## 4. Déjà couvert — ne pas dupliquer

- **Mastodon / Fédivers** → `docs/distribution-mastodon.md` (candidature piaille.fr, plans B/C).
- **Presse** → `docs/press/campagne-1.json` (envoyée le 30/09) + `docs/press/campagne-2.json` (bascule vers le gratuit) + relances.
- **Bluesky** → compte `@communaute-ia.fr` en place (diffusion automatique des brèves).
- **SEO / GEO** → `docs/geo-playbook.md` (llms.txt, JSON-LD, IndexNow, archives).

## 5. Ordre recommandé (7 à 10 jours)

1. **J0 — contrôle bloquant** : openclaw-france.fr sert bien la version gratuite (accueil + `/openclaw/` + `/hermes/` en 200).
2. **J0–J1** — Journal du Hacker (demande d'invitation en amont) + jlai.lu + 1–2 Discords (se présenter avant de poster).
3. **J1–J2** — PR awesome-selfhosted / awesome-ai-agents (besoin d'un compte GitHub de l'équipe).
4. **J2–J3** — Uneed, puis Microlaunch.
5. **J3** — AIxploria (+ Futurepedia seulement si conditions compatibles).
6. **J4–J5** — Reddit : r/selfhosted → r/SideProject → (r/LocalLLaMA, en partage technique).
7. **Semaine 2** — Show HN (mardi–jeudi, matin US) ; Product Hunt ensuite, avec mobilisation ; Ben's Bites News en continu.
8. **Rythme** : jamais plus d'une action par plateforme par semaine ; toute réaction négative ou tout retrait = on s'arrête sur cette plateforme, sans discuter.

## 6. Interdits absolus

Faux comptes ou comptes multiples · votes/mentions/backlinks achetés ou sollicités · demande d'upvotes à l'entourage · DM non sollicités · rafales et cross-posts bruts · dissimulation de la nature du projet (équipe + IA derrière le média) · promesses non vérifiables.

---

*Fichier interne — OpenClaw France / La Communauté 🦀. Préparé le 30/09/2026 ; mandat autonome actualisé le 03/10/2026. **Une action par jour maximum, une par plateforme et par semaine ; règles locales et déclaration IA obligatoires.***
