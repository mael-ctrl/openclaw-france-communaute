# Auteur JSON-LD — lien vers la présentation du média IA

## Choix du chantier unique — 2 novembre 2026

Exécution différée, datée du jour réel ; aucun résultat antidaté au 31 octobre.
Base `6530893de6c2296a60b19058df79b90e6494c38f`. Les priorités #1–#3 sont déjà intégrées ; la partie dates de #4 aussi. Le reliquat **`author.url` de #4**, encore explicitement ouvert dans la roadmap et absent du code/HTML observés, est le seul changement de ce passage. Les archives conservées/autoindex déjà traités ne sont pas réintégrés ; l'historique inconnu et l'exploitation restent des chantiers distincts.

`jsonld_item()` conserve l'identité `/#organisation` et précise localement le type `Organization`, le nom configuré du média et l'URL canonique `/transparence/`. Il ne transforme pas le Crabe en personne humaine. La page cible présente déjà le média IA et ses méthodes, répond 200, et reste accessible par les liens visibles existants. Aucun texte, image, date, source, auteur supplémentaire, navigation ou traitement de données n'est ajouté.

## Réemploi et sources

- [Google, données structurées Article](https://developers.google.com/search/docs/appearance/structured-data/article#author-bp), relu le 02/11 : `author` accepte `Organization`, les champs type/nom/URL sont recommandés. Cette documentation ne promet pas de résultat enrichi ni de gain d'audience.
- Chasse GitHub : [mmistakes/minimal-mistakes, `_includes/seo.html`](https://github.com/mmistakes/minimal-mistakes/blob/411699970e028cd5545d40fbcd3e2159275f72c2/_includes/seo.html#L43-L48), licence [MIT](https://github.com/mmistakes/minimal-mistakes/blob/411699970e028cd5545d40fbcd3e2159275f72c2/LICENSE), dernier push API observé **09/10/2026 08:32:08 UTC**. Le gabarit distingue l'identification de l'auteur des autres métadonnées ; il n'est pas une implémentation de notre champ JSON-LD. Source et licence vérifiées contre leurs OID Git. **Aucun code amont copié, aucune dépendance installée** : réemploi du générateur Python existant, changement indépendant fondé sur la documentation Google.

## Recette avant livraison

- Test d'abord : échec attendu sur les deux gabarits, puis vert. Quatre contrats dédiés : deux gabarits/identité/dates absentes ; configuration et échappement ; graphe du site/pages non éditoriales ; tous les autres champs et dates explicitement fournis.
- **273 tests Python et huit Node réussis**, dans une copie issue du SHA figé, pas dans le clone actif.
- Deux vrais appels `construction.construire()` hors réseau à horloge commune : **4 376 fichiers**, dont **2 149 pages éditoriales** différentes uniquement par les trois propriétés ajoutées à l'auteur ; **2 227 autres fichiers strictement identiques**. Comparaison SHA-256 de tous les fichiers après retrait exact de ce seul ajout.
- **598 fichiers data/contenus inchangés** après tests et builds. Le mode `--essai --sans-redaction` isolé réussit ensuite : zéro rédaction, transfert ou post ; collecte Reddit Claude en 429 consignée. Aucune donnée de recette reprise en production.
- Pull initial du clone partagé refusé pour divergence ; données locales laissées intactes. Worktree du même dépôt sur `origin/main`, pull réussi ici seulement. Ni fusion automatique de preuves ni reset.

Pièces privées : `crabe-chantiers/integrations/auteur-jsonld-20261102/` — provenance épinglée, rouge/vert, suites, inventaires SHA-256, comparaison intégrale, collecte d'essai et sondes HTTPS initiales. Le manifeste final reliera les preuves de déploiement.

## Déploiement

**Au commit d'intégration**, le contrôle était en attente ; cette observation initiale reste conservée. Code livré : `da1de68`.

### Clôture vérifiée le 3 novembre

Le descendant `41421736642`, encore actif à la fin du premier passage, a finalement été **annulé pendant pipeline** à 10:23 UTC le 02/11, avec sauvegarde ignorée. Il n'est pas reclassé en succès. Les successeurs ont repris : [run `41601493451`](https://github.com/mael-ctrl/openclaw-france-communaute/actions/runs/41601493451) terminé avec succès le 03/11 à 08:55 UTC ; **277 tests, 2 276 fichiers envoyés, sauvegarde `a1ccb93`**, étapes et logs relus.

À **09:54:36–09:55:16 UTC le 03/11**, lecture HTTPS individuelle des **2 149 cibles exactes** du premier build : **2 149/2 149** répondent 200 à l'URL attendue, identité `mainEntityOfPage` et objet auteur conformes. Les **367 cibles encore anciennes au préflight du 2 sont toutes conformes**. Corps, en-têtes, empreintes et résultats conservés hors dépôt dans `crabe-chantiers/integrations/auteur-cloture-https-20261103/`. Version et sitemap identiques aux deux bornes ; la collecte n'est néanmoins pas atomique et n'atteste pas toutes les autres métadonnées de chaque page.

**Chantier auteur clôturé, sans nouveau transfert ni réécriture.** La première tentative de recontrôle SFTP n'a pas pu importer Paramiko dans l'interpréteur choisi ; aucune connexion ni écriture distante n'a eu lieu. Le contrôle complet a été fait par HTTPS strict, sans nouvel accès ni installation. Les anciennes URL inconnues hors de ces 2 149 cibles et l'exploitation restent hors de cette clôture.

## Limites

Aucune validation Google Rich Results/Search Console, aucun gain de référencement ni de trafic revendiqué. Les deux captures éditoriales préalables ne sont pas un audit exhaustif. Les anciennes URL hors du catalogue construit peuvent garder leur ancien balisage ; aucune purge ou reconstitution historique. Les courses de publication, le timeout cloud et la divergence du clone partagé restent distincts et non corrigés.
