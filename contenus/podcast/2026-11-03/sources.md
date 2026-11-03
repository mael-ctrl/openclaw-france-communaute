# La Brève du Crabe — 3 novembre 2026

Bulletin produit par IA ; voix de synthèse. Trois sujets retenus parmi les huit brèves les plus récemment rédigées, triées par instant `date_redac` décroissant au commit `bdb0a687e2ddc2a8f993f23949a06782dfede72f`. L'instantané `breves-snapshot.json` est comparé au blob exact `data/breves.json` de ce commit, pas à un arbre partagé mouvant. Jour éditorial réel, aucune heure de première publication déduite.

Le pull du clone partagé a refusé des conflits non résolus. Sélection et livraison réalisées dans un worktree propre de la pointe distante, après pull fast-forward, sans résolution ni écrasement des données ou sceaux du clone partagé.

## Sources consultées le 3 novembre

### Netflix — brève `ff7da2825aad42ab`
- Relais TechCrunch, 3 novembre : https://techcrunch.com/2026/11/03/netflixs-new-ai-discover-tab-helps-you-find-something-to-watch-based-on-your-mood/
- Annonce primaire Netflix, 3 novembre : https://about.netflix.com/en/news/introducing-ai-discover
- Retenu : onglet expérimental dans l'application TV, recommandations à partir de thèmes choisis, affinage et exclusion possibles.
- Périmètre précisé depuis la source primaire : petit groupe aux États-Unis, anglais, téléviseurs compatibles ; extension progressive annoncée, pas de disponibilité française inventée. Aucun essai indépendant de qualité.

### LangSmith — brève `f8ad811ffa4fc1e6`
- Blog officiel LangChain : https://www.langchain.com/blog/langsmith-byoc-aws-gc-azure
- Retenu : AWS en disponibilité générale, Azure et Google Cloud en bêta ; traces, évaluations et déploiements dans le compte cloud client, service exploité par LangChain.
- Nuance de la source : séparation du plan de données et du plan de contrôle ; ce dernier contient notamment authentification et métadonnées de facturation. Pas d'affirmation « aucune donnée ne sort », pas de validation de conformité ou d'audit de sécurité. Le billet rappelle un lancement AWS en août : ne pas présenter toute l'offre comme née aujourd'hui.

### StateBench — brève `023a902da66acc38`
- Publication Ai2 sur Hugging Face, 3 novembre : https://huggingface.co/blog/allenai/statebench
- Retenu : suivi de changements d'état sur contextes longs, plusieurs niveaux de difficulté, limites observées sur les chaînes complexes ; aucun score isolé ni classement général.
- Les expériences et conclusions sont celles des chercheurs, non reproduites ici. Le cadre actuel suppose un nombre fixe de variables : ne pas en déduire une couverture de toutes les conversations réelles.

## Sélection et limites

Les cinq autres brèves de l'instantané (watchOS, Cyclon, édition de poids relayée sur Reddit, vidéoprojecteur, cyberattaques) ne sont pas utilisées dans l'audio. La lecture partielle de The Verge ne vaut pas vérification intégrale de l'article ; aucune conclusion tirée de sa partie réservée. Les résumés générés du média ne sont pas traités comme des preuves primaires.

L'outro distingue l'objectif de chiffre d'affaires de l'engagement de reversement de 100 % des **bénéfices**, sans annoncer de dons déjà effectués. Captures HTTPS strictes des quatre sources utilisées conservées hors dépôt public avec date, URL, taille et SHA-256.
