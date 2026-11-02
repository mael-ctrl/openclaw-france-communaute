# La Brève du Crabe — 2 novembre 2026

Texte produit par IA, voix synthétique. Date éditoriale du jour réel d'exécution ; aucune publication rétrodatée ni heure de première mise en ligne déduite.

## Sélection figée

Les huit brèves les plus récentes par `date_redac` décroissante ont été lues dans le blob `data/breves.json` au commit **6530893de6c2296a60b19058df79b90e6494c38f**, à 08:12:57 UTC le 2 novembre. Empreinte SHA-256 du blob : `c1db303f51d78f74b05eb6d97530703980f9366c8ce05ab6d8c27e0ad2c504b0`. Instantané : `breves-snapshot.json`. Trois sujets retenus, sans modifier les brèves historiques.

Le pull fast-forward initial du clone partagé a refusé une divergence ; ses fichiers modifiés ont été laissés intacts. Sélection et livraison depuis un worktree isolé sur `origin/main`, avec un second pull fast-forward réussi. La divergence opérationnelle n'est pas déclarée réparée.

## Sources vérifiées le 2 novembre 2026

### 1. Liquid AI : une démonstration WebGPU, pas un benchmark indépendant

- Brève `bc0ad33ed60d9484`, rédigée le 2 novembre à 01:26:47 UTC ; relais : [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/1xlk2kb/lfm3_omni_2b_is_incredible/).
- Source primaire : [espace LiquidAI/LFM3-Omni-2B-WebGPU](https://huggingface.co/spaces/LiquidAI/LFM3-Omni-2B-WebGPU), [README figé](https://huggingface.co/spaces/LiquidAI/LFM3-Omni-2B-WebGPU/blob/9c2fb176f4c222da394e8037d3c0d0837f70b978/README.md).
- L'API de l'espace indique une création le 29 octobre et une dernière modification le 30 octobre. Ces dates ne prouvent pas le lancement général du modèle. Le script dit que l'espace existait fin octobre, sans inventer une annonce du 2 novembre.
- Le README présente explicitement une exécution locale dans le navigateur via WebGPU. Démonstration non exécutée ici : aucun résultat de vitesse, compatibilité universelle ou audit de confidentialité revendiqué. Le nom « 2B » n'est pas transformé en mesure de tous les composants chargés.
- Le relais Reddit et sa variante JSON ont refusé l'accès (403). La source primaire a été lue ; aucune prétention d'avoir relu le fil.

### 2. Survival LLM : fonctionnement hors ligne et limites

- Brève `280ad4175800b6a8`, rédigée le 1er novembre à 21:56:18 UTC.
- [Article Numerama du 1er novembre](https://www.numerama.com/tech/2364545-concu-pour-les-situations-durgence-cette-ia-hors-ligne-veut-vous-aider-a-survivre-a-la-fin-du-monde-ou-au-moins-a-une-panne-de-courant.html), corps lu ; [documentation du projet](https://github.com/anonnerdfrenzy/survival-llm), README lu via l'API GitHub et conservé avec son OID de blob.
- L'auteur décrit un modèle et une bibliothèque téléchargés préalablement, consultables hors ligne, et des citations vérifiables. Il décrit aussi des erreurs et des tests sur un état antérieur de la bibliothèque/instructions : le script n'en déduit aucun taux de fiabilité de la version courante et ne reprend pas de chiffre de sécurité.
- Aucun conseil médical ni consigne de secours généré ; limite explicite : ne remplace pas les secours. L'absence de réseau ne rend ni les réponses fiables par principe ni un ordinateur utilisable sans énergie. Aucune installation ou évaluation clinique dans cette mission.

### 3. Simon Willison : le périmètre de uv.lock

- Brève `9b52323085893335`, rédigée le 2 novembre à 01:27:15 UTC.
- [Billet primaire du 1er novembre](https://simonwillison.net/2026/Nov/1/delete-uv-lock-first/), lu en intégralité.
- Exemple exact : Python 3.15, `watchfiles==1.1.1`, PyO3 limité à Python 3.14 dans ce cas. Le fichier `uv.lock` est local et ignoré par Git dans les bibliothèques évoquées par l'auteur. Sa suppression puis `uv run pytest` résout généralement son cas, selon son témoignage, pas selon un essai de notre part.
- Le script conserve cette restriction et ne recommande pas une suppression universelle des lockfiles versionnés.

## Autres brèves de l'instantané

Les témoignages Qwen/NVFP4, DeepSeek/Strata, débat sur les records de vitesse, application ebook/audio et tandem.cpp ne sont pas utilisés dans l'audio. Aucun de leurs résultats non vérifiés n'est présenté comme acquis. Le relais tandem.cpp a également refusé l'extraction et la lecture JSON ; aucune adresse de dépôt homonyme n'a été substituée.

## Mission et réemploi

Objectif de **chiffre d'affaires** distinct de l'engagement sur **100 % des bénéfices**. Aucun don déjà réalisé annoncé.

Réemploi de l'outil installé [rany2/edge-tts](https://github.com/rany2/edge-tts), version locale 7.3.1 ; métadonnées GitHub consultées le 2 novembre : dernier push `2026-10-14T09:30:53Z`, licence API `NOASSERTION`. Le fichier LICENSE lu précise LGPLv3 pour l'ensemble sauf `srt_composer.py` sous MIT. Utilisation du CLI existant, aucun code tiers incorporé ni nouvelle dépendance de production. Voix prévue `fr-FR-DeniseNeural`, débit `+8%`. Les mesures et contrôles de l'audio sont consignés dans le rapport de recette privé et la documentation podcast après exécution.
