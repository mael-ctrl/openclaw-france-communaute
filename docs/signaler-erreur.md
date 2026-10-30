# Signalement d’une erreur — chantier quotidien du 30 octobre 2026

## Choix et périmètre

Une seule intégration : un lien natif **« Signaler une erreur par email »** en fin de brève et d’article, séparé des abonnements. Le brouillon contient le titre et l’URL canonique, adressé à `crabe@blockos.fr`. Le lecteur choisit ses précisions et décide de l’envoi. Le texte rappelle la rédaction par IA, sans promesse de réponse ni délai.

C’est le **premier candidat site recommandé** par le relais de l’orchestrateur du 30/10. Le chantier des filtres du 29 n’est pas recommencé. Les priorités historiques couvertures, dates JSON-LD/HTML, autoindex des archives et catalogue des sources conservées sont déjà intégrées ; leurs limites historiques restent documentées. La proposition du 14/10 n’est pas une photographie actuelle du site : CSS/cache, chemins historiques inconnus et alias OVH ne sont pas déclarés résolus par ce lien.

La fiabilité des publications demeure prioritaire côté exploitation, mais ses deux prototypes cache/sauvegarde ne sont pas activables sur leurs seules recettes privées. Aucun wrapper, workflow, cron, cache FTP, donnée éditoriale ou manifeste historique n’est modifié ici.

## Provenance et base

- Préparation réemployée : `engagement/2026-10-30-signaler-erreur/`, base `89267c8c45fd290e1dd1a8aae7b22f66076a7f79`.
- Rapport et manifeste parent du 30/10 relus : **336 références conformes**, vérifiées par empreinte avant import.
- Pull demandé sur le clone partagé : **refusé, six fichiers non fusionnés**. Aucun reset, abort ou fusion forcée. Worktree propre du même dépôt, base **`4ebe40adf88fa82fc3521c08f55f153553f3efae`**, pull `--ff-only` réussi ici seulement ; gabarits/tests/assets ciblés inchangés depuis la préparation. Absence du lien contrôlée avant import.
- Réemploi conceptuel, sans dépendance ni copie amont : [jekyll/minima](https://github.com/jekyll/minima/blob/4de322363fca5927e6f4012cb94f6dad69ab5e6c/_includes/footer.html#L10-L20), MIT, dernier push API `2026-04-07T19:28:29Z` ; [mdn/learning-area](https://github.com/mdn/learning-area/blob/21973263ba859ff3477919087b488157f9d618a6/accessibility/html/good-links.html#L10-L16), CC0-1.0, dernier push `2026-10-20T11:04:14Z`. Métadonnées reconsultées le 30/10 ; sources/licences épinglées du lot comprises dans la vérification d’empreintes. HTML natif et encodage Python standard, pas de thème installé.

## Recette exécutée à l’intégration

1. Tests avant code : deux refus attendus sur les deux gabarits, puis quatre tests ciblés verts. Suite originale **`python3 -m unittest discover -s tests` : 263 tests réussis** ; Node : **huit réussis**.
2. **Deux builds complets isolés**, avant/après, sur archive du SHA figé sous le scratch Hermes ; appel réel `construction.construire()`, réseau interdit, horloge commune `2026-10-30T10:32:24.085054+00:00`.
3. **4 236 sorties comparées** : **2 080 pages éditoriales** strictement identiques après retrait du seul bloc ajouté ; **2 156 autres fichiers identiques**, y compris CSS/JS/flux/sitemaps/livrables. **580 fichiers data/contenus préservés**. Deux variantes de brève conservées dans les données, sélection existante inchangée.
4. Six configurations Chromium sans JavaScript du site : brève et article à **320/390/1 440 px**. Tab/Shift+Tab, ordre précédent/suivant, nom accessible, focus visible, texte entier, absence de débordement sur les deux pages. Deux captures réellement relues, mobile et bureau.
5. **Douze activations mailto interceptées**, souris et Entrée ; CDP + CSP de recette + interdiction OS de LaunchServices/`open` et du réseau externe. Aucun email envoyé, aucun client de messagerie ouvert. Les captures ne prouvent pas la configuration du client du lecteur ou la délivrabilité.
6. Vrai `engine/run.py --essai --sans-redaction` dans la copie : code 0, aucune rédaction, aucun transfert/social ; journal seulement enrichi dans la copie, préfixe intact, **35 fichiers de preuves inchangés**. Collecte partielle : Siècle Digital 403, Reddit Claude 429, conservés dans le log. Aucune donnée de recette reprise en production.

Le sujet/corps sont encodés séparément puis échappés pour HTML. Caractères spéciaux, pseudo-paramètres `bcc/body`, accents, emoji, URL avec query/fragment sont éprouvés ; aucune donnée de navigation du lecteur utilisée. RSS, RSS articles, Bluesky, podcast et newsletter gardent leurs destinations et ordre.

## Publication

**Au commit initial :** fonctionnalité et recettes locales complètes ; push, dispatch et preuve HTTPS à compléter après leur exécution. Aucune réussite cloud anticipée.

## Pièces et limites

Pièces privées : `crabe-chantiers/integration-site/2026-10-30-signalement/` (rouge/vert, suites, comparaison de builds, captures, essai et observations de publication). Ces fichiers de recette ne sont pas importés dans le dépôt public.

Le bloc concerne les pages reconstruites depuis les données conservées, pas tous les chemins historiques inconnus. Il facilite une démarche volontaire, sans établir qu’un signalement a été reçu, qu’une erreur a été corrigée, que les contenus sont factuellement validés ou que l’engagement augmente. L’état du clone partagé et le risque de republication locale périmée restent distincts et non corrigés ici.
