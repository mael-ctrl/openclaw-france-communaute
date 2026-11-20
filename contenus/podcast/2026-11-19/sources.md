# La Brève du Crabe — 19 novembre 2026

Édition assistée par IA, voix synthétique. Jour éditorial, pas heure de première publication.

## Sélection figée

Huit brèves les plus récentes triées par instant `date_redac` décroissant, lues dans `data/breves.json` au commit `5ca37805fc608d232e1474168685649e618a1e29`. L'[instantané](breves-snapshot.json) conserve les entrées et l'empreinte du blob exact. Quatre sujets retenus. Le clone partagé refuse le pull à cause de conflits non résolus : lecture et livraison depuis un worktree isolé de `origin/main`, sans modifier ses données ou sceaux.

## Sources relues le 19 novembre

1. **Canva — `6df0ab3392f50ebd`.** [The Verge, Emma Roth, 19 novembre](https://www.theverge.com/ai-artificial-intelligence/1037126/canva-ai-features-off-button), recoupé avec [l'annonce Canva du 19 novembre](https://www.canva.com/newsroom/news/ai-controls-canva/). Réglages annoncés pour Free et Pro sans supplément ; désactivation des fonctions génératives distincte de celle de toutes les fonctions IA. Background Remover et Magic Grab restent disponibles. Le contrôle de bibliothèque réduit les contenus générés, sans promettre leur disparition totale. Pas de test utilisateur de notre part.
2. **Cohere/HCLTech — `06a9021fc10b4e0d`.** [ActuIA, article consulté le 19](https://www.actuia.com/actualite/cohere-sappuie-sur-hcltech-pour-son-ia-souveraine-en-allemagne/), recoupé avec [le communiqué HCLTech du 17 novembre](https://www.hcltech.com/press-releases/hcltech-and-cohere-partner-build-and-deliver-sovereign-ai). Un des intégrateurs privilégiés, pas une exclusivité. Canada et Allemagne ; assurance, services financiers et industrie ; environnement choisi par le client. La certification de management ISO 42001 citée ne démontre pas à elle seule un lieu d'hébergement. Annonce du 17 distincte du relais du 19 ; aucun hébergeur ni engagement contractuel universel inventé.
3. **Siri Recap — `dc3ce02c49544382`.** [The Verge, Victoria Song, 19 novembre](https://www.theverge.com/tech/1037100/apple-siri-recap-audio-intelligence-hands-on). Essai personnel de Siri Recap bêta sur Apple Watch Ultra 4 et mise en perspective avec Bee Frontier. Les confusions avec du son de vidéo sont des observations rapportées par l'autrice, pas un benchmark indépendant effectué par le Crabe. Titre « two weeks », introduction « last month or so » pour les deux dispositifs et corps « past week » pour la bêta : durée d'essai omise de l'audio, sans résoudre artificiellement ces périmètres. Les garanties techniques d'Apple ne sont pas étendues à Amazon. Question d'information de l'entourage, sans avis juridique universel.
4. **OpenClaw — `cf0a2ae9815bcde8`.** [Release exacte `v2026.11.10-beta.1`](https://github.com/openclaw/openclaw/releases/tag/v2026.11.10-beta.1), [API GitHub](https://api.github.com/repos/openclaw/openclaw/releases/tags/v2026.11.10-beta.1). `prerelease=true`, `created_at=2026-11-19T12:22:28Z`, `published_at=2026-11-19T15:45:29Z` au relevé. La brève de 13:11 UTC indiquait une note sans détail : le texte officiel relu est désormais complet. L'audio annonce explicitement cette actualisation ; la brève historique n'est pas réécrite. Reprise en main du navigateur et modèles d'agents ClawHub décrits par la release, non éprouvés ici. Le numéro du tag n'est pas présenté comme une date de publication.

Non retenus dans ce format : seconde entrée OpenClaw redondante ; sujet financier Anthropic non recoupé ici ; WorldCraft et Perplexity, datés du 17. Leur présence dans l'instantané n'est pas une validation de leurs affirmations.

## Mission et production

Objectif de chiffre d'affaires en douze mois distinct de l'engagement de reversement de **100 % des bénéfices**. Aucun don déjà réalisé annoncé. Pas de soumission aux annuaires ni de mesure d'audience dans cette routine.

Réemploi du CLI installé [rany2/edge-tts](https://github.com/rany2/edge-tts), métadonnées relues le 19 novembre : dernier push amont `2026-11-18T14:00:40Z`. API licence `NOASSERTION`, fichier LICENSE lu : LGPLv3, sauf `src/edge_tts/srt_composer.py` sous MIT. Aucun code tiers copié dans le média, aucune nouvelle dépendance de production. Module podcast interne conservé.

Les captures de sources, logs de synthèse, durée mesurée, décodage complet et vérifications Git/HTTPS sont conservés dans le dossier privé daté de l'édition.

## Reprise technique le 20 novembre (UTC)

La sélection et le script du 19 sont conservés : aucune nouvelle édition du 20 ni heure de publication antidatée. Les captures HTTPS directes complémentaires ont été réalisées le **20 à 19:29 UTC**. Cinq sources récupérées en 200 ; Canva a refusé cette capture urllib en 403, distinct de la lecture réussie via l'extracteur lors de la préparation.

Edge TTS a retourné **0**, mais son MP3 ne dure que **16,320 secondes pour 351 mots**. Bien que décodable, ce fichier trop court est rejeté et conservé séparément ; aucune cause HTTP ou troncature précise n'est prétendue établie. Repli autorisé avec **Amélie à 190 mots/minute**, puis FFmpeg à 96 kbit/s : **115,356735 secondes**, **1 384 638 octets**, mesure `afinfo` et décodage intégral réussis. SHA-256 de l'audio retenu : `be3c2a9c51392e20aed10e5383f4e547b3c68b5adb49bcf21f6d78afc2d7e4fc`. Aucun audio déjà publié n'a été remplacé. L'index distant relu le 20 ne contenait pas cet épisode avant intégration.
