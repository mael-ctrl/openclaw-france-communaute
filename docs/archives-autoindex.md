# Archives : fermer les listings, conserver les URL

## Intégration du 18 octobre 2026 — chantier quotidien #5

Périmètre livré par ce lot : configuration des deux parents d'archives seulement.
Le plafond éditorial reste **400 brèves reconstruites, maillées et déclarées au
sitemap**, réparties en quatre pages de 100 au volume actuel. Ce lot ne prétend
pas réconcilier toutes les URL historiques ni fermer tous les listings OVH.

### Comportement

- `breves/.htaccess` généré : `Options -Indexes` et redirection permanente
  **exacte** de `/breves` ou `/breves/` vers `https://communaute-ia.fr/actus/`.
  Aucun sous-chemin de brève n'est redirigé ; les anciennes URL restent lisibles.
- `actus/page/.htaccess` généré : `Options -Indexes`, sans toucher aux pages
  numérotées. Le parent sans index doit répondre 403, pas 500.
- La configuration racine du domaine est conservée, ainsi que ses redirections
  `www` et `.com`. Aucun fichier de données, sceau ou historique n'est réécrit.
- Les deux fichiers de configuration sont hors sitemap. HTML, RSS, dates,
  images, téléchargements et règles commerciales sont inchangés.

### Préflight et réemploi

Base figée après pull : `ee9619dcedc3beebca87072554f6a3a3fdacd0d8`.
Les **77 pièces** du lot préparatoire `archives/2026-10-18` ont été vérifiées
contre le manifeste de la vague avant réemploi. Patch appliqué à une archive
neuve du SHA courant, puis complété par la redirection exacte, testée rouge/vert.
Aucune donnée ni sortie `_site` de préparation n'est importée.

Lecture SFTP du 18/10 à 08:49 UTC : les deux cibles `.htaccess` sont absentes,
ainsi que les configurations des parents du compte et `/actus/`. Le `.htaccess`
racine existant est sauvegardé hors dépôt ; il contient seulement les règles de
canonicalisation des domaines. Aucune configuration existante n'est écrasée.
La clé SFTP a été relevée puis épinglée avant authentification (TOFU, pas une
attestation d'identité indépendante). Aucun secret n'est dans ce document.

L'hébergeur documente explicitement `Options -Indexes` dans les `.htaccess` :
[OVHcloud, opérations possibles](https://docs.ovhcloud.com/en/guides/web-cloud/web-hosting/htaccess-what-else-can-you-do).
La redirection est fondée sur [Apache mod_alias, RedirectMatch](https://httpd.apache.org/docs/2.4/mod/mod_alias.html#redirectmatch).
La documentation ne remplace pas la recette HTTPS du serveur après publication.

Chasse aux dépôts, métadonnées revérifiées le 18/10 :

| Dépôt | Licence | Dernier push API | Décision |
|---|---|---|---|
| [h5bp/server-configs-apache](https://github.com/h5bp/server-configs-apache) | MIT | 14/07/2026 13:04:51 UTC | Directive Apache native ; pas de copie de configuration globale |
| [getpelican/pelican](https://github.com/getpelican/pelican) | AGPL-3.0 | 13/10/2026 10:31:16 UTC | Pagination interne réemployée ; aucun code AGPL copié |

### Recette locale réellement exécutée

- Contrat `tests/test_autoindex_archives.py` vu échouer sur l'absence des règles,
  puis sur l'absence de redirection exacte ; vert après chaque ajout. Regex testée
  avec/sans slash et contre des sous-chemins anciens, inconnus et non concernés.
- **130 tests Python** (`python3 -m unittest discover -s tests`) et **4 Node**.
- Deux builds isolés via `construction.construire()` à horloge identique :
  **1 368 sorties préexistantes identiques**, seulement deux fichiers ajoutés,
  aucune sortie supprimée ; **294 fichiers de données inchangés**.
- Vrai CLI `--essai --sans-redaction` en troisième copie : retour 0, zéro
  rédaction, transfert ou post. Collecte partielle : deux flux Hacker News 502,
  Siècle Digital 403 et Reddit Claude 429 ; un item collecté dans la copie.
  Journal à préfixe intact, registre et manifestes identiques, rien réimporté.
- Premier lancement de test refusé par le confinement à cause du `TMPDIR` macOS
  sous `/var` ; relancé sous scratch Hermes, sans affaiblir le contrôle des liens.

### Inventaire et limites assumées

Au SHA figé : **832 chemins connus, 831 IDs uniques** ; un ID possède deux slugs.
**400 pages construites = 400 liens uniques dans la pagination = 400 URL du
sitemap** ; 432 chemins connus hors fenêtre. Le plafond est documenté et conservé
plutôt que d'élargir arbitrairement le build en prétendant couvrir tout l'historique.

Le listing lu dans la préparation du matin contenait **1 532 répertoires**, dont
700 absents des données figées : ce ne sont pas 700 articles individuellement
validés. Le parent a lui-même relu 14 réponses HTTPS avant déploiement, confirmant
les listings `/breves/`, `/actus/page/` et `/__ovh_icons/`, ainsi que l'accès direct
à deux anciennes brèves hors fenêtre.

**Restent distincts :** réconciliation historique, politique d'archives pérennes,
ancien balisage des pages non reconstruites, dette OG/RSS/News/lastmod. Ne pas
purger, fusionner des IDs, déduire des redirections de suffixes, ni fabriquer une
date de première publication. Les autres listings (`/__ovh_icons/`, `/assets/`,
`/assets/podcast/`, `/fichiers/`) sont hors de ces deux répertoires : aucune
fermeture globale de l'hébergement n'est revendiquée. `-Indexes` ne rend pas
les fichiers privés. Aucun gain de crawl, d'indexation ou de trafic mesuré.

### Production

À renseigner après le workflow : identifiant et conclusion du run, sauvegarde
cloud, relecture SFTP des deux cibles et de la racine, redirections exactes,
absence de listing/500, pages numérotées et anciennes URL accessibles.

Preuves privées : `crabe-chantiers/archives/2026-10-18/integration/` ; recettes
isolées sous scratch Hermes. Les pièces préparatoires originales restent intactes.
