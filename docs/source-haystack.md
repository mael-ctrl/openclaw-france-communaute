# Veille Haystack — 26 novembre 2026

## Une amélioration

Ajout du flux primaire `https://github.com/deepset-ai/haystack/releases.atom`,
libellé « Haystack (releases, préversions incluses) », anglais, priorité 3.
Les 43 sources précédentes restent identiques et dans le même ordre ; le catalogue,
l'export OPML et le compteur de Transparence passent à 44 sources.

Effet attendu : compléter la veille des agents par les versions de Haystack,
framework de pipelines de recherche documentaire et de génération augmentée par
récupération (RAG). Aucun gain d'audience mesuré. Collecteur et projections existants
réemployés, sans dépendance ni code amont ajoutés. Fenêtre de trois jours, quotas et
plafond DeepSeek de 30 €/mois inchangés. La priorité départage les dates égales :
ce n'est ni un quota par source ni un filtre des préversions.

## Qualification amont

- Dépôt : [deepset-ai/haystack](https://github.com/deepset-ai/haystack).
- Révision consultée : `a63cb9072db4c2e9daf1359141f431e30f46dfaf`.
  Dernier push API observé : `2026-11-26T11:57:47Z`.
- Licence API et [LICENSE épinglé](https://github.com/deepset-ai/haystack/blob/a63cb9072db4c2e9daf1359141f431e30f46dfaf/LICENSE) : Apache-2.0.
  Octets vérifiés contre le blob Git `6fb66d8d5fa55912ee80f4fdab94cab99140c448`.
  Logiciel non installé ni exécuté ; seule l'adresse du flux est utilisée.
- HTTPS strict le 26 novembre à **13:05 UTC** : HTTP 200, 158 242 octets,
  SHA256 `db8d1a52365834c0ced1c9852d54ae757ca98a9e00162dfa33d6635f604d5c14`.
- Vrai parseur du média sur les octets conservés : dix entrées, **aucune dans la
  fenêtre de trois jours**. Dernières dates lues : 10 novembre. Ajout prospectif,
  sans redatation ni élargissement de fenêtre pour fabriquer une actualité.
  Les titres comportent des préversions `rc`, explicitement signalées par le libellé.

## Validation locale

Base : `4ea42308632bf8fe13e57e96e08eb4a547ee94ed`.
Clone partagé en rebase conflictuel laissé intact ; travail hors Bureau dans un
worktree neuf sur `origin/main`, avec pull rebase réussi dans ce seul arbre.
Rapport et manifeste de la vague du 26 lus. Aucun candidat moteur privé, cache,
verrou ou wrapper de cette vague intégré ; les défauts d'exploitation restent
un chantier distinct.

`tests/test_source_haystack.py` : rouge avant ajout, vert ensuite (unicité,
projection OPML exacte et compteur). **467 tests Python réussis** dans une copie
séparée, puis vrai `engine/run.py --essai --sans-redaction` réussi : **2 659 pages**,
zéro rédaction payante, transfert ou publication sociale. Clé utilisée seulement
pour la lecture du solde, jamais affichée. Erreurs tierces conservées : HN agents
(502), LocalLLaMA (404), L'Usine Digitale (403), Reddit Claude (429).

Les 65 fichiers de preuves/publications contrôlés sont identiques et le préfixe
du journal intact ; aucune donnée de recette reprise dans le dépôt.
OPML candidat : 5 492 octets, SHA256
`a6e18429ab34f244c78b9d89d5fca827af56b1064ebab87489d37235670fb0f8`.
Pièces privées : `crabe-chantiers/croissance/2026-11-26/`.

## Livraison ciblée vérifiée

Code livré : **`7c6a77d38e5b2d383e48e4e58cf89fc6d38ac2c1`**. Les trois fichiers
ciblés ont été relus sur `main` par l'API GitHub : octets identiques au local.
Dispatch unique : `45827218891`. À **14:15 UTC**, contrats cloud réussis,
pipeline en cours et sauvegarde en attente ; aucune clôture cloud revendiquée.
Le run précédent `45823840501` est terminé annulé pendant le pipeline, sauvegarde
sautée. Nous n'avons annulé aucun run ni relancé le dispatch.

**Régression réobservée :** l'export public et le compteur sont de nouveau à
28 sources au premier relevé, au lieu des 43 vérifiées la veille. Le premier
préflight SFTP refuse cette base, sans écriture. Son OPML correspond octet pour
octet au catalogue historique `0bcc84f0cb89cf2847d31e2b5496c23f416f2789`.
L'origine de cette remise en ligne n'est pas établie par ce rapprochement.

Préflight séparé à **13:43 UTC**, après la fin du run à l'ancien catalogue :
inventaire paginé des cinq statuts actifs complet ; seul le nouveau run à
44 sources actif ; aucun pipeline local détecté. Ces sondes ne constituent pas
un verrou transactionnel. Clé hôte vérifiée avant secret, cibles sauvegardées,
bases SFTP/HTTPS exactes, upload `.part` puis renommage : **deux fichiers seulement**.
Restauration des 15 sources antérieures manquantes et ajout Haystack dans l'OPML ;
remplacement du seul compteur **28 → 44** dans la page Transparence, tous ses autres
octets préservés. Aucun déployeur intégral, cache, wrapper ou conflit Git modifié.

Relectures SFTP exactes après écriture ; première comparaison HTTPS discordante
conservée, **sans nouvelle écriture**. À **14:15:14 UTC**, recontrôle en lecture
seule : deux passages SFTP + HTTPS strict identiques aux deux cibles attendues,
44 couples nom-URL et compteur exacts, témoins `.htaccess` racine/veille/CORS Skool
inchangés. L'écart initial ne suffit pas à attribuer une cause de cache.
Preuve privée : `recontrole-01/result.json` sous le chantier du jour.

La publication ciblée est vérifiée ; la régression d'exploitation et la clôture
cloud restent distinctes de cet ajout. Aucun gain de trafic ou de publications
Haystack déduit : cette nouvelle source est prospective.
