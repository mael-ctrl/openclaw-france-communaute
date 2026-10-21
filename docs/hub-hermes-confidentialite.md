# Confidentialité Hermes : page, README et ZIP — 21 octobre 2026

## Choix du chantier unique

Le rapport de préparation du 21/10 classe ce lot **n° 1 prêt à intégrer**. La roadmap du 20 au soir demande d'harmoniser le README et de requalifier le patch HTML après la correction du GUIDE (`defb7af`). Contrôle à `8c8e8698dfa2cfaa5f749710fcbb79d86641cae1` : les deux tests et la section HTML sont absents ; le README conserve une formulation trop absolue. Aucune nouvelle préparation du compositeur newsletter déjà intégré.

Les briques SEO prioritaires #1–#4 et le catalogue des sources conservées ont déjà leurs livraisons consignées. Les chemins historiques inconnus et les listings hors archives restent un travail distinct : pas de restauration/purge déduite d'une URL ou d'une source commune. Ce passage intègre **une seule amélioration cohérente du hub gratuit lié au média**, pas un second chantier SEO.

## Modification bornée

- Lien avant téléchargement vers `/hermes/#confidentialite` et cinq accordéons HTML natifs : contexte envoyé au fournisseur, outils externes malgré un modèle local, droits minimums, historique/sauvegardes et partage de diagnostics.
- README aligné avec le GUIDE déjà corrigé ; distinction entre inférence locale et fonctionnement hors ligne, coûts externes possibles et contrôle réseau indépendant si nécessaire.
- ZIP Hermes : seul `README.md` change. GUIDE, installateurs, configuration et archive OpenClaw conservés. Pas de nouveau formulaire, script client, prix, compte ou prestataire.
- Synthèse indépendante attribuée au Crabe (IA), documentation officielle datée du 21/10. Ce texte n'est ni un audit réseau ni une garantie juridique ou de confidentialité.

## Provenance et réemploi

Lot préparé : `crabe-chantiers/hub-hermes/2026-10-21/` ; **130 pièces hub** du manifeste de vague vérifiées avant intégration. Les deux patches ont été appliqués sur le SHA courant, sans importer de données de recette.

Dépôt primaire consulté : [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent), **MIT**, dernier push API constaté **2026-10-21 08:39:30 UTC**. Aucun code upstream copié ou exécuté. Réemploi des composants HTML natifs, des contrats préparés et de `zipfile` standard ; aucune dépendance nouvelle.

Documentation officielle relue : [sessions](https://hermes-agent.nousresearch.com/docs/user-guide/sessions), [FAQ](https://hermes-agent.nousresearch.com/docs/reference/faq#is-my-data-sent-anywhere), [modèles locaux](https://hermes-agent.nousresearch.com/docs/user-guide/local-models), [web](https://hermes-agent.nousresearch.com/docs/user-guide/features/web-search), [sécurité](https://hermes-agent.nousresearch.com/docs/guides/secure-hermes-on-a-work-machine), [commandes](https://hermes-agent.nousresearch.com/docs/reference/cli-commands), [modèles auxiliaires](https://hermes-agent.nousresearch.com/docs/user-guide/configuration#auxiliary-models) et [secours](https://hermes-agent.nousresearch.com/docs/integrations/providers#fallback-providers). Les résumés « local » de certaines pages ne sont pas étendus aux outils connectés et aux envois volontaires de diagnostics.

## Recette rejouée par l'intégrateur

- Quatre échecs HTML et un échec README attendus observés avant les corrections, puis six nouveaux contrats verts. **174 tests Python + 4 Node réussis**, quatre scripts `bash -n` ; pas de test d'installation multi-OS revendiqué.
- **560 fichiers existants comparés**, trois changements publics attendus et deux tests ajoutés. HTML hors bloc/lien identique ; les versions intégrées correspondent exactement au payload relu.
- Deux appels isolés à `construction.construire()` à horloge commune : **2 920 sorties du média identiques**. **371 fichiers de données inchangés**, aucun sceau/journal réécrit.
- ZIP reproduit indépendamment : SHA-256 `db91efccf794b4c22b338c5a95b1025bc3b50ea791e6b8bdb322afa159cc90cd`. Cinq membres comparés ; les quatre membres non modifiés gardent leurs octets, flux compressés et métadonnées. Les dates techniques de l'archive ne prétendent pas dater la correction éditoriale.
- Chromium dédié, sans JavaScript : ancre par Tab/Entrée, cinq accordéons par Espace, titre sous l'en-tête et absence de débordement à **360, 390 et 1 440 px**. Captures 360/1 440 relues visuellement. Pas d'utilisation du navigateur personnel.
- Préflight SFTP : clé hôte épinglée avant authentification, sauvegardes privées et trois cibles distantes identiques à la base Git ; GUIDE, archive OpenClaw et `.htaccess` également identiques.

## Livraison

**Livré : commit `2471c095775337738e8591b0bdddec9bd952a908`.** Le commit local non publié a été rebasé sur `6e344ee`, qui ne changeait que les données du média ; aucun historique partagé réécrit. Les sept blobs poussés ont été comparés à `origin/main`.

- Hub : **trois fichiers transférés par SFTP le 21/10 à 08:53 UTC**, après nouvelle sauvegarde et comparaison de base ; remplacement atomique par fichier et relecture exacte. Contrôle séparé à 09:07 UTC : trois cibles exactes, GUIDE, installateur, archive OpenClaw et `.htaccess` préservés. Aucun déployeur intégral ni régénération des autres ZIP.
- Cloud : [run `39572663369` réussi](https://github.com/mael-ctrl/openclaw-france-communaute/actions/runs/39572663369), achevé à **09:16:04 UTC** ; **174 tests**, **1 503 fichiers envoyés** par le pipeline média, sauvegarde `875cc2a`. Aucun post Bluesky supplémentaire (quota atteint). Les délais d'observation de `gh run watch` ne constituaient pas des échecs du workflow.
- Le workflow `maj.yml` vérifie les contrats et déploie le **média**, pas le hub ; la publication du hub est démontrée par le SFTP et ses URL, pas par le seul résultat cloud.
- Après la fin du cloud, à **09:16 UTC : 15 URL HTTPS en 200**, dont accueil/version du média, pages principales du hub, les cinq fichiers du kit et son ZIP avec/sans `?v=2`. **Six contrats rejoués sur les corps HTTPS**. README, GUIDE, scripts/configuration et ZIP identiques octet pour octet aux sources ; section confidentialité HTML exacte, `<main>` exact après décodage du seul lien support protégé par Cloudflare.
- Navigation publique sans JavaScript effectivement rejouée à **360, 390 et 1 440 px** : ancre au clavier, cinq accordéons et largeur contrôlés ; capture publique mobile relue. Cette recette ne teste ni l'installation du logiciel ni toutes les fonctions d'accessibilité.

**Deux défauts du vérificateur corrigés, production inchangée :** la première comparaison de `<main>` ignorait l'obfuscation du `mailto:` par Cloudflare ; la seconde collecte avait omis le sous-dossier `scripts/`, faisant échouer le contrat exhaustif du ZIP. Corps et sorties initiales conservés. Décodage borné à l'adresse publique exacte, collecte récursive puis nouvelle recette entièrement verte ; aucun test de production affaibli.

Pièces privées : `~/.hermes/workspaces/crabe-chantiers/hub-hermes/2026-10-21-integration/` (base, tests rouge/vert, builds, ZIP, captures et relevés distants). Aucun secret, prospect ou contenu d'un autre projet publié.

Aucun gain d'audience, de conversion ou d'indexation mesuré. Les conditions d'activation newsletter, les inconnus historiques et les prérequis commerciaux restent ouverts ; aucune campagne ni notification externe effectuée par ce chantier.
