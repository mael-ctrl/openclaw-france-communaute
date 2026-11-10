# Cache HTTP des couvertures — 10 novembre 2026

## Périmètre livré

**Une intégration autonome du chantier SEO #7 : le cache long des couvertures déjà versionnées.** Les actions antérieures (images, dates visibles, auteur, archives du catalogue conservé et CSS intégrée) ne sont pas refaites. Le cache des fichiers non versionnés, la compression XML et la précompression Brotli restent hors de cette livraison ; **le chantier #7 global n'est pas déclaré clos**.

Le constructeur copie déjà les fichiers cachés des assets. Le nouveau fichier `assets/couvertures/.htaccess` utilise cette voie existante, sans modifier le moteur, les contenus ni le workflow :

- seulement les noms `^[a-f0-9]{64}\.jpg$` sous ce dossier ;
- `Cache-Control: public, max-age=31536000, immutable` sur réponses **200, 206 et 304** ;
- retrait de l'ancien `Expires` sur ces seules réponses, sans supprimer Last-Modified/ETag ;
- aucun cache immuable ajouté aux erreurs, fichiers JSON, HTML, CSS, JavaScript, SVG, podcast ou livrables payants ;
- directive gardée par `IfModule mod_headers.c`, repli sans ce module éprouvé.

Les noms sont des empreintes **des entrées et versions du générateur**, pas les SHA256 des JPEG. `couvertures.py` inclut les données, sa VERSION, Pillow et l'encodeur dans cette clé. **Toute évolution du dessin ou de l'encodage impose d'incrémenter VERSION** ; ne jamais remplacer arbitrairement un JPEG sous un ancien nom. Les contrats existants de déterminisme et de séparation des encodeurs restent actifs. Cette livraison ne renomme ni ne réécrit les images.

## État initial et choix

Base propre `466e9a20c3e59a38438a27401685fde2041f1247`, après fetch puis pull réussi dans un worktree dédié. Pull du clone partagé refusé à 10:45 CET : six conflits et journal indexé laissés intacts. Le rapport de préparation du 10 et **ses 1 181 références** ont été lus/vérifiés ; ni capsule wrapper, ni reprise Git, ni candidat délai cloud n'ont été activés. La priorité d'exploitation reste ouverte, indépendante de cette politique HTTP bornée.

Lecture SFTP à **09:59 UTC** : cible absente, **3 760 noms JPEG conformes** listés (ce décompte n'est pas un contrôle du contenu de chaque image). Racine, restrictions des dossiers et CORS Skool sauvegardés. Trois JPEG répartis dans le listing relus en SFTP et HTTPS, octets identiques. Les trente requêtes HTTPS de qualification initiale confirment :

- pas de directive `immutable` sur les trois images ;
- gzip déjà actif pour accueil, podcast, CSS et JS, avec octets décompressés identiques ;
- **`/feed.xml` reste non compressé**, malgré Accept-Encoding gzip. Le premier vérificateur le supposait compressé : son échec est conservé, puis le constat a été explicitement séparé du cache JPEG.

Aucun nouveau gzip/Brotli n'est revendiqué. Ajouter une compression serveur XML nécessite une livraison racine distincte, préservant ses redirections. Aucun gain d'audience, CWV ou de bande passante réelle n'est mesuré ici.

## Recette exécutée

- TDD : absence du fichier puis absence du filtrage par statut reproduites en rouge ; deux passages verts conservés.
- `python3 -B -m unittest discover -s tests` : **321 tests réussis**. Première recette complète : 320 réussites et une erreur du nouveau test, qui supposait à tort le CORS Skool versionné localement ; cette règle existe seulement à distance et est désormais contrôlée dans la recette SFTP, sans changer les anciens contrats.
- `node --test tests/test_pack_copie.cjs` : **huit tests réussis**.
- Deux appels réels `construction.construire()` dans une archive scratch du SHA figé, réseau refusé, horloge commune : **2 405 pages par build**, **4 813 fichiers identiques**, ajout du seul `.htaccess` attendu ; **693 fichiers de données/contenus/sites préservés**.
- Apache local **2.4.67** réellement exécuté : règle absente → refus attendu du contrôle ; candidat → **neuf requêtes conformes**, puis neuf sans `mod_headers`. GET/HEAD/Range/If-Modified-Since, JPEG mutable témoin, JS, dossier interdit, fichier inexistant et protection `.htaccess` vérifiés. Les tests statiques ne sont pas présentés comme une exécution Apache.
- Deux incidents du banc local conservés : arrêt initial SIGTERM (Apache isolé ensuite dans sa propre session de processus) ; module autoindex initialement absent, ajouté au serveur jetable pour reproduire son statut 403. Aucun serveur de production touché.

## Réemploi

Recherche GitHub effectuée avant développement : `h5bp/server-configs-apache`, **MIT**, révision [`f9feb463fe136620ccde264b4cfbddfd8cd473b5`](https://github.com/h5bp/server-configs-apache/tree/f9feb463fe136620ccde264b4cfbddfd8cd473b5), dernier push observé le 14 juillet 2026. Licence et sources `cache-control.conf`, `cache_expiration.conf`, `compression.conf` conservées et vérifiées contre leurs OID Git. Réemploi du principe versionnement → cache long et des directives standard Apache ; **aucun bundle amont installé ni copié**. Le cache annuel générique du projet amont n'est pas repris : nos fichiers non versionnés en sont exclus.

`google/brotli` (MIT, push observé le 9 novembre) a aussi été repéré ; non adopté car aucun besoin de dépendance n'est démontré pour cette livraison. La fraîcheur des dépôts n'est pas une preuve de performance.

## Publication et suivi

Au commit initial : tests et builds terminés, **publication à confirmer**. Une seule nouvelle cible SFTP autorisée, après comparaison de sa non-existence et des sept témoins exacts, upload `.part` + renommage et relecture octet pour octet. Le workflow média doit être déclenché puis contrôlé séparément : ses annulations historiques à 45 minutes et sa sauvegarde ignorée ne sont pas réparées par ce fichier.

Preuves privées : `crabe-chantiers/integration-site/2026-11-10-cache-couvertures/` (journaux rouge/vert, suite complète, sources amont, manifestes des deux builds, Apache, snapshots SFTP et HTTPS). Aucun fichier de recette, donnée de test ou preuve privée n'est publié avec ce document.
