# Sources — édition du 26 novembre 2026

Script et voix synthétique produits par IA. Les huit dernières brèves ont été triées par `date_redac` décroissante au SHA `71d6f76b475ad1dbc032ad9cbe2cae5a6254ff1c` ; elles ont été rédigées les 24 et 25 novembre. Le script le précise et ne présente pas les annonces comme des sorties du 26. Sélection exacte conservée dans `breves-snapshot.json`.

## Sujets retenus et vérifications du 26 novembre

1. **Simon Willison**, brève `37e6d5e175f8cc99` : [Three LLM inflection points in twelve months](https://simonwillison.net/2026/Nov/24/llm-inflection-points/), billet du 24 novembre. Retour d'expérience personnel sur Claude Opus 4.5 et Claude Code, pas benchmark indépendant ni garantie générale. Article primaire relu en entier ; seules les informations de la brève sur le premier point de bascule sont résumées. Le bandeau sponsor WorkOS n'est pas repris comme contenu éditorial.
2. **LiteLLM**, brève `a01c6e94e4190e43` : [release v1.110.4](https://github.com/BerriAI/litellm/releases/tag/v1.110.4), API GitHub `published_at=2026-11-25T00:31:02Z`, `prerelease=false`. Note actuelle : nginx/zlib de l'image UI remis à jour, optimisation de lecture des clients restreints, procédure cosign. Les scans OSV/grype évoqués dans le résumé historique ne sont pas affirmés dans l'audio car la note actuelle relue ne les décrit pas. La signature ne vaut pas absence de vulnérabilité.
3. **Pydantic AI**, brève `6439efdc4fcbd054` : [release v2.74.0](https://github.com/pydantic/pydantic-ai/releases/tag/v2.74.0), API `published_at=2026-11-24T23:22:14Z`, distinct de la date du flux conservée dans la brève. `ComputerTool` exige une configuration ; correction des totaux de streaming Gemini via `OpenAIProvider` : baisse possible du coût rapporté, pas modification tarifaire. La note actuelle contient aussi des correctifs de sécurité : l'audio ne prétend pas couvrir tout le changelog. Aucune manipulation de logiciel client ni essai de ces fonctions n'est revendiqué.
4. **Codex**, brève `c15884125cadd7ab` : [rust-v0.174.0-alpha.5](https://github.com/openai/codex/releases/tag/rust-v0.174.0-alpha.5), API `published_at=2026-11-25T01:11:35Z`, `prerelease=true`. Corps limité à « Release 0.174.0-alpha.5 » lors de la consultation. Aucune capacité ajoutée déduite ; préversion non présentée comme stable. La date du flux reste distincte du `published_at` GitHub.

Les quatre autres entrées de la sélection ne sont pas reprises. Aucune brève historique n'est modifiée. Les captures primaires et réponses API sont conservées dans le dossier privé `podcast/2026-11-26-execution-065055Z/sources-http/` ; leurs dates de consultation ne redatent pas les annonces.

## Mission et réemploi

Objectif : un million d'euros de **chiffre d'affaires** en douze mois. Engagement : 100 % des **bénéfices** à des associations françaises loi 1901, tout documenté. Aucun don déjà effectué annoncé ; aucune date de première publication inventée dans le flux.

Réemploi du CLI déjà installé [rany2/edge-tts](https://github.com/rany2/edge-tts), métadonnées GitHub relues le 26 : dernier push `2026-11-18T14:00:40Z`. API licence `NOASSERTION`, fichier licence effectivement relu : LGPLv3, exception MIT pour `src/edge_tts/srt_composer.py`. Exécution du CLI externe, aucun code tiers copié ni nouvelle dépendance incorporée au média. Module podcast interne conservé.
