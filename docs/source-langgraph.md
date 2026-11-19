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

Au commit initial, livraison HTTPS et relais cloud restaient à confirmer.

## Intégration et livraison — vérification terminée le 19 novembre

Deux pushes ont été refusés après des livraisons voisines. Rebase du seul ajout
sur les commits voisins, sans toucher au clone partagé : **399 tests réussis**
après intégration du podcast et du correctif du guide ; la dernière avancée
ne touchait que `docs/monetisation.md`. Contrat LangGraph rejoué avant push.
Commit de configuration : `0646bf88e0895e0836417230b6e452e69c68eeaa` ; ses trois
blobs relus identiques par l'API GitHub sur `main`.

Dispatch `44318944671` effectué le 18 à 13:56 UTC, ensuite annulé sans job.
Le run précédent `44317447293` a été annulé **pendant son pipeline** le 18 à
14:33 UTC, sauvegarde sautée : ce n'est pas une simple attente annulée.
Les observations suivantes sont du **19 novembre**, pas antidatées au 18.

Le premier préflight SFTP a refusé d'écraser un export déjà à 37 sources.
La lecture HTTPS suivante a pourtant servi 28 sources ; une seconde lecture
SFTP a ensuite confirmé ce catalogue ancien, identique à
`0bcc84f0cb89cf2847d31e2b5496c23f416f2789`. Les captures contradictoires sont
conservées : leur cause n'est pas établie et n'est pas attribuée au cache.

Nouveau préflight à 12:09 UTC, avec concordance SFTP/HTTPS et base historique
identifiée ; aucun ancien catalogue actif trouvé dans les statuts Actions
paginés. Le run actif `44521077410` contient déjà les 37 sources. Aucun pipeline
local observé au relevé ponctuel ; ces contrôles ne constituent pas un verrou.

Livraison ciblée des seuls `/veille/sources.opml` et compteur **28 → 37** de
`/transparence/`, rétablissant aussi les sources antérieures déjà intégrées.
Clé hôte vérifiée avant secret, sauvegardes exactes, fichiers `.part`, comparaison
de base avant renommage, relecture SFTP identique. Aucun autre octet de la page
Transparence ni règle `.htaccess` modifié. Une première comparaison HTTPS a
différé après écriture : refus conservé, puis relecture sans nouvel envoi.

**Deux lectures HTTPS canoniques exactes à 12:09:36–37 UTC le 19** : 37 flux,
LangGraph une seule fois, compteur 37 unique ; HTTP 200 et octets égaux aux
relectures SFTP. Export : empreinte inchangée ci-dessus. Transparence : SHA256
`81f8db62c0afd25cf3aa766bfaa1f1076d74e0892bdfcf97f33a8dc104dab00b`.
Preuves privées : `livraison-ciblee/`, `recontrole-20261119/`,
`livraison-requalifiee-20261119/`, `verification-finale-20261119/result.json`.

Publication publique confirmée. Le successeur cloud est encore en cours au
relevé : aucune réussite globale ni sauvegarde finale affirmée. Les conflits
du clone partagé restent distincts et non réparés. Aucune brève LangGraph ni
croissance d'audience déduite de l'ajout prospectif.
