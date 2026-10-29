# Recherche et filtres progressifs du fil et des archives

## Périmètre — chantier quotidien du 29 octobre 2026

Une seule intégration : le premier candidat **site** prêt du relais du 29 (`accessibilite/2026-10-29-filtres-actus`). Les couvertures, dates, catalogue des sources conservées et fermetures d'autoindex déjà livrés ne sont pas refaits. La réconciliation des chemins historiques inconnus et l'alias OVH restent distincts. Le wrapper local et la migration du cache FTP ne sont pas activés par ce chantier.

Le pull demandé dans le clone partagé a refusé sur six fichiers non fusionnés. Cet état est laissé intact ; worktree propre du même dépôt, pull réussi sur `b205fd38942febced5197d6a7add3e0c6b5d27ae`. Les trois fichiers de code visés sont identiques à la base préparatoire `d5f2d085e0e3d3c84cc7f5e294f7f11d7f99677a` ; 159 pièces de préparation relues et vérifiées par empreinte avant application des seuls patches code/tests.

## Comportement

- Le champ possède un libellé visible « Rechercher sur cette page » ; ce n'est pas un moteur de recherche de tout le site.
- Les boutons HTML natifs conservent leur nom et leur focus ; `aria-pressed` suit la sélection visuelle. Entrée/Espace restent natifs.
- Un statut poli expose le nombre de cartes visibles **sur cette page**, après interaction seulement ; les annonces de saisie sont espacées de 250 ms et une annonce obsolète est annulée lors du clic suivant.
- Sans JavaScript, les outils inopérants restent masqués ; toutes les cartes et la pagination HTML sont accessibles. Les règles CSS explicites préservent l'effet visuel de `hidden` sur la barre et les cartes.
- Tri, titres, liens, données, limites de page, catalogue et sitemap inchangés. Aucun compteur, transport, dépendance ou collecte supplémentaire.

## Réemploi et licences

Concepts uniquement, implémentation indépendante ; aucun code tiers copié ni exécuté :

- [`w3c/aria-practices`, bouton](https://github.com/w3c/aria-practices/blob/0f765e4dc33e966026114ac12a8380db1de3b787/content/patterns/button/button-pattern.html) — W3C Software and Document License ; push API du 14/10/2026 16:55:56 UTC.
- [`w3c/aria`, statut](https://github.com/w3c/aria/blob/35824ad3b14c40de289f274fbc43f36ce6d0b0f4/index.html#L9530-L9543) — W3C Document License ; push API du 28/10/2026 16:07:43 UTC.

Métadonnées reconsultées le 29 ; licences réelles lues, API `NOASSERTION` non assimilée à MIT. Provenance et octets épinglés conservés hors dépôt.

## Recette d'intégration réellement exécutée

- **Rouge :** nouveaux tests appliqués seuls, deux tests Python refusés (quatre assertions) et quatre Node refusés ; absence du statut, de l'état pressé et du montage progressif constatée.
- **Vert : 259 tests Python + huit Node**, suite originale non adaptée, sans échec ni skip. Contrats : `tests/test_filtres_actus.py`, `tests/test_filtres_actus.cjs` et suite existante.
- Deux appels complets à `construction.construire()` en copies scratch, à horloge commune : **4 112 fichiers, 4 090 identiques** ; seuls vingt HTML de listes et les deux assets JS/CSS changent. Les vingt HTML sont identiques après retrait de la seule barre d'outils. **568 fichiers data/contenus préservés**, dont journal et manifestes.
- Vrai `--essai --sans-redaction` dans une copie séparée, sans clé : code 0, six éléments collectés, aucune rédaction/FTP/publication sociale. Collecte partielle (403 Siècle Digital, 429 Reddit Claude) conservée ; **34 fichiers de preuves inchangés**, préfixe du journal intact. Aucune donnée de cette copie importée.
- **321 contrôles Chromium, douze configurations** : fil/archives à 320/390/1440 px avec/sans JS ; Tab, Shift+Tab, Entrée, Espace, clic, recherche combinée, zéro/retour et pagination. Octets du build complet utilisés, fixture vide privée séparée. Treize chargements externes avortés avant transport sous confinement réseau/écriture ; aucune mesure d'audience de recette envoyée. Captures mobile/desktop relues.

Preuves privées : `crabe-chantiers/accessibilite/integration-2026-10-29/` (logs rouge/vert, builds, essai, captures et arbres AX). Le navigateur expose les textes et états dans l'arbre d'accessibilité ; cela **ne prouve pas** une annonce vocale effectivement entendue sous VoiceOver/NVDA ni une conformité WCAG globale. Aucun gain d'audience revendiqué.

## Publication

**Au commit d'intégration :** code testé, publication cloud et contrôle HTTPS encore à effectuer. Le résultat sera ajouté après lecture du run, de sa sauvegarde et des octets réellement servis. Un succès ancien n'atteste pas la version publique actuelle ; les régressions possibles de la routine locale restent un risque distinct non corrigé ici.
