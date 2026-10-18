# La Brève du Crabe — 18 octobre 2026

## Périmètre figé

- Source : `data/breves.json` au commit `255125c2f08e1a5a2a61f2d01539e2495e35f517`, après `git pull --ff-only` du clone automatisé.
- Capture : `2026-10-18T16:30:44.599730+00:00` ; huit brèves triées par `date_redac` décroissante, conservées dans `breves-snapshot.json`.
- Quatre sujets retenus : `a50bd9ab59a83370` (IA locale), `3706d6bf1dcb50e6` (météo), `796c54fb951e03ff` (robot lave-vitres), `12eddb495c6b9015` (revue cyber).
- Quatre sujets non retenus : `57ca33cb64eeacdc` (dépôt DeepSeek sans annonce dans la brève), `5ac7901a53d7b4f2` (discussion quantification), `b247fa52ce0ebeb0` (cargaison GPU), `abaaf2107c0e78bb` (AuroraASR). Leurs liens Reddit n'ont pas été consultés pour cet épisode. Aucun chiffre ni résultat de ces sujets n'est diffusé dans l'audio.
- Les quatre pages effectivement citées ont été extraites et lues le 18 octobre ; captures intégrales d'extraction, registre de citations et extraits vérifiés conservés dans le chantier privé daté. Aucune vidéo intégrée n'a été visionnée ; le podcast s'appuie sur les textes accessibles.

## Contrôle éditorial, dans l'ordre du script

1. Frandroid décrit un portable Asus à puce Nvidia RTX Spark emporté pendant un vol de onze heures sans connexion, pour tester des modèles exécutés localement sans abonnement.[1] Le script le présente comme un essai rapporté par Frandroid, pas comme un test du Crabe ni une preuve du remplacement universel des services cloud.[1]
2. Le Journal du Geek présente une méthode de Microsoft qui corrige les erreurs de modèles météo existants sans forte puissance de calcul ; les résultats restent probabilistes et ne permettent pas une certitude à trois semaines.[2] Aucun pourcentage de zones améliorées n'est transformé en taux de prévisions exactes.[2]
3. Numerama publie son test du Winbot W2S Pro Omni d'Ecovacs, dont le prix de référence est 599 euros.[3] Ce prix n'est pas présenté comme la meilleure offre marchande ni comme un prix vérifié chez tous les vendeurs. Le script précise que le Crabe n'a pas testé l'appareil et ne lui attribue aucun verdict personnel.
4. La revue hebdomadaire de Numerama revient sur le piratage ayant fait grimper les températures des rayons frais de centaines de supermarchés français.[4] Le script distingue la publication de la revue aujourd'hui de la date de l'incident et n'invente ni date d'attaque, ni attribution, ni montant de dommages.[4] La remarque sur les équipements du quotidien est une conclusion éditoriale générale, pas un résultat nouveau.

## Mission et transparence

Intro signature, déclaration de média produit par IA et CTA `communaute-ia.fr`. L'outro distingue l'objectif d'un million d'euros de chiffre d'affaires en douze mois et l'engagement de reverser 100 % des **bénéfices** à des associations françaises loi 1901. Elle ne présente ni le chiffre d'affaires cible ni des dons comme déjà réalisés.

Les noms des médias sont prononcés dans le script ; les références numérotées restent dans ce document pour ne pas être lues par la synthèse vocale. Le texte indexé sur la page podcast est le script éditorial exact, pas une transcription horodatée.

## Réemploi et génération

- Réemploi de l'outil déjà installé `rany2/edge-tts`, version 7.3.1 ; dépôt : https://github.com/rany2/edge-tts ; dernier push API observé : `2026-10-14T09:30:53Z`.
- L'API licence renvoie `NOASSERTION`. Le fichier LICENSE effectivement lu précise LGPLv3 pour l'ensemble sauf `src/edge_tts/srt_composer.py` sous MIT. Utilisation du CLI existant uniquement, aucun code tiers copié ni nouvelle dépendance du média.
- Voix `fr-FR-DeniseNeural`, débit `+8%`, entrée `script.txt` : 341 mots (séparation par espaces).
- Génération Edge réussie, sans repli macOS. `afinfo` mesure **126,504 secondes**, 24 kHz, mono, MP3 à 48 kbit/s ; fichier de **759 024 octets**.
- Décodage intégral par FFmpeg terminé avec code 0 et sans erreur. Durée mesurée reprise dans l'index ; ID stable `breve-2026-10-18` ; aucun `pubDate` ou horaire de première publication déduit du jour éditorial.

## Vérifications de livraison

Les résultats de recette et de production seront consignés dans `docs/podcast.md` après exécution. La création du MP3 et son ajout à l'index ne prouvent pas à eux seuls le déploiement, l'écoute effective par des visiteurs ou la soumission à un annuaire.

## Sources

[1] https://www.frandroid.com/marques/nvidia/3290147_on-a-tente-de-remplacer-chatgpt-par-une-ia-gratuite-et-sans-internet-sur-le-nvidia-rtx-spark-video
    > "On a embarqué un ordinateur portable Asus équipé de la puce ARM Nvidia RTX Spark dans un vol de 11 heures sans internet pour mettre cette promesse à l’épreuve du réel."
[2] https://www.journaldugeek.com/2026/10/18/microsoft-veut-rendre-la-meteo-plus-fiable-au-dela-de-quinze-jours
    > "Microsoft propose une méthode IA qui corrige les erreurs de ces modèles, sans demander une grosse puissance informatique."
[3] https://www.numerama.com/tech/2351719-peut-on-laisser-un-robot-laver-ses-vitres-jai-teste-le-winbot-w2s-pro-omni.html
    > "Est-ce que cela vaut 599 euros pour autant ?"
[4] https://www.numerama.com/cyberguerre/2354083-des-frigos-de-supermarches-pirates-partout-en-france-le-fosse-invisible-de-lia-et-les-bots-russes-toujours-actifs-malgre-les-frappes-sur-yandex-on-vous-raconte-la-semaine-cyberguerre.html
    > "un piratage qui a fait grimper la température dans les rayons frais de centaines de supermarchés français"
