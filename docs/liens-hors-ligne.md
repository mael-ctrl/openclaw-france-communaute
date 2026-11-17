# Liens et ancres : contrôle local du catalogue — 17 novembre 2026

## Choix d'une seule intégration

Le dernier relais privé du 17 recommande en premier ce vérificateur : nouvelle amélioration de qualité du média, issue du point SEO #15, sans ajouter une nouvelle page ou changer les contenus. Les couvertures, métadonnées étayées, `<time>`, archives, CSS intégrée et assets versionnés disposent déjà de contrats et livraisons ; ils ne sont pas réintégrés. Les reliquats (dates de première publication non démontrées, alias OVH, optimisations spéculatives, grille du hub et coordination des écrivains) ne sont pas réputés résolus. Le classement ancien du 14 octobre ne suffit pas à justifier un deuxième chantier ni une promesse SEO.

**Livrable complet et borné : CLI autonome documenté, 27 tests dédiés, exécution réelle sur le catalogue complet.** Son intégration n'ajoute pas de garde automatique avant FTP ; seule sa suite unitaire entre dans les contrats CI existants. Ce point #15 reste plus large que ce livrable. Aucun gabarit, contenu, asset, workflow, cron, preuve éditoriale ni donnée modifié.

## Base et réemploi

Pull initial du clone partagé refusé avec code 128 : six conflits et journal indexé, préservés sans reset/abort/stash/fusion. Worktree propre du même dépôt créé sur **`bb75aee359e4d4fb5ef47eca53757764a42ef9f0`**, pull réussi ici seulement. Les 44 pièces du manifeste parent du 17 ont été relues et leurs SHA256 vérifiés.

Les deux patches privés sont appliqués en séparant les contrats du produit : rouge « CLI absent », puis 21 tests verts ; rouge du budget historique (deux échecs), puis trois tests de capacité verts. Le plafond dur admet 128 Mo, mais le défaut reste 20 Mo. Revue d'intégration : sept assertions ont reproduit des faux liens/ancres dans `title`/`textarea` et des faux éléments actifs après `/>`. Correction bornée du contexte texte/template et trois tests supplémentaires verts, sans prétendre implémenter tout HTML5.

Références/licences/fraîcheur : [mode d'emploi](../outils/README-liens.md#tests-et-provenance). Réemploi du candidat interne ; aucun code tiers copié ni dépendance ajoutée.

## Recettes réellement exécutées

- `python3 -m unittest discover -s tests` : **394 tests, code 0** sur Python local ; tous les contrats existants conservés.
- `node --test tests/*.cjs` : **huit tests, code 0**, exécutable résolu explicitement.
- Build neuf depuis l'archive du SHA courant, `import construction; construire()`, dans un scratch séparé, réseau refusé par audit hook ; aucune collecte/rédaction/FTP/social. **1 016 fichiers source relus identiques après construction**.
- **5 217 fichiers construits, dont 2 596 HTML / 94 293 418 octets HTML**. Inventaire indépendant, pas le compteur de sorties du constructeur.
- Scan avec `--canonical-host communaute-ia.fr --max-bytes 100000000 --max-links 200000` : **127 460 références, 96 767 contrôlées, 30 693 exemptées, zéro erreur, `complete=true`, code 0**. Les exemptions de ce corpus sont disjointes des contrôles ; ce n'est pas une propriété générale du format.
- Deux scans successifs produisent le même JSON ; empreintes des 5 217 sorties inchangées. Le nombre et les octets HTML correspondent exactement à l'inventaire, aucun HTML absent.

Preuves privées durables : `crabe-chantiers/site/2026-11-17/evidence/` (`red-*`, `green-*`, `full-tests.*`, `node.*`, `source-inventory.json`, `build-inventory.json`, `scan.json`, `build-result.json`). Copie de recette jetable sous le scratch Hermes, jamais importée en production. Les anciens lots et leurs manifestes sont conservés.

## Limites et publication

Le scan est local et hors réseau : existence des cibles ≠ HTTP, validité HTML5, installation de kit, abonnement, paiement, indexation ou gain de trafic. Aucun diagnostic ne confirme ici un défaut de lien de gabarit ; aucun correctif de page inventé. Les non-couvertures et quotas sont dans le mode d'emploi et chaque JSON.

**Au commit initial : code prêt et recettes locales réussies ; push, contrats cloud, déploiement, sauvegarde et sondes HTTPS encore à confirmer.** Ces étapes seront consignées séparément. Le dispatch `maj.yml` demandé conserve son fonctionnement éditorial habituel ; aucune seconde intégration ni modification de ses garde-fous.
