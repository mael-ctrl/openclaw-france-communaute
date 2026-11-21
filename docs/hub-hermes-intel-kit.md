# Kit Hermes : cohérence Mac Intel — 21 novembre 2026

## Une seule intégration

Premier candidat site intégrable du rapport privé du 21 novembre : reporter dans le GUIDE, le README et le ZIP la réserve Desktop Intel déjà publiée sur `/hermes/`, puis retirer de cette page son diagnostic désormais périmé sur le kit. Le guide général, `demarrage.md`, les commandes, les scripts, les CSS et le kit OpenClaw ne changent pas.

Les priorités SEO déjà intégrées (couvertures, dates étayées, catalogue courant, règles de listing et cache) ne sont pas refaites. Les archives historiques, l'alias OVH et surtout la fiabilité des producteurs restent des chantiers distincts ; ce correctif documentaire ne les clôt pas.

**Cinq cibles publiques :** `hermes/index.html`, `dl/kit-hermes/GUIDE.md`, `dl/kit-hermes/README.md`, `dl/kit-hermes.zip`, `dl/SHA256SUMS.txt`. Deux nouveaux contrats documentaires et deux contrats historiques ajustés. Aucun code d'installation modifié ou exécuté.

## Sources et réemploi

Chasse ciblée officielle du lot préparatoire : [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent), licence **MIT** lue, révision `aeb5a071069dbd85d85f2c8d44337f16df29d475`. Métadonnées reconsultées avant intégration : dernier push API observé `2026-11-21T08:46:19Z` ; cette activité ne prouve pas une installation.

- [Matrice des plateformes, lignes 38–63](https://github.com/NousResearch/hermes-agent/blob/aeb5a071069dbd85d85f2c8d44337f16df29d475/website/docs/getting-started/platform-support.md#L38-L63) : bundles Desktop macOS ARM seulement, pas de mise à jour pour les anciens bundles Intel ; possibilité CLI évoquée séparément.
- [Installation officielle](https://hermes-agent.nousresearch.com/docs/getting-started/installation) et [matrice publique](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support) relues en HTTPS le 21. La formulation générale sur Intel diffère de la possibilité CLI décrite dans la matrice : réserve maintenue, aucune garantie de compatibilité.
- Source épinglée retéléchargée indépendamment, identique au lot. Reformulation française indépendante ; aucun code upstream adopté ou exécuté.
- Réemploi du patch combiné préparé le matin. **40 références du manifeste parent et 307 du lot** contrôlées avant reprise ; aucun ancien lot réécrit.

## Recette réellement exécutée

Le pull `--ff-only` du clone partagé a refusé ses six conflits et son journal indexé. Aucune réparation/reset/fusion : travail dans un nouveau worktree sur **`cd0ebb221c31c84aeb05e9cd08371a32276c8a65`**, où le pull seul réussit.

- Trois nouveaux tests exécutés contre la base : quatre assertions en échec attendues, puis vert après application du correctif.
- **412 tests Python réussis**, commande `python3 -m unittest discover -s tests`, dans une copie scratch ; **huit tests Node réussis**. Aucun lot de données de test importé dans Git.
- **Deux builds média isolés à horloge commune : 5 262 fichiers identiques**, dont 2 617 HTML ; **631 fichiers de données et 87 contenus préservés**. Seules les cinq cibles du hub changent.
- ZIP : CRC valide et cinq membres exacts aux fichiers du kit. Les trois membres non modifiés conservent contenu, métadonnées et flux compressés ; les métadonnées des deux membres modifiés sont conservées. Offsets, CRC et tailles peuvent varier. Date technique ZIP historique ≠ date éditoriale.
- SHA-256 du ZIP : `baef7698500b2a485286021a8f490c9940f3b3ea83b9141faa12a8ffd8d9fb76`.
- Chromium sans JavaScript applicatif, 320/375/760/1 280 px : **59 contrôles réussis**, clic/Entrée/Espace/Tab et quatre téléchargements natifs comparés aux octets attendus. Texte développé sans débordement horizontal, vrai header conservé. Captures mobile et bureau relues visuellement.
- Premier banc navigateur erroné conservé : il supposait le `<details>` fermé alors que l'HTML le livre volontairement ouvert. Corrigé dans le vérificateur, **pas dans le site**. Première vérification ZIP avait un préfixe disque incorrect ; correction du vérificateur seulement.

## Publication

Préflight SFTP : clé hôte vérifiée avant lecture du secret, **cinq bases distantes exactes à Git** et sauvegardées avec onze témoins. Aucune écriture pendant ce préflight.

**Publication hub confirmée à 09:54 UTC le 21 novembre**, commit `3ac0900`. Les cinq cibles ont été installées par `.part` et renommage après double contrôle de leur base, puis relues octet pour octet en SFTP ; onze témoins inchangés. Deux captures HTTPS complètes indépendantes (09:54 et 09:56 UTC), **16 requêtes chacune**, vérifient les cinq cibles, les fichiers individuels du kit, les témoins et l'URL réellement liée du ZIP `?v=2`. Les cinq membres de l'archive sont exacts à leurs fichiers HTTPS ; la projection Cloudflare de comparaison se limite à l'adresse publique connue. Corps bruts conservés.

Le replay local des **réponses publiques capturées** réussit **59 contrôles** à quatre largeurs, sans JS, avec quatre téléchargements exacts. Ce n'est pas une session navigateur directement sur le site. Une capture intermédiaire interrompue par un timeout de lecture de 40 s est conservée ; elle ne prouve pas une indisponibilité générale.

**Le dispatch média [44891738252](https://github.com/mael-ctrl/openclaw-france-communaute/actions/runs/44891738252), sur `3ac0900`, a finalement expiré le 21 à 11:13:59 UTC.** Après l'attente initiale sans job, le job a démarré à 10:28:44 UTC ; **412 tests cloud réussis** en 138,047 s, puis pipeline annulé et consignation ignorée. Annotation officielle conservée : `The job has exceeded the maximum execution time of 45m0s`. **1 490 lignes de transfert** dans le groupe pipeline attestent une tentative partielle, pas un déploiement complet ni une relecture distante. Aucune sauvegarde d'état attribuée à ce run.

`maj.yml` teste et publie le média, **pas le hub**. La livraison ciblée des cinq fichiers du hub demeure confirmée : nouvelle série de **16 GET HTTPS à 11:14 UTC**, tous conformes, y compris les cinq membres du ZIP et l'URL liée. Accueil/version/Transparence du média en HTTP 200 à 11:15 UTC ; ces réponses ne clôturent pas son transfert incomplet. Aucun nouveau dispatch de substitution ni annulation du run actif : P9 (durée, volume, reprise et sauvegarde) reste ouvert, sans deuxième intégration quotidienne.

Les attentes bornées du watcher sont conservées ; un timeout de l'outil terminal et une erreur réseau locale du watcher n'ont pas été confondus avec l'annotation finale de GitHub. Les trois annotations du check ont été relues, dont l'avertissement hérité sur les actions Node 20. Ce correctif ne modifie pas les workflows.

Continuité : le run précédent `44809487457` est finalement **annulé pendant le pipeline**, contrats réussis et sauvegarde ignorée. Il ne clôt pas le déploiement média de la veille. La grille déjà livrée n'est pas réintégrée.

Pièces privées : `crabe-chantiers/hub-hermes/2026-11-21-integration-intel/` (sources, rouges/verts, suite globale, inventaires des builds, contrôle ZIP, captures et snapshots SFTP). Aucun cron modifié, aucun email/Discord, aucun paiement ni autre projet. Installation multi-OS, conformité globale et gain de téléchargements ne sont pas démontrés.
