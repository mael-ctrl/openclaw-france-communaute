# Politique du hub gratuit — correction technique du 24/10/2026

Une seule intégration, priorité P2 de la roadmap : retirer les descriptions
techniques obsolètes du parcours payant sur `/politique-de-confidentialite/`.
Les grands aperçus, couvertures, dates JSON-LD, archives, clavier et RSS sont déjà
intégrés ; le garde de concurrence n'est pas prêt à activer. Les archives inconnues
et l'alias OVH restent distincts. Aucun lot commercial n'est importé.

## Périmètre

- Téléchargement direct, sans compte, formulaire ni paiement : ne plus décrire
  une collecte Qonto ou une livraison du kit par email comme parcours actuel.
- Distinguer journaux OVH bruts/cache local, agrégats et analyse dans le navigateur.
  Pas d'affirmation « zéro cookie » ni de suppression de données anciennes.
- Décrire l'origine OVH et le proxy Cloudflare ; requalifier le retrait des appels
  Tailwind, Font Awesome et Google Fonts livré le 23, sans réintroduire ces appels.
- Date technique réelle et réserve explicite sur les clauses juridiques héritées.
  Responsable, bases légales, durées, droits et garanties restent à valider.
  Les sections existantes non concernées sont conservées, pas certifiées.
- Sitemap : seule la date de cette URL change. Kits, mentions légales, CSS,
  métadonnées, liens et infrastructure restent intacts.

## Réemploi et provenance

Lot privé du 23 relu : 108 pièces, son manifeste et 11 pièces parent conformes.
Patch appliqué par hunks sur `7313eda`, requalifié pour le retrait des CDN.
Dépôts de méthode revérifiés le 24 : [webbkoll](https://github.com/andersju/webbkoll)
(MIT à la racine, dernier push observé 18/11/2022 ; fichiers particuliers pouvant
être MPL-2.0) et [blacklight-collector](https://github.com/the-markup/blacklight-collector)
(GPL-3.0, 03/09/2026). Aucune copie ni dépendance amont ajoutée : tests stdlib et
réemploi du patch interne seulement. Une inspection statique n'est pas un audit
juridique ni une preuve d'absence de cookies en toutes circonstances.

## Recette locale avant publication

- Quatre contrats ciblés échouent avant et passent après ; suite complète :
  **211 tests Python + 4 Node réussis** sur la base préparatoire.
- Deux vrais builds isolés de **1 753 pages**, 3 503 sorties chacun : seules
  les horloges de feed.xml, feed-articles.xml et version.txt diffèrent entre
  les instants de construction ; le hub est publié séparément du média.
- Données de la copie intactes ; identité de l'en-tête, du footer, des liens et
  des sections juridiques non visées comparée à Git.
- Six configurations Chrome locales : 360/390/1 440 px, JavaScript activé ou
  désactivé, sans débordement ; retour accueil au clavier fonctionnel.
- Préflight SFTP : clé hôte épinglée avant authentification, deux cibles et
  trois témoins (mentions et deux ZIP) sauvegardés et exactement égaux à Git.

## Publication

- Code **`f9a8893`**, trois blobs de code relus exactement sur GitHub.
  Les pushes refusés pour travaux parallèles ont été conservés ; rebase ciblé,
  aucune fusion forcée de données. Le sitemap reprend les dates voisines des kits.
- Recette combinée finale : **218 tests Python + 4 Node réussis**. Deux builds
  isolés sur le parent `2cc331c`, à horloge commune : **3 504 sorties du média
  identiques**, **443 fichiers de données intacts**. Le hub est hors de ce build.
- **Hub publié le 24 à 17:33:56 UTC** : deux fichiers envoyés par SFTP et relus
  octet pour octet. Mentions légales et deux ZIP témoins inchangés ; snapshot de
  base refait après la livraison voisine, avant toute écriture.
- À **17:35:25 UTC**, **huit URL HTTPS en 200** : corps principal exact après
  seul décodage du contact public Cloudflare ; sitemap et deux ZIP exacts.
  Les quatre tests de politique passent aussi sur la réponse publique capturée.
- **Six configurations publiques Chrome** (360/390/1 440 px, JS activé/désactivé)
  passent : pas de débordement, styles lisibles, retour accueil au clavier.
  La protection email Cloudflare reste héritée : sans JS, elle affiche
  `[email protected]`. Ce test n'affirme pas un contact mail utilisable sans JS.
- **Validation cloud non acquise au relevé 2026-10-24T17:53:12.802634+00:00** : le
  [run 40116677135](https://github.com/mael-ctrl/openclaw-france-communaute/actions/runs/40116677135)
  est `in_progress`, job depuis 17:44 UTC, aucune étape exposée et logs directs
  404. Deux attentes bornées n'en font pas un échec du code, ni un succès.
  Le run antérieur `40115442150`, bloqué à « Set up job » depuis 17:17 sans
  checkout/pipeline annoncé, a été annulé ; annulation relue `completed/cancelled`.
  Aucun workflow ni cron modifié. Ne pas relancer aveuglément ce déploiement :
  relire l'issue du run avant de décider d'une reprise sur main courant.

Le déploiement effectif du hub et ses recettes sont confirmés indépendamment
du workflow média, dont le démarrage reste bloquant pour la recette cloud
exigée. Aucune conformité juridique, hausse d'audience ou installation des kits
n'est revendiquée.

Preuves privées : `crabe-chantiers/integration-site/2026-10-24-politique/`.
