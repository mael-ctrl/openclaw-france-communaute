# Garde des liens avant publication — 22 novembre 2026

## Périmètre livré

Une intégration : raccorder le vérificateur local déjà livré au pipeline normal, **après construction et écriture de la clé IndexNow, avant FTP et annonces**. Candidat n° 1 du relais privé du 22, volet qualité SEO #15. Couvertures, dates visibles, archives, autoindex, cache et kit Intel ne sont pas refaits ; les limites historiques de ces dossiers restent distinctes.

Le CLI reste inchangé, sans dépendance supplémentaire. Un rapport incomplet, invalide, sans HTML, avec liens/ancres absents, quota dépassé ou lien symbolique provoque un code 1 avant transfert et annonces. La routine de preuves et le bilan existants restent exécutés ; aucune donnée ou ancien sceau réécrit. Les modes essai/sans-déploiement ne scannent pas : leur succès ne certifie pas les liens.

## Qualification préalable réelle

Pull du clone partagé refusé : six conflits et journal indexé, rebase actif préservé. Pull réussi **seulement dans le worktree isolé**, base `a5ab7695fc5b3dd4e5c70ff097e56102a85b2686`. Aucun reset, abort, fusion automatique ou modification de cron/wrapper.

- Rapport et manifeste du relais relus ; **38 pièces parent et 191 pièces du candidat** revérifiées par empreinte.
- Chasse GitHub recontrôlée : [Lychee](https://github.com/lycheeverse/lychee/tree/f10ac2774dac100dfdbf014647487520a8ffe08d), MIT/Apache-2.0, dernier push API 16/11 12:44:27 UTC ; [Linkinator](https://github.com/JustinBeckwith/linkinator/tree/62ba21965daddd9db2a451e8eacc510a010d6762), MIT, 20/11 11:36:36 UTC. Licences/sources épinglées du relais relues ; concepts seulement, aucun amont installé ni code tiers copié.
- Contrats appliqués seuls : refus attendus reproduits sur la base, notamment le FTP partant sans scan ; puis garde appliquée et **12 tests dédiés réussis**.
- **424 tests Python réussis** (`python3 -m unittest discover -s tests`) dans la copie scratch, et **huit tests Node** (`node --test tests/*.cjs`). Pas de test ignoré.
- **Deux builds isolés à horloge commune : 5 291 fichiers strictement identiques**, 724 sources `data/` et `contenus/` préservées. Aucune nouvelle page ou modification visuelle.
- **Deux scans réels complets**, chacun code 0 : **2 631 HTML / 7 930 entrées fichiers-dossiers / 95 534 564 octets HTML / 129 154 références**, dont **98 058 contrôlées et 31 096 exemptées**, zéro erreur. Les exemptions ne sont pas des liens validés.
- Les cinq budgets restent **10 000 entrées / 100 000 000 octets HTML / 2 000 000 par page / 200 000 références / profondeur 32**. Plus grosse page : `articles/index.html`, 861 098 octets ; profondeur maximale des fichiers : 4 composants. **Réserve HTML 4 465 436 octets : surveiller et requalifier avant saturation**, pas de relèvement automatique.
- Essai réel `--essai --sans-redaction` : code 0, aucun transfert/publication/rédaction ; quatre flux en erreur consignés, pas de collecte intégralement réussie revendiquée. **62 fichiers de sceaux identiques, préfixe du journal préservé** ; 776 octets ajoutés seulement au journal de la copie. Aucun `data/` de recette importé.

Preuves privées : `crabe-chantiers/site/2026-11-22-garde-liens-integration/` (`base.json`, `manifestes-revus.json`, `red.*`, `green.*`, `tests-all.*`, inventaires et scans `base/patched`, `essai.*`). Six anciennes copies générées `_site` de dates ≤11/11 nettoyées après inventaire/empreintes, **1 176 022 466 octets logiques** ; sources, manifestes, preuves et archives préservés. Espace après nettoyage : 3 025 702 912 octets, avant créations ultérieures ; pas une capacité actuelle garantie.

## Publication et limites

**Code `aba300c0484589c6a44e368a18675dbc1506129a` poussé et les six fichiers relus sur `origin/main`.** Un seul dispatch demandé par cette mission : [45009967046](https://github.com/mael-ctrl/openclaw-france-communaute/actions/runs/45009967046). Les deux successeurs ci-dessous ont été observés, pas redéclenchés ici.

| Run sur le même code | Contrats | Transferts réels journalisés | Issue du pipeline / sauvegarde |
|---|---|---:|---|
| `45009967046` | 424 tests réussis | 1 491 | Annulé à la limite officielle de 45 min, fin 11:18:50 UTC ; sauvegarde ignorée |
| `45016754940` | 424 tests réussis | 2 180 | Annulé pendant le pipeline, fin 12:04:52 UTC ; sauvegarde ignorée |
| `45022798615` | 424 tests réussis | 2 633 | Annulé à la limite officielle de 45 min, fin 13:17:38 UTC ; sauvegarde ignorée |

Les annotations GitHub du premier et du dernier attestent `The job has exceeded the maximum execution time of 45m0s`. Les flèches ci-dessus sont comptées **après le groupe de commande du vrai pipeline**, pas dans les fixtures des tests. Le premier parseur filtrant les noms d'étapes avait renvoyé zéro car le log affichait `UNKNOWN STEP` ; ce relevé invalide est conservé séparément des décomptes corrigés.

**La garde a été franchie avant ces transferts sur le code exact : activation dans le chemin cloud établie. Mais les événements `verification_liens` de ces runs ne sont pas sauvegardés dans Git**, puisque leur étape de consignation est ignorée. Aucun chiffre de scan cloud ni clôture de déploiement complet n'est inventé. Les 95 534 564 octets et autres compteurs ci-dessus proviennent de la recette locale figée, pas de la rédaction cloud.

**HTTPS final à 13:18–13:19 UTC : douze réponses contrôlées**, pages/flux/sitemaps en 200, `/veille/` en 403 sans listing. Version stable aux deux bornes : `2026-11-22T12:38:10+00:00`, 2 038 brèves / 564 articles déclarés. Cela ne rend pas la collecte atomique : ce marqueur peut être envoyé avant les dernières pages. Les corps ont changé depuis le relevé initial ; aucune égalité globale avec le SHA ni validation de toutes les URL n'est affirmée. **Intégration du garde vérifiée ; déploiement intégral et sauvegarde bloqués par les interruptions cloud.**

Aucun deuxième dispatch, repli FTP/SFTP d'HTML inchangé, changement de timeout/concurrence ou modification de cron n'a été lancé pour masquer l'échec. Prochaine étape : qualifier dans P9 un arrêt/export/reprise durable et la coordination des écrivains ; ne pas réintégrer le garde, ni faire passer les copies locales pour une sauvegarde distante.

Cette garde ne sérialise pas les écrivains et ne fige pas le répertoire entre scan et FTP. Le runner cloud isolé bénéficie du contrôle ; le clone partagé reste en rebase et sa routine peut masquer les erreurs : **pas de réparation P9 annoncée**. Aucun lien externe, CSS, JavaScript dynamique, formulaire, XML, validité HTML complète ou résultat SEO/audience n'est certifié. Les délais/annulations de déploiement restent un chantier distinct ; aucun repli SFTP d'HTML inchangé n'est nécessaire pour démontrer une garde Python.
