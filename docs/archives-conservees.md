# Catalogue des brèves conservées — 19 octobre 2026

## Périmètre du chantier quotidien #5

La fermeture des parents d'archives du 18/10 reste en place. Ce lot complète la
**couverture des sources éditoriales encore présentes**, sans restaurer des
versions retrouvées seulement dans Git et sans faire passer le catalogue pour
l'ensemble des URL historiques.

- `/actus/` garde son plafond de **400 brèves**, quatre pages de 100.
- `/archives-breves/` réemploie le même gabarit avec un périmètre distinct :
  toutes les brèves de `data/breves.json`, par pages de 100. Pages suivantes :
  `/archives-breves/page-2/`, etc. Canonical propre, précédent/suivant HTML,
  recherche et filtres limités à la page. Un lien depuis le fil et `llms.txt`
  rend le catalogue découvrable sans JavaScript.
- Toutes ces brèves sont reconstruites à leur **URL d'origine**, avec les
  couvertures et le balisage actuels ; elles sont toutes dans le sitemap.
- Le préflight contrôle tous les slugs avant écriture : collision de chemin
  ou traversée refusée. Deux slugs portant le même ID restent deux pages.
- Ni date de publication ni date de modification JSON-LD inventée. Les brèves
  ajoutées hors fil n'héritent pas d'un `lastmod` non établi. La dette distincte
  des dates du fil, du News-sitemap et des RSS n'est pas corrigée par ce lot.
- Aucun fichier historique, journal, manifeste ou enregistrement éditorial
  modifié ; aucun effacement FTP, redirection nouvelle ni configuration Apache.
  Les règles de `/breves/` et `/actus/page/` restent identiques.

## Pourquoi ce choix

Les actions #1–#4 majeures sont déjà intégrées, et #5 reste le chantier SEO
prioritaire. Le rapport de la vague du 19/10 et ses **823 pièces d'archives**
ont été relus/vérifiés contre le manifeste. Il distingue les sources actuelles,
les versions seulement retrouvées dans Git et les chemins inconnus.

Le présent lot traite uniquement la troisième recommandation de ce rapport :
reconstruire les pages actuelles hors fenêtre après vérification de leur contenu,
sans élargir le fil récent. Le registre historique durable et les arbitrages
sur les versions disparues restent séparés. Aucun des patches newsletter,
preuves ou audit commercial n'est importé.

### Chasse aux dépôts et réemploi

Métadonnées GitHub relues le 19/10 :

| Dépôt | Licence API | Dernier push | Décision |
|---|---|---|---|
| [jekyll/jekyll-paginate](https://github.com/jekyll/jekyll-paginate) | MIT | 25/01/2023 17:55:35 UTC | `lib/jekyll-paginate/pager.rb` lu : pagination statique et canonical de première page. Pas de dépendance Ruby ni copie ; réemploi du gabarit Python existant. |
| [getpelican/pelican](https://github.com/getpelican/pelican) | AGPL-3.0 | 13/10/2026 10:31:16 UTC | Aucune adoption ni copie AGPL ; le moteur du média suffit. |

## Recette locale exécutée

Base après pull et fusion sans conflit : `2f97abc0e195523978495ee5f262970fa4b7e64c`.
Le pull rapide était impossible : seul le commit local de métriques divergeait,
et ses changements sont conservés. Aucun `-X ours`, reset ou réécriture de preuve.

- Contrat vu rouge sur la brève 401 absente, puis sur l'absence du catalogue ;
  vert après les deux tranches. **142 tests Python et 4 Node réussis**.
- Deux builds réels isolés, horloge commune, sans réseau : **1 405 fichiers
  préexistants identiques**, six changements attendus (quatre pages du fil,
  sitemap, llms.txt), **993 ajouts**, aucune sortie supprimée.
- **892 enregistrements = 892 chemins construits = 892 liens uniques du
  catalogue = 892 brèves dans le sitemap** ; neuf pages du catalogue.
  891 IDs : la relation d'un ID vers deux slugs est préservée.
- **492 anciennes pages** lues individuellement en HTTPS avant déploiement :
  200, URL finale inchangée, titre/résumé exacts, source et lien présents comme
  dans les données. Corps et empreintes conservés hors dépôt. Aucun changement
  éditorial n'est requis pour les reconstruire avec le gabarit actuel.
- **315 fichiers de données inchangés** après tests/builds. Essai réel
  `--essai --sans-redaction` : retour 0, trois items collectés dans la seule
  copie, zéro rédaction/transfert/post, sceaux identiques et préfixe du journal
  préservé. Erreurs de collecte consignées : Hacker News OpenClaw 502,
  Siècle Digital 403, Reddit Claude 429 ; aucun résultat de test réimporté.
- Chromium isolé, JavaScript désactivé : parcours fil → catalogue → suivant →
  précédent → ancienne brève vérifié à **390 et 1 440 px**, sans débordement.
  Captures relues. Le header mobile préexistant reste haut, sans chevauchement
  du texte ; il n'est pas refondu dans ce chantier. Navigateur personnel laissé
  intact malgré son profil verrouillé.

## Livraison

Le premier run **39228430624**, code `85740f9`, a été **annulé à la limite de
25 minutes**, pendant le transfert FTP : 1 176 envois consignés, dernier chemin
sous `breves/pre-entrainement-…`. Ce n'est pas un déploiement achevé ; la sauvegarde
finale a été sautée par l'annulation. Les tests cloud (142) étaient verts.

Cause observée : le premier transfert du catalogue et de ses couvertures dépasse
le budget précédent. Le budget du job est porté à **45 minutes, toujours borné**,
sans changer cadence, concurrence, secrets ou mécanisme de sauvegarde. Contrat
rouge/vert ajouté ; **143 tests Python et un nouveau build isolé réussis** sur
la base rafraîchie `3bc6406`, 316 fichiers de données inchangés. La relance doit
partir de `main` à jour, pas rejouer l'ancien SHA. **Cloud/HTTPS final en attente**.
Le catalogue répondait 404 avant cette intégration.

Preuves privées : `crabe-chantiers/archives/2026-10-19/integration-conservees/` ;
recette isolée `archives-conservees-_o_u738j` sous scratch Hermes.

## Limites restant ouvertes

Ce n'est pas un registre pérenne append-only : un enregistrement absent des
données courantes n'est pas automatiquement restauré depuis Git. Les anciennes
URL hors de ce périmètre ne sont ni supprimées, ni redirigées, ni déclarées
corrigées. Les listings d'assets et `/__ovh_icons/` sont distincts. **#5 reste
partiellement ouvert**, même si le catalogue des sources actuelles est complet.
Aucune indexation effective ni hausse de trafic n'est démontrée.
