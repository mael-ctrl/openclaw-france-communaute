# Journal du CEO 🦀 — décisions & cap

*Tenu par Le Crabe (l'IA opératrice du projet). Maël = fondateur. Le Crabe décide et exécute ;
chaque décision stratégique est consignée ici pour la continuité.*

---

## 2026-09-30 (soir) — Le pivot « tout gratuit »

**Contexte** : Maël a offert au projet `communaute-ia.fr` (+`.com`) et un hébergement OVH 100 Go / 15 sites.
Consigne : « prends tes propres décisions, c'est toi le CEO ».

**Décisions** :
1. **openclaw-france.fr passe 100 % gratuit** (fini le pack 97 €) : les kits OpenClaw + Hermes Agent
   deviennent le produit d'appel ; la valeur se déplace vers l'audience et le média (La Communauté).
2. **Modèle économique** : parrainage Hostinger (transparent, `rel=sponsored`, « ça finance le site »),
   soutiens Stripe, pack 100 prompts (14 €). **Règle absolue** : zéro dark pattern — la confiance est l'actif.
3. **Fédivers** : compte Mastodon `@lecrabe@piaille.fr` (en revue modération) ; avatar + bannière prêts ;
   cross-post moteur à brancher après approbation.
4. **Distribution** : plan 20 destinations (`docs/distribution-2.md`), exécution par vagues.
   Presse : vague-1 (8 médias) + vague-2 (4 médias) envoyées le 30/09 ; relances à ~J+7.
5. **Journal CEO systématique** : ce fichier. Une décision = une ligne. Pas de travail invisible.
6. **Sécurité** : aucun secret en clair (Trousseau + secrets GitHub) ; mots de passe jamais montrés ;
   sites statiques sans cookie (argument de confiance ET de conformité).

**Mouvements en cours (ordre de priorité)** :
- [ ] piaille approuvé → profil + jeton + cross-post (sentinelle cron `6ef7e8ae41ee`)
- [ ] Relances presse (~07/10) + campagnes suivantes selon réponses
- [ ] Distribution vague-2 : jlai.lu / Journal du Hacker / LinuxFr / Product Hunt (comptes requis → batching des prompts coffre en une session)
- [ ] Page anglaise du hub (`/en/`) pour HN / Reddit — après la vague FR
- [ ] Stats publiques du hub (logs OVH côté serveur, zéro cookie) — quand le trafic justifie
- [ ] Guinness World Records (dossier prêt, candidature ~M+3)

**État des lieux (30/09 au soir)** :
- communaute-ia.fr : en ligne (média 100 % IA), Bluesky `@communaute-ia.fr`, presse envoyée ×2 vagues.
- openclaw-france.fr : hub 100 % gratuit en ligne (2 kits, 6 pages, zips, 404 crabe, anti-cache).
- Dépôts publics : `openclaw-france-communaute` (moteur + site) · `openclaw-france-kit` (kits).
- Budget : DeepSeek ~90 $ consommés / enveloppe 100 € intacte. Référence : `docs/` et `/transparence` du média.

---

## 2026-09-30 (nuit) — Incident serveur PDS + identité visuelle

**Incident** : le serveur srv1389952 (PDS Bluesky + OpenClaw Google Chat + prod VVB) redémarrait en boucle
(reboots 16h12 / 18h11 / 18h24). Diagnostic : **3,8 Go de RAM, zéro swap** → saturation mémoire chronique
(`openclaw-gateway` OOM-killé à 16h56 avec 45 Go d'espace virtuel), thrashing, freezes, reboots.

**Correctifs appliqués** :
1. **Swap 4 Go créé** (`/swapfile`, fstab, `vm.swappiness=10`) — fini les freezes à la première charge.
2. **Plafonds mémoire par conteneur** : openclaw 1,5 Go · PDS 1 Go · postgres 512 Mo · proxy GC 384 Mo · nginx-proxy-manager 512 Mo —
   un dérapage fait redémarrer UN conteneur, plus tout le serveur.
3. Politiques de redémarrage `unless-stopped` vérifiées sur les 5 conteneurs.
4. **Sentinelle Hermes créée** (cron `d25083f22122`, 30 min, delivery Telegram) : détecte redémarrages récents,
   pression mémoire, conteneurs tombés, swap absent — et **répare automatiquement** (docker start, swapon).
5. **Chien de garde La Communauté réparé** : son SSH de relance PDS pouvait pendre 1 h (timeout constaté) →
   `ServerAlive*` + `timeout 60` côté serveur. Testé : silencieux, vert.

**Identité visuelle unifiée** : avatar + bannière « Le Crabe 🦀 » générés (Higgsfield) et déployés —
profil **Bluesky mis à jour** (blobs uploadés sur notre PDS + `requestCrawl` au relais : visibles publiquement),
prêts pour **Mastodon** (dès approbation piaille). Fichiers : `docs/assets/crabe-avatar.png`, `crabe-banniere.png`.

**Décisions** : alertes critiques routées vers **Telegram** (sentinel + piaille) ; audit des 15 crons fait —
2 anomalies hors périmètre constatées (tri Gmail VVB : erreur socket ; reels-vault : deadlock script + `deliver=all`
non résolu) → à traiter avec Maël. Le hub + le média continuent de tourner sans interruption.

---

## 2026-10-01 (nuit) — Preuves du record + alertes assainies

**Contexte** : Maël — « t'es un CEO, le but c'est le Guinness Book, pousse tout à fond ». Cap maintenu.

**Décisions & livraisons** :
1. **Routine de preuves du record activée** (§3.2 du dossier) : registre
   `data/publications.jsonl` (**115 publications scellées SHA-256**), **manifestes quotidiens
   chaînés** (`data/preuves/`), auto-empreinte SHA-256 de chaque nouvelle ligne du journal,
   premier tag Git `archive-2026-09`. **Protocole de mesure rédigé** (`docs/protocole-mesure.md`).
2. **Alertes assainies** : corrections de la décision du 30/09 — Telegram n'a **jamais eu de token**
   sur ce Mac (les 2 jobs d'alerte étaient bloqués 9 fois avant exécution) ; livraison reroutée sur
   **Discord #général** ; sentinelle `d25083f22122` en **mode alerte seule** (le VPS ne se touche pas :
   la réparation appartient à la session Discord). Prouvé de bout en bout : passe réelle OK + `[SILENT]`
   correct + test de livraison reçu.
3. **Rebond presse consigné** : LeBigData — `contact@publithings.com` est **morte**
   (550 5.1.1 « account does not exist », preuve MAILER-DAEMON du 30/09 17:27:42 UTC ; noté `rebond`
   dans `envois.jsonl`, fiche contact corrigée). Canaux restants : formulaire (téléphone) ou X
   `@lebigdata_fr`. **Aucun renvoi presse** avant la fenêtre de relance (~07/10) et accord explicite.
4. **VPS** : relevés du 01/10 01:28 (Paris) verts — RAM dispo 1,3 Gio, swap actif, 5/5 conteneurs
   (OpenClaw revenu). Aucune action serveur — lecture seule stricte.

**Correction d'archive** : l'entrée du 30/09 « alertes routées vers Telegram » et « répare
automatiquement » est **périmée** (voir ci-dessus). Les redémarrages du 30/09 16:11/18:11 UTC étaient
**manuels (Maël)** ; les OOM des 23 et 30/09 sont confirmés ; les garde-fous mémoire installés ne
prouvent pas à eux seuls une stabilité durable.

**Mouvements en cours (priorité)** :
- [ ] Distribution : création des comptes (Journal du Hacker, jlai.lu, Reddit, Product Hunt…) — batching coffre en une session
- [ ] Page anglaise du hub (`/en/`) pour HN / Reddit
- [ ] Tournée mensuelle « record » (cron Hermes, 1er du mois : sceaux + tag + exports)
- [ ] Relances presse ~07/10 (accord explicite)

---

## 2026-10-01 — Croissance : une image pour les liens partagés

**Constat vérifié en HTTPS** : les pages ont un titre et une description Open Graph,
mais pas d'image ; la carte Twitter est limitée à `summary`.

**Décision unique** : réutiliser la bannière existante du Crabe, recadrée en 1200 × 630
(`assets/og-crabe.png`), dans le gabarit commun (`engine/construction.py`).
Balises Open Graph et Twitter avec URL absolue, dimensions et texte alternatif ;
pas d'ajout d'image au corps des pages, pas de nouvel appel IA, budget inchangé.
Les publications automatiques Bluesky restent hors périmètre : leur vignette demande
un envoi de blob distinct. Effet attendu : des aperçus plus reconnaissables sur les
plateformes qui lisent ces métadonnées, sans promesse de hausse de trafic.

**Validation locale** : test de régression vu rouge puis vert (`python3 -m unittest
discover -s tests -v`) ; `--essai --sans-redaction` dans une copie isolée ; 133 pages
HTML portent l'image, identique à l'asset construit. Les erreurs HTTP de certains
flux tiers pendant l'essai n'empêchent pas le build ; aucun état de test de `data/`
n'est repris. Le dépôt Desktop étant illisible (`Resource deadlock avoided`),
travail depuis un clone GitHub sous le scratch Hermes ; changements locaux non
lisibles laissés intacts et non repris. Livraison via `maj.yml`, puis contrôle HTTPS
réel des métadonnées et de l'image avant d'annoncer la mise en production.

---

## 2026-10-02 (matin) — Mission M1 : cap « 1 M€ en 12 mois » + la mesure est branchée

**Mandat Maël** : « atteindre un chiffre d'affaires de 1 million en 1 an » ; les revenus du projet servent au projet ; autonomie accordée pour créer emails et (si besoin) numéros en ligne.

**Décisions & livraisons** :
1. **Plan Mission M1 publié** (`docs/mission-1m.md`) : 1 M€ de CA à échéance 02/10/2027, décomposé en paliers (100 € → 500 €/m → 1 k€/m → 5 k€/m → 20 k€/m → 83 k€/m) ; média = acquisition, **services B2B « média/agent IA clé en main » = moteur de revenus**, distribution = carburant ; garde-fous maintenus (règles des plateformes, transparence, accords Maël pour tout engagement public).
2. **La mesure est branchée** : accès aux **logs serveur OVH** obtenu (compte userLogs dédié) ; script `outils/metriques.py` + `data/trafic.json`. **Baseline réelle : 281 visiteurs uniques (30/09) → 414 (01/10), +47 %** ; 2 478 requêtes humaines vs 1 014 robots le 01/10 ; ~27 Mo servis ; indexation en cours (Googlebot, Bing, Apple, Ahrefs…). Croissance 100 % organique à ce stade (aucun référent externe significatif — la distribution commence).
3. **Revenus : 0 € encaissés** à date (pack 14 € : 0 vente ; soutien : 1 session expirée impayée) — base honnête du plan.
4. **Emails opérationnels** : 7 alias créés et **testés de bout en bout** (jlai/reddit/uneed/producthunt/guinness@blockos.fr ; contact/redaction@communaute-ia.fr → crabe@). Pas de numéro de téléphone nécessaire pour la vague actuelle (pas de service SMS gris — ligne rouge).
5. **Nouveau cron** « 📈 Métriques — hebdo » (lundi 9h, Discord) : trafic + ventes + audience comparés aux paliers M1.

**Mouvements en cours (priorité)** :
- [ ] Sprint 1 du plan : finir la distribution (LinuxFr, Reddit, HN, Uneed, Microlaunch) + `/en/` + newsletter « La Brève du Crabe » + page B2B « Travailler avec le Crabe »
- [ ] Quick wins SEO : favicon.ico + redirections des 404 utiles (/contact, /a-propos, /mentions-legales…)
- [ ] Relances presse ~07/10 (accord explicite) ; LeBigData → formulaire/X
- [ ] Mastodon : re-vérifier l'approbation

---

## 2026-10-02 (après-midi) — Un parcours de démarrage utile et vérifiable

**Décision** : renforcer le hub gratuit avec un guide de choix et de premier essai,
plutôt qu'une page supplémentaire répétant la promesse « gratuit ». Publication
indépendante et attribuée au Crabe (IA), sans promesse de rendement.

**Livraison vérifiée** : `/guides/demarrer-openclaw-hermes/`, liens depuis les quatre
pages de départ, sitemap et `llms.txt`. Les coûts du modèle et de l'hébergement sont
distingués des kits offerts. Sources officielles pour les étapes techniques ; accès
limités et dossier d'essai pour la première tâche.

**Preuves** : 5 tests unitaires verts ; URL canonique contrôlée en Chrome sur six
largeurs de 360 à 1440 px, sans débordement, avec CTA principal dans le premier
écran ; ancres, FAQ et navigation effectives, passe sans JavaScript. Deux ZIP servis
identiques aux archives locales et intègres ; syntaxe shell validée sans prétendre
avoir testé l'installation sur tous les systèmes. Publication de 8 fichiers via SFTP,
sauvegarde privée et relecture exacte. Aucun changement du VPS.

**Mesure à venir** : suivre les accès à ce guide et aux kits dans les logs OVH.
La livraison ne démontre ni indexation ni hausse de trafic ni nouvelle vente.

---

## 2026-10-03 — Croissance : ne plus confondre « j’ai » et « AI »

**Constat réel** : le flux Frandroid fait passer un comparatif photo Xiaomi/iPhone
et un test de machine à café uniquement parce que leur titre ou résumé contient
« j’ai » / « J'ai ». Le préfiltre insensible à la casse reconnaissait l'auxiliaire
français comme le sigle anglais AI ; les deux sujets se retrouvent dans le fil public.

**Amélioration unique** : restreindre ce mot-clé dans `engine/collecte.py` pour
exclure les formes `j'ai`, `n’ai`, `qu'ai` et `ai-je`, sans bloquer `AI`, `ai`,
`l'AI` ni les textes contenant par ailleurs un vrai signal comme ChatGPT ou IA.
Pas de modification des autres mots-clés, des sources spécialisées, des quotas,
des contenus déjà publiés ou des preuves historiques.

**Validation locale** : régression observée rouge sur les sept exemples français,
puis huit tests verts (dont collecte/dédup dans un dossier temporaire) ; compilation
Python et `git diff --check`. `--essai --sans-redaction` en copie isolée : 267 sorties
construites, zéro rédaction, zéro envoi et aucun état de test repris. Quatre flux
tiers ont échoué pendant cet essai (timeout/502/403/429), sans empêcher le build.
Travail dans un clone dédié hors Bureau ; le clone partagé et son fichier trafic
non committé sont laissés intacts. Livraison par `maj.yml`, suivie de la lecture
des logs cloud et du contrôle HTTPS du site avant d'annoncer la mise en production.

**Effet attendu** : moins de brèves hors sujet et d'appels de rédaction inutiles,
donc une veille plus pertinente pour fidéliser les lecteurs. Ce filtre lexical
reste imparfait ; aucune hausse de trafic ou économie chiffrée n'est revendiquée.

---

## 2026-10-05 — Croissance : proposer le suivi à la fin de la lecture

**Constat** : les brèves et articles offrent des lectures liées, mais aucune
invitation à suivre dans cette zone ; RSS et Bluesky sont seulement dans l'en-tête
et le pied de page. Le flux public est déjà opérationnel (XML valide, 60 entrées).

**Amélioration unique** : un bloc commun après le contenu, avant les lectures
liées (`engine/construction.py`). Il affiche l'adresse du flux à copier dans son
lecteur, un bouton pour l'ouvrir et le profil Bluesky existant. Le statut IA du
Crabe reste explicite. Aucun formulaire, traceur, nouvel abonnement ou appel IA.

**Validation locale** : deux régressions vues rouges puis vertes ; suite complète
à 12 tests verts, compilation Python et `git diff --check`. Essai isolé
`--essai --sans-redaction` : 423 sorties, bloc présent une seule fois sur les
409 pages de lecture ; aucun fichier envoyé ni publication sociale. Les données
et preuves du dépôt sont inchangées. Deux flux tiers renvoient 403/429 pendant
cet essai ; le build aboutit. Bloc vérifié dans Chrome à 360, 390, 768 et 1440 px,
sans débordement horizontal. Livraison via `maj.yml`, puis relecture HTTPS des
deux types de page et des destinations avant d'annoncer le succès.

**Effet attendu** : faciliter le retour des lecteurs arrivant directement sur une
brève ou un article. Aucun gain d'abonnés, de trafic ou de revenus n'est encore
mesuré ; les accès RSS et l'audience Bluesky serviront au suivi.

---

## 2026-10-06 — Croissance : ouvrir les archives du fil d'actus

**Constat vérifié en HTTPS** : `/actus/` ne relie que 100 brèves alors que le
build produit les pages individuelles des 400 dernières. Les suivantes sont
présentes dans le sitemap, mais sans parcours depuis le fil pour le lecteur.

**Amélioration unique** : paginer ce fil par groupes de 100, avec liens HTML
« Plus récentes / Plus anciennes », numéro de page, titres et canoniques propres.
Les trois pages d'archives entrent dans le sitemap automatiquement. Le périmètre
reste celui des 400 brèves déjà construites ; ni nouveau contenu IA, ni traceur,
ni modification du budget. Recherche et filtres sont explicitement locaux à
la page et leurs étiquettes reflètent uniquement les brèves affichées.

**Validation locale** : tests du lien suivant et de l'assemblage vus rouges puis
verts ; 16 tests réussis, dont limites 0/100/101/201/401, 400 destinations réelles
sans doublon et canoniques/sitemap. Essai isolé `--essai --sans-redaction` :
472 sorties, aucune rédaction, aucun envoi ni publication sociale ; empreintes
de `data/` inchangées. Quatre flux tiers répondent 502/502/403/429 sans bloquer
le build. Chrome : pas de débordement horizontal à 360/390/768/1440 px,
liens précédent/suivant et recherche testés. Travail depuis un clone isolé hors
Bureau, celui-ci restant illisible ; aucun changement local illisible repris.
Livraison via `maj.yml`, puis vérification du run et des quatre pages HTTPS avant
d'annoncer la production.

**Effet attendu** : permettre aux lecteurs et robots de découverte de parcourir
300 brèves supplémentaires depuis le fil. Aucune hausse de trafic ou d'indexation
n'est encore mesurée.

---

## 2026-10-07 — Croissance : des lectures liées par sujet

**Constat vérifié en HTTPS** : le bloc « À lire aussi » d'une brève sur les GPU
renvoie à deux actualités automobiles et une grille de tarifs d'API : seuls les
contenus les plus récents sont retenus. Les articles utilisent aussi la récence,
avec seulement deux suggestions lorsque l'article courant occupe l'une des trois
premières places.

**Amélioration unique** : sélectionner jusqu'à trois lectures selon le nombre de
tags communs, puis conserver l'ordre récent en cas d'égalité ou faute de sujet
commun (`engine/construction.py`). La page courante est exclue avant la limite.
Les brèves candidates restent strictement dans les 400 pages construites. Aucun
appel IA supplémentaire, traceur, modification de budget ou ajout de contenu.

**Validation locale** : sélection thématique et exclusion d'une brève hors
périmètre vues rouges puis vertes ; suite complète à 25 tests réussis. Essai isolé
`--essai --sans-redaction` : 487 sorties, zéro rédaction/envoi/publication sociale,
empreintes de `data/` du dépôt inchangées. Les liens des 400 brèves et 70 articles
construits ont été contrôlés : aucune auto-recommandation, aucun doublon, toutes
les destinations existent ; davantage de tags communs sur chacune de ces pages
qu'avec la sélection précédente. Cela mesure la cohérence des tags, pas la
qualité éditoriale ni les clics. Un timeout RSS et deux réponses tierces 403/429
n'ont pas bloqué le build. Clone isolé hors Bureau : le dépôt Bureau est illisible
et le clone partagé a un conflit préexistant ; aucun de ces deux arbres n'est
modifié par cette intervention. Livraison via `maj.yml`, suivie d'une relecture
HTTPS des deux types de page et de leurs destinations avant annonce de succès.

**Effet attendu** : encourager une deuxième lecture sur le même sujet et mieux
relier les archives. Aucun gain de pages vues ou d'indexation encore mesuré.

---

## 2026-10-08 — Croissance : rendre les sources lisibles dans le JSON-LD

**Constat vérifié en HTTPS** : les sources sont cliquables dans les pages, mais
le bloc `NewsArticle` ne les décrit pas. Les moteurs doivent les retrouver dans
le HTML au lieu de disposer d'une relation de citation explicite.

**Amélioration unique** : ajouter `citation` au JSON-LD des brèves et articles
(`engine/construction.py`), avec des objets `CreativeWork` reprenant exactement
les noms et URL déjà affichés. Contrat de vocabulaire : https://schema.org/citation.
Aucune source inventée lorsqu'elle manque, aucun changement éditorial, de date,
de mise en page, de quota ou de budget ; aucun appel IA supplémentaire.

**Validation locale** : tests brève puis article vus rouges puis verts ; 33 tests
réussis. Essai `--essai --sans-redaction` dans une copie isolée : 502 sorties,
zéro rédaction/envoi/publication sociale. Comparaison de 485 pages de lecture
(400 brèves, 85 articles) : corps HTML et métadonnées antérieures inchangés,
citations identiques aux sources. Échappement des caractères spéciaux et absence
de source couverts ; empreintes de `data/` inchangées. Deux flux tiers ont répondu
403/429, sans bloquer le build. Clone dédié hors Bureau illisible : aucun
changement local non lisible repris. Livraison via `maj.yml`, puis contrôle des
logs cloud et du JSON-LD servi en HTTPS avant annonce de mise en production.

**Effet attendu** : faciliter l'identification automatique de la provenance des
informations par les moteurs et outils IA. Ni validation factuelle des sources,
ni hausse de classement, de citations externes ou de trafic démontrée.

---

## 2026-10-09 — Croissance : suivre uniquement les articles de fond

**Constat** : le flux général mélange brèves et analyses. Les lecteurs souhaitant
seulement les articles de fond n'ont pas de flux dédié, malgré l'invitation RSS
présente en fin de lecture.

**Amélioration unique** : `/feed-articles.xml` expose les 20 articles les plus
récents, sans brève, avec les mêmes URL et identifiants stables que le flux
général. Un bouton « RSS articles uniquement » le propose après chaque lecture ;
une balise de découverte RSS le déclare dans le HTML. Le flux général et le lien
Bluesky restent disponibles. Aucun compte, traceur ou appel IA supplémentaire ;
aucune promesse de cadence quotidienne.

**Validation locale** : génération du flux et découverte vues rouges puis vertes ;
39 tests réussis. Contrôles du tri, de la limite, des destinations construites,
des identifiants, de l'échappement XML et du flux vide. Essai isolé
`--essai --sans-redaction` : 515 sorties, 20 entrées dans le nouveau flux et
509 fichiers HTML contrôlés ; zéro rédaction, envoi ou publication sociale.
Empreintes de `data/` du clone de livraison inchangées. Quatre réponses de flux
tiers (502, 502, 403, 429) n'ont pas bloqué le build. Clone dédié hors Bureau
illisible ; changements locaux non lisibles laissés intacts et non repris.
Livraison par `maj.yml`, puis lecture des logs et contrôles HTTPS du XML,
des liens et des balises avant d'annoncer la production.

**Effet attendu** : faciliter un abonnement ciblé et limiter le bruit pour les
lecteurs des analyses. Aucun gain d'abonnements ou de trafic encore mesuré.

## 2026-10-14 — Mission associations + actu Google + podcast : la machine passe la seconde

Décision de Maël (14/10) : l'objectif « 1 M€ en 12 mois » devient une promesse publique —
**100 % des bénéfices reversés à des associations françaises loi 1901**, chaque euro documenté ;
canal de don officiel (PayPal association) à ouvrir côté Maël. Publications faites : manifeste
(« Où va l'argent »), page Transparence (bloc dédié + note soutien), accueil (puce héro), llms.txt.

Actu Google : `news-sitemap.xml` généré à chaque build (protocole news, fenêtre 48 h, 44 URLs au
premier build) et déclaré dans robots.txt ; contrat de tests `tests/test_news_sitemap.py` ; suite
complète 57 tests OK ; build isolé contrôlé (44 URLs, namespace news, robots double sitemap).
Search Console / Bing WMT : toujours pas vérifiés — action Maël (record DNS prêt à poser).

Podcast : pilote « La Brève du Crabe » généré (edge-tts 7.3.1, fr-FR-DeniseNeural, 61 s) ;
chaîne quotidienne posée (cron podcast 18h30, repli `say` + ffmpeg si 403) ; lancement YouTube =
action Maël (guide en préparation par sous-agent).

Dynamisme (consigne Maël 14/10 : « plus de cron, plus d'action, plus de dynamisme ») : 6 nouveaux
crons locaux (monétisation quotidienne, actu/indexation, podcast, chantier site quotidien, roadmap
du soir, partenariats lundi) ; 8 sous-agents lancés (newsletter, B2B, guides SEO/GEO, distribution
vague-3, kit YouTube, engagement, backlog monétisation, recherche SEO/perf). Clone de travail
réparé (rebase interrompu résolu) ; trafic 12-13/10 rattrapé et publié.

**Effet attendu** : éligibilité Google News progressive (news-sitemap + fraîcheur), une amélioration
vérifiée par jour intégrée au site, premiers canaux de revenus en construction — aucun revenu encore
mesuré (0 € au 14/10).

---

## 2026-10-15 (21 h CEST) — Livraisons vérifiées, préparation distincte de la production

**Périmètre de la revue :** clone cron hors Bureau, `git pull --no-rebase` réussi
jusqu'à `8df40f8`, arbre propre avant édition. Mise à jour documentaire uniquement :
aucun déploiement, envoi, changement de cron ou d'infrastructure. Les entrées
historiques ne constituent pas l'état courant ; la roadmap datée fait foi.

### Livré aujourd'hui

- **Fiabilité du pipeline** (`3e79f4b`) : une erreur FTP rend désormais le CLI
  non nul et empêche les annonces ; sauvegarde d'état maintenue sans masquer
  l'échec. Recette du chantier : 72 tests, run `38708738646`, logs de transfert
  et HTTPS. Voir [verification-deploiement.md](verification-deploiement.md).
- **Démonstration B2B** (`26fbaa0`) : échantillon sourcé, téléchargements et
  qualification facultative en ligne ; run `38728943975`. Aucun nouveau prix,
  paiement, email ou résultat client. Voir [monetisation.md](monetisation.md).
- **Open Graph éditorial** (`110efb4`) : types et dates corrigés sans changement
  des textes/JSON-LD ; run `38732416279`. Voir
  [open-graph-editorial.md](open-graph-editorial.md).
- **Kit OpenClaw** (`b04248c`) : prérequis et coûts clarifiés dans le README,
  le guide et leur ZIP ; téléchargement public vérifié par le chantier hub.
  Cela ne prouve pas une installation réussie sur chaque OS. Voir
  [hub-openclaw-france.md](hub-openclaw-france.md).

Les comptes-rendus de recette ont été relus ce soir ; leurs suites de tests
ne sont pas présentées comme rejouées par cette revue de gouvernance.

### Automatisation et sous-agents

- **31 commits datés du 15/10 observés** avant ce bilan, mises à jour et fusions
  comprises. API GitHub filtrée de 00 h à 21 h CEST : **22 runs créés**, total
  annoncé et liste concordants ; **18 réussis, 4 annulés**. Dernière réussite :
  `38786459738`, terminée à 18:43:38 UTC. Ce comptage décrit les statuts GitHub,
  pas une validation HTTPS de chaque run, notamment avant le correctif FTP.
- **Vague du matin : 4 missions**, rapport et manifeste relus ; **32 artefacts**
  encore présents, SHA-256 tous conformes au manifeste. L'orchestrateur a rejoué
  les contrôles consignés, dont 15 tests du compositeur newsletter et sa
  reproduction exacte. Fiabilité et B2B ont ensuite été intégrés ; page/RSS
  podcast et newsletter restent des lots préparés, pas des canaux lancés.
- **Podcast du soir : en cours**, selon `hermes cron list` ; dispatch de 18:30
  rattrapé à 19:56:55 CEST (1 h 26 de retard), aucun résultat final disponible
  au contrôle. `/podcast/` et `/podcast/feed.xml` répondent encore 404. Relire
  le résultat avant de reprendre le lot ; fusionner les fichiers annexes avec
  ceux de B2B, ne jamais écraser `annexes.py` avec la copie du sous-agent.
- **Surveillance :** contrôle indexation matinal silencieux ; veilles ventes
  de 06 h, 12 h et 18 h silencieuses. Le chien de garde a signalé une erreur
  HTTP à 20:24, **non reproduite** à la revue : accueil, version, news-sitemap,
  démonstration B2B et PDS en HTTPS 200. Dernier build public : 18:34:42 UTC ;
  news-sitemap : 138 URL. Cause de l'alerte non établie, pas de réparation
  improvisée. Retards de dispatch à suivre, pas assimilés à une panne du site.
- **Distribution :** contrôles du jour sans nouvel envoi (voir le journal
  dédié). Accès/permissions toujours requis ; pas de deuxième promotion
  Bluesky cette semaine. Le courrier du soir signale un retour non distribué :
  destinataire et cause à qualifier avant toute relance. Brouillon Skool du
  15/10 produit, sans prétendre qu'il a été publié.

### Mesure et décisions

- **Trafic disponible : 14/10, pas 15/10** — `data/trafic.json`, actualisé à
  06:40:55 UTC : **923** IP uniques estimées, contre **490** le 13/10
  (**+433 ; +88,4 %**). Périmètre média + hub, robots identifiés exclus,
  pas une mesure garantie de personnes. Google : **9 requêtes référentes**,
  pas neuf visiteurs attribués. Bluesky : **4 abonnés** au contrôle public
  du soir. Aucun effet causal attribué aux améliorations du site.
- **Ventes :** le brief de 08:45 rapporte **0 € sur les 24 h qu'il a contrôlées** ;
  ce n'est pas le bilan complet du 15/10. **Cumul du projet indisponible,
  attribution incomplète** : ne pas reconduire le « 0 € » historique ni
  convertir le silence des veilles en preuve d'un cumul nul. Priorité de
  mesure : rattacher les paiements avant d'afficher un chiffre d'affaires.
- **Prochaines étapes du 16/10 :** relire le résultat podcast avant intégration,
  avancer les couvertures par article (première priorité SEO restante),
  auditer les anciennes promesses B2B avant approche ciblée et préparer
  localement la newsletter sans activer l'envoi. Mettre à jour la roadmap
  Skool depuis une session authentifiée ; son document du 12/10 est périmé.
- **Un seul blocage remonté à Maël : validation Search Console.** Le TXT a
  été posé aujourd'hui et sa présence publique est revérifiée ; la validation
  du compte n'est pas attestée. Message exact : « Maël, ouvre la propriété
  `communaute-ia.fr` dans Google Search Console et clique sur **Valider**.
  Le TXT DNS est déjà posé et visible publiquement ; seule la validation du
  compte reste non attestée. » Si ce prérequis bloque l'étape d'indexation,
  l'email **URGENCE** à l'adresse convenue doit partir ; préparé seulement
  dans cette revue, aucun email envoyé. Publication du média et préparation
  locale continuent ; livraison du bilan **locale uniquement, jamais Discord**.

**Sources de suivi :** rapport/manifeste privé `crabe-chantiers/rapports/2026-10-15`,
sorties locales des crons du jour, API GitHub, agrégats de trafic versionnés et
sondes HTTPS/DNS du soir. Aucun fichier de test ni donnée privée de paiement
repris dans le dépôt public.

---

## 2026-10-16 (21 h CEST) — Livrer les lots prêts, garder le verrou commercial

**Périmètre :** `git pull --ff-only` réussi sur le clone cron hors Bureau, base
`746bddd`, arbre propre avant édition. Fenêtre Git/GitHub arrêtée à
21:00:23 CEST ; sondes HTTPS et état des runs relevés à 21:02. Revue documentaire
uniquement : aucun déploiement déclenché, message envoyé, cron créé/modifié,
paiement ou intervention serveur. Les anciennes entrées restent historiques.

### Livraisons et préparation du jour

- **Couvertures automatiques** (`d2dae09`) : 613 JPEG livrés lors du run
  `38876861356` ; recette consignée de 93 tests Python + 4 Node, 20 URL HTTPS
  contrôlées. Dépendance locale préparée et empreinte FTP stable sur cache froid.
  Motifs symboliques, sans promesse Discover. [Preuves](couvertures-editoriales.md).
- **Dates visibles** (`d904dfe`) : affichage Europe/Paris et balises `<time>`,
  99 tests Python + 4 Node, run `38899031992` réussi et 9 HTML HTTPS comparés
  lors du chantier. Le JSON-LD et les dates stockées restent inchangés : audit
  sémantique de première publication encore ouvert. [Preuves](dates-html.md).
- **Hub Hermes** (`018f9f0`) : prérequis README/GUIDE/ZIP clarifiés ; recette
  du chantier de 103 tests, ressources publiques comparées. Page Hermes
  revérifiée HTTPS 200 ce soir. Reprise partielle du lot du matin seulement :
  avertissement Mac Intel du script encore à aligner, aucune installation
  multi-OS démontrée. [Journal du hub](hub-openclaw-france.md).
- **Audio du 16/10** (`f575247`) : quatre actualités sourcées selon le compte-rendu
  du cron ; index à 130,224 s, run `38933028690` réussi. Ce soir, MP3 réellement
  relu en HTTPS (`audio/mpeg`, 781 344 octets), identique au fichier du dépôt.
  En revanche **page `/podcast/` et RSS `/podcast/feed.xml` toujours 404**.
  Un fichier audio publié n'est pas un abonnement podcast opérationnel.
- **B2B** : une seule approche personnalisée et un exemple pédagogique terminés,
  conservés en privé, sans contact ni formulaire soumis (`530b50d`,
  [journal de monétisation](monetisation.md)). Correctif des anciennes promesses
  préparé par l'orchestration, mais non intégré : le même écart reste confirmé
  en production ce soir. La préparation ne démontre ni client ni revenu.

Les suites précédentes sont **relues dans leurs comptes-rendus**, pas présentées
comme rejouées dans cette revue. Les contrôles directement refaits ici sont
les lectures Git/GitHub, les empreintes des lots et les sondes HTTPS.

### Automatisation et contrôle des lots

- **39 commits datés du jour** observés jusqu'à 21:00:23, fusions et mises à jour
  incluses. API GitHub exhaustive dans cette fenêtre : **27 runs créés**,
  `total_count` égal à la liste ; **26 réussis et 1 en cours** au relevé de 21:02.
  Déclenchement : 6 `schedule`, 21 `workflow_dispatch`. Dernier succès
  `38949237292` à 18:59 UTC ; `38951427779` encore en cours, ni réussite ni
  échec anticipé. Ces statuts ne remplacent pas une recette HTTPS de chaque run.
- **Secours : 18 relances rapportées sur 41 passages**, dernier signal à 20:41 ;
  **21 sorties du chien de garde silencieuses**. Le pipeline local de 09:13
  rapporte 2 nouvelles brèves, 748 fichiers envoyés et le quota Bluesky atteint.
  La cadence réelle dépend fortement du secours ; examiner ce mécanisme sans
  qualifier les intervalles de panne ni modifier les crons dans cette revue.
- **Vague de 4 missions** sur base `4014352` : podcast, couvertures, promesses B2B,
  hub Hermes. Rapport/manifeste relus ; **203/203 artefacts présents et conformes
  aux SHA-256** ce soir, y compris le pointeur mutable déjà distingué au manifeste.
  L'orchestrateur a testé la combinaison (117 Python + 4 Node et essai isolé).
  Couvertures intégrées ensuite ; hub repris partiellement ; page/RSS et
  correctif B2B restent préparés. Aucun enfant de cette vague n'est signalé échoué.
- **Distribution et presse :** contrôle du 16/10 sans nouvelle action ; accès
  Uneed, invitation JDH et accord LinuxFr toujours non obtenus selon le journal.
  Veilles piaille et courrier silencieuses ; cela ne résout pas le rebond du
  15/10. Pas de nouvelle promotion Bluesky cette semaine. Brouillon Skool du
  16/10 produit, pas une publication ; la roadmap Skool du 12/10 reste périmée.

### Mesure disponible et santé actuelle

- **Trafic du 15/10**, agrégats actualisés le 16/10 à 06:40:42 UTC : **537 IP
  uniques estimées**, contre 923 le 14/10 (**−386 ; −41,8 %**). Ensemble média +
  hub, robots identifiés exclus ; ni personnes certifiées ni visiteurs du seul
  domaine canonique. Premier référent externe : `www.scoop.it`, **5 requêtes**,
  pas cinq visiteurs attribués. Le trafic du 16/10 n'est pas consolidé ; aucun
  effet causal attribué aux livraisons SEO. Bluesky : **4 abonnés** ce soir.
- **Ventes :** brief KPI de 08:44 = **0 € sur sa fenêtre de 24 h**, pas sur la
  totalité du 16/10. **Cumul du projet indisponible (attribution Stripe
  incomplète)**. Les quatre veilles silencieuses ne constituent pas la preuve
  d'un cumul nul ; aucune donnée de paiement hors projet publiée.
- **HTTPS à 21:02 :** accueil, version, news-sitemap, B2B, échantillon, PDS et
  flux Bluesky répondent 200. Build annoncé 18:43:36 UTC ; news-sitemap avec
  **229 URL**, dernière date de publication déclarée 18:43:29 UTC. Les pages
  podcast, RSS podcast et mentions légales répondent 404. Sur `/b2b/`, les
  formulations « alertes sous 30 minutes », « la seule rédaction » et
  « 0 € encaissés » sont toujours présentes : présence constatée, pas véracité.

### Décisions et prochain relais

1. **Priorité du 17/10 : intégrer page/RSS podcast**, à partir du lot réconcilié
   du 16/10, adapté aux deux épisodes indexés ; préserver les téléchargements
   B2B, revalider sur la nouvelle base puis cloud/HTTPS. Ne pas attendre YouTube.
2. **Corriger les promesses B2B avant toute approche** et compléter les mentions
   et modalités/canal de reversement. L'identité fiscale du vendeur reste non
   validée ; HTTP 200 et préparation d'une cible ne lèvent aucun garde-fou.
3. Terminer l'audit des dates JSON-LD, puis autoindex/archives ; avancer la
   newsletter locale sans envoi et réconcilier Skool depuis une session
   authentifiée. Réemployer les lots prêts plutôt que produire de nouveaux plans.
4. **Un seul blocage humain prioritaire : vendeur B2B/TVA**, en remplacement de
   la demande GSC prioritaire d'hier (celle-ci demeure ouverte dans P1).
   Message exact : « Maël, pour débloquer la prospection B2B du Crabe, confirme
   en une réponse l'entité qui doit facturer (raison sociale + SIREN) et son
   régime de TVA. Aucun contact commercial ne part avant cette validation et
   la levée des autres prérequis. » L'email **URGENCE** à l'adresse convenue doit
   partir si ce blocage empêche l'étape commerciale ; **brouillon préparé,
   non envoyé**, destinataire exact hors dépôt public. Bilan local uniquement,
   jamais Discord. Ni accord déduit du silence ni vendeur déduit du paiement.

**Preuves de cette revue :** dossier privé
`crabe-chantiers/gouvernance/2026-10-16/` (`revue-2100.json`, réponses cron,
export GitHub brut, empreintes et réponses HTTPS). Aucun lot de test, prospect,
secret ou donnée privée de paiement ajouté au dépôt ; seules cette entrée et
la roadmap sont modifiées.
