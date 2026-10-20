# Aide à l’abonnement RSS — croissance du 20 octobre 2026

## Une seule amélioration

Un mode d’emploi dépliable « Première fois avec un flux RSS ? » est ajouté au bloc de suivi en fin de brève et d’article. Il explique l’écran XML, l’ajout dans un lecteur et le choix entre le flux général et les articles seuls. Les deux adresses sont du texte sélectionnable. Le `<details>` natif fonctionne sans JavaScript, est fermé au départ et ne remplace aucun bouton existant.

Aucun compte, formulaire, tracker, email ou abonnement tiers n’est créé. Le lecteur externe peut avoir ses propres conditions, un compte ou un coût : le texte le précise. Les flux XML, leurs GUID, les dates, les sources et les textes éditoriaux restent inchangés.

**Hypothèse de croissance :** réduire l’incompréhension devant un flux XML et faciliter le retour des lecteurs. Aucun nouvel abonnement ni gain d’audience n’est mesuré par cette livraison.

## Chasse GitHub et décision de réemploi

Recherche `gh search repos 'rss reader'` et métadonnées API le 20/10/2026 :

| Dépôt | Licence API | Dernier push API | Décision |
|---|---|---|---|
| [miniflux/v2](https://github.com/miniflux/v2) | Apache-2.0 | 20/10/2026 01:03:34 UTC | Lecture de `internal/template/templates/views/add_subscription.html` : ajout d’un flux par son URL. Concept confirmé, aucun code copié ni logiciel installé. |
| [FreshRSS/FreshRSS](https://github.com/FreshRSS/FreshRSS) | AGPL-3.0 | 20/10/2026 07:52:31 UTC | Alternative repérée, non adoptée ; pas d’import de code copyleft. |

Réemploi retenu : `bloc_suivre()` et les styles `.prose` déjà présents. Texte français original, HTML natif, aucune dépendance nouvelle.

## Recette avant publication

- Bureau inaccessible à Git depuis le cron ; clone isolé hors Bureau, pull réussi, base **`278d060194a1fe46c674b2688eabf403aa32b522`**. Aucun changement local illisible repris et aucun dépôt partagé réparé.
- Contrat `tests/test_aide_rss.py` observé rouge (mode d’emploi absent), puis vert. **165 tests Python et 4 tests Node réussis** dans une copie isolée.
- Deux builds complets à la même horloge : **1 313 pages éditoriales modifiées uniquement par l’ajout du bloc**, **1 371 autres sorties identiques** ; **347 fichiers de données préservés**. Ni CSS ni JavaScript modifiés.
- Vrai `engine/run.py --essai --sans-redaction` réussi dans une autre copie : 10 éléments collectés, zéro rédaction, transfert ou post ; préfixe du journal intact et sceaux identiques. Collecte partielle : deux flux Hacker News en 502, Siècle Digital en 403 et Reddit Claude en 429. Ces échecs amont sont conservés, pas présentés comme corrigés.
- Chromium isolé, JavaScript désactivé : deux pages réelles à **360, 390 et 1 440 px**, ouverture souris, fermeture Entrée, réouverture Espace, deux adresses exactes et navigation vers le flux articles contrôlées. Pas de débordement horizontal du document ou du nouveau contenu. L’en-tête mobile existant est haut ; l’accès demande un défilement, pas de promesse de visibilité immédiate.
- Le premier lanceur navigateur a expiré dans `addStyleTag` ; remplacement de cette seule injection de style de capture par une insertion DOM puis recette rejouée avec succès. Aucun changement applicatif pour masquer l’échec.

Preuves privées : `crabe-chantiers/croissance/2026-10-20-aide-rss/` (copies, comparaison, logs, captures et scripts de recette). Les données et sites de recette ne sont pas intégrés au dépôt.

## Production

**Livré et vérifié le 20/10/2026 à 14:44 CEST.**

- Code : **`8719835b8a5b0bae18c127625dff72d2763ede03`** ; trois fichiers poussés puis relus octet pour octet sur `main`.
- [Run `39420136195`](https://github.com/mael-ctrl/openclaw-france-communaute/actions/runs/39420136195) réussi : **165 tests Python**, **1 385 fichiers envoyés**, IndexNow 200 ; sauvegarde **`a8c767c1ed45c8ac32479e7cc51952d2a09a2c6b`**, fusion `33eb62a`. L’acceptation IndexNow ne prouve pas l’indexation.
- **Trois HTML HTTPS complets identiques au rendu des données sauvegardées** : brève récente, article et dernière brève du tableau de données. **Deux flux RSS comparés** au même commit (seul `lastBuildDate` volatile neutralisé) ; `version.txt` identique aux deux bornes.
- Recette Chromium sans JavaScript rejouée **sur la production** : deux pages × trois largeurs (360/390/1 440 px), souris/Entrée/Espace, adresses et navigation vers le flux articles vérifiées ; captures mobile et desktop relues.

Les données courantes du média ont avancé pendant l’attente ; la comparaison HTTPS utilise le commit de sauvegarde du run, pas les données de la recette locale. Un chantier indépendant du kit Hermes est arrivé sur `main` pendant ce délai : il n’est ni intégré ni revendiqué comme action de cette mission.

La couverture est celle des pages reconstruites depuis les données conservées, pas de toutes les anciennes URL ; les trois pages lues en HTTPS ne constituent pas une relecture exhaustive des HTML distants. Aucun gain d’abonnés, de rétention ou d’audience établi.
