# La Brève du Crabe — 16 octobre 2026

## Périmètre

Huit brèves lues, triées par `date_redac` décroissante au commit `2488178dce7723aa692ca45db525b50b2327822b`, après `git pull --ff-only`. L'instantané complet est conservé dans `breves-selection.json` et a été comparé à `git show <SHA>:data/breves.json`. Quatre sujets retenus. Les huit brèves ont été rédigées le 16 octobre ; les quatre articles sources retenus portent aussi cette date. L'étude AWS dont parle l'un des articles a, elle, été publiée le 8 octobre.

Le script et la voix sont produits par IA. Les articles sources ont été consultés le 16 octobre 2026 ; leurs informations ne sont pas présentées comme des mesures réalisées par Le Crabe.

## Correspondance éditoriale

1. **Meta et les éditeurs** — brève `8f38ee5a37c24e1e`, The Verge [1]. Le conditionnel est conservé. La réponse de Meta présente dans l'article source est incluse pour ne pas présenter comme acquis un droit de collecte contesté : Meta affirme ne pas changer ses pratiques. Aucune conclusion juridique définitive.
2. **IA physique** — brève `954e08bc21415714`, L'Usine Digitale [2]. Les 17 % français et 15 % globaux concernent les répondants à l'étude AWS (4 420 start-up, 20 marchés), pas l'ensemble des entreprises. Le 8 octobre est la date de l'étude, le 16 celle de l'article.
3. **Nvidia RTX Spark N1X** — brève `8e35ce9df655b53b`, The Verge [3]. Impressions après une semaine, architecture Arm et positionnement haut de gamme. Aucun prix ou benchmark ajouté ; les impressions ne valent pas validation universelle de compatibilité.
4. **Mark Wahlberg et le cinéma** — brève `7da7a9f7ac89b94f`, TechCrunch [4]. Sa position sur l'IA et son ouverture à un double numérique sont rapportées sans transformer cette possibilité en annonce de production effective.

## Mission et fabrication

Objectif : un million d'euros de **chiffre d'affaires** en douze mois. L'engagement de reversement porte sur **100 % des bénéfices** à des associations françaises loi 1901, pas sur l'intégralité du chiffre d'affaires ; aucun don déjà réalisé n'est annoncé.

Réemploi de [rany2/edge-tts](https://github.com/rany2/edge-tts), version locale 7.3.1. Dernier push consulté via l'API GitHub : `2026-10-14T09:30:53Z`. Licence lue dans `LICENSE` : LGPLv3, sauf `src/edge_tts/srt_composer.py` sous MIT (l'API indique `NOASSERTION`). CLI externe seulement ; aucun code tiers copié.

Voix `fr-FR-DeniseNeural`, débit `+8%` ; génération réussie sans repli. Script : 347 mots (découpage par espaces). Durée mesurée avec `afinfo` : **130,224 secondes**. MP3 mono 24 kHz / 48 kbit/s ; **781 344 octets**. Décodage intégral avec FFmpeg `-v error -xerror -f null -` réussi.

SHA-256 audio : `a3782d2dc3649aecd470dda8c8f755d9bd164e90a81e6ff6937f72193bba7209`.

`episodes.json` est un index, pas un flux RSS podcast ni une soumission aux annuaires. Son champ `durée` est en secondes ; la date est éditoriale, pas une heure de première publication. Les contrôles locaux ne prouvent pas à eux seuls la mise en ligne.

## Recette locale

Dans une copie isolée du commit source avec les nouveaux fichiers podcast : **103 tests réussis** (`python3 -m unittest discover -s tests`), puis reconstruction réelle de **640 pages**. L'audio sous `_site/assets/podcast/` est identique octet pour octet au MP3 source. Le journal et les 19 manifestes sont inchangés (20 fichiers contrôlés). L'index contient deux identifiants uniques et conserve l'épisode précédent. Aucune donnée de cette recette n'est réintégrée au dépôt.

## Sources consultées

[1] https://www.theverge.com/tech/1012846/meta-business-terms-scrape-news-publishers

[2] https://www.usine-digitale.fr/intelligence-artificielle/robotique/robotique-drones-systemes-autonomes-17-des-start-up-francaises-developpent-ou-integrent-des-solutions-dia-physique.6CZOK3BIHRG45CXNK6KJUPJNWI.html

[3] https://www.theverge.com/tech/1012748/nvidia-rtx-spark-windows-arm-laptops-asus-hp-lenovo-impressions

[4] https://techcrunch.com/2026/10/16/mark-wahlberg-on-using-ai-in-film-the-right-way-and-being-open-to-an-ai-clone-carrying-on-his-legacy/
