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

La recette locale ne vaut pas confirmation de publication : contrôle distant
Git, workflow et HTTPS à consigner séparément. Les conflits du clone partagé et
les interruptions FTP antérieures restent hors périmètre de cet ajout.
