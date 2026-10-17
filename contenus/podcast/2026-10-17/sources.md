# La Brève du Crabe — 17 octobre 2026

## Périmètre

Huit brèves lues après `git pull --ff-only`, triées par `date_redac` décroissante au SHA figé `1156f5d2bed9130cd995fab01434b1d2d1c98c6f`. L’instantané `breves-selection.json` est extrait du blob de ce commit, pas d’un fichier susceptible de changer pendant le run. Quatre sujets retenus ; les huit rédactions sont du 17 octobre. La date de rédaction n’est pas nécessairement celle de l’événement.

Script et voix produits par IA. Les sources complémentaires ci-dessous ont été consultées le 17 octobre 2026. Les deux fils Reddit ont renvoyé 403 via le service d’extraction ; vérification directe sur la fiche Nvidia et la pull request GitHub, sans prétendre avoir lu les fils.

## Correspondance éditoriale

1. **Meta** — brève `7cc15d40c9c66059` : retrait de la formulation des conditions commerciales et réponse de Meta, qui nie un changement de ses pratiques de collecte. Le conditionnel et l’absence de conclusion juridique définitive sont conservés.[1]
2. **Nvidia Dory** — brève `57c3359f3a172edc`, relayée aujourd’hui sur r/LocalLLaMA : quatre milliards de paramètres, couches partagées répétées, contexte annoncé jusqu’à 256K tokens et anglais seul. La fiche officielle date la sortie du **16 octobre**, explicitement distinguée du relais du jour.[2]
3. **llama.cpp** — brève `2400844a4248a68b` : optimisation CUDA pour certaines quantifications basses, notamment Q2_K et Q3_K. La PR #30517 est fusionnée lors de la consultation ; les résultats rapportés par son auteur varient selon GPU et modèle, et ne sont pas une mesure indépendante du Crabe.[3]
4. **BYD** — brève `2676a39126eea79b` : design d’un humanoïde interne après publication d’un brevet. Le dessin ne prouve ni modèle final ni commercialisation massive ; l’article du jour précise que le brevet a été publié le 9 octobre.[4]

Les quatre autres brèves sont conservées dans l’instantané mais non reprises : VBIOS, table Qwen FP8, classement DeepSeek sans méthode dans l’extrait et témoignage individuel sur les prix GPU. Aucun benchmark ni prix n’est extrapolé.

## Mission et réemploi

Objectif : un million d’euros de **chiffre d’affaires** en douze mois. Engagement de reversement de **100 % des bénéfices**, et non du chiffre d’affaires, à des associations françaises loi 1901 ; aucun don déjà réalisé n’est annoncé.

Réemploi du CLI externe [rany2/edge-tts](https://github.com/rany2/edge-tts), version locale 7.3.1. Métadonnées GitHub consultées : dernier push `2026-10-14T09:30:53Z`, licence API `NOASSERTION`. Le fichier `LICENSE` précise LGPLv3, sauf `src/edge_tts/srt_composer.py` sous MIT. Aucun code tiers copié ni nouvelle dépendance ajoutée au média.

Le jour dans `episodes.json` est éditorial ; il ne devient pas une heure de publication. Les IDs existants et leurs GUID sont conservés. L’index alimente désormais la page et le RSS podcast via le moteur existant, sans soumission à un annuaire.

## Fabrication et recette exécutées

- Voix `fr-FR-DeniseNeural`, débit `+8%`, edge-tts 7.3.1 : génération réussie sans repli. Script de **353 mots** (découpage par espaces).
- `afinfo` : **125,280 secondes**, MP3 mono 24 kHz, 48 kbit/s, **751 680 octets**. Décodage intégral FFmpeg avec `-v error -xerror -f null -` : retour 0.
- SHA-256 audio : `b704b4e272682e0f92990358ed430ea1818990c96c6e154306a599f6457fb378`.
- Recette isolée du SHA source avec les seuls fichiers de l’épisode : **129 tests Python réussis**, puis vrai build de **667 pages**. Aucun moteur modifié, aucun FTP/social exécuté localement.
- **276 fichiers de données inchangés** par empreinte, journal et manifestes compris. Huit brèves de l’instantané vérifiées contre le blob source ; trois épisodes indexés sans doublon et deux anciennes entrées conservées exactement.
- MP3 source/build identiques ; quatre entrées RSS (trois épisodes et le pilote), nouvel épisode en tête, GUID stable, enclosure de taille exacte, durée RSS arrondie à 125 secondes ; aucune heure de publication inventée.

Ces contrôles locaux ne suffisent pas à prouver la mise en ligne ; la vérification HTTPS et le résultat cloud sont consignés séparément après publication.

## Sources

[1] https://www.theverge.com/tech/1013409/meta-removes-language-that-may-have-allowed-it-to-scrape-news-sites
[2] https://huggingface.co/nvidia/NVIDIA-Nemotron-Labs-Dory1.0-4B-BF16
[3] https://github.com/ggml-org/llama.cpp/pull/30517
[4] https://www.journaldugeek.com/2026/10/17/byd-aussi-a-son-propre-robot-humanoide
