# Veille Promptfoo — 17 novembre 2026

## Une amélioration

Ajout de `https://github.com/promptfoo/promptfoo/releases.atom` au catalogue :
« Promptfoo (releases, préversions incluses) », anglais, priorité 3.
Les **35 sources antérieures** restent identiques et dans le même ordre ;
le catalogue et son export OPML comptent **36 sources**. Réemploi du collecteur,
du générateur OPML et du compteur de Transparence, sans dépendance nouvelle.

Effet attendu : mieux couvrir les outils d'évaluation des prompts, agents et
applications à modèles de langage, depuis des notes de versions primaires.
Ce n'est ni une recommandation d'installation, ni une preuve de sécurité des
outils, ni une croissance d'audience mesurée. Fenêtre de trois jours, filtres,
quotas et plafond DeepSeek de 30 €/mois inchangés. La priorité ne départage
que les dates égales, sans garantir la sélection d'un sujet.

## Qualification et réemploi

Chasse préalable : `promptfoo/promptfoo` et `langchain-ai/langgraph` (API : MIT ;
derniers pushes observés le 17 à 08:31:35 UTC et 06:44:02 UTC). Promptfoo retenu
pour couvrir l'évaluation, complémentaire aux frameworks d'agents déjà suivis.
Aucun code amont installé, copié ou exécuté : seule l'adresse du flux est ajoutée.

- Dépôt : [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo).
- Révision qualifiée : `9a7187a33b53277295151cc20d24cf96fa0d5cfb`.
- Licence MIT confirmée dans le [LICENSE épinglé](https://github.com/promptfoo/promptfoo/blob/9a7187a33b53277295151cc20d24cf96fa0d5cfb/LICENSE),
  octets vérifiés contre le blob Git `af3fa111d9303b3041d225fb851534e50a4bbec2`.
- Consultation du flux à 13:02 UTC : HTTPS strict, HTTP 200,
  `application/atom+xml`, 223 409 octets, SHA256
  `e4174e727b5cedfe1454238cef3fb0330d45999e79c5f644bb62430dc08d627d`.
- Dix entrées lues par le vrai parseur sur les octets conservés ; toutes datées
  et liées aux releases du dépôt. Plus récente : `2026-10-25T01:53:11+00:00`.
- **Aucun candidat récent dans la fenêtre de trois jours**. Ajout prospectif :
  aucune date réécrite, aucune fenêtre élargie pour forcer une publication.
  L'activité du dépôt ne se confond pas avec la fraîcheur de son flux de releases.

## Recette locale

Base `d9d83426e36f31d797eed507cb8c39c802310237`, worktree propre hors Bureau ;
pull rebase réussi dans ce seul worktree. Le Bureau est inaccessible depuis
cette routine et le clone partagé porte des conflits préexistants : aucun abort,
reset, résolution automatique ni modification de ses données.

`tests/test_source_promptfoo.py` : rouge avant ajout, vert après. Contrat de
source unique, libellé explicite, export fidèle et compteur cohérent.
**395 tests Python réussis**, puis `python3 engine/run.py --essai --sans-redaction`
dans une copie isolée : code 0, 2 610 pages, zéro rédaction payante, transfert
ou publication sociale. Clé chargée uniquement pour la lecture du solde, sans
affichage. Les deux flux HN ont répondu 502, L'Usine Digitale 403 et Reddit
Claude 429 : le succès du build ne garantit pas la disponibilité de tous les flux.

60 fichiers de preuves/publications inchangés et préfixe du journal intact.
Aucune donnée de la recette reprise en production. Export OPML égal au générateur,
SHA256 `8682c896c9f30a8ef475020071880b3b61cbe7cdc1e36ed604ca68923663ecb7`.
Pièces privées : `crabe-chantiers/croissance/2026-11-17-promptfoo/evidence/`.

Au commit initial, la publication HTTPS et le relais cloud restaient à confirmer.
Le run antérieur `44081967086`, sans ce changement, a été annulé pendant le
pipeline à 13:04 UTC ; sa sauvegarde d'état a été sautée. Ce n'est pas une
annulation en file d'attente, ni un résultat du présent ajout.

## Publication vérifiée à 13:07:55 UTC

Commit de configuration `30bae65680d029a169965515b86207aff4438d9b` :
les trois fichiers livrés ont été relus identiques par l'API GitHub sur `main`.
Le dispatch `44089556269` utilise exactement ce commit.

Livraison SFTP limitée à `/veille/sources.opml` et au seul compteur **35 → 36**
de `/transparence/`, sans remplacer ses autres statistiques. Clé hôte épinglée
vérifiée avant le secret, sauvegardes privées et base OPML exactement égale au
catalogue parent ; HTTPS et SFTP concordaient avant écriture. Inventaire paginé
des statuts actifs avant transfert : aucun ancien catalogue actif relevé. Ce
contrôle ponctuel n'est pas un verrou transactionnel.

Staging `.part`, comparaison de base avant renommage et relecture SFTP exacte.
La transformation inverse du seul compteur restitue tous les octets antérieurs.
La première lecture HTTPS immédiatement après transfert a différé : refus
code 1 et corps conservés, sans réécriture. Deux nouvelles lectures canoniques
à **13:07:55 UTC** correspondent exactement aux deux fichiers attendus :
**36 flux, Promptfoo une seule fois**, compteur 36 présent une fois. La cause du
décalage initial n'est pas établie.

Pièces privées : `livraison-ciblee/` (avant/après, préflight, résultat SFTP et
premier corps HTTPS divergent), `recontrole-https/result.json` et ses quatre
corps. Publication publique confirmée ; le relais cloud est encore en cours au
relevé suivant. Cela ne prouve ni sa sauvegarde finale, ni la publication d'une
brève Promptfoo, ni un gain de trafic. Les conflits du clone partagé restent
inchangés et distincts de cette livraison.
