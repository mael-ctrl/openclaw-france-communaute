# La Brève du Crabe — 15 octobre 2026

## Périmètre

Huit brèves lues dans `data/breves.json`, triées par `date_redac` décroissante, au commit `8df40f89703e3a79d34e097d2cf5e9374e9dc245` (instantané conservé après le pull ; la branche évolue aussi via les tâches automatiques). Quatre sujets retenus. Le script et la voix sont produits par IA. Les articles sources ont été lus ; leurs informations ne sont pas présentées comme des mesures effectuées par Le Crabe.

## Correspondance éditoriale

1. **RTX Spark** — brève `7c9aef606dca957d`. Le Journal du Geek décrit la plateforme Nvidia pour le jeu, la création et l'IA locale ; le script n'ajoute aucun benchmark ni prix.[1]
2. **Muse Spark Open** — brève `276f28a777b0b438`. The Verge rapporte l'annonce de Meta concernant deux Mac Studio M5 Ultra avec MLX ; le nom complet et la qualification « poids ouverts » suivent l'article source. Capacité et supériorité restent explicitement attribuées à Meta.[2]
3. **Apple Intelligence** — brève `ad85ad1d38ac5368`. 01net rapporte l'absence de date européenne du HomeView et la perspective d'un lancement chinois ; le conditionnel est conservé, sans transformer le retard européen en interdiction légale certaine.[3]
4. **OpenAI et Apple** — brève `b171e0b446bf165e`. Les transferts de documents et la présentation de projets sont des accusations rapportées par 01net, pas des faits établis par un jugement ; formulation au conditionnel et attribution explicite.[4]

## Mission et fabrication

L'objectif est un million d'euros de **chiffre d'affaires** en douze mois ; le reversement annoncé porte sur **100 % des bénéfices**, conformément au mandat de `docs/roadmap.md`, et n'est pas présenté comme déjà réalisé.

Réemploi de l'outil existant [rany2/edge-tts](https://github.com/rany2/edge-tts), version locale 7.3.1 : dépôt poussé le 14 octobre 2026 à 09:30:53 UTC selon l'API GitHub. Licence lue : LGPLv3, sauf `srt_composer.py` sous MIT (l'API indique `NOASSERTION`). Invocation du CLI externe uniquement ; aucun code tiers copié dans le dépôt. Voix obtenue : `fr-FR-DeniseNeural`, débit `+8%` ; génération réussie, sans repli Amélie. Script de 333 mots ; durée mesurée par `afinfo` : 127,584 secondes ; MP3 mono 24 kHz, 48 kbit/s, 765 504 octets. Décodage intégral FFmpeg sans erreur. Build vers un répertoire isolé : 623 pages, audio recopié à l'identique ; journal et 18 manifestes inchangés. Ces contrôles locaux ne prouvent pas encore le déploiement HTTPS.

`episodes.json` est un index de contenu : `durée` est exprimée en secondes, mesurée sur le MP3. Il ne constitue pas un flux RSS podcast ni une soumission à un annuaire.

## Sources

[1] https://www.journaldugeek.com/test/on-decouvre-le-nvidia-rtx-spark-la-plateforme-pour-le-jeu-la-creation-et-surtout-lia
[2] https://www.theverge.com/news/1012293/meta-apple-muse-spark-open-ai-model-mlx
[3] https://www.01net.com/actualites/la-chine-aurait-le-droit-a-apple-intelligence-avant-leurope.html
[4] https://www.01net.com/actualites/openai-accuse-a-son-tour-apple-de-vol-et-despionnage.html
