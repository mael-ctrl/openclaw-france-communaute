# La Brève du Crabe — 20 octobre 2026

## Périmètre figé

- `git pull --ff-only` exécuté dans le clone automatisé ; source `data/breves.json` au commit `add8e05c3dfa015501036f5a26460fae82ba137c`.
- Les huit brèves les plus récentes par `date_redac` décroissante sont conservées dans `breves-snapshot.json`, avec heure de consultation et empreinte du blob ; instantané comparé au contenu Git exact.
- Quatre sujets retenus : `ddda3b77ed5de97e` (Spotify), `4da2a6a8d0900e9d` (Ornith), `214713c135d71638` (MDPH), `06d8eb77aab349f9` (Lightroom).
- Non retenus : `fba484654a94ab29` (GGUF Unsloth, même famille que le sujet Ornith), `a3dfff99eccc4726` (question utilisateur sur les comptes Claude, pas une règle établie), `000c7f1bf822fca2` (Pocket TTS), `4aa29a362823b171` (benchmark communautaire Geezuz). Leurs sources n'ont pas été vérifiées pour cet épisode.
- Consultation des sources le 20 octobre 2026. L'extraction du relais Reddit Ornith a échoué avec une erreur 403 du service d'extraction ; cela ne prouve pas un refus direct de Reddit. Repli sur la fiche officielle Hugging Face et le billet des auteurs, sans prétendre avoir lu le fil.

## Contrôle éditorial, dans l'ordre du script

1. **Spotify.** The Verge parle de plus de cinquante millions de titres exclus des recommandations « over the past year ».[6] Le communiqué primaire dit « This year alone » ; le script retient donc « cette année » et attribue le bilan à Spotify.[1] Le communiqué distingue ces exclusions des suppressions de catalogue, sans interdire toute création avec IA ; le script conserve cette distinction et ne présente pas les chiffres comme audités indépendamment.[1]
2. **Ornith.** La fiche officielle confirme l'existence du modèle nommé Ornith-1.5-122B.[4] Le billet des auteurs décrit pour la **famille** Ornith-1.5 une boucle de génération de tâches, de stratégies et de solutions, optimisée par renforcement.[8] Le script sépare explicitement la fiche de cette variante et la méthode de la famille : le billet consulté détaille d'autres tailles, pas un protocole propre au 122B.[4][8] Aucun score, nombre de paramètres effectif, conseil d'installation ou date de lancement n'est repris ; aucune expérience du Crabe n'est prétendue.
3. **MDPH.** La CNSA décrit les essais de gestion documentaire et annonce, dans son communiqué du 15 octobre, des résultats attendus à la mi-octobre ainsi qu'une publication de la méthode d'évaluation.[3] ActuIA rapporte le cadre des tests sur dossiers de personnes décédées, sans injection dans le système d'information, et constate au 20 octobre l'absence de résultats et de méthode publiés.[5] Le script attribue ce dernier constat au journal, sans prétendre avoir audité exhaustivement le site de la CNSA.[5] Aucune réduction effective des délais, généralisation ou conformité juridique n'est annoncée.
4. **Lightroom.** L'annonce Adobe est datée du **19 octobre**, le relais The Verge du 20 : le script dit bien « publiée hier ».[2][7] Adobe décrit la détection des yeux fermés et la proposition de l'action Open Eyes en un geste ; le résultat est une retouche générée, pas une nouvelle prise de vue.[2] Ni gratuité illimitée, ni perfection des résultats, ni test utilisateur du Crabe ne sont promis.

## Mission et transparence

Intro signature, date éditoriale, média produit par IA et voix synthétique annoncés. L'outro distingue l'objectif d'un million d'euros de **chiffre d'affaires** en douze mois de l'engagement de reverser cent pour cent des **bénéfices** à des associations françaises loi 1901. Aucun objectif atteint ni don déjà réalisé n'est affirmé. CTA oral : `communaute-ia.fr`.

Sources attribuées oralement ; références numérotées réservées à ce document, pas à l'entrée TTS. Le champ `script` de l'index pointe vers le texte exact utilisé, sans le présenter comme une transcription synchronisée.

## Réemploi et génération

- CLI existant : [rany2/edge-tts](https://github.com/rany2/edge-tts), version **7.3.1**, dernier push API consulté : `2026-10-14T09:30:53Z`.
- API licence : `NOASSERTION`. Fichier LICENSE relu : LGPLv3 sauf `src/edge_tts/srt_composer.py` sous MIT. Aucun code copié et aucune dépendance ajoutée au média.
- **344 mots** par séparation sur espaces ; `fr-FR-DeniseNeural`, débit `+8%`. Edge TTS réussi, sans repli macOS.
- Durée mesurée avec `afinfo` : **125,640 secondes** ; MP3 mono, 24 kHz, 48 kbit/s ; **753 840 octets**.
- Décodage intégral FFmpeg `-v error -xerror` réussi, retour 0 sans erreur. SHA-256 : `5a03905cbc82ab84ad40c60856855a83ee709ee5ec5f77f1131456e12b98e30d`.
- ID stable `breve-2026-10-20`, durée mesurée et chemin du script ajoutés à l'index, anciens épisodes préservés ; aucune heure de première publication fabriquée.

## Vérification de livraison

Les contrôles locaux, le résultat cloud et les lectures HTTPS sont distincts de la génération audio. Ils sont consignés après exécution dans `docs/podcast.md`. Cette livraison de contenu n'ajoute aucun moteur, ne refait pas la recette navigateur de la fonctionnalité et ne soumet le flux à aucun annuaire. Les captures complètes et le registre de citations restent dans le chantier privé daté.

## Sources

[1] https://newsroom.spotify.com/2026-10-20/prioritizing-human-artistry — One Year In: Putting Human Artistry First on Spotify — Spotify
    > "This year alone, we’ve taken more than 50 million slop and spam tracks out of recommendations."
[2] https://blog.adobe.com/en/publish/2026/10/19/give-your-photos-a-second-chance-with-open-eyes-in-lightroom-on-mobile — Give your photos a second chance with Open Eyes in Lightroom on mobile
    > "When Lightroom automatically detects closed eyes in a photo, it presents the Open Eyes icon as a Quick Action, so you can choose to generate the fix, and get authentic results that save the shot."
[3] https://www.cnsa.fr/actualites/intelligence-artificielle-dans-la-branche-autonomie-un-apres-son-lancement-80-de-la — Intelligence artificielle dans la branche Autonomie : un an après son lancement, 80 % de la feuille de route déjà déployée | CNSA.fr
    > "Les résultats de ces expérimentations sont attendus mi-octobre 2026 et seront partagés avec l’ensemble des MDPH, ainsi qu’à tous les acteurs de la branche Autonomie."
[4] https://huggingface.co/ornith-ai/Ornith-1.5-122B — ornith-ai/Ornith-1.5-122B · Hugging Face
    > "This model card documents **Ornith-1.5-122B**,"
[5] https://www.actuia.com/actualite/dossiers-mdph-la-cnsa-a-fait-tester-lia-pour-raccourcir-48-mois-dattente — Dossiers MDPH : la CNSA a fait tester l'IA pour raccourcir 4,8 mois d'attente — ActuIA
    > "Au 20 octobre, cnsa.fr ne publie ni les résultats ni la méthode."
[6] https://www.theverge.com/entertainment/1014284/spotify-ai-slop-spam-songs-removed — Spotify pulled 50 million AI slop and spam tracks from its recommendations | The Verge
    > "Spotify says it has removed more than 50 million songs considered AI-generated slop or spam from user recommendations over the past year."
[7] https://www.theverge.com/tech/1014246/adobe-lightroom-mobile-ai-quick-action-open-eyes-closed-blink-repair — Adobe Lightroom mobile can now open closed eyes in photos with a simple tap | The Verge
    > "Adobe announced yesterday"
[8] https://ornith.ai/ornith_1_5.html — Ornith-1.5: From Self-Scaffolding to Self-Improvement | Ornith Blog
    > "proposes new tasks, generates task-specific scaffolds, and produces solution rollouts"
