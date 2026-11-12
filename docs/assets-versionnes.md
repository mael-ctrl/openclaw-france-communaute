# CSS/JS versionnés par contenu — 12 novembre 2026

## Une intégration, suite du chantier SEO #7

Les couvertures, dates/auteur JSON-LD, archives conservées, CSS commune intégrée, cache des JPEG et gzip XML/OPML étaient déjà livrés : ils ne sont pas réintégrés. Le relevé préalable confirme que les trois ressources locales chargées utilisent encore des URL stables et un cache de **900 secondes**. Le chantier retenu est le **versionnement et le cache annuel de ces trois CSS/JS**, pas un allongement aveugle du cache des originaux.

P9 (clone conflictuel, faux vert du wrapper, reprise et sauvegarde cloud) reste une priorité opérationnelle distincte. Le pull du clone partagé a été refusé ; ses conflits/données sont préservés. Travail sur un worktree propre issu de `51851b701c297d563818980c6003f03b503e1b3a`, avec pull réussi ici seulement. Aucun cron, wrapper ou lot de reprise non qualifié activé.

## Contrat livré

- `app.js`, `pack-copie.js` et `b2b-demo.css` deviennent `/assets/versionnes/<nom>.<sha256-des-octets>.<extension>`.
- Les **octets ne changent pas** ; les templates référencent les nouvelles URL. Le script du Pack reste réservé au Pack et sa CSS B2B à la page B2B. Podcast et démonstration autonome restent sans JavaScript.
- `engine/assets_versionnes.py` limite la lecture aux trois noms autorisés, refuse traversées/liens symboliques et produit les copies exactes. Toute modification de contenu change l'URL, sans dépendance ajoutée.
- `assets/versionnes/.htaccess` réserve `public, max-age=31536000, immutable` aux trois motifs exacts et aux statuts **200/206/304**. Pas de cache annuel sur erreurs, dossiers ou fichiers non versionnés. Repli sans `mod_headers` éprouvé.
- Le mtime **technique** des copies immuables est fixé à `946684800` afin de ne pas déclencher leur renvoi FTP sur chaque runner froid. Ce n'est pas une date de publication éditoriale.
- Les originaux restent disponibles pour les anciennes pages ; le déployeur incrémental ne supprime pas les anciennes versions distantes. **Ne pas purger celles-ci tant que des HTML peuvent les référencer.** Aucune réécriture Apache vers « la dernière version » : une ancienne empreinte ne doit jamais désigner de nouveaux octets.
- Les quatre fichiers nouveaux sont prépubliés par SFTP **avant** le push/dispatch qui peut publier leurs références HTML. Clé hôte épinglée avant authentification, bases absentes, `.part` puis renommage et relecture exacte ; onze témoins inchangés, dont racine, CORS, restrictions et originaux.

## Réemploi et licences

Audit du dépôt [h5bp/server-configs-apache](https://github.com/h5bp/server-configs-apache), **MIT**, HEAD `f9feb463fe136620ccde264b4cfbddfd8cd473b5`, dernier push API **14 juillet 2026 à 13:04:51 UTC**. Licence, `cache-control.conf` et `filename-based_cache_busting.conf` lus et vérifiés par OID Git. Références : [cache](https://github.com/h5bp/server-configs-apache/blob/f9feb463fe136620ccde264b4cfbddfd8cd473b5/h5bp/web_performance/cache-control.conf) et [noms versionnés](https://github.com/h5bp/server-configs-apache/blob/f9feb463fe136620ccde264b4cfbddfd8cd473b5/h5bp/web_performance/filename-based_cache_busting.conf).

Concept réemployé, **pas de framework ni copie de configuration amont** : leur réécriture vers le fichier mutable est volontairement écartée. Le générateur utilise SHA-256 de la bibliothèque standard et la règle de cache du projet déjà éprouvée pour les couvertures, confinée à un nouveau dossier.

## Vérifications réellement exécutées

- TDD : absence du module, destination manquante, périmètre des sources et politique absente observés rouges, puis verts. L'erreur initiale de fixture CSS manquante reste conservée.
- **338 tests Python**, **huit tests Node**, zéro échec final ; les tests historiques Pack/B2B vérifient désormais l'empreinte calculée indépendamment, sans affaiblir leurs périmètres.
- Deux builds isolés à horloge de test commune : **2 476 pages chacun**, **2 467 HTML modifiés uniquement par les URL**, **2 491 fichiers inchangés**, quatre ajouts, aucune suppression. **2 469 références** contrôlées vers leurs octets ; **713 fichiers sources** conservés. Aucun `data/` de recette importé.
- **42 requêtes sur Apache réel** : 21 avec et 21 sans `mod_headers` ; GET/HEAD, Range 206, If-Modified-Since et ETag 304, erreurs 404, dossiers/configurations 403, témoins mutables.
- Chromium local à **375 et 1 440 px**, avec/sans JavaScript : quatre configurations, douze réponses d'assets réussies ; recherche Actus, trois accordéons et **six copies de prompts exactes dans le vrai presse-papiers**, CSS B2B et absence de scripts podcast vérifiés. Capture mobile inspectée ; pas de changement visuel revendiqué.
- Vrai `--essai --sans-redaction` dans une copie distincte : code 0, zéro rédaction/transfert/publication sociale, manifestes inchangés et préfixe du journal préservé. Collecte partielle : deux 502 Hacker News, 403 L'Usine Digitale et 429 Reddit conservés ; pas un échec du build.
- Prépublication SFTP des **quatre fichiers relus**, **onze témoins préservés**. À **10:02:42 UTC**, **26 requêtes HTTPS conformes** : trois corps exacts, cache 200/206/304, gzip cohérent, originaux préservés, erreurs hors cache annuel et gzip XML/OPML toujours actif.

Pièces privées : `crabe-chantiers/site/2026-11-12/` (`build-evidence`, `apache-*`, `browser-local`, `sftp-*`, `https-prepublication`, logs des tests et de l'essai). Le premier lancement SFTP manquait de Pillow dans son venv : échec avant connexion conservé, puis utilisation du manifeste de build sans installer ni importer le moteur dans ce venv.

## État de publication au commit initial

**Assets et règle HTTP prépubliés et vérifiés ; références HTML et clôture cloud encore à confirmer après dispatch.** Ce statut intermédiaire sera complété par les observations finales. La prépublication additive évite des références vers des fichiers absents ; elle ne rend pas atomique le déploiement de l'ensemble du site.

Hors périmètre : cache annuel des images non versionnées, icônes, MP3 ou fichiers payants ; précompression, score Lighthouse et gains de trafic/conversion. Les ressources originales gardent leur cache court. Aucune amélioration de classement, de visites ou de ventes déduite du cache.
