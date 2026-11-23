# La Brève du Crabe — revue du 23 novembre 2026

Texte produit par IA et voix synthétique. Les huit brèves les plus récentes, triées par `date_redac` décroissante, ont été figées le **23 novembre à 17:31:10 UTC** au commit **`14c8291466b6e3ddee0d5315718545fb7ba1354e`**. L'instantané `breves-snapshot.json` a été comparé au blob Git exact (`data/breves.json`, SHA256 `3ae271b0f8df2da84fda35b914c648dc263644d24ad253e193f52a79d38b796e`).

**Fraîcheur limitée : les huit entrées datent du 21 novembre.** L'introduction l'annonce explicitement : ce sont les derniers sujets disponibles, pas des annonces du 23. Certains sont repris des épisodes précédents ; aucune nouveauté artificielle, aucune date de brève réécrite. Le jour éditorial ne documente pas l'heure de première publication audio.

Le pull du clone partagé a refusé des conflits non résolus (code 128). L'édition est préparée dans un worktree propre sur `origin/main`, après pull fast-forward réussi, sans réparation ni fusion des données et sceaux du clone partagé.

## Les quatre sujets retenus

### 1. Financement de la French Tech — `f425f1156929a59b`

[Maddyness, bilan du 21 novembre](https://www.maddyness.com/2026/11/21/genesis-ai-propulse-les-levees-de-la-french-tech-a-526-millions-deuros-cette-semaine/), relu le 23. Le début public donne 525,8 M€ en neuf opérations, dont 455 M€ pour Genesis AI. L'audio garde l'arrondi de la brève (environ 526 M€), pas une somme recalculée ni du chiffre d'affaires. Périmètre déclaré par Maddyness : fonds propres, entreprises de dix ans au plus avec siège social principal en France. Article partiellement réservé aux abonnés ; aucune lecture de la partie verrouillée revendiquée.

### 2. Connaissances des agents — `bf9a6cb8a6b0cdc9`

[LangChain, Harrison Chase, « How to build a knowledge factory »](https://www.langchain.com/blog/knowledge-factory), daté du 21 novembre et relu le 23. Les agents signalent les informations manquantes ou incorrectes ; un curateur consulte alertes, traces et sources pour maintenir les connaissances. Retour d'expérience de l'éditeur, pas démonstration indépendante ni garantie d'absence d'erreurs. Le script distingue signalement et correction.

### 3. Modèles locaux sur NPU — `88037dd21a6a62de`

- [Frandroid, article repris par la brève du 21](https://www.frandroid.com/culture-tech/intelligence-artificielle/3333831_npu-des-pc-portables-a-quoi-sert-vraiment-cette-puce-ia-avec-ses-tops-et-comment-sen-servir), relu le 23.
- [Annonce primaire AMD du **19 novembre**](https://www.amd.com/en/blogs/2026/unlocking-the-amd-ryzen-ai-npu-for-unsloth-desktop.html), relue le 23 : intégration d'Unsloth Desktop avec les NPU XDNA 2, via Lemonade/FastFlowLM.
- [Documentation Unsloth](https://unsloth.ai/docs/get-started/install/amd/npu), relue le 23, redirige vers `/amd/amd-npu` : compatibilité matérielle et modèles Q4NX spécifiques.

L'annonce du 19 n'est pas transformée en sortie du 23. Pas de compatibilité universelle, de vitesse ou de gain d'autonomie chiffré promis ; pas d'essai matériel réalisé ici. Le script garde la réserve de Frandroid sur les performances réelles sans recycler ses chiffres comme nos mesures.

### 4. Correctif GeForce — `f539c9e8c350a5ce`

- [Frandroid, relais du 21](https://www.frandroid.com/marques/nvidia/3333757_jusqua-30-go-par-heure-sur-le-ssd-nvidia-corrige-enfin-ses-pilotes-geforce-voici-les-pilotes-a-telecharger), relu le 23.
- [Fiche officielle Nvidia du hotfix 621.35](https://nvidia.custhelp.com/app/answers/detail/a_id/5940), relue via extraction web le 23 ; date affichée « Updated 11/20/2026 01:54 PM ». Lecture HTTPS Python refusée en 403, conservée séparément, pas annoncée comme réussie.

La fiche confirme « Excessive writes to file nvlog.nvlgstg may occur in background [7116722] ». Le hotfix est « beta, optional and provided as-is » avec un processus de test abrégé. L'audio conserve ces limites, sans conseiller une installation universelle. Les 30 Go/h rapportés chez un utilisateur ne sont pas repris, aucune usure extrapolée ni installation réalisée.

## Exclusions, mission et preuves

Les sujets SMS, Motorola, téléviseurs et ARTEX restent dans l'instantané, mais ne sont pas utilisés dans cet épisode. Les anciennes brèves et les anciens audios sont conservés.

L'outro distingue l'objectif d'un million d'euros de **chiffre d'affaires** en douze mois de l'engagement de reversement de **100 % des bénéfices** aux associations françaises loi 1901. Il ne prétend pas à des dons déjà effectués.

Audio : **347 mots, 129,360 secondes**, voix `fr-FR-DeniseNeural`, débit `+8%`, sans repli. Durée mesurée avec `afinfo`, décodage intégral FFmpeg réussi ; 776 160 octets, SHA256 `f2117c13e5ea6c9faa2960130c42a7251a2d53077ce92646bfa4bfaf683e1269`. Captures, journal de synthèse et recette conservés hors dépôt dans le chantier privé `podcast/2026-11-23/`.
