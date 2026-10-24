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

À compléter avec le commit, le workflow média, les deux relectures SFTP et la
recette HTTPS. Un workflow média vert ne publie pas le hub ; aucune conformité
juridique, hausse d'audience ou installation des kits n'est revendiquée.

Preuves privées : `crabe-chantiers/integration-site/2026-10-24-politique/`.
