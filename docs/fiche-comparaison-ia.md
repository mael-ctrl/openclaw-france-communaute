# Fiche gratuite : comparer deux IA — 26 octobre 2026

## Une amélioration de croissance

`/skills/` propose une nouvelle fiche : **Comparer deux IA sur vos propres cas**. Téléchargement Markdown natif, gratuit et sans inscription ; lien également dans `llms.txt`. Le contenu comprend cinq exercices **fictifs**, une grille de critères, un prompt de préparation et les limites de la méthode. Aucun résultat de modèle n'est inventé et cette méthode proposée aux lecteurs n'est pas présentée comme un contrôle déjà appliqué par le média.

Effet attendu : proposer une ressource utile à conserver et partager, avec retour vers les ressources du média. Aucun gain de trafic, téléchargement ou vente mesuré. Les offres payantes, le suivi d'audience, les formulaires et les réglages éditoriaux ne changent pas.

## Base et réemploi

- Base figée : `915240126f6ff80cda57a77bfb98bd43f7a757de`. Bureau illisible par Git ; clone automatisé avec rebase/conflit `data/trafic.json`, préservé. Worktree propre sur `origin/main`, hors du clone actif ; pull réussi dans ce worktree.
- Rapport et manifeste de la vague du 26 relus ; aucune copie de données, patch en attente ou recette de cette vague importés.
- Chasse GitHub : recherche `llm evaluation` (DeepEval, OLMES, LLM-Evaluation), puis étude ciblée de **promptfoo/promptfoo** : licence MIT vérifiée dans `LICENSE`, dernier push API observé `2026-10-26T11:19:23Z`, révision `b4c2404a0dee93dcd4d53a323d6f32f87ee27558`.
- Sources épinglées relues : `site/docs/configuration/test-cases.md`, `site/docs/configuration/expected-outputs/index.md` ; contenu vérifié contre les SHA de blobs Git. L'ancien chemin `expected-outputs.md` répond 404 ; le chemin courant a été découvert dans l'arbre Git, sans inventer le contenu manquant.
- **Réemploi conceptuel seulement** : entrées communes et critères attendus. Aucun code amont copié, outil Promptfoo installé, modèle appelé ou résultat d'évaluation produit. Exercices et texte originaux ; deux sources documentaires citées dans la fiche avec extraits conservés et contrôle du registre de citations.

## Recette exécutée

- Nouveau contrat `tests/test_fiche_comparaison.py` : rouge sur l'absence du lien, puis vert. Contrôle du téléchargement natif, du contenu, de sa découverte et de l'identité des octets après build.
- Suite complète : **231 tests Python réussis**, plus **4 tests Node**. Build réel après les fixtures : **1 895 pages + assets**.
- Comparaison à horloge commune : `/skills/` identique après retrait de la seule carte ajoutée ; `llms.txt` identique après retrait de la seule ligne ajoutée. **547 fichiers data/contenus/assets inchangés** pendant la recette (la nouvelle fiche est déjà incluse dans cette photographie).
- Essai isolé `--essai --sans-redaction` : retour 0, plafond 30 €/mois conservé, clé chargée sans affichage ; aucune rédaction payante, aucun transfert ni annonce. **31 fichiers de preuves inchangés**, préfixe du journal et registre de publications conservés. Collecte partielle : HN agents/OpenClaw 502, Siècle Digital 403, Reddit Claude 429 ; ces erreurs tierces ne sont pas présentées comme des succès.
- **8 téléchargements Chromium vérifiés** : 320/1 440 px, avec/sans JavaScript, souris et Tab/Entrée depuis le lien OPML précédent. Fichier reçu identique octet pour octet, nom conservé, lien non masqué par l'en-tête, pas de débordement horizontal aux deux largeurs. Captures mobile/desktop relues ; pas de conformité globale ou multi-navigateur revendiquée.
- Requêtes externes bloquées pendant la QA ; aucun formulaire soumis, email, inscription ou mesure de conversion déclenché.

Preuves privées : `~/.hermes/workspaces/crabe-chantiers/croissance/2026-10-26/` : `red.log`, `green.log`, `tests.log`, `essai.log`, `local-result.json`, sources épinglées, registre de citations, `browser-local-20261026T144038Z/` et scripts de vérification. Playwright installé uniquement dans un venv de recette sous le scratch ; Chromium headless existant, aucun navigateur personnel utilisé.

## Livraison

En attente de vérification cloud/HTTPS au moment du premier commit. La réussite du test local ne vaut pas publication.

### Confirmation du 26 octobre, 15:20 UTC

- Rebase du seul correctif sur la livraison voisine du hub `681b8aa`, puis **234 tests Python réussis** dans cette combinaison. Commit publié : `5925651b8b157c48c55d3984ef4f194e808a0244` ; cinq blobs distants relus après push.
- Run [40342393320](https://github.com/mael-ctrl/openclaw-france-communaute/actions/runs/40342393320) : **completed/success**, contrats (234 tests), pipeline et sauvegarde réussis. Envois des trois cibles présents dans le log. État automatique `f25406b`, sauvegardé sur `main` via `013a73f92bfb61bf89a8c9a4752a9195623d81ef` après fusion d'une livraison documentaire voisine ; les cinq blobs de ce correctif restent identiques. Aucun SFTP de secours ni intervention sur les données du clone partagé.
- HTTPS strict : `/skills/`, `/llms.txt` et `/fichiers/comparer-reponses-ia.md` répondent 200 avec **les octets attendus intégralement**. Fiche : 9 259 octets, SHA-256 `7a6198f4ff61e025a9535a94c9d6bd48b3310f905fae75b4cb199cc1d9b53577`. Le serveur n'annonce pas de Content-Type pour ce Markdown ; son téléchargement natif est néanmoins éprouvé, sans prétendre à un type MIME servi.
- **8 téléchargements publics** supplémentaires vérifiés (mêmes largeurs, modes JS et actions que la recette locale), octets et nom de fichier identiques. Captures publiques mobile/desktop relues.
- Les sondes de 15:02 et 15:18 UTC, pendant le transfert, servaient encore l'ancienne page à quatre cartes : écarts conservés, pas interprétés comme résultat final du déploiement.

Pièces finales : `cloud-final.log`, `cloud-final.json`, `tests-rebase.log`, `https-20261026T152027Z/`, `browser-production-20261026T152027Z/` dans le même dossier privé. Les messages de transfert du hub visibles dans l'étape de tests appartiennent aux fixtures ; seul le transfert média de l'étape pipeline est revendiqué ici. Aucun gain d'audience ni de conversion mesuré.
