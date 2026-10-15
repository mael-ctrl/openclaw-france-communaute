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

- Code intégré : [`3e79f4b4167decdb3395cd243c9b29cfa652bd4e`](https://github.com/mael-ctrl/openclaw-france-communaute/commit/3e79f4b4167decdb3395cd243c9b29cfa652bd4e).
- [`maj.yml` — run 38708738646](https://github.com/mael-ctrl/openclaw-france-communaute/actions/runs/38708738646), dispatch du 15/10 à 08:52:03 UTC : **success**, terminé à 09:03:09 UTC. Pipeline et sauvegarde d'état réussis.
- Déploiement confirmé par log **et** journal : **628 fichiers, 10 423 636 octets** envoyés ; entrée `deploiement` à 09:03:04 UTC. État cloud sauvegardé au commit [`8546b3643c68c3b09f05a727d24a302bb44b3725`](https://github.com/mael-ctrl/openclaw-france-communaute/commit/8546b3643c68c3b09f05a727d24a302bb44b3725).
- Contrôle TLS strict à **09:05:04 UTC** : accueil, `/version.txt`, `/news-sitemap.xml`, dernière brève et dernier article **HTTP 200**. Le marqueur de build correspond à l'entrée `construction` du run ; les deux nouveaux contenus figurent au news-sitemap.
- Les HTML HTTPS de la [brève](https://communaute-ia.fr/breves/nvidia-ouvre-sa-plateforme-d-orchestration-de-gpu-run-ai-en-open-sourc-5177be/) et de l'[article](https://communaute-ia.fr/articles/run-ai-en-open-source-gemini-4-argon-mondial-l-ia-monte-d-un-5177be/) sont **identiques octet pour octet** au rendu des données du commit sauvegardé. Cela vérifie la livraison, pas la véracité éditoriale de ces contenus.
- Preuves locales brutes : `06-cloud-complet.log`, `07-cloud.json`, `08-verification-https.json`, corps HTTPS et en-têtes associés dans le dossier de recette. SHA-256 des HTML : brève `b613537180b663ab37a8ffb430a04ee22879111b41f48e7aa9d4dcca8181f0e0` ; article `4b02415a55a6d8908e14d99d976b213e7cf4cdda36ee70d4b945f70a8f9b65cc`.

Le run garde des incidents éditoriaux/collecte non bloquants documentés : deux réponses de rédaction non JSON et les refus 403/429 déjà observés. Le scénario FTP en échec est éprouvé par injection locale et contrat du workflow, **pas par une panne provoquée en production**. Aucun gain de trafic ou de revenus n'est revendiqué.

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
