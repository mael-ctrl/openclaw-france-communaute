# Veille LangGraph — 18 novembre 2026

## Une amélioration

Ajout du flux officiel `https://github.com/langchain-ai/langgraph/releases.atom`,
libellé « LangGraph (releases, préversions incluses) », anglais, priorité 3.
Les **36 sources précédentes** restent identiques et dans le même ordre ;
le catalogue, l'export OPML et le compteur de Transparence passent à **37**.
Réemploi du collecteur et des générateurs existants, sans dépendance nouvelle.

Effet attendu : mieux couvrir les évolutions des graphes d'agents et de leurs
composants (checkpoints, SDK, CLI), depuis leurs notes de versions primaires,
en complément du blog LangChain déjà suivi. Aucune promesse de trafic ou de
publication automatique de chaque release ; ce n'est pas un audit de sécurité.
La fenêtre de trois jours, les filtres, quotas et plafond de 30 €/mois restent
inchangés. La priorité ne départage que les dates égales.

## Qualification GitHub et flux

- Dépôt : [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph),
  déjà repéré dans la chasse précédente, requalifié le 18 à 13:48 UTC.
- Révision : `84ced603d3a201ab0f9379936bb35868e243f3f3` ; dernier push observé
  via l'API : `2026-11-18T08:34:22Z`.
- Licence MIT lue dans le [LICENSE épinglé](https://github.com/langchain-ai/langgraph/blob/84ced603d3a201ab0f9379936bb35868e243f3f3/LICENSE),
  octets contrôlés contre le blob `fc0602feecdd6748623c852ab534e1ca612673c7`.
  Aucun code amont copié, installé ou exécuté : seule l'adresse Atom est ajoutée.
- HTTPS strict : HTTP 200, `application/atom+xml`, 42 408 octets, SHA256
  `609c93b9721987f200bba2822759438d91fb697b5b282ff9652a0da9705ca21e`.
- Dix entrées datées et liées au dépôt, lues par le vrai parseur sur les octets
  conservés. Dernière date : `2026-11-14T01:43:55+00:00` ; **aucun candidat
  dans la fenêtre courante de trois jours**. Ajout prospectif, sans redatation
  ni élargissement de fenêtre. L'activité Git n'est pas la fraîcheur du flux.

## Recette locale et préservation

Base `cfbef2806aa42c5c3173fa0a28438357df2bf3e3`. Pull rebase réussi dans un
worktree propre hors Bureau. Bureau inaccessible depuis le cron et conflits
préexistants du clone partagé préservés ; aucune résolution automatique.

`tests/test_source_langgraph.py` : rouge avant ajout, vert après ; source unique,
libellé explicite, export fidèle du catalogue et compteur cohérent.
**396 tests Python réussis**, puis `engine/run.py --essai --sans-redaction`
dans une copie isolée : code 0, 2 610 pages, zéro rédaction payante, transfert
ou publication sociale. Clé chargée uniquement pour consulter le solde, sans
l'afficher. HN OpenClaw a subi une connexion réinitialisée ; LocalLLaMA 404,
L'Usine Digitale 403 et Reddit Claude 429 : le succès du build ne valide pas
la disponibilité de tous les flux tiers.

Les 60 fichiers de preuves/publications sont inchangés et le préfixe du journal
est intact ; aucune donnée de recette importée en production.
Export OPML construit identique au générateur, SHA256
`8bf1b235ea33e03675c1c8f33427835a80df1b58eb69914803d9625d3d0e5876`.
Pièces privées : `crabe-chantiers/croissance/2026-11-18-langgraph/evidence/`.

Au commit initial, livraison HTTPS et relais cloud restent à confirmer.
