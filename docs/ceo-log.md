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
