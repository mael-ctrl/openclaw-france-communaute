# /veille/ : export public sans listing

## Choix du 18 novembre 2026

Une seule intégration, reliquat SEO **#5** : fermer le listing du dossier `/veille/`, découvert pendant la recette des liens du 17. Les couvertures, dates, archives connues, cache et CLI de liens déjà intégrés ne sont pas refaits. Cette correction ne clôt ni l'alias OVH `/__ovh_icons/`, toujours listable, ni la réconciliation des URL historiques.

Préflight HTTPS du 18 : `/veille` répond 301, `/veille/` répond 200 avec `Index of`, `/veille/sources.opml` répond 200 et une ressource inconnue répond 404. SFTP : `veille/.htaccess` absent ; racine, règles des archives/ressources et CORS Skool sauvegardés hors dépôt avant modification.

## Réemploi et changement

Réemploi du générateur ciblé de `.htaccess` de `construction.construire()` : **une entrée ajoutée** pour produire uniquement `Options -Indexes\n`. Ni nouvelle page, redirection, authentification, dépendance ni changement du téléchargement OPML. Aucun gain SEO ou de fréquentation mesuré ; un dossier non listable ne rend pas ses fichiers privés.

Chasse GitHub : [apache/httpd](https://github.com/apache/httpd), licence Apache-2.0 vérifiée dans le fichier LICENSE, dernier push API observé le 17 novembre à 19:19:48 UTC. Révision lue : `acc0183cd16bf022926e8d88f9752a45b886ff36`. [Code natif du refus d'index](https://github.com/apache/httpd/blob/acc0183cd16bf022926e8d88f9752a45b886ff36/modules/generators/mod_autoindex.c#L2322-L2348). Trois fichiers épinglés, OID Git et SHA-256 vérifiés ; aucun code amont copié ou exécuté, seulement la directive native déjà utilisée par le projet.

## Recette locale

- Base initiale `cfbef2806aa42c5c3173fa0a28438357df2bf3e3` ; pull partagé refusé pour divergence, fichiers locaux préservés. Pull réussi dans un worktree propre du même dépôt, sans fusion de données ni de sceaux.
- Contrat `tests/test_autoindex_veille.py` : rouge observé sur les deux builds, puis vert. Un premier complément de test supposait à tort le CORS Skool versionné ; erreur conservée et assertion ramenée au fichier assets réellement suivi. Le CORS distant reste contrôlé séparément par SFTP.
- **396 tests Python et huit Node réussis** sur cette base. Deux builds complets à horloge commune dans une copie scratch : **5 231 sorties existantes identiques**, seul ajout `veille/.htaccess`, **2 603 HTML**, **627 fichiers de données préservés**.
- Essai isolé `--essai --sans-redaction` réussi : zéro rédaction, transfert ou publication Bluesky ; collecte partielle (quatre sources en erreur HTTP). Les données de recette ne sont jamais reprises dans le dépôt. Le journal de cette copie peut normalement s'allonger, sans réécriture des sceaux.

## Publication

Rebase sur `258e502c01c379dae7a98aa9f909bfb571ee0809` après livraisons voisines (podcast, source, guide et gouvernance) : conflit documentaire résolu en conservant les deux ajouts. **400 tests Python et huit Node réussis**, rouge/vert et deux builds complets rejoués : **5 232 sorties existantes identiques**, une seule règle ajoutée, 2 603 HTML et 627 fichiers de données préservés. Aucun changement de gabarit hors de cette règle.

**Livré le 18 à 15:13 CET, revérifié le 19 à 13:09 CET.** Code `1f455b9f0e19ccb1fbae0ca8e70dfa970521311d` poussé sur main ; les quatre fichiers du commit relus via l'API GitHub, octets et OID vérifiés. La reprise du contrôle le lendemain ne constitue pas une deuxième intégration quotidienne.

Installation ciblée de **17 octets par SFTP**, clé hôte épinglée avant authentification, cible absente revérifiée, fichier `.part` puis renommage et relecture exacte. Huit témoins intacts immédiatement après, dont l'OPML, la racine et le CORS Skool. Les runs actifs ont été inventoriés exhaustivement : les anciens constructeurs n'écrivent pas cette règle et le transport ne supprime pas les fichiers ; les nouveaux écrivent les mêmes octets. Cela n'est pas un verrou global entre producteurs.

**Deux séries de onze routes HTTPS après livraison :** `/veille` conserve sa 301 vers `/veille/` (port HTTPS explicite `:443` préservé), `/veille/` passe à 403 sans listing, l'OPML reste 200 et l'inconnu 404. Le 19, la règle et les sept autres configurations SFTP sont encore exactes ; l'OPML public contient désormais les **37 couples nom/URL exacts à Git**, après l'ajout LangGraph livré par un autre chantier. Notre transfert ciblé avait conservé ses 36 entrées initiales octet pour octet. Aucun catalogue ni page n'a été transféré par cette opération.

**Cloud distinct :** dispatch demandé [44321723463](https://github.com/mael-ctrl/openclaw-france-communaute/actions/runs/44321723463), **400 tests réussis** (146,736 s). Pipeline annulé le 18 à 15:18:52 UTC après environ 45 minutes de job, sauvegarde ignorée ; aucune ligne d'envoi de `veille/.htaccess` identifiée dans ses logs. Le correctif HTTPS est prouvé par la livraison ciblée et ses relectures, **pas par une réussite complète du cloud**. L'observateur avait subi timeout/réinitialisation réseau ; statut et logs relus le 19. Run automatique `44521077410` sur le même SHA encore en cours à 13:09 CET, sans nouvelle relance ni annulation ici. P9 et la consignation cloud restent ouverts.

Erreurs de recette conservées : première assertion trop stricte sur la redirection avec port `:443` ; état/statistiques/journal peuvent changer dans l'essai isolé. Tous les sceaux et le préfixe du journal sont vérifiés intacts, aucune donnée de recette intégrée.

Pièces privées : `crabe-chantiers/site/2026-11-18-veille-autoindex/` — préflight, rouges/verts, suites, comparaison de builds, sources Apache et captures. Aucun cron, wrapper, infrastructure, paiement, campagne ni notification Discord modifié.

## Continuité du 17

Le descendant `44081967086`, encore actif dans le précédent bilan, est désormais `completed/cancelled` : contrats réussis, pipeline interrompu le 17 à 13:04 UTC et sauvegarde ignorée. Ce résultat ne devient pas un succès du CLI livré ; son intégration Git et ses recettes locales restent distinctes. Le présent chantier n'active toujours pas ce CLI avant FTP et ne prétend pas réparer P9.
