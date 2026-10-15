# Fiabilité du résultat de déploiement — 15 octobre 2026

## Choix du chantier unique

Le rapport d'orchestration du 15/10 classe en priorité P2 le faux succès du pipeline après une exception FTP. Défaut encore présent sur `70d2ba2ad50b4e5b908721b36950a8aa3a97ed12`, reproduit avant intégration : code processus 0 et annonces après une panne injectée. Ce prérequis de livraison fiable est traité avant l'ajout des images de couverture (premier chantier SEO restant, action #3). Aucun autre lot de la vague n'est intégré.

## Contrat livré

- Une exception de connexion, authentification, transfert ou fermeture FTP entraîne le code processus **1** et un bilan explicite d'échec.
- IndexNow, Wayback et Bluesky ne sont appelés qu'après le retour normal du déployeur. Le retour incrémental `(0, 0)` reste un succès.
- `--sans-deploiement` ne diffuse plus les pages locales ; `--essai` reste sans FTP, annonces ni sceaux.
- Le workflow tente la sauvegarde de `data/` après succès **ou échec** du pipeline non annulé. Aucun `continue-on-error` ne masque l'échec.
- Les anciens journaux et manifestes ne sont pas réécrits. Pas de nouveau protocole, dépendance, retry, ordonnanceur ou service.

## Vérifications locales exécutées

Dans une copie isolée de Git, sans importer de données de tests dans le dépôt :

1. Tests de régression appliqués avant le correctif : **11 tests, 12 échecs de cas/sous-cas attendus** sur l'ancien code (dont le code 0 après panne FTP).
2. Après application complète : `python3 -m unittest discover -s tests` — **72 tests réussis**, dont les 11 nouveaux contrats. Les tests démarrent le vrai CLI et le vrai déployeur, avec transport distant simulé et accès réseau/credentials interdit dans les processus de test.
3. Build réel : `import construction; construction.construire()` — code 0 ; **605 fichiers HTML**, **606 URL sitemap**, toutes les destinations présentes.
4. `python3 engine/run.py --essai --sans-redaction` — code 0, 0 rédaction, 0 envoi FTP et 0 publication sociale. Collecte réelle : 12 nouveautés ; deux flux ont refusé la lecture (403 Siècle Digital, 429 Reddit Claude), sans bloquer le build.
5. **221 fichiers de données du dépôt réel inchangés**, empreintes comparées avant/après recette. Syntaxe Bash du script de sauvegarde testée.

Sorties brutes locales : `crabe-chantiers/integration-site/2026-10-15-fiabilite/` (`01-rouge.log`, `02-suite-complete.log`, `03-build-isole.log`, `04-essai-sans-redaction.log`, `verification-locale.json`).

## Recette cloud et HTTPS

En attente du push et du run `maj.yml` de cette intégration. Ne pas confondre les tests de panne injectée avec un incident provoqué chez OVH. La validation de production doit consigner ici le run, sa conclusion, le déploiement effectif et les URL HTTPS relues.

## Limites conservées

Le déploiement FTP n'est pas transactionnel : des fichiers peuvent avoir été reçus avant une panne ; aucun rollback n'est ajouté. Le cache taille/mtime ne prouve pas la présence distante. Les compteurs et le registre décrivent des contenus locaux, pas une disponibilité HTTPS. Une annulation ou perte du runner ne garantit pas la sauvegarde. Le chemin d'échec est testé par injection locale, sans provoquer une panne en production.

## Reconnaissance open source et provenance

Métadonnées revérifiées via l'API GitHub le 15/10/2026 ; aucun code tiers copié, aucune bibliothèque ajoutée. Réemploi du pipeline existant, correctif stdlib issu du lot `fiabilite-deploiement/2026-10-15` relu puis retesté.

| Dépôt | Licence API | Dernier push UTC observé | Décision |
|---|---|---|---|
| [fabric/fabric](https://github.com/fabric/fabric) | BSD-2-Clause | 2026-04-10T13:53:02Z | Résultat après transfert terminé ; pas de migration SFTP |
| [pyinvoke/invoke](https://github.com/pyinvoke/invoke) | BSD-2-Clause | 2026-04-07T15:39:24Z | Distinguer essai et échec ; `_run_body`/`_finish` relus au SHA `6a71e680c535ba6520e935c497099fbca011d03c` |
| [jd/tenacity](https://github.com/jd/tenacity) | Apache-2.0 | 2026-10-12T13:10:05Z | Pas de retry : préserver l'échec final sans répéter des effets partiels |

La condition de sauvegarde suit les [fonctions de statut GitHub Actions](https://docs.github.com/en/actions/reference/workflows-and-actions/expressions#status-check-functions) : `!cancelled()` permet le contrôle explicite de l'issue du pipeline, sans convertir son échec en succès.
