# Favicon versionné — chantier du 14 novembre, poursuivi le 16

## Une amélioration, suite bornée du SEO #7

Les couvertures, dates/auteur JSON-LD, archives conservées, CSS intégrée, gzip XML/OPML et CSS/JS versionnés sont déjà présents. Ils ne sont pas réintégrés. Le reliquat retenu est **le favicon mutable** : lui donner une URL liée aux octets permet un cache long sans empêcher sa future mise à jour. Aucun changement du dessin, de l'image Open Graph, des contenus ou des dates éditoriales.

Le premier pull partagé a refusé la divergence locale/cloud. Ce clone et ses données sont préservés ; travail dans un worktree propre. Base initiale `33c4b84afc5070f5686affaa149da83bb413dfdc`, puis reprise explicite le **16 novembre** sur `ecb4e847746112dc7321cec2058b08eff6f78991`. Les observations du 16 ne sont pas antidatées au 14. P9, l'exploitation et les autres routines restent distincts.

## Contrat

- Réemploi du générateur `assets_versionnes` : `/assets/versionnes/favicon.<SHA256-des-octets>.svg` ; copie exacte, mtime technique fixe, refus des symlinks et des noms hors liste.
- Le lien `rel=icon` des gabarits commun et podcast, et le logo JSON-LD de l'organisation, utilisent cette URL. Le podcast reste **sans script ni iframe**.
- Le favicon original reste disponible pour les anciennes pages. Les anciens fichiers immuables ne sont ni remplacés ni purgés.
- Cache annuel `public, max-age=31536000, immutable` seulement pour le motif exact et les statuts **200/206/304**, avec repli sans `mod_headers`. Autres images, erreurs et originaux hors périmètre.
- Pas de dépendance nouvelle ; deux fixtures existantes reçoivent leur fichier favicon, sans affaiblir leurs assertions.

## Réemploi documenté

[h5bp/server-configs-apache](https://github.com/h5bp/server-configs-apache), **MIT**, révision `f9feb463fe136620ccde264b4cfbddfd8cd473b5`, dernier push API observé **14 juillet 2026 à 13:04:51 UTC**. Licence et sources `cache-control.conf` / `filename-based_cache_busting.conf` retéléchargées et vérifiées par OID Git dans le dossier privé. Réemploi du concept et des outils déjà intégrés au projet, **aucune copie de configuration amont ni réécriture vers un fichier mutable**.

## Vérifications réellement exécutées

- TDD : référence absente puis règle/podcast absents observés rouges ; quatre contrats nouveaux. Premier essai d'assertion JSON sensible aux espaces corrigé par parsing réel. Deux erreurs de fixtures historiques sans favicon conservées, puis corrigées sans changement du garde-fou.
- Sur la base initiale : **359 tests Python et huit Node**, deux builds isolés, 56 requêtes Apache réel (28 avec le module / 28 sans). GET, HEAD, Range, conditionnels 304, MIME SVG, erreurs et témoins CSS/JS vérifiés.
- Après rebase : **363 tests Python réussis**, deux nouveaux builds isolés à horloge commune du 16/11 11:00 UTC : **2 580 HTML changent seulement l'URL du favicon**, 2 605 autres fichiers inchangés, une règle cache modifiée, un fichier SVG ajouté, aucune suppression. **737 fichiers sources préservés**, 5 161 références vers des assets vérifiées. Les deux compteurs de tests correspondent à deux bases, ils ne s'additionnent pas.
- Vrai `engine/run.py --essai --sans-redaction` dans la copie initiale, exécuté le 16 : code 0, aucune rédaction, aucun transfert ni post ; erreurs tierces 502/403/429 de collecte consignées. Les données de recette ne sont pas importées.
- **Préflight SFTP initial refusé sans écriture** : le fichier SVG versionné existait déjà à distance. Origine de cette présence non attribuée. Nouvelle recette : octets exactement égaux au source et à son SHA256, fichier conservé sans réécriture ; seule la règle `.htaccess` est transférée après contrôle de la base Git exacte et sauvegarde. Relecture exacte, **14 témoins préservés**, clé hôte épinglée avant secret.
- **23 réponses HTTPS avant publication des gabarits**, toutes conformes : SVG exact, cache 200/206/304, original et CSS/JS conservés ; erreurs/dossier hors cache annuel. Les pages sont encore contrôlées séparément après le déploiement cloud.

Preuves privées : `crabe-chantiers/site/2026-11-14/` : logs rouge/vert, `build-evidence/`, `build-rebase/`, `apache-*`, `sftp-before/` (refus), `sftp-requal-*`, `https-before/`, `upstream/`. Les premières observations ne sont pas remplacées.

## Publication

Au commit de préparation : **règle HTTP publiée et vérifiée ; nouveaux gabarits prêts, publication et sauvegarde cloud à confirmer**. Le code est complet et les contrats passent ; ce statut intermédiaire ne revendique pas encore la fin du déploiement.

### Vérification finale du 16 novembre, 13:10 CET

**Code `3d8d787`, documentation initiale `4fb2416`, publication HTTP confirmée.** Le run [43855631049](https://github.com/mael-ctrl/openclaw-france-communaute/actions/runs/43855631049) exécute **363 tests avec succès** ; son bilan métier rapporte **2 651 fichiers envoyés**. Il est néanmoins **annulé à la limite de 45 minutes**, à la fin du pipeline ; l'étape de sauvegarde est **skipped**. Aucun succès global ni commit de sauvegarde inventé, aucune augmentation du délai ni réparation de P9 par ce chantier.

Après la fin du run : **deux séries de 23 réponses HTTPS conformes**. Dans chacune, onze pages (accueil, Actus, Articles, Pack, B2B, Podcast, Transparence, deux articles et deux anciennes brèves conservées) référencent le favicon exact ; logo JSON-LD également vérifié hors podcast. SVG exact, MIME et cache 200/206/304, original préservé, erreurs hors cache annuel. Les trois CSS/JS précédemment versionnés restent exacts ; **23 références icon/CSS/JS sur ces onze pages** contrôlées selon leur périmètre. Podcast sans script ni iframe. La première sonde effectuée pendant le transfert échouait sur l'accueil encore ancien : conservée dans `https-after/`, non remplacée par les recontrôles `https-after-final/` et `https-after-confirmation/`.

Cette recette clôt **la publication de la fonction**, pas la sauvegarde des nouvelles données éditoriales de ce run. Le rendu HTTPS n'est pas attribué à un commit de données sauvegardé absent. Les neuf fichiers du correctif initial ont été relus identiques sur `origin/main` ; aucune donnée du build d'essai n'est publiée. Prochaine action d'exploitation : traiter séparément le dépassement et la consignation, sans relancer aveuglément le même pipeline ni réécrire les preuves.

Hors périmètre : cache annuel de l'image OG générique, MP3 ou livrables ; précompression ; résolution de la concurrence des producteurs ; comparaison de tous les anciens HTML hors données conservées. Aucun gain de classement, trafic ou conversion mesuré ni promis.
