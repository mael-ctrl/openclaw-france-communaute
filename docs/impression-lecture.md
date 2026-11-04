# Impression des pages de lecture — 4 novembre 2026

## Périmètre et choix

Seule intégration fonctionnelle de ce chantier quotidien : une feuille d'impression pour les articles et brèves, sans JavaScript et sans changement du rendu écran. Candidat n° 1 du relais site du 4 novembre (`rapports/2026-11-04.md`), absent de la base propre `bca54c7c69f05895a59732e674d4f570c52b5881`. C'est le confort de lecture de la proposition SEO #12, pas une nouvelle intégration de couvertures, dates, auteur ou sommaire déjà livrés. Les inconnus historiques #5, minification/cache #6–7 et leurs préparations ne sont pas déclarés terminés.

Le `git pull --ff-only` du clone actif a refusé les fichiers non fusionnés. Aucun abort/reset/stash ni fusion des données : travail dans un worktree du même dépôt sur `origin/main`, où le pull a réussi. Ce contournement n'est pas une réparation de l'exploitation du clone partagé.

## Modification

- CSS exclusivement `@media print`, ciblée sur `.section-lecture article.lecture` : fond blanc, texte noir, typographie papier et retrait de la navigation, du sommaire et des invitations commerciales/sociales.
- Titres, textes, couvertures réelles, légendes, dates, sources et déclaration IA conservés. Les URL absolues des sources sont imprimées ; les brèves explicitent le nom du Crabe et son rôle IA sur le papier.
- Les sauts restent naturels, sans hauteur fermée ni page forcée. Le titre du bloc Sources reste avec sa première source ; ce complément a été ajouté après reproduction d'un titre isolé sur la page précédente dans les deux PDF d'articles.
- Aucun HTML, script, flux, GUID, date éditoriale, audio, paiement, métadonnée ou donnée historique modifié. Le manifeste, le Pack et le podcast servent de témoins hors périmètre print.

## Réemploi et licences

Recherche GitHub requalifiée le 4 novembre avant intégration :

- [h5bp/main.css](https://github.com/h5bp/main.css/blob/6d6a990596f67c4c0ad6e46c19388934452180db/src/_print.css) — MIT, dernier push observé **31/10/2026** ; séparation print, ombres, liens et pagination.
- [BafS/Gutenberg](https://github.com/BafS/Gutenberg/blob/cec4afe4bcdd9ee4789557a44d14fef0a8d890cb/scss/_reformat.scss) — MIT, dernier push observé **03/02/2024**, ancienneté assumée ; URL imprimée et principes de lecture papier.

Adaptation indépendante, aucun framework installé. Licences/code épinglés et OID conservés dans le lot préparatoire ; **1 481 pièces** du manifeste parent vérifiées avant reprise. Seuls CSS et contrats repris, jamais les données/PDF/fixtures synthétiques du lot. Le complément Sources est propre à cette intégration.

## Recette locale réellement exécutée

Base `bca54c7`, données figées ; cinq contrats print (rouge avant CSS puis vert, dont rouge séparé pour le titre Sources). **297 tests Python + huit Node réussis**, suite originale complète dans une copie isolée.

Deux builds complets `construction.construire()` à la même horloge de recette : **4 559 sorties**, dont **4 558 identiques** ; seule `assets/style.css` diffère (21 752 → 24 075 octets). **662 fichiers** de données, contenus et hub préservés. Le périmètre éditorial courant (**511 articles + 1 728 brèves**) respecte la structure ciblée, sans prétendre avoir imprimé chaque page.

**56 contrôles Chromium sans JS**, deux articles et deux brèves réels (les plus courts/longs en octets HTML de chaque type), leurs couvertures téléchargées localement et trois annexes témoins. Écran 320/1 440 px inchangé en pixels, DOM, styles et géométrie. Print : texte/date/source/mention IA visibles, images chargées et largeur contrôlée. Réseau externe refusé dans le navigateur confiné, aucune mesure d'audience émise.

**24 contrôles PDF**, huit pages éditoriales A4 relues visuellement : article long quatre pages, court deux pages, une page par brève. Titres Sources conservés avec la première source ; les paragraphes peuvent se poursuivre naturellement à la page suivante. Manifeste/Pack/podcast : texte et pagination inchangés (4/3/11 pages). Comparaison exacte des multiensembles alphanumériques éditoriaux et des URL, pas certification de l'ordre de lecture ni de toute la ponctuation PDFKit.

## Publication

**Au commit initial : recette locale terminée ; cloud et HTTPS encore à vérifier.** La clôture sera ajoutée avec le run exact, ses étapes de contrats/transfert/sauvegarde et la relecture des octets servis. Aucun résultat distant anticipé.

## Limites

`:has()` exige un moteur moderne ; Chromium 156 est le navigateur éprouvé. Pas de test d'imprimante physique, de tous les navigateurs ou paramètres du dialogue d'impression ; pas de certification PDF accessible. Les illustrations conservées consomment de l'encre. Cette recette vérifie présentation et conservation du contenu, pas sa véracité. Aucun gain d'audience, de conversion ou de classement revendiqué.

Preuves privées : `crabe-chantiers/integration-impression/2026-11-04/` (intégrité, rouge/vert, sélection, journaux, builds, captures, PDF) ; résultats finaux locaux sous `final-local/` et `browser-final/`. Les premiers rendus montrant le titre Sources isolé sont conservés sous `browser-local/`. Aucune preuve historique réécrite ; aucun changement de cron ou d'infrastructure.
