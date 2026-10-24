# Fin de lecture → podcast — croissance du 24 octobre 2026

## Une seule amélioration

Le bloc « Gardez le Crabe dans votre veille », après chaque brève/article reconstruit, propose maintenant **Écouter le podcast** vers `/podcast/`. Les lecteurs arrivant directement depuis une recherche ou un lien partagé n'ont plus besoin de retrouver le pied de page ou de repasser par l'accueil pour découvrir les épisodes.

Une ligne HTML dans `engine/construction.py`, styles existants réemployés. RSS général, RSS articles seuls, Bluesky et aide RSS conservés. Aucun nouveau service, lecteur embarqué, script, traceur, chargement MP3 ou abonnement automatique. Audio, scripts éditoriaux, GUID et flux inchangés. Effet attendu : faciliter le passage de la lecture à l'écoute ; aucune hausse d'écoute ou d'audience mesurée.

## Réemploi examiné

Reconnaissance GitHub le 24/10/2026 : [shipshapecode/starpod](https://github.com/shipshapecode/starpod), MIT (`LICENSE.md` relu), dernier push API `2026-09-02T18:33:16Z`, SHA `c9601ca128507c4fd19910714095425007bfbe45`. Le fichier [`packages/starpod/src/pages/index.astro`](https://github.com/shipshapecode/starpod/blob/c9601ca128507c4fd19910714095425007bfbe45/packages/starpod/src/pages/index.astro) compose une liste d'épisodes. Une migration Astro serait disproportionnée : aucun code tiers copié ni installé. Réemploi du lien natif déjà éprouvé dans l'accueil et de la page podcast existante. La recherche a aussi remonté `jiangfengfz/podsite` : dépôt vide (409), aucune licence API, écarté.

## Validation locale exécutée

- Bureau inaccessible à Git depuis le cron : aucune réparation ni reprise de fichiers illisibles. Worktree isolé hors Bureau depuis `origin/main`, pull réussi, base `7313eda0cfce19353a79d61399f7c3cef0b796f9`.
- Statistiques, sources, quarante dernières lignes du journal, documentation et dernier rapport/manifeste de préparation consultés. Dépense mensuelle enregistrée : 5,64 USD, mode normal. Budget inchangé, aucune rédaction payante locale.
- `tests/test_suivre.py` : deux échecs attendus avant (destination podcast absente), deux réussites après. **207 tests Python et quatre tests Node réussis.** Contrats des deux gabarits : destinations existantes et ordre conservés, libellé explicite, lien natif, aucun lecteur/MP3 ajouté.
- **1 312 brèves et 405 articles** comparés au rendu de la base à horloge commune : tous identiques après retrait de l'unique ligne ajoutée. Build réel : 1 753 sorties comptées par le moteur. Les **500 fichiers** de données, contenus et assets contrôlés restent identiques.
- Vrai `engine/run.py --essai --sans-redaction` dans une seconde copie : retour 0, un item collecté, zéro rédaction/envoi/annonce. **29 manifestes** et registre inchangés, journal conservé en préfixe ; aucune donnée d'essai reprise. Collecte partielle : HN OpenClaw 502, Siècle Digital 403, Reddit Claude 429 ; ces réponses tierces ne sont pas corrigées par cette amélioration.
- Chromium éphémère sans JavaScript, 390 et 1 440 px : **huit parcours** (brève/article × clic/clavier × deux largeurs), destination podcast atteinte, texte d'épisode déplié, aucun débordement horizontal et aucune requête MP3 sur la page de lecture. Le clavier passe du lien Bluesky au nouveau bouton avec Tab, puis Entrée. En-tête sticky conservé ; défilement nécessaire sur mobile. Pixel de mesure tiers bloqué pendant la recette pour ne pas gonfler l'audience.

## Livraison

Recette cloud et contrôle HTTPS à consigner après publication. Le succès des tests locaux seul n'est pas une preuve de production.
