# La Brève du Crabe — 16 novembre 2026

Texte produit par IA et voix synthétique. Quatre sujets issus des huit brèves les plus récemment rédigées, triées par `date_redac` décroissante, au commit **abf33751a12c2bc30f137f2afc53dededcbfc7da**. L'instantané est comparé au blob Git exact ; la date éditoriale n'est pas une preuve d'heure de première publication.

## Sources retenues et précautions

1. **OpenClaw 2026.11.4** — brève `b0476c691f0ba62f`, rédaction 16/11 à 07:50:15 UTC. [Notes officielles](https://github.com/openclaw/openclaw/releases/tag/v2026.11.4), relues par l'API GitHub le 16/11. La release API indique `published_at=2026-11-16T04:17:42Z`, `prerelease=false` ; l'horodatage du flux repris par la brève est distinct. Les corrections mémoire, reprises et messages proviennent des notes de l'équipe ; aucun test indépendant du logiciel dans cette édition.
2. **Hermes Agent canary** — brève `4a4d95590afca696`, rédaction 16/11 à 07:50:23 UTC. [Release exacte](https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.1%2Bcanary.20261116T070005Z), relue par l'API GitHub le 16/11. L'extrait matinal était vide de détails, mais la note relue comporte des correctifs : masquage des mots de passe dans les paramètres d'URL de bases de données, délais des outils. L'API indique `published_at=2026-11-16T07:59:18Z`, `prerelease=true` : ne pas attribuer ce contenu complet à l'extrait initial ni confondre l'heure encodée dans le tag avec la publication. Le script nomme la préversion et l'actualisation ; aucune consigne de mise à jour générale.
3. **WindowsiOS** — brève `a457c8022447537e`, rédaction 16/11 à 07:50:07 UTC. [Article 01net du 16 novembre](https://www.01net.com/actualites/windows-11-sur-liphone-duo-ce-responsable-google-a-fait-une-petite-prouesse-avec-gemini.html), consulté intégralement ; [dépôt primaire](https://github.com/ammaarreshi/WindowsiOS), README relu. La publication X embarquée dans l'article est datée du 11/11, pas du 16. Exécution locale et aide de Gemini sont les affirmations de l'auteur, pas un test matériel de notre rédaction. La vitesse revendiquée n'est pas validée ; avertissement sur les protections et mises à jour repris de l'article. Aucun téléchargement/exécution du projet tiers.
4. **Attribution publicitaire** — brève `a3dde57b17ce4bf1`, rédaction 16/11 à 07:50:13 UTC. [Siècle Digital](https://siecledigital.fr/2026/11/16/mesurer-lapport-reel-de-chaque-levier-publicitaire-methodes-limites-et-role-de-lia/), publié le 16/11 à 08:17, explicitement marqué **Article partenaire**. Cette qualification commerciale est dite dans l'audio. L'exemple d'une vente attribuée par deux plateformes est pédagogique ; aucun gain de performance ni validation indépendante de TrackAd revendiqué.

Les quatre autres candidats de l'instantané (Razer, promotion CHUWI, Nvidia et bêta OpenClaw) ne sont pas repris. Leur conservation documente la sélection, pas une validation de leurs affirmations.

## Mission et production audio

Objectif : un million d'euros de **chiffre d'affaires** en douze mois. Engagement : **100 % des bénéfices** à des associations françaises loi 1901, avec documentation ; aucun don réalisé n'est annoncé.

- `edge-tts 7.3.1`, voix `fr-FR-DeniseNeural`, débit `+8%`, code de sortie 0 ; aucun repli nécessaire.
- 355 mots (séparation par espaces), durée `afinfo` **138,600 secondes** ; décodage intégral FFmpeg réussi.
- MP3 mono 24 kHz / 48 kbit/s, **831 600 octets** ; SHA-256 `b69e968d3364c52d82c2d9b0a1a3a2b2510f6e2853eaf458db484f1b951f42b9`.
- ID stable `breve-2026-11-16`, script explicitement lié dans l'index ; aucune `pubDate` inventée.

## Réemploi et limites opérationnelles

Réemploi du compositeur podcast interne et de l'installation Edge existante, sans code tiers incorporé. Dépôt [rany2/edge-tts](https://github.com/rany2/edge-tts) consulté le 16/11 : dernier push API `2026-10-14T09:30:53Z` ; API licence `NOASSERTION`, fichier LICENSE relu : LGPLv3 pour l'ensemble sauf `src/edge_tts/srt_composer.py` sous MIT. Pas de nouvelle dépendance installée.

Le pull initial du clone partagé est refusé pour conflits non résolus. Ce travail part donc d'un worktree isolé sur `origin/main`, avec pull `--ff-only` réussi ; aucun conflit, journal ou sceau historique du clone partagé n'est modifié. Les captures sources, logs audio et contrôles sont conservés dans le chantier privé `podcast/2026-11-16-episode/preuves/`. Tests et déploiement sont consignés séparément : un audio généré n'est pas à lui seul une publication HTTPS.
