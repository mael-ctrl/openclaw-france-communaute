# Veille Langflow — 25 novembre 2026

## Une amélioration

Ajout du flux primaire `https://github.com/langflow-ai/langflow/releases.atom`,
libellé « Langflow (releases, préversions incluses) », anglais, priorité 3.
Les 42 sources précédentes restent identiques et dans le même ordre ; le catalogue,
l'export OPML et le compteur de Transparence passent à 43 sources.

Effet attendu : compléter la veille des bibliothèques d'agents par les versions
d'un outil de construction visuelle de workflows IA. Aucun gain d'audience mesuré.
Collecteur et projections existants réemployés, sans dépendance ni code amont
ajoutés. Fenêtre de trois jours, quotas et plafond DeepSeek de 30 €/mois inchangés.
La priorité départage les dates égales : ce n'est ni un quota par source ni un
filtre des préversions. Le libellé signale les versions de développement.

## Qualification amont

- Dépôt : [langflow-ai/langflow](https://github.com/langflow-ai/langflow).
- Révision consultée : `6c9aea6f5d5f47a76a25e8e3e1b4779a4f83d522`.
  Dernier push API observé : `2026-11-25T13:20:08Z`.
- Licence API et [LICENSE épinglé](https://github.com/langflow-ai/langflow/blob/6c9aea6f5d5f47a76a25e8e3e1b4779a4f83d522/LICENSE) : MIT.
  Octets vérifiés contre le blob Git `ee3d6be71bdd1b5e4cc5b85da4a4aabc7bfe3347`.
  Logiciel non installé ni exécuté ; seule l'adresse du flux est utilisée.
- HTTPS strict le 25 novembre à **14:37 UTC** : HTTP 200, 29 297 octets,
  SHA256 `e4371b4c28bfdd82dbff59773152ff01b37e3bbf7cb3246f725863ce5ddf183b`.
- Vrai parseur du média sur les octets conservés : dix entrées, quatre dans la
  fenêtre de trois jours. Parmi elles, trois préversions `v1.14.0.dev36` à
  `dev38` et la release `1.13.4`. Dates d'origine conservées ; ce sont des
  candidats de collecte, pas quatre nouvelles publications revendiquées.

## Validation locale

Base : `26f2a676ee648e8dc94a060880b9124eeb416187`.
Pull au Bureau tenté, refusé avec `Resource deadlock avoided`. Clone partagé en
rebase conflictuel laissé intact. Worktree neuf sur `origin/main`, pull rebase
réussi dans ce seul arbre ; rapport et manifeste de la vague du 25 lus. Aucun
candidat moteur privé, cache ou verrou de cette vague intégré.

`tests/test_source_langflow.py` : rouge avant ajout, vert ensuite (unicité,
projection OPML exacte et compteur). **444 tests Python réussis** dans une copie
séparée, puis vrai `engine/run.py --essai --sans-redaction` réussi : **2 659 pages**,
zéro rédaction payante, transfert ou publication sociale. La clé n'est utilisée
que pour la lecture du solde, jamais affichée. Les erreurs tierces LocalLLaMA
(404), L'Usine Digitale (403) et Reddit Claude (429) restent visibles.

Les 65 fichiers de preuves/publications contrôlés sont identiques et le préfixe
du journal intact ; aucune donnée de recette reprise dans le dépôt. OPML candidat :
5 351 octets, SHA256 `9eed936c79de5a11e6e5d610a5f67ad9569c244048d573787ffb88d71c653f9f`.
Pièces privées : `crabe-chantiers/croissance/2026-11-25/`.

## Livraison vérifiée et régression distante conservée

Code livré : **`25b927c1fe9f9e6bb241220044e26bbe9b7eb4f3`**. Les trois fichiers
ciblés ont été relus par l'API GitHub sur `main` : octets identiques au local.
Dispatch unique `45636975809`, ensuite annulé en attente sans job. Successeur
`45638350597`, SHA `2c888549f016040aea687ed081d52dd99894b87d` : ascendance et
identité des fichiers vérifiées, contrats réussis. À **15:30 UTC**, pipeline
encore en cours, sauvegarde en attente : aucune clôture cloud revendiquée.

Le run précédent `45631208375` s'est terminé annulé pendant le pipeline à
14:55:58 UTC, sauvegarde sautée. Le watcher avait rencontré une erreur réseau
GitHub ; les lectures API ultérieures ont rétabli le constat, sans nouveau
dispatch ni annulation d'un run actif par cette mission.

**Premier préflight SFTP refusé, aucune écriture :** l'OPML distant et le compteur
étaient revenus à **28 sources**, pas les 42 du parent attendu. Les couples
nom-URL correspondent exactement au catalogue historique
`0bcc84f0cb89cf2847d31e2b5496c23f416f2789`. Ce rapprochement ne prouve ni la date
ni la cause de sa remise en ligne. Les corps et le refus sont conservés dans
`livraison/`, sans réécriture des preuves.

Préflight distinct à **15:29 UTC** dans `livraison-requalifiee/` : base historique
exacte confirmée en SFTP et HTTPS ; inventaire paginé des cinq statuts actifs
complet, seul le successeur à 43 sources actif ; aucun éditeur local du pipeline
détecté. Ces sondes ponctuelles ne sont pas un verrou transactionnel.

Clé hôte vérifiée avant secret, cibles sauvegardées, transfert `.part` puis
renommage de deux fichiers seulement : l'OPML courant (restauration des 14 sources
antérieures manquantes, plus Langflow) et **le seul compteur 28 → 43** de la page
Transparence. Tous ses autres octets, dont ses autres statistiques, sont préservés.
Aucun déployeur intégral ni modification des caches, wrappers ou conflits Git.

À **15:30:25 UTC**, recontrôle en lecture seule : deux passages SFTP + HTTPS strict
confirment les octets attendus, les **43 couples nom-URL**, le compteur et les
témoins `.htaccess` racine/veille/CORS Skool inchangés. OPML : 5 351 octets,
SHA256 `9eed936c79de5a11e6e5d610a5f67ad9569c244048d573787ffb88d71c653f9f`.
Preuve privée : `recontrole-01/result.json` sous le chantier du jour.

La publication ciblée est confirmée ; la régression d'exploitation reste signalée,
non attribuée et non résolue par cet ajout. Les conflits du clone partagé et la
sauvegarde cloud restent distincts. Aucun gain d'audience déduit.
