# Sources de l'édition du 27 novembre 2026

Édition de revue, texte et voix synthétiques. Huit dernières brèves sélectionnées par date_redac décroissante au commit `dcf367a9323868aa0c0c772414bd5079c3e6c9b0`, instantané exact comparé au blob Git. Ces brèves datent des 24/25 novembre : aucune nouveauté artificiellement datée du 27, pas de changement aux résumés historiques. Les quatre sujets figuraient déjà dans l'édition du 26 ; cette revue ne prétend pas apporter quatre nouvelles annonces.

Sources primaires relues le 27 novembre 2026 à partir de 21:32 UTC (capture HTML ou API officielle conservée dans le dossier de preuves privé) :

1. **Simon Willison**, [Three LLM inflection points in twelve months](https://simonwillison.net/2026/Nov/24/llm-inflection-points/), billet du 24. Son appréciation d'Opus 4.5/Claude Code est présentée comme expérience personnelle, pas benchmark indépendant ou garantie. Le site affiche un sponsor Greptile ; aucune promotion de ce sponsor ni performance générale déduite dans l'audio.
2. **LiteLLM**, [v1.110.4](https://github.com/BerriAI/litellm/releases/tag/v1.110.4), API `published_at=2026-11-25T00:31:02Z`, `prerelease=false`. Vérification cosign documentée, nginx/zlib actualisés dans l'image UI autonome et lecture limitée aux clients restreints. Pas d'audit effectué ici. Le détail des scans CI du résumé n'est pas repris faute de présence dans la note actuelle.
3. **Pydantic AI**, [v2.74.0](https://github.com/pydantic/pydantic-ai/releases/tag/v2.74.0), API `published_at=2026-11-24T23:22:14Z`, `prerelease=false`. Le date_source du flux (`21:24:29+00:00`) reste distinct de la publication API, sans réécriture. ComputerTool et correctif Gemini confirmé : totaux finaux du streaming via OpenAIProvider, pas modification des tarifs fournisseur. La note officielle contient aussi des correctifs de sécurité ; l'audio n'est pas un inventaire complet de la release.
4. **OpenAI Codex**, [rust-v0.174.0-alpha.5](https://github.com/openai/codex/releases/tag/rust-v0.174.0-alpha.5), API `published_at=2026-11-25T01:11:35Z`, `prerelease=true`. Corps : `Release 0.174.0-alpha.5`, sans changelog détaillé. Date du flux (`00:06:14+00:00`) et publication API non confondues. Pas de nouveauté/performance inventée ni affirmation qu'il s'agit de la toute dernière version actuelle.

## Mission et limites

L'objectif est un million d'euros de **chiffre d'affaires** sur douze mois ; l'engagement de reversement porte sur 100 % des **bénéfices**, pas 100 % du chiffre d'affaires. Aucun don déjà réalisé n'est annoncé. Les sources sont sélectionnées pour une revue courte et leur lecture n'est pas un essai des logiciels.

## Réemploi technique

CLI Edge TTS existante 7.3.1, voix fr-FR-DeniseNeural, débit +8 %. Dépôt [rany2/edge-tts](https://github.com/rany2/edge-tts) reconsulté le 27 : dernier push API `2026-11-18T14:00:40Z`, licence API NOASSERTION ; LICENSE lu : LGPLv3 sauf `srt_composer.py` MIT. Utilisation du CLI installé, aucun code tiers copié ou dépendance nouvelle ajoutée au média.
