# Garde des liens avant publication — 22 novembre 2026

## Périmètre livré

Une intégration : raccorder le vérificateur local déjà livré au pipeline normal, **après construction et écriture de la clé IndexNow, avant FTP et annonces**. Candidat n° 1 du relais privé du 22, volet qualité SEO #15. Couvertures, dates visibles, archives, autoindex, cache et kit Intel ne sont pas refaits ; les limites historiques de ces dossiers restent distinctes.

Le CLI reste inchangé, sans dépendance supplémentaire. Un rapport incomplet, invalide, sans HTML, avec liens/ancres absents, quota dépassé ou lien symbolique provoque un code 1 avant transfert et annonces. La routine de preuves et le bilan existants restent exécutés ; aucune donnée ou ancien sceau réécrit. Les modes essai/sans-déploiement ne scannent pas : leur succès ne certifie pas les liens.

## Qualification préalable réelle

Pull du clone partagé refusé : six conflits et journal indexé, rebase actif préservé. Pull réussi **seulement dans le worktree isolé**, base `a5ab7695fc5b3dd4e5c70ff097e56102a85b2686`. Aucun reset, abort, fusion automatique ou modification de cron/wrapper.

- Rapport et manifeste du relais relus ; **38 pièces parent et 191 pièces du candidat** revérifiées par empreinte.
- Chasse GitHub recontrôlée : [Lychee](https://github.com/lycheeverse/lychee/tree/f10ac2774dac100dfdbf014647487520a8ffe08d), MIT/Apache-2.0, dernier push API 16/11 12:44:27 UTC ; [Linkinator](https://github.com/JustinBeckwith/linkinator/tree/62ba21965daddd9db2a451e8eacc510a010d6762), MIT, 20/11 11:36:36 UTC. Licences/sources épinglées du relais relues ; concepts seulement, aucun amont installé ni code tiers copié.
- Contrats appliqués seuls : refus attendus reproduits sur la base, notamment le FTP partant sans scan ; puis garde appliquée et **12 tests dédiés réussis**.
- **424 tests Python réussis** (`python3 -m unittest discover -s tests`) dans la copie scratch. Pas de test ignoré.
- **Deux builds isolés à horloge commune : 5 291 fichiers strictement identiques**, 724 sources `data/` et `contenus/` préservées. Aucune nouvelle page ou modification visuelle.
- **Deux scans réels complets**, chacun code 0 : **2 631 HTML / 7 930 entrées fichiers-dossiers / 95 534 564 octets HTML / 129 154 références**, dont **98 058 contrôlées et 31 096 exemptées**, zéro erreur. Les exemptions ne sont pas des liens validés.
- Les cinq budgets restent **10 000 entrées / 100 000 000 octets HTML / 2 000 000 par page / 200 000 références / profondeur 32**. Plus grosse page : `articles/index.html`, 861 098 octets ; profondeur maximale des fichiers : 4 composants. **Réserve HTML 4 465 436 octets : surveiller et requalifier avant saturation**, pas de relèvement automatique.
- Essai réel `--essai --sans-redaction` : code 0, aucun transfert/publication/rédaction ; quatre flux en erreur consignés, pas de collecte intégralement réussie revendiquée. **62 fichiers de sceaux identiques, préfixe du journal préservé** ; 776 octets ajoutés seulement au journal de la copie. Aucun `data/` de recette importé.

Preuves privées : `crabe-chantiers/site/2026-11-22-garde-liens-integration/` (`base.json`, `manifestes-revus.json`, `red.*`, `green.*`, `tests-all.*`, inventaires et scans `base/patched`, `essai.*`). Six anciennes copies générées `_site` de dates ≤11/11 nettoyées après inventaire/empreintes, **1 176 022 466 octets logiques** ; sources, manifestes, preuves et archives préservés. Espace après nettoyage : 3 025 702 912 octets, avant créations ultérieures ; pas une capacité actuelle garantie.

## Publication et limites

Au commit initial : code et qualification locale achevés ; **push, exécution cloud et relecture HTTPS encore à confirmer**. L'absence de changement HTML rend la disponibilité HTTP seule insuffisante pour prouver l'activation : exiger aussi le journal cloud `verification_liens` avant le déploiement et la sauvegarde d'état.

Cette garde ne sérialise pas les écrivains et ne fige pas le répertoire entre scan et FTP. Le runner cloud isolé bénéficie du contrôle ; le clone partagé reste en rebase et sa routine peut masquer les erreurs : **pas de réparation P9 annoncée**. Aucun lien externe, CSS, JavaScript dynamique, formulaire, XML, validité HTML complète ou résultat SEO/audience n'est certifié. Les délais/annulations de déploiement restent un chantier distinct ; aucun repli SFTP d'HTML inchangé n'est nécessaire pour démontrer une garde Python.
