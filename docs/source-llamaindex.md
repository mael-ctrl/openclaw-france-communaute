# Veille LlamaIndex — 27 novembre 2026

## Une amélioration

Ajout de la source primaire `https://github.com/run-llama/llama_index/releases.atom`,
libellée « LlamaIndex (releases, préversions incluses) », anglais, priorité 3.
Les 44 sources antérieures sont conservées à l'identique et dans le même ordre ;
le catalogue et ses projections OPML/compteur passent à 45 sources.

Effet attendu : élargir la veille des outils de traitement documentaire, RAG et
agents connectés aux données. Aucun gain d'audience mesuré. Réemploi du collecteur
et des projections existants, sans code amont ni dépendance ajoutés. Fenêtre de
fraîcheur de trois jours, quotas et budget DeepSeek de 30 €/mois inchangés.
La priorité ne départage que les dates égales ; elle ne réserve pas de quota et
ne filtre pas les préversions.

## Qualification de la source

- Dépôt : [run-llama/llama_index](https://github.com/run-llama/llama_index).
- Révision consultée : `40d4f79eb9d8f68430692d0cc156483ca2d7f4f6` ; dernier push
  observé par API : `2026-11-26T17:46:19Z`.
- Licence MIT, confirmée par API et lecture du
  [LICENSE épinglé](https://github.com/run-llama/llama_index/blob/40d4f79eb9d8f68430692d0cc156483ca2d7f4f6/LICENSE),
  octets vérifiés contre le blob Git `e6074042d0391061b7d7d45d21e6693ae108daec`.
  Le logiciel n'a été ni installé ni exécuté ; seule l'adresse du flux est utilisée.
- HTTPS strict à **13:02:49 UTC** : HTTP 200, 805 595 octets ; SHA256
  `f0136df93e211cc28ef088f590acd230fca0fd52c341e3b6a2c044da860496a0`.
- Vrai parseur du média sur les octets conservés : dix entrées, aucune dans la
  fenêtre de trois jours ; dernière date lue le 13 novembre, version `v0.14.26`.
  Ajout prospectif, sans redatation ni élargissement de fenêtre.

## Recette locale

Base de recette : `3b658c9fc12128fe4e8788247e7e5c4bfe9e69d8`.
Bureau illisible depuis le cron ; clone partagé en rebase conflictuel laissé
intact. Worktree neuf sur `origin/main`, pull rebase réussi uniquement dans cet
arbre. Rapport et manifeste du 27 novembre lus ; aucun candidat moteur, cache ou
reprise Git de la vague n'est intégré à cet ajout.

Contrat `tests/test_source_llamaindex.py` : échec attendu avant ajout puis succès
(unicité, projection OPML exacte, compteur). Suite complète dans une copie
isolée : **475 tests Python réussis**. Vrai `engine/run.py --essai --sans-redaction`
réussi : **2 659 pages**, zéro rédaction payante, transfert ou publication sociale.
Clé chargée uniquement pour la lecture du solde, jamais affichée. Erreurs tierces
conservées : les deux flux HN (502), LocalLLaMA (404), L'Usine Digitale (403),
Reddit Claude (429). Le nouveau flux n'a pas échoué, mais fournit zéro candidat
récent lors de cet essai.

Les 65 fichiers de preuves/publications contrôlés sont inchangés et le préfixe du
journal est intact ; aucune donnée de recette reprise dans Git. Les conflits et
les expirations du déploiement général restent des problèmes distincts de cette
amélioration. Pièces privées : `crabe-chantiers/croissance/2026-11-27/`.

## Livraison vérifiée

Commit de code : **`cd1200c26583ea409d93354a4b7a545d015b7de9`**. Le premier push
a rencontré une réinitialisation de connexion ; la lecture distante a confirmé
l'absence du commit, puis une nouvelle tentative non forcée a réussi. Le rebase
avait intégré la livraison voisine des fichiers d'extraits Pack ; **477 tests**
ont ensuite réussi dans la copie de recette combinée. Aucune modification du
Pack par cette mission. Les trois blobs ciblés ont été relus identiques sur
`main` distant par l'API GitHub.

À **13:38 UTC**, export et compteur distants encore à 44, conformes au parent,
sans la régression à 28 observée hier. Préflight paginé des cinq statuts actifs :
seul le dispatch **`46007897692`**, au catalogue courant, est actif ; aucun
pipeline local détecté. Ces sondes ne constituent pas un verrou transactionnel.
Le run antérieur `46002010790` est terminé annulé pendant le pipeline, sauvegarde
sautée ; le run `46003605934` est annulé sans job. Aucun run annulé par cette mission.

Clé hôte épinglée vérifiée avant secret, sauvegardes exactes et bases HTTPS/SFTP
comparées : livraison de **deux fichiers seulement**, par `.part` puis renommage.
L'OPML comporte 45 couples nom-URL ; seul le compteur **44 → 45** a changé dans
la page Transparence, tous ses autres octets étant préservés. Témoins racine,
veille et CORS Skool inchangés. Aucun déployeur intégral ni modification de cache,
wrapper ou conflit Git.

À **13:38:42 UTC**, relecture SFTP exacte puis deux passages HTTPS strict identiques :
- `/veille/sources.opml` : 5 637 octets, SHA256
  `2c6f39d112e434378d7e5bc2ba919caac19b4ed51a6963f422bd0c3abdd64873` ;
- `/transparence/` : 20 544 octets, SHA256
  `1cd32b053f8293e9d280f56ed041222d6f43d9f2bcd799931f3622ecff3bfd2a`.

À **13:39 UTC**, contrats cloud réussis, pipeline en cours et sauvegarde en attente.
Le journal complet du job actif n'est pas encore disponible ; aucune clôture
cloud ni publication d'une actualité LlamaIndex revendiquée. Livraison ciblée
confirmée indépendamment de ce pipeline. Pièces : `livraison/https-result.json`,
`remote-01/result.json` et `cloud-01/summary.json` sous le chantier du jour.
