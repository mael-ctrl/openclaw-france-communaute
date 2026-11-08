# CSS commune compacte et intégrée au HTML

## Choix et périmètre

Chantier commencé le **7 novembre 2026**, poursuivi et vérifié le **8 novembre** après interruption de l'exécution ; aucune observation n'est antidatée. Une seule intégration fonctionnelle : **action SEO/performance n° 6**, CSS commune minifiée puis intégrée dans le `<head>` des pages média et podcast. Les couvertures, dates JSON-LD, auteur, catalogue conservé et impression étaient déjà livrés. L'alias OVH et les chemins historiques inconnus restent des limites distinctes, pas une raison de les purger.

`engine/styles.py` relit `assets/style.css`, minifie sa syntaxe et mémorise seulement le résultat par contenu, pas par date de fichier. Le HTML, les textes préformatés, le JavaScript, les métadonnées, les fichiers payants, RSS, sitemaps, images et données ne sont pas minifiés/réécrits. La feuille originale reste disponible pour les anciennes URL non reconstruites. Les CSS spécialisées B2B restent externes. Le podcast garde son contrat sans `<script>` ni iframe.

Garde explicite : source manquante/vide, fermeture `</style`, `url(...)`, `@import` ou `@charset` reconnus refusés avant publication. Il s'agit d'un contrat conservateur pour notre CSS versionnée sans ressource, **pas d'un assainisseur de CSS non fiable**. Une évolution nécessitant des URL/échappements doit requalifier la base de résolution et le contrat.

## Réemploi, sans nouvelle installation

[RCSSmin](https://github.com/ndparker/rcssmin/blob/7e457c8163324f02d2df10ed1612c91b53dcf276/rcssmin.py), Apache-2.0, révision `7e457c8163324f02d2df10ed1612c91b53dcf276`, version déclarée 1.3.0 ; dernier push API observé le 10/10/2026. Module et licence copiés **sans modification**, OID Git vérifiés. Appel explicite de la variante Python, sans extension C ni installation cloud/local. Provenance dans `engine/vendor/README.md`, licence intégrale jointe. `wilsonzlin/minify-html` (MIT) écarté pour ne pas réécrire les contenus HTML.

## Recette locale réellement exécutée

- Pull du clone partagé refusé pour divergence, modifications/données locales préservées. Worktree propre sur `4913b10`, puis avance rapide sans conflit sur **`555f3e7`** pour inclure les livraisons voisines ; aucun reset, rebase des données ou écrasement de sceau.
- Trois rouges observés puis verts : CSS intégrée, podcast sans requête commune, refus des sources non transportables. Six nouveaux tests couvrent aussi cache par contenu, source absente, chaînes/Unicode, `calc`, pseudo-classes, impression et commentaires de licence.
- **311 tests Python réussis sur la base actualisée**, dans une copie scratch ; **huit tests Node réussis** (scripts inchangés par l'actualisation). Première recette scratch incomplète (workflow omis) conservée, puis `.github` copié et suite entière rejouée, sans affaiblir les tests.
- Deux builds à horloge commune sur `4913b10` : **4 727 fichiers**, **2 355 HTML** ne diffèrent que par le remplacement du lien CSS ; **2 372 autres fichiers identiques**. **705 fichiers d'entrée préservés**. Build et essai isolé sur `555f3e7` : **2 377 sorties de pages**, **712 fichiers d'entrée du worktree préservés**.
- `engine/run.py --essai --sans-redaction` : code 0, aucune rédaction/transfert/publication sociale, manifestes inchangés et préfixe du journal conservé. Collecte partielle : deux flux HN expirés, reset Hermes releases, Usine Digitale 403 et Reddit Claude 429 ; ce n'est pas une collecte entièrement réussie. Aucune donnée de recette importée.
- **210 contrôles Chromium réussis, 60 vues** : dix pages, écran 390/1 440 px et média print. Corps exact, géométrie/styles calculés, pixels de viewport et images inchangés ; requête `/assets/style.css` supprimée. Compteurs et réseau tiers bloqués en recette.
- Premier comparateur trop strict conservé : ordre d'énumération des propriétés CSS et espaces après virgule dans trois variables (`--sans`, `--mono`, `--ombre`) différaient, sans différence de pixels. Diagnostic élément par élément puis comparaison triée ; seuls les espaces après virgule hors chaînes sont normalisés pour les tokens CSS. Déclarations résolues, géométrie et pixels restent contrôlés sans normalisation.

## Mesures et limites

CSS source **24 075 octets**, intégrée **19 526 octets** : **−18,9 %** sur la feuille commune. Une requête CSS bloquante en moins sur les pages reconstruites ; pas une mesure LCP/INP ou de trafic.

L'intégration ajoute **19 511 octets bruts** à chaque HTML. Accueil : 27 582 → 47 093 octets, donc le budget théorique ancien de 40 Ko n'est **pas** respecté. Gzip simulé en laboratoire, HTML + feuille sur première visite : 13 052 → 12 102 octets à l'accueil ; aucune affirmation sur compression HTTP réelle. Les visites suivantes ne bénéficient plus du cache mutualisé de cette CSS : arbitrage assumé pour une première navigation sans requête commune, à réévaluer sur métriques réelles. Aucune minification HTML globale ni cache serveur modifié.

Les contrôles visuels portent sur des échantillons Chromium, pas tous les navigateurs/imprimantes. Les anciennes pages hors catalogue reconstruit peuvent conserver le lien externe. Aucun gain d'audience ou de référencement démontré.

## Publication

**Au commit initial : code et recettes locales complets ; publication cloud, sauvegarde et HTTPS à confirmer.** Le suivi final complète cette section après vérification, sans confondre push et déploiement.

Preuves privées : `crabe-chantiers/site-integration/2026-11-07/` (bases, sources/licence amont, rouges, suites, builds, diagnostic et recette navigateur, essai scratch). Aucun lot d'exploitation, cron, archive historique, newsletter ou paiement activé.
