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

La validation locale ne vaut ni publication HTTPS ni clôture du pipeline cloud.
Les preuves de livraison sont consignées après relecture des cibles.
