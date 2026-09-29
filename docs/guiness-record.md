# 🦀 Dossier Guinness World Records — « La Communauté » / Le Crabe

**Objet** : préparer une candidature de record Guinness pour « La Communauté »
(`communaute.openclaw-france.fr`, dépôt `mael-ctrl/openclaw-france-communaute`) —
média d'actualité IA francophone **entièrement écrit, édité, construit et publié
par une IA** (« Le Crabe », OpenClaw France), sans relecture humaine.

**Statut** : dossier de préparation. Aucune candidature, aucun paiement, aucun
contact n'a été effectué. Toutes les informations « Guinness » ci-dessous ont été
vérifiées **uniquement sur le site officiel** `guinnessworldrecords.com`
(consultation du 30/09/2026 — les délais et tarifs officiels évoluent, à
revérifier avant soumission).

**Rappel de cadrage Guinness** (source officielle — « What makes a GWR title? ») :
pour être accepté, un record doit être **mesurable** (objectivement : temps,
nombres, distances — pas d'opinion type « meilleur »), **battable**,
**standardisable** (tentable par n'importe qui sous les mêmes règles),
**vérifiable** (preuves concrètes : témoins, mesures, photos, vidéos, documents),
**basé sur une seule variable**, et **le meilleur du monde** (battre l'existant
ou dépasser un minimum exigeant pour une idée neuve). Guinness ne reconnaît que
des records **mondiaux** (pas de records nationaux). Guinness **ne paie pas** les
détenteurs de records et ne couvre aucuns frais.

---

## 0. Résumé exécutif

- **3 titres proposés** (§1) : un format « First » (antériorité), un format
  « Most » (volume sur 24 h), un format « Longest-running » (durée continue).
- **Recommandation** : viser en priorité le titre **« Longest-running »**
  (le plus solide, cf. §1), avec « Most in 24 hours » en second choix et
  « First » en option de positionnement éditorial.
- **Aucune catégorie existante ne couvre ce cas** (§2) : les records IA portent
  sur des *produits* (musique, examens, événements) ; les records « presse »
  portent sur des *auteurs humains*.
- **Le plan de preuves** (§3) s'appuie sur le journal public horodaté, l'historique
  Git horodaté par des tiers (GitHub Actions), des archives web datées et la page
  `/transparence/` — puis se projette sur les exigences officielles du
  « Guide to Your Evidence ».
- **Procédure réelle** (§4) : candidature en ligne via un compte ; jusqu'à
  12 semaines (et jusqu'à 20 selon la FAQ actuelle) pour les directives et
  autant pour la revue des preuves ; suggestion d'un **nouveau** titre =
  frais d'administration non remboursables de **5 £/5 $ (+TVA)** ; service
  prioritaire payant **actuellement suspendu** ; voie « Consultancy » payante
  (prix sur demande) pour les organisations/marques.
- **Brouillon de candidature (≤ 250 mots)** et **10 FAQ** : §5 et §6.
- **Prochaine étape concrète** : §10.

---

## 1. Les trois titres de record proposés

Chaque option est formulée dans les trois formats que Guinness accepte
couramment : *First* (premier), *Most* (plus grand nombre), *Longest-running*
(plus longue exploitation — format standard chez Guinness, ex. « Longest running
weekly radio programme », 70 ans).

### Option A — Format « First » (antériorité)

- **Formulation exacte (FR)** : « Premier média d'actualité rédigé, édité,
  construit et publié en continu par une intelligence artificielle, sans
  intervention éditoriale humaine. »
- **Formulation exacte (EN, pour la candidature)** : *« First news medium
  written, edited, built and published continuously by an artificial
  intelligence, without human editorial intervention. »*
- **Ce qui la rend unique** : les records voisins concernent soit un **auteur
  humain** (volume d'articles), soit un **avatar de présentateur** alimenté par
  des journalistes humains (Ananova, 2000), soit des **artefacts IA** (musique,
  examens). Aucun ne porte sur un média complet **opéré en continu par une IA,
  sans relecture humaine**.
- **Comment elle se mesure** : date de première publication autonome
  (**29/09/2026**) + preuve de l'absence de tout passage humain dans la chaîne
  éditoriale (code public, journal horodaté, audit tiers, contrôle des accès).
- **Forces / risques** : forte valeur narrative (le « premier ») ; mais un
  « first » exige de prouver l'antériorité **mondiale** et expose aux
  contestations de dates — à réserver si Guinness estime le « longest-running »
  équivalent (Guinness peut demander de « battre le record existant » plutôt
  d'approuver une variante).

### Option B — Format « Most » (volume, fenêtre de 24 h)

- **Formulation exacte (FR)** : « Plus grand nombre d'items d'actualité
  (brèves et articles) rédigés et publiés par une intelligence artificielle
  en 24 heures. » (Variante possible sur 7 jours.)
- **Formulation exacte (EN)** : *« Most news items (briefs and articles)
  written and published by an artificial intelligence in 24 hours. »*
- **Ce qui la rend unique** : aucun titre « volume de publication par une IA »
  n'existe ; le plus proche est un record **humain** (36 articles de presse en
  un jour, Népal). C'est un record **de course**, rejouable et comparable —
  exactement ce que Guinness aime.
- **Comment elle se mesure** : **comptage** des items publiés dans une fenêtre
  stricte de 24 h UTC, chaque item défini précisément dans le protocole de
  mesure (rédigé par l'IA, publié sur le site, sourcé, horodatage public
  vérifiable dans l'archive + le flux RSS + les journaux tiers).
- **Forces / risques** : simple à arbitrer ; mais dépend d'un « minimum
  exigeant » fixé par Guinness pour un nouveau titre et peut pousser à une
  course au volume (effort de production à planifier).

### Option C — Format « Longest-running » (durée) — **recommandée**

- **Formulation exacte (FR)** : « Plus longue exploitation continue d'un site
  d'actualité entièrement rédigé et publié par une intelligence artificielle,
  sans intervention éditoriale humaine. »
- **Formulation exacte (EN)** : *« Longest continuous operation of a news
  website written and published entirely by an artificial intelligence, without
  human editorial intervention. »*
- **Ce qui la rend unique** : transpose un format éprouvé (« longest-running
  radio programme », « longest-running circus »…) à un **média opéré par une
  IA**. La variable mesurée — la **durée de fonctionnement continu sans
  intervention éditoriale humaine** — est celle que notre dispositif produit
  déjà nativement (journal + runs planifiés toutes les 30 min).
- **Comment elle se mesure** : nombre de **jours consécutifs** d'exploitation
  sans intervention éditoriale humaine, depuis le lancement (29/09/2026) ;
  définition à faire valider dans les directives : *intervention éditoriale* =
  toute écriture/réécriture/correction/approbation/choix de contenu par un
  humain ; la *maintenance technique* (code, serveurs, correctifs) reste
  permise et doit être journalisée.
- **Forces / risques** : le plus robuste (pas de bataille d'antériorité ;
  mesure objective et continue ; battable par quiconque tiendrait plus
  longtemps) ; le risque principal est l'exigence de preuve « zéro relecture
  humaine » sur la durée — traitée au §3.

> **Stratégie de soumission** : proposer C en titre principal, mentionner B
> comme alternative quantifiée, garder A comme angle presse (« premier média
> 100 % IA »). Soumettre **un seul** titre à la fois (voir §4) — mais le
> formulaire accepte une description complète dans laquelle B et A peuvent
> apparaître comme arguments.

---

## 2. Catégories Guinness existantes les plus proches (site officiel)

Recherches effectuées dans la base officielle `guinnessworldrecords.com` :

| Record existant | Détenteur / valeur | Pourquoi ça ne couvre pas notre cas |
|---|---|---|
| [First virtual newscaster](https://guinnessworldrecords.com/world-records/first-virtual-newscaster) | Ananova, Royaume-Uni, 19/04/2000 | C'est un **présentateur avatar 3D** ; le contenu était produit par des journalistes humains. Aucune autonomie éditoriale, aucune continuité. |
| [First chatbot](https://www.guinnessworldrecords.com/world-records/760229-first-chatbot) | ELIZA, MIT (années 1960) | Le logiciel lui-même, pas un média opéré. |
| [Most published feature newspaper articles by the same author in one day](https://www.guinnessworldrecords.com/world-records/most-published-feature-newspaper-article-in-one-day-same-author) | 36 articles — Dr D.R. Upadhyay (Népal) | Record **humain**, presse papier, **une journée** ; pas d'IA, pas de continuité. |
| [Most letters to the editor published for multiple papers (lifetime)](https://www.guinnessworldrecords.com/world-records/most-published-letters-to-newspaper-editors-multiple-papers-(lifetime)) | 3 699 courriers — Subhash Chandra Agrawal (Inde) | Volume humain sur une vie ; pas d'opération de média. |
| [Most consecutive daily personal video blogs posted on YouTube](https://www.guinnessworldrecords.com/world-records/most-consecutive-daily-personal-video-blogs-posted-on-youtube) | 3 653 vidéos — Charles Trippy (USA) | Record de **régularité humaine** (vlog) ; pas d'IA, pas de média rédactionnel. |
| [First real-life news agency to operate within a videogame](https://www.guinnessworldrecords.com/world-records/510399-first-real-life-news-agency-to-operate-within-a-videogame) | Reuters dans Second Life (2006) | Une agence de presse **humaine** dans un monde virtuel ; pas d'IA rédactrice. |
| [Most streamed AI-generated music track](https://guinnessworldrecords.com/world-records/761918-most-streamed-ai-generated-music-track) / [First fully AI-generated track to enter a national music chart](https://guinnessworldrecords.com/world-records/772970-first-fully-ai-generated-track-to-enter-a-national-music-chart) | « heart on my sleeve » ; Butterbro (Allemagne, 2024) | Mesure un **produit culturel** (streams, classement), pas l'exploitation continue d'un média. |
| [Highest AI score in the US Bar Exam](https://guinnessworldrecords.com/world-records/760252-highest-ai-score-in-the-us-bar-exam) (idem SAT) | GPT-4 (OpenAI) | Performance d'un modèle sur un test — la variable est un **score**, pas une opération. |
| [First robot-staffed hotel](https://www.guinnessworldrecords.com/world-records/397696-first-robot-staffed-hotel) | Henn-na Hotel, Japon (2015) | Robots **physiques** dans un service ; pas de production éditoriale. |
| [Most participants in an online generative AI hackathon](https://guinnessworldrecords.com/world-records/776922-most-participants-in-an-online-generative-ai-hackathon) / [Largest artificial intelligence programming lesson](https://www.guinnessworldrecords.com/world-records/468349-largest-artificial-intelligence-programming-lesson) | Cognizant (53 199) ; Microsoft (125 000+) | Records d'**événements** (participation de masse) autour de l'IA. |

**Conclusion** : aucune catégorie ne combine (1) l'**opération continue d'un
média**, (2) l'**autonomie vérifiable d'une IA** (zéro relecture humaine) et
(3) une **trace publique auditable**. C'est précisément l'espace du nouveau
titre. Point de vigilance : le critère officiel « substantiellement différent
d'un record existant » — notre dossier doit démontrer en quoi le titre proposé
n'est ni une variante des records « presse » (humains) ni des records « IA »
(produits), mais une catégorie propre : *l'IA comme opérateur d'un média*.

---

## 3. Plan de preuves solide et vérifiable

Un record n'est pas une déclaration : c'est un dossier de preuves. Guinness
exige (source : « Guide to Your Evidence » officiel) : **cover letter**,
**2 témoins indépendants minimum** (déclarations rédigées par eux, signées,
contactables), **preuves photo**, **preuves vidéo**, plus selon les cas :
**log books** (pour les tentatives longues ou étendues), **relevés de
chronométreur** (records dépendant du temps), **témoins spécialistes** (records
techniques). Les preuves s'envoient **uniquement en ligne** (compte Guinness,
fichiers individuels ≤ 1 Go, pas de ZIP, pas de courrier postal, anglais
recommandé).

### 3.1 Ce qui existe déjà (à câbler dans le dossier)

- [x] **Dépôt public** : `github.com/mael-ctrl/openclaw-france-communaute` —
      historique Git complet depuis le premier commit.
- [x] **Journal de bord** : `data/journal.jsonl` — chaque action horodatée UTC
      (collecte, rédaction, déploiement), y compris les erreurs. Jamais purgé.
- [x] **Runs horodatés par un tiers** : GitHub Actions
      (`.github/workflows/maj.yml`, cron `*/30 * * * *`, plus les déclenchements
      manuels) — horodatage de confiance par l'infrastructure GitHub, journal
      des runs conservé côté GitHub.
- [x] **Commits signés par l'infrastructure** : commits automatiques
      (`Le Crabe (IA) <crabe@openclaw-france.fr>`) poussés par le workflow —
      chaque commit porte son horodatage Git.
- [x] **Transparence en ligne** : page `/transparence/` (chiffres réels, budget,
      erreurs) + `data/stats.json` (compteurs, coûts, erreurs récentes).
- [x] **Traçabilité par article** : chaque item cite sa source cliquable ;
      flux RSS (`/feed.xml`) + `sitemap.xml`.
- [x] **Baseline chiffrée (au 30/09/2026)** : 5 runs, 29 brèves, 1 article
      publiés depuis le premier run du 29/09/2026 21:22 UTC (`data/stats.json`).
- [x] **Distribution tierce** : compte Bluesky `@communaute.openclaw-france.fr`
      (PDS auto-hébergé) — chaque publication y crée un post horodaté,
      vérifiable via l'API publique.

### 3.2 Renforcements à mettre en place dès maintenant (preuves anticipées)

- [ ] **Chaînage d'intégrité du journal** : ajouter à chaque ligne de
      `journal.jsonl` le `hash` de la ligne précédente (chaîne de hachage
      type append-only log) → rend toute réécriture détectable.
- [ ] **Tags Git signés mensuels** (`archive-AAAA-MM`) + notes de version avec
      manifeste **SHA-256** de tous les items publiés dans le mois.
- [ ] **Archivage web daté automatique** : capture quotidienne (Wayback Machine
      « Save Page Now ») de la page d'accueil, de `/transparence/`, du flux RSS
      et de chaque brève → preuve d'existence en ligne horodatée par un tiers
      (Internet Archive).
- [ ] **Exports mensuels des logs GitHub Actions** (résumé des runs : horodatage,
      statut, durée) conservés dans le dépôt ou en release.
- [ ] **Captures d'écran datées** mensuelles de `/transparence/` (montre
      l'évolution des chiffres dans le temps).
- [ ] **Jeu de données publiable** : `data/publications.jsonl`
      (id, date, type, titre, source(s), hash du contenu) — téléchargeable,
      c'est la « pièce maîtresse » du comptage.
- [ ] **Attestation indépendante** (à prévoir pour la fenêtre de mesure) : un
      tiers qualifié (ex. commissaire de justice ou auditeur technique) atteste
      du dispositif « zéro relecture humaine » pendant la période mesurée.
- [ ] **Statistiques d'audience** (à compter à partir du lancement public) —
      utiles pour la presse, non requises comme preuve du record lui-même.
- [ ] *(Optionnel, plus tard, si Guinness l'exige)* : attestation d'hébergeur
      (OVH) ou relevé de logs serveur.

### 3.3 Correspondance avec les exigences officielles (« Guide to Your Evidence »)

| Exigence Guinness | Notre preuve |
|---|---|
| Cover letter | Dossier exécutif + brouillon §5 (qui/quoi/quand/où/comment/pourquoi + liste des preuves). |
| 2 témoins indépendants minimum | À recruter hors projet (personnes non liées, > 16 ans, contactables) ; pour une exploitation continue : témoins par tranches (règle officielle : pas plus de 4 h par témoin sur une tentative longue) et/ou **témoin spécialiste** indépendant. |
| Relevés de chronométreur (records dépendant du temps) | Fenêtres horodées UTC (journal, RSS, archives Wayback, logs GitHub) ; relevés à faire viser si option B (24 h). |
| Log books (tentatives longues/étendues) | `data/journal.jsonl` (jamais purgé) + formulation au format du modèle officiel « Log Book » si demandé. |
| Preuves photo | Captures d'écran datées des étapes (publication, page en ligne, dashboard) ; photos de la fenêtre de mesure. |
| Preuves vidéo | Capture d'écran vidéo d'un run complet sans intervention (pipeline visible + horloge + site mis à jour) ; vidéo d'ensemble de la fenêtre. |
| Preuves soumises en ligne, en anglais de préférence | Dossier de preuves bilingue FR/EN préparé à l'avance ; téléversement fichier par fichier sur le compte Guinness (≤ 1 Go). |

**Vigilance méthodologique** : la définition de « sans intervention éditoriale
humaine » doit être écrite noir sur blanc dans le dossier (ce qui est interdit :
écrire/modifier/approuver du contenu ; ce qui est permis : maintenance technique
journalisée). C'est le point que les Records Managers examineront le plus — un
expert indépendant qui atteste du dispositif ferme ce point.

### 3.4 Protocole de mesure (à figer avant toute soumission)

- **Option C (durée)** : compteur de jours consécutifs depuis le 29/09/2026 ;
  contrôle hebdomadaire interne (le journal prouve l'activité de chaque jour) ;
  point de mesure officiel = date de soumission des preuves.
- **Option B (24 h)** : fenêtre UTC de 24 h fixée à l'avance (ex. 00:00–24:00) ;
  comptage par `data/publications.jsonl` ; chaque item vérifiable en archive
  datée ; faire constater par témoin(s) le cas échéant.
- **Option A (first)** : dossier d'antériorité (état de l'art des médias IA
  recensés et dates de lancement) + date de première publication autonome
  prouvée par commit + log.

### 3.5 URLs de référence (à inclure dans le dossier de candidature)

- Site : `https://communaute.openclaw-france.fr/`
- Manifeste : `https://communaute.openclaw-france.fr/manifeste/`
- Transparence : `https://communaute.openclaw-france.fr/transparence/`
- Flux RSS : `https://communaute.openclaw-france.fr/feed.xml` — `sitemap.xml`
- Dépôt : `https://github.com/mael-ctrl/openclaw-france-communaute`
- Journal : `…/blob/main/data/journal.jsonl` — Stats : `…/blob/main/data/stats.json`
- Runs : `https://github.com/mael-ctrl/openclaw-france-communaute/actions`
- Bluesky : `https://bsky.app/profile/communaute.openclaw-france.fr`
- Archives web : `https://web.archive.org/web/*/communaute.openclaw-france.fr*`
- (optionnel) Santé PDS : `https://atproto.openclaw-france.fr/xrpc/_health`

---

## 4. Procédure de candidature officielle, étape par étape

**Uniquement via le site officiel** `guinnessworldrecords.com` (compte → « Apply
for a record »). Pas de conseil individuel par e-mail ou téléphone ; pas de
courrier (détruit) ; pas d'envoi postal de preuves.

1. **Choisir la voie** : *Standard* (self-service, réservée aux **individus** —
   pas de promotion d'une entreprise/marque) ou *Consultancy* (organisation /
   marque / licence de la marque GWR — **services payants, prix sur demande**).
   Remarque officielle : une candidature peut être réaiguillée vers la
   Consultancy (complexité ou usage de la marque). C'est un scénario à prévoir
   (voir §7).
2. **Créer un compte** sur `guinnessworldrecords.com/account/register` et
   activer l'e-mail.
3. **« Apply for a record »** (bouton vert du tableau de bord) → rechercher le
   titre dans la base (50 000+ titres) → si introuvable, **« Apply for a new
   record title »**.
4. **Remplir le formulaire** : quoi/comment/où/pourquoi + liens utiles
   (site, dépôt, journal, transparence). Nouveau titre = **frais
   d'administration non remboursables de 5 £/5 $ (+TVA)**. Limite : 3
   candidatures par personne / 24 h.
5. **Revue par la Records Management Team** → en cas d'acceptation, réception
   des **Record Guidelines** + **Guide to Your Evidence** via le compte.
   Délai annoncé : **jusqu'à 12 semaines** (la FAQ officielle actuelle indique
   **jusqu'à 20 semaines**). ⚠️ **Ne pas commencer la tentative avant d'avoir
   reçu les directives.**
6. **Préparer la tentative** selon les directives (protocole §3.4) et
   **collecter les preuves** (§3.3).
7. **Téléverser les preuves** sur le compte, fichier par fichier (≤ 1 Go, pas de
   ZIP, anglais recommandé), puis cliquer **« Submit Evidence »** (les fichiers
   seuls ne suffisent pas — tant que ce bouton n'est pas cliqué, ils ne sont pas
   dans la file de revue).
8. **Revue des preuves** : **jusqu'à 12 semaines** (FAQ : jusqu'à 20).
   Si le record est validé : **certificat officiel offert** (1 exemplaire) ;
   badge numérique gratuit pour les candidatures standard.
9. **Silence au-delà des délais** : contacter via le compte (réponse jusqu'à
   2 semaines) ou le support avec **application ID + e-mail + titre proposé**
   après le délai officiel. Un **processus de recours** (« Review and appeals »)
   est prévu en cas de rejet.
10. **Après validation seulement** : communication publique, presse, mise en
    avant (ne pas annoncer « on va battre un record » avant).

**Coûts — tableau factuel (site officiel, 30/09/2026)** :

| Élément | Coût |
|---|---|
| Candidature standard — titre **existant** | **Gratuit** |
| Suggestion d'un **nouveau titre** | **5 £ / 5 $ (+TVA)**, non remboursable |
| Priority Application (traitement en 5 jours ouvrés) | 500 £/800 $ (titre existant) ; 650 £/1 000 $ (nouveau titre) — **service actuellement suspendu** (« temporarily unable to expedite applications ») |
| Evidence Review prioritaire | Payant (tarif annoncé séparément) — même service suspendu |
| Consultancy (organisations / marques) | **Prix sur demande** |
| Adjudicateur sur place | Service payant (via Consultancy) |
| Certificat supplémentaire | Boutique officielle (payant) |

**Anti-arnaque** : les seuls canaux légitimes sont le site officiel et les
e-mails du compte. Guinness **ne paie pas** les détenteurs de records et **ne
demande jamais** de payer un « consultant » intermédiaire. Aucun paiement ne
sera effectué (hors frais officiels éventuels de nouveau titre, 5 £/5 $, à la
charge du candidat au moment de soumettre).

---

## 5. Brouillon du texte de candidature (EN, ≤ 250 mots)

> **Proposed record title (new)** : *Longest continuous operation of a news
> website written and published entirely by an artificial intelligence, without
> human editorial intervention.*
>
> Since 29 September 2026, « La Communauté » (communaute.openclaw-france.fr), a
> French-language news outlet covering the global AI ecosystem, has been
> operated exclusively by an autonomous AI system (« Le Crabe », OpenClaw
> France). Every task — source collection, writing and editing of all news
> briefs and articles, site building, deployment and social publishing — is
> performed by a scheduled software pipeline (GitHub Actions, every 30
> minutes). No human writes, rewrites, approves, edits or publishes any
> content at any stage; humans only maintain the infrastructure.
>
> The system's complete activity journal, source code, publishing datasets and
> a live transparency page (real figures, budget, errors) are public and
> permanent. Every published item is sourced and timestamped in the public
> archive, the RSS feed and third-party infrastructure records.
>
> Measurement: consecutive days of operation with zero human editorial
> intervention, from launch. As of [DATE]: [N] days and [N] published news
> items.
>
> Evidence available: public Git history with infrastructure commits,
> third-party scheduled-run logs, append-only machine journal, dated web
> archives, downloadable dataset of all published items, and independent
> expert attestation.
>
> No existing title covers a continuously AI-operated media: current AI
> records concern products (music, exams, events), while news-related titles
> involve human journalists.

*(Version française de travail : voir §1 ; le texte s'adapte aux options A et
B en changeant la première phrase et la phrase « Measurement ».)*

---

## 6. 10 FAQ anticipées (et réponses)

1. **Est-ce que candidater coûte quelque chose ?** — Standard + titre existant :
   gratuit. Suggestion d'un nouveau titre : 5 £/5 $ (+TVA), non remboursable.
   Priorité/consultance/adjudicateur : payants (priorité suspendue à ce jour).
2. **Quels délais réels ?** — Annoncés « jusqu'à 12 semaines » pour recevoir les
   directives, et autant pour la revue des preuves ; la FAQ officielle actuelle
   parle de **jusqu'à 20 semaines**. Prévoir ~6 mois au total.
3. **Peut-on se faire conseiller avant de déposer ?** — Non : Guinness ne donne
   pas d'avis par e-mail/téléphone ; tout passe par le formulaire et le compte.
4. **Une IA peut-elle être « record holder » ?** — Guinness enregistre un
   « who » (personne ou entité — ex. un hôtel, une série de jeux) avec une
   nationalité. Proposer « Le Crabe — OpenClaw France (France) » ; le titulaire
   exact est confirmé par Guinness.
5. **Faut-il des témoins humains pour une opération 24 h/24 ?** — Oui : 2 témoins
   indépendants minimum ; pour les tentatives longues, témoins par tranches de
   ≤ 4 h et/ou **témoin spécialiste**. Un expert indépendant (commissaire de
   justice/auditeur) attestant le dispositif est notre réponse à l'absence de
   témoin permanent.
6. **Comment prouver « sans relecture humaine » ?** — Code public, journal
   horodaté append-only, contrôle des accès, absence d'étape d'approbation
   humaine dans le pipeline, audit tiers. Les humains ne font que la
   maintenance technique — et c'est journalisé.
7. **Et si le « first » est contesté ?** — Le format « first » exige
   l'antériorité mondiale ; c'est pourquoi nous positionnons le
   « longest-running » en titre principal (mesure par durée, plus difficile à
   contester) et le volume 24 h en alternative.
8. **Et si la candidature est refusée ?** — Pas de remboursement des éventuels
   frais ; procédure de recours officielle (« Review and appeals ») ; on peut
   re-soumettre un autre titre.
9. **Peut-on communiquer sur le record avant validation ?** — Non : pas de
   communication « record » ni d'usage de la marque GWR avant validation.
   Préparer la presse, ne pas annoncer le record.
10. **Faut-il une structure juridique ?** — La voie standard est réservée aux
    individus (sans promotion d'une organisation) ; un projet média/marque peut
    être réaiguillé vers la Consultancy payante — scénario budgété dans §7.

---

## 7. Risques identifiés & contre-mesures

- **Réaiguillage vers la Consultancy payante** (organisation/marque) → budget
  à prévoir ; en attendant, postuler en tant qu'individu est la voie la moins
  coûteuse, sans garantie d'acceptation de la voie.
- **Exigence de preuves « zéro humain » difficile à établir sur la durée** →
  protocole écrit + audit tiers + journal chaîné (§3.2).
- **« Substantiellement différent » / existence d'un titre proche** → dossier
  argumenté §2 ; accepter la bascule éventuelle vers un titre existant à battre.
- **Délais longs (6 mois+)** → lancer tôt, chiffres à jour au moment de la
  soumission (le site publie en continu, le dossier doit citer les chiffres du
  jour).
- **Naissance de concurrents (autres médias IA)** → la longueur d'exploitation
  et la qualité d'archive font notre avantage ; ne pas retarder la collecte de
  preuves.
- **Mots interdits dans les records** : rester factuel — pas de « best », « most
  beautiful », etc. ; une seule variable par titre.

---

## 8. Calendrier réaliste

- **M+0 (fait)** : socle de preuves en place (dépôt, journal, workflow, transparence).
- **M+0 à M+1** : renforcements §3.2 (chaînage du journal, archivage Wayback,
  tags signés, dataset) ; protocole de mesure figé.
- **M+3** : ~3 mois de journal continu (auto-exigence de crédibilité, pas une
  règle Guinness) → **soumission de la candidature** (compte + formulaire +
  frais de nouveau titre le cas échéant).
- **M+3 → M+8** : revue Guinness (directives puis preuves), ajustements, envoi
  des preuves par fenêtre, témoins/attestation.
- **Validation** : certificat + communication presse (« média 100 % IA
  officiellement record »).

## 9. Sources officielles (consultées le 30/09/2026)

- Processus & formulaires : https://www.guinnessworldrecords.com/records ·
  https://www.guinnessworldrecords.com/records/faqs ·
  https://www.guinnessworldrecords.com/contact/application-enquiry ·
  https://www.guinnessworldrecords.com/records/apply-to-set-or-break-a-record/index.html
- Standard vs Consultancy + frais 5 £/5 $ :
  https://www.guinnessworldrecords.com/records/the-application-process/standard-applications.html
- Délais actuels : https://www.guinnessworldrecords.com/records/the-application-process/current-wait-times.html
- Critères : https://www.guinnessworldrecords.com/records/what-makes-a-guinness-world-records-record-title/index.html
- Preuves : https://www.guinnessworldrecords.com/records/how-to-collect-and-submit-evidence/index.html ·
  « Guide to Your Evidence » (PDF) : https://www.guinnessworldrecords.com/records/how-to-collect-and-submit-evidence/guide-to-your-evidence-2022.pdf
- Recours : https://www.guinnessworldrecords.com/records/the-application-process/review-and-appeals-process.html

## 10. Prochaine étape concrète

1. **Valider la formulation du titre principal** (Option C, « Longest-running »)
   — une phrase, une variable, zéro opinion.
2. **Activer la routine de preuves horodatées** (§3.2) : chaînage du journal,
   archivage Wayback quotidien, tag Git signé mensuel, dataset
   `publications.jsonl`.
3. **Rédiger le protocole de mesure** (définition précise de « sans intervention
   éditoriale humaine ») et le faire relire par un tiers indépendant pressenti.
4. **Soumettre la candidature** via un compte officiel dès ~3 mois de journal
   continu (≈ fin décembre 2026) — sans paiement en dehors des frais officiels
   éventuels de nouveau titre (5 £/5 $, à confirmer au moment du dépôt).
