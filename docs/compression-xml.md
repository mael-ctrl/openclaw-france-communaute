# Compression XML/OPML — 11 novembre 2026

## Périmètre

**Une intégration du chantier SEO #7 : gzip négocié pour les fichiers `.xml` et `.opml` du média.** Le cache annuel des couvertures est déjà publié ; images, dates visibles, auteur, catalogue conservé et CSS intégrée ne sont pas refaits. Aucun cache long n'est ajouté aux fichiers mutables ; aucun Brotli, fichier précompressé, changement éditorial ou gain de classement n'est revendiqué.

Les six ressources qualifiées sont `/feed.xml`, `/feed-articles.xml`, `/sitemap.xml`, `/news-sitemap.xml`, `/podcast/feed.xml` et `/veille/sources.opml`. Avant changement, leurs GET `Accept-Encoding: gzip` restent non compressés. HTML et JavaScript sont déjà compressés, et doivent le rester.

`outils/compression_xml.py` prépare **hors réseau** l'ajout au `.htaccess` racine réellement sauvegardé :

- précondition SHA256 exacte, octets de la base conservés ;
- bloc limité par `FilesMatch` aux extensions XML/OPML, puis par les cinq types MIME XML/RSS/Atom/OPML ;
- gardes `mod_deflate` et `mod_filter`, négociation normale d'Apache, sans `force-gzip` ;
- réapplication identique sans doublon ; refus d'un bloc différent, incomplet, dupliqué ou d'une sortie déjà existante ;
- aucun accès réseau, secret, transfert ou modification du fichier de base par cet outil.

**La racine Apache demeure gérée séparément du constructeur.** Son adoption automatique aurait pu écraser les redirections de domaine. Le build conserve une racine existante, n'en crée pas sur sortie neuve ; le déployeur ne supprime pas les fichiers distants absents du build. La mise en production se fait donc par SFTP ciblé après relecture de la base exacte, pas par déploiement intégral. Le snapshot distant du 11 contient les redirections `www` et `.com`, conservées octet pour octet avant le nouveau bloc. Le `_site` partagé ne contient pas de `.htaccess` racine au contrôle initial.

## Choix et état initial

Base propre `edab0f3d038676807ed39143cb0a002be1f1953d`, pull réussi dans le worktree dédié ; pull partagé refusé (128) pour fichiers non fusionnés, conflits préservés. Rapport du 10 lu, **1 181 références vérifiées intactes**. P9 reste prioritaire mais ses préparations ne sont pas activées implicitement : ni reprise Git/sceaux, ni candidat délai cloud, ni cron modifié par ce chantier.

Capacité initiale très basse (199 Mio affichés), puis plus de 3 Go disponibles à la mesure suivante **sans nettoyage par cette mission**. Recettes séquencées ; pas de purge des anciens lots. Les observations ne démontrent pas la cause du changement d'espace libre.

Le run de la précédente livraison, `42796037518`, est maintenant confirmé **annulé pendant pipeline**, sauvegarde ignorée. Ce constat ne retire pas la preuve HTTPS du cache déjà publié et ne signifie pas que le présent correctif répare l'exploitation.

## Recettes exécutées

- TDD en cinq étapes : ajout du bloc, précondition d'empreinte, idempotence/refus des marqueurs, CLI sans écrasement, confinement des extensions. Chaque refus initial est conservé.
- **330 tests Python et huit tests Node réussis.** Les anciens contrats de préservation de la racine et des protections voisines ne sont pas modifiés.
- Deux appels réels `construction.construire()` sur archive scratch de la base, à horloge commune et réseau refusé : **2 441 pages par build, 4 887 fichiers identiques, 704 fichiers de données/contenus/sites préservés**. Aucun HTML/flux/image n'est modifié par ce changement HTTP.
- Apache **2.4.67** réellement exécuté : **46 requêtes conformes** pour le candidat final, puis 46 sans `mod_deflate`, puis 46 sans `mod_filter`. GET, HEAD, refus `gzip;q=0`, identité, `br` seul, Range identité, 304, types MIME, redirections, protections et cache JPEG éprouvés. Fixtures locales, non données de production.
- **Régression détectée avant publication :** la première règle globale par MIME supprimait la compression HTML héritée dans le banc Apache. Ce candidat n'a jamais été publié. `FilesMatch` isole désormais les fichiers XML/OPML ; le contrôle réel de l'HTML redevient vert. Les pièces initiales sont conservées.

## Réemploi et documentation

Recherche GitHub avant développement : [`h5bp/server-configs-apache`](https://github.com/h5bp/server-configs-apache/tree/f9feb463fe136620ccde264b4cfbddfd8cd473b5), **MIT**, dernier push observé le **14 juillet 2026**, révision `f9feb463fe136620ccde264b4cfbddfd8cd473b5`. Licence et `h5bp/web_performance/compression.conf` conservés, octets vérifiés contre leurs OID Git. Réemploi des concepts et directives standard, **aucun bundle amont copié ou installé** ; sa longue liste de MIME et ses réécritures de `Accept-Encoding` ne sont pas reprises. `apache/httpd` (Apache-2.0, push observé le 11 novembre) et documentation officielle consultés ; exécution du serveur macOS existant, pas compilation du dépôt amont.

Sources : [mod_deflate](https://httpd.apache.org/docs/2.4/mod/mod_deflate.html), [AddOutputFilterByType](https://httpd.apache.org/docs/2.4/mod/mod_filter.html#addoutputfilterbytype). La compatibilité réelle OVH doit être constatée séparément du banc local.

## Opération reproductible

Après sauvegarde SFTP exacte et calcul de son empreinte, sur une **nouvelle sortie** :

```sh
python3 outils/compression_xml.py base.htaccess candidate.htaccess --sha256 EMPREINTE_EXACTE_DE_LA_BASE
```

Le jeton de commande ci-dessus est un paramètre à fournir, pas une empreinte valide. Vérifier syntaxe et négociation sur Apache ; relire la racine distante avant transfert ; refuser si différente de la base. Envoyer uniquement ce candidat via `.part` puis renommage atomique, relire les octets et les témoins voisins, enfin contrôler en HTTPS les six ressources et leurs variantes `identity`/`gzip`. Un rétablissement éventuel utilise seulement la sauvegarde exacte, après vérification que la racine courante est encore le candidat livré ; ne pas écraser un changement concurrent.

## Publication

**Au commit initial : code et recettes terminés, publication ciblée et contrôle HTTPS à confirmer.** Le workflow `maj.yml` vérifie les contrats et publie le média, mais n'installe pas cette configuration racine : son état doit être rapporté séparément. Aucun succès global cloud ou réparation de sauvegarde déduit d'une publication SFTP.

Preuves privées : `crabe-chantiers/integration-site/2026-11-11-compression-xml/` : logs rouge/vert, tests complets, manifestes des builds, Apache, sources amont et captures SFTP/HTTPS. Aucun secret ni corps de capture privé publié dans le dépôt.
