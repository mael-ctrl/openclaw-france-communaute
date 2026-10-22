# La Brève du Crabe — 22 octobre 2026

## Périmètre et provenance

Édition datée du jour réel d'exécution, le 22 octobre, et non du jour de démarrage de la conversation. Sélection des huit entrées les plus récentes par `date_redac` décroissante au SHA `f2d0bce6c522bb20cff695b34c5d5f2766edec81`, capturée le 22/10 à 09:14:13 UTC. L'instantané `breves-snapshot.json` a été comparé aux huit entrées du blob `git show <SHA>:data/breves.json` ; il conserve les données lues même si le clone partagé avance. Trois sujets retenus, script de 358 mots ; les cinq autres entrées ne sont pas transformées en affirmations dans l'audio.

## Vérification des sujets

- **Claude Duet — `10a8b4888b8eb673`.** Numerama rapporte une annonce du 21 octobre, pas une sortie le 22. L'ordinateur cloud, le résumé matinal et les demandes d'approbation sont confirmés par la page du produit. Celle-ci précise « research preview », liste d'attente, abonnements Pro/Max et États-Unis : aucune disponibilité générale en France annoncée.[1][4]
- **Walmart — `66da132be7e30f51`.** ActuIA et le communiqué primaire du 21 octobre décrivent les profils d'agents, l'approbation des achats ou le plafond fixé par le client, la passerelle et le blocage des agents non conformes. Les profils sont annoncés pour le mois suivant, pas déjà disponibles ; la passerelle commence en bêta. Le script ne transforme pas ces promesses en efficacité de protection mesurée.[3][5]
- **IBM Granite — `420968b05ee395b8`.** Billet IBM Research publié sur Hugging Face le 22 octobre : recette de quatre modèles, prévisions médianes et quantiles sans réentraînement, coût supérieur en mémoire et inférence. IBM invite à comparer sur des fenêtres/horizons représentatifs et ne garantit ni calibration ni robustesse universelles. Aucun score de benchmark n'est repris comme validation indépendante.[2]

Sources consultées le 22 octobre 2026. Les annonces du 21 sont explicitement datées dans le script ; « publié aujourd'hui » ne concerne que le billet IBM daté du 22. Le mot « sources vérifiées » désigne la lecture et le recoupement documentaire, pas des essais indépendants des produits.

## Choix éditoriaux et limites

Les entrées Meta, témoignage Reddit, version canary Hermes, verrouillage ChatGPT et photographie de police ne sont pas retenues. La vérification GitHub du tag exact de la brève Hermes a répondu HTTP 404 ; aucun correctif de version ni détail de release n'est inventé. Cela ne démontre pas que la brève était fausse lors de sa rédaction.

L'outro distingue l'objectif d'un million d'euros de chiffre d'affaires en douze mois de l'engagement de reverser 100 % des **bénéfices** à des associations françaises loi 1901. Aucun don effectué ni objectif atteint n'est annoncé. Texte produit par IA et voix synthétique explicités.

## Réemploi

Moteur podcast existant inchangé, aucun ajout de bibliothèque. CLI `rany2/edge-tts` déjà installé en version 7.3.1, réutilisé avec Denise et débit +8 %. Métadonnées GitHub consultées le 22/10 : dernier push `2026-10-14T09:30:53Z`, licence API `NOASSERTION`. Le fichier LICENSE officiel précise LGPLv3 pour le programme, sauf `srt_composer.py` en MIT. Aucun code tiers copié ou redistribué dans ce lot.

## Recette exécutée avant publication

- Voix `fr-FR-DeniseNeural`, débit `+8%`, edge-tts réussi sans repli : MP3 de **130,224 secondes**, **781 344 octets**, mono 24 kHz / 48 kbit/s. Mesure `afinfo`, type `audio/mpeg`, décodage intégral FFmpeg sans erreur. SHA-256 : `76b52bee7bd06a74a0271972527519f62d964a8ef8c8f6b0566daa8698b5b893`.
- Clone isolé au SHA de sélection : **182 tests Python réussis**, puis build réel hors mocks. **419 fichiers** de données/audio/contenus préservés ; **1 563 sorties** comptées par le constructeur. MP3 construit identique à la source et script affiché exact après parsing HTML.
- Index : anciens épisodes inchangés, nouvel ID stable `breve-2026-10-22`, durée mesurée et champ `script` explicite. **8 GUID distincts** dans le flux, pilote compris ; nouvel épisode en tête, enclosure exacte, aucun `pubDate` déduit du jour éditorial.
- Ce contrôle local ne prouve pas le déploiement. Les vérifications cloud/HTTPS sont consignées après lecture effective de la production ; aucune soumission aux annuaires ni hausse d'audience revendiquée.

## Sources

[1] https://www.numerama.com/tech/2358555-anthropic-devoile-claude-duet-un-agent-ia-qui-travaille-pour-vous-comme-muse-meta-et-dots-openai.html
[2] https://huggingface.co/blog/ibm-research/granite-timeseries-ensemble-r1
[3] https://www.actuia.com/actualite/commerce-agentique-walmart-impose-ses-regles-aux-agents-dia
[4] https://claude.com/product/claude-duet
[5] https://corporate.walmart.com/news/2026/10/Making-It-Possible-for-Agents-to-Shop-on-Behalf-of-Customers
