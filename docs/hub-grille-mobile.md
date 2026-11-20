# Grille des kits du hub — 20 novembre 2026

## Périmètre unique

Relais n° 1 du dernier rapport de préparation (18 novembre, repris le 19) : corriger la grille des deux kits gratuits de `openclaw-france.fr`. Les couvertures, dates étayées, catalogue des brèves et règles de listing déjà intégrés ne sont pas refaits. Les reliquats historiques SEO et la fiabilité des écrivains restent distincts.

Une ligne dans la règle mobile existante `@media (max-width:760px)` : `.grille-2{grid-template-columns:minmax(0,1fr)}`. Le minimum de 320 px des pistes du bureau débordait dans un conteneur mobile de 280 px. Aucun masquage `overflow` ajouté. La grille de bureau reste inchangée ; à 760 px, le passage à une colonne est intentionnel.

Les huit pages qui consomment `/static/style.css` portent désormais la même clé de version `sha256-80a14dcabde0542736d19ab9c3dec7912d13d5f3f8f86e7d010a52da6020d87d`. Les textes, commandes, liens de navigation, dates éditoriales, ZIP et scripts d'installation ne changent pas. Le fichier CSS reste mutable : cette clé n'est pas une nouvelle politique de cache immuable.

## Réemploi et licence

Candidat local préparé, pas un nouveau framework. Consultation de [w3c/csswg-drafts](https://github.com/w3c/csswg-drafts) avant intégration ; dernier push API observé le 20 novembre à 20:01:35 UTC, HEAD `328444151a63bf1c31228ec6d7ca354637d83ca0`.

- [CSS Grid, `minmax` et minimum automatique](https://github.com/w3c/csswg-drafts/blob/328444151a63bf1c31228ec6d7ca354637d83ca0/css-grid-1/Overview.bs#L1538-L1562).
- [Licence](https://github.com/w3c/csswg-drafts/blob/328444151a63bf1c31228ec6d7ca354637d83ca0/LICENSE.md) : **W3C Software and Document License**, API `NOASSERTION` ; les blobs de la spécification et de la licence sont identiques aux sources conservées du lot préparatoire.
- Concepts seulement : aucun code amont copié, installé ou exécuté. Les 417 pièces du manifeste parent du 18 ont été relues par empreinte avant reprise ; la délégation initiale demeure inachevée, les recettes nouvelles sont celles du présent chantier.

## Recette exécutée

Pull du clone partagé refusé pour divergence : `6f62095` local, `87310d9` distant au départ, **23 commits locaux / 146 distants** distincts. Rien n'est fusionné, réinitialisé ni effacé dans ce clone. Pull réussi dans un worktree propre seulement. Première base `87310d9`, puis rebase du seul correctif sur `b7d750c` pour préserver la réserve Mac Intel publiée entre-temps (`11e86cd`).

- Tests grille et cache réellement rouges avant leurs modifications, puis verts. Quatre contrats existants adaptés à la nouvelle clé exacte, sans retirer leurs contrôles métier.
- **409 tests Python**, commande `python3 -m unittest discover -s tests`, tous réussis sur la base finale ; **huit tests Node** réussis.
- Premier essai : 405 tests, une erreur **ENOSPC**, conservée dans les preuves. Nettoyage borné de six anciennes copies générées `_site`, inventaire et empreintes conservés ; aucune source, archive de preuve ou manifeste supprimé. Nouvelle suite initiale de 405 tests réussie, puis suite finale de 409 après rebase.
- **Deux builds média isolés à horloge commune : 5 261 fichiers identiques**, dont 2 617 HTML ; 631 fichiers de données et 84 fichiers de contenus inchangés. Dans les 36 fichiers du hub, seules la ligne CSS et les huit href attendus diffèrent. Nouvelle recette finale à 20:07 UTC, distincte de la première.
- Chromium sans JavaScript applicatif : **20 parcours et 217 contrôles réussis** à 320/375/760/1 280 px ; deux défauts attendus sur la base à 320 px. Le document passe de **340 à 320 px** ; 105 comparaisons de préservation (DOM, header, navigation, bureau) réussies.
- Huit téléchargements natifs (clic ou Tab+Entrée) comparés aux deux ZIP, accès au contenu et liens de guides contrôlés ; aucune commande d'installation exécutée. Réseau loopback et écritures du navigateur confinés, canaris de refus vérifiés. Les captures n'occultent pas le vrai header.

## Préflight distant et publication

Un premier snapshot SFTP a **refusé toute écriture** : la page Hermes distante contenait déjà la nouvelle réserve Intel. La comparaison a identifié le commit voisin, puis le correctif a été rebasé et testé. Nouveau préflight : les **neuf cibles sont exactement la base Git courante** ; sauvegarde des cibles et de huit témoins existants (règle racine, sitemap, CSS guide, pages légales, deux ZIP et sommes SHA-256). Clé SSH vérifiée avant accès au secret.

**Au commit documentaire initial : publication encore à confirmer.** Le transfert prévu est exclusivement SFTP, neuf fichiers, CSS puis HTML, `.part` et renommage après requalification. Le workflow `maj.yml` vérifie les contrats et publie le média, **pas le hub** : ses résultats seront distingués des relectures SFTP/HTTPS du hub.

Pièces privées : `crabe-chantiers/site/2026-11-20-grille-hub-integration/` (rouges, suites complètes, replays navigateur, snapshots SFTP, refus initial, inventaires des builds et nettoyage borné). Aucun lot de données de recette repris dans Git.

## Limites

Chromium seulement, pas certification WCAG, Safari/Firefox ou installation multi-OS. Le parcours des kits est mieux contenu dans le viewport ; aucun gain de téléchargement, d'audience ou de conversion n'est mesuré. Aucun cron, wrapper, sceau, paiement ou campagne modifié. Cette livraison ne résout ni l'alias OVH ni les courses de publication du média.
