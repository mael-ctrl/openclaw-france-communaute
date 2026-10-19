# La Brève du Crabe — 19 octobre 2026

## Périmètre figé

- Source : `data/breves.json` au commit `8e6bffd4836de6b503bd1bfe6890099062713079`, après `git pull --ff-only` du clone automatisé. Les huit entrées triées par `date_redac` décroissante et l'heure de capture sont conservées dans `breves-snapshot.json` ; comparaison au blob Git obligatoire avant livraison.
- Quatre sujets retenus : `c1aa0fd9be2b8618` (OpenAI), `58c71e210f15d97b` (Claude Code), `98d4c14e87ed6a79` (Nvidia), `266233f5dfc23920` (Ming tiny).
- Quatre sujets non retenus : `be9807a3f275885f` (rendu de personnages), `0d9730ea84322dbf` (Volundr), `c3737c0d7a8fbc13` (Cohere/llama.cpp), `9197ebb0e4ba1c9d` (Ming flash). Leurs fils Reddit n'ont pas été consultés pour cet épisode.
- Les trois articles de presse et la fiche officielle du modèle ont été extraits et lus le 19 octobre. Pour Ming, contrôle direct de la fiche Hugging Face, sans prétendre avoir lu le relais Reddit. Captures complètes et registre de citations conservés dans le chantier privé daté.

## Contrôle éditorial, dans l'ordre du script

1. L'Usine Digitale rapporte la confirmation par Sam Altman d'un projet de robot humanoïde et une démonstration évoquée pour 2027, sans détails sur son apparence, ses applications ou les modèles embarqués.[1] Le podcast n'annonce ni disponibilité commerciale ni confirmation faite aujourd'hui : l'article du jour rapporte notamment des propos d'un podcast du mois précédent.[1]
2. 01net explique que Claude Code compresse les conversations avec gzip ; l'annonce attribuée à Anthropic date du 16 octobre, même si l'article est relayé le 19.[2] Le script distingue optimisation du transport et capacité de raisonnement ; aucun facteur d'accélération propre au Crabe n'est annoncé.
3. TechCrunch décrit des modèles à poids ouverts pour agents d'entreprise et sur PC, avec exécution sur l'infrastructure des organisations ou certaines machines locales.[3] Le corps de l'article dit « on Thursday » malgré sa date du 19 octobre : le script ne transforme donc pas cette date de publication en date certaine de lancement. Les comparatifs de performances du fabricant ne sont pas repris, et aucun test matériel du Crabe n'est prétendu.
4. La fiche officielle de Ming-3.0-audio-tiny donne 9,3 milliards de paramètres au total, 2,7 milliards activés par étape, une entrée audio et texte, des usages de reconnaissance/questions-réponses audio et une synthèse vocale optionnelle.[4] Elle indique le chinois et l'anglais comme langues principales.[4] Le script attribue ces capacités à la fiche et ne revendique ni test en français ni validation indépendante ; aucune date de sortie n'est déduite du relais du jour.

## Mission et transparence

Intro signature, média produit par IA et voix synthétique ; CTA vers `communaute-ia.fr`. L'outro distingue l'objectif d'un million d'euros de chiffre d'affaires en douze mois et l'engagement de reverser 100 % des **bénéfices** à des associations françaises loi 1901. Elle n'annonce ni objectif atteint ni dons déjà effectués.

Les médias et la fiche Hugging Face sont attribués oralement. Les références numérotées restent dans ce document, pas dans l'entrée de synthèse vocale. Le champ `script` de l'index lie le texte exact à sa page d'écoute ; ce n'est pas une transcription synchronisée.

## Réemploi et génération

- CLI déjà installé : [rany2/edge-tts](https://github.com/rany2/edge-tts), version 7.3.1 ; dernier push API observé le 19 octobre : `2026-10-14T09:30:53Z`.
- L'API licence renvoie `NOASSERTION`. Le fichier LICENSE relu précise LGPLv3, sauf `src/edge_tts/srt_composer.py` sous MIT. Aucun code tiers copié ni nouvelle dépendance incorporée au média.
- Script définitif : **336 mots** par séparation sur espaces ; voix `fr-FR-DeniseNeural`, débit `+8%`. Premier rendu de 137,112 s raccourci avant publication ; seul le second rendu est livré.
- Edge TTS réussi sans repli macOS. Durée `afinfo` : **129,120 secondes**, MP3 mono 24 kHz, 48 kbit/s ; **774 720 octets**.
- Décodage intégral FFmpeg avec `-v error -xerror` réussi, code 0 sans erreur. SHA-256 final : `be3104ce84f54aa9c5d73d0f00d68003d2d909fe28c2c152df889129bbcb7fc4`.
- Index : ID stable `breve-2026-10-19`, durée mesurée et chemin du script explicites, sans `pubDate` ni heure de première publication inventée.

## Vérification de livraison

L'ajout du fichier et de l'index ne prouve pas le déploiement. Recette isolée, résultat cloud et contrôle HTTPS doivent être consignés séparément dans `docs/podcast.md` après exécution. Aucun envoi vers un annuaire ou un réseau social réalisé par cette mission de podcast.

## Sources

[1] https://www.usine-digitale.fr/intelligence-artificielle/robotique/openai-prepare-un-robot-humanoide-qui-pourrait-etre-presente-des-2027.FDY3CAZ7FJDHTMIFMDADODRL5Y.html
    > "L’entrepreneur américain a ensuite évoqué à Fortune une “démo géniale” en 2027."
[2] https://www.01net.com/actualites/anthropic-rend-claude-encore-plus-rapide-grace-a-une-technologie-de-1992.html
    > "Claude Code compresse la conversation en gzip à chaque tour, et les sessions cloud démarrent dès les premiers caractères saisis."
[3] https://techcrunch.com/2026/10/19/nvidia-launches-new-open-models-to-run-agents-in-the-enterprise-and-on-pcs
    > "Nvidia on Thursday launched new open-weight models designed for always-on agents and edge computing."
[4] https://huggingface.co/inclusionAI/Ming-3.0-audio-tiny
    > "Ming-3.0-audio-tiny is a compact native audio-language model from inclusionAI."
