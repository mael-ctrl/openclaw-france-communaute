# Édition du 22 novembre 2026 — sources éditoriales

Texte produit par IA, voix synthétique. Jour éditorial, pas heure de première publication.

## Sélection et dates

Huit brèves réellement lues, triées par `date_redac` décroissante au commit **9eb9db31d0214ad2e616731c3f2839a2b01798e9**. Snapshot privé `podcast/2026-11-22-edition/selection.json`, comparé aux octets de `git show <SHA>:data/breves.json`. Le pull du clone partagé a refusé les fichiers non fusionnés ; un worktree indépendant sur `origin/main` a ensuite effectué un pull fast-forward sans changement. Aucun arbitrage des conflits ni modification des données historiques.

Les dernières brèves du catalogue sont datées du **21 novembre**, et non du 22. L'introduction le dit explicitement. L'annonce AMD remonte au **19 novembre**. Aucun sujet n'est redaté artificiellement.

## Quatre sujets retenus et requalification

1. **Genesis AI et financement de la French Tech** — brève `f425f1156929a59b`, rédaction `2026-11-21T18:49:54+00:00`.
   - Source : [Maddyness, 21 novembre](https://www.maddyness.com/2026/11/21/genesis-ai-propulse-les-levees-de-la-french-tech-a-526-millions-deuros-cette-semaine/).
   - Partie publiquement accessible relue : 525,8 millions d'euros sur neuf opérations, dont 455 millions pour Genesis AI ; le script dit « près de 526 millions ». Périmètre explicite : fonds propres, entreprises de dix ans au plus, siège principal en France. Ni chiffre d'affaires ni financement européen total. Article partiellement réservé aux abonnés : aucune prétention d'avoir lu la partie fermée.
2. **Fabrique de connaissances LangChain** — brève `bf9a6cb8a6b0cdc9`, rédaction `2026-11-21T18:49:50+00:00`.
   - Source primaire : [Harrison Chase, blog LangChain, 21 novembre](https://www.langchain.com/blog/knowledge-factory).
   - Signalement par les agents puis correction par un curateur distinct, avec accès aux sources. Retour d'expérience et proposition du fournisseur, pas test indépendant ni garantie d'exactitude.
3. **Agents dans les messages** — brève `b8b9289525dc29f0`, rédaction `2026-11-21T18:49:47+00:00`.
   - Source : [TechCrunch, Lauren Forristal, 21 novembre](https://techcrunch.com/2026/11/21/all-the-ai-agents-that-can-live-in-your-text-messages/).
   - Panorama de services par SMS et messageries ; plusieurs bêtas sont explicitement indiquées. Aucun tarif, classement de fiabilité ou disponibilité française extrapolé. Extraction web lisible conservée ; la capture urllib directe a reçu **403**. Ce refus est conservé, pas présenté comme une lecture directe réussie.
4. **NPU et Unsloth Desktop** — brève `88037dd21a6a62de`, rédaction `2026-11-21T18:49:36+00:00`.
   - Relais : [Frandroid, dossier NPU](https://www.frandroid.com/culture-tech/intelligence-artificielle/3333831_npu-des-pc-portables-a-quoi-sert-vraiment-cette-puce-ia-avec-ses-tops-et-comment-sen-servir).
   - Primaire : [AMD, annonce du 19 novembre](https://www.amd.com/en/blogs/2026/unlocking-the-amd-ryzen-ai-npu-for-unsloth-desktop.html), [documentation Unsloth](https://unsloth.ai/docs/get-started/install/amd/npu).
   - Compatibilité XDNA 2 et modèles compatibles confirmés. Aucune promesse chiffrée de vitesse ou de batterie reprise. Le script ne dit ni que tous les PC sont compatibles, ni que tous les composants d'un agent restent hors réseau. Encarts publicitaires du relais exclus.

## Brèves non retenues

Motorola (`7fe412343dac8d80`) et guide TV (`b3e39cc78c28168b`) : hors des quatre sujets IA choisis. ARTEX (`b8bbbc3f9a58e7fe`) et pilote Nvidia (`f539c9e8c350a5ce`) : déjà traités dans l'édition du 21, non répétés ici.

## Mission, génération et preuves

L'outro distingue **objectif de chiffre d'affaires de 1 M€ en douze mois** et **engagement de reverser 100 % des bénéfices** aux associations françaises loi 1901. Aucun don déjà réalisé annoncé.

Script : 356 mots séparés par espaces. Génération le 22 novembre à 20:20 UTC avec `fr-FR-DeniseNeural`, débit `+8%`, retour 0. Durée `afinfo` : **135,624 secondes** ; MP3 intégralement décodé par FFmpeg avec `-xerror`. Taille : **813 744 octets**. SHA-256 : `fa61c02166dedb6434cf4e36ce035d378e6c55f88c1b5243cb73952521e92fa4`.

Avant génération : épisode absent de l'index Git et du RSS public, URL audio **404**. Captures HTTPS strictes, journaux et métadonnées conservés dans le lot privé `podcast/2026-11-22-edition/`. Aucun remplacement d'un GUID ou d'un audio existant. Les observations de publication sont consignées séparément dans `docs/podcast-2026-11-22.md` ; génération et tests ne suffisent pas à prouver la mise en ligne.
