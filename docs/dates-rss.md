# Dates RSS éditoriales : omission plutôt qu'une publication inventée

Décision préparée avec une IA (Hermes) le 22 octobre 2026 sur la base
`d97d178657a878210e24529b8f18db527754e01d`, requalifiée le 23 sur
`54d86c69c501d41ae57941f57e135c6fdd098934`. Intégration ciblée du 23 octobre
sur `742ca8e1a53ce5bfa2f02a886e53ba6ffb4b7a16` : recette locale réussie,
publication cloud et HTTPS à vérifier séparément.

## Provenance des champs, vérifiée dans les producteurs

- `engine/collecte.py:_date_depuis_item` essaie `pubDate`, `published`,
  `updated`, puis `date`, sans conserver le type d'événement retenu. Il s'agit
  de la date d'une source tierce, non de la mise en ligne de notre brève.
- `engine/redaction.py:rediger_breve` copie cette date dans `date_source` et
  crée `date_redac` à la rédaction. `_rediger_article` crée `date` à la rédaction.
- `engine/run.py` rédige, construit, puis déploie : ces dates précèdent donc
  l'éventuelle mise en ligne. `engine/preuves.py:_ligne_breve/_ligne_article`
  les réemploie dans le registre ; une empreinte ne change pas leur nature.
- `docs/dates-jsonld.md` expose déjà cette distinction. Aucun producteur audité
  n'établit ici un premier instant de disponibilité par URL et version.

## Contrat des deux flux

RSS 2.0 indique que `item/pubDate` est facultatif et représente la publication
  de l'item ; l'absence de date n'invalide pas un item ayant titre/description.[1]

`feed.xml` et `feed-articles.xml` omettent désormais **tous les `item/pubDate`**.
Pas de balise vide, de 1970, de substitution par la rédaction, par le build,
par un champ de publication supposé ou par une date `dc:date` équivalente.
Aucun champ de première publication n'est créé et aucune donnée n'est migrée.

Le `lastBuildDate` du canal reste l'instant UTC de **construction du flux**,
formaté par `email.utils.format_datetime(datetime.now(timezone.utc))`.
Le `+0000` est celui d'un objet réellement UTC ; jours/mois ne dépendent plus
  de la locale. Il ne prouve ni déploiement, ni première publication, ni même
  une modification éditoriale depuis le build précédent. La spécification parle
  de dernière modification du contenu du canal ; l'usage comme horodatage de
  construction reste la convention locale conservée, pas une preuve historique.[1]

## Compatibilité conservée

- Signature de `feed_xml`, titres de canaux, descriptions, langue, liens et
  GUID (valeur et `isPermaLink="true"`) inchangés.
- Les dates restent **uniquement des clés de tri internes** : même tri lexical
  décroissant, même stabilité des égalités, même priorité source → rédaction.
- Même sélection : 20 premiers articles, 50 premières brèves, puis 60 items
  au total ; 20 articles maximum dans le flux dédié. Aucun nouveau tri chrono.
- Pas de changement HTML, Open Graph, JSON-LD, sitemaps, podcast ou données.
- Les anciens tests ne sont ni réécrits ni affaiblis. Un test dédié est ajouté.

La norme autorise l'omission ; le comportement visuel des agrégateurs n'est
pas garanti. Certains pourront afficher une date de réception ou aucune date.
Les GUID conservés évitent de présenter les items comme de nouvelles identités,
mais cela n'est pas une validation de tous les clients RSS.

## Dettes séparées / conditions de réactivation

Open Graph `article:published_time`, `news:publication_date` et `lastmod`
restent hors périmètre. Le tri lexical des ISO à offsets différents n'est pas
un tri absolu des instants ; les types non textuels mélangés ne sont pas un
nouveau contrat accepté. L'échappement des métadonnées de canal configurables
et des URI reste à auditer séparément (la configuration réelle est testée).
Aucune correction podcast, d'archives distantes, de journaux ou de sceaux ici.

Réintroduire une date exige un contrat de preuve par URL canonique/version,
distinct de la création, du build et d'une observation ultérieure. Un GET 200,
un commit ou une réussite FTP ne suffit pas à prouver la première publication.

## Réemploi / provenance

Django (BSD-3-Clause) et python-feedgen (BSD-2-Clause) sérialisent `pubDate`
conditionnellement ; Django utilise le formateur standard `format_datetime`.[9][4]
Leur code a été consulté, pas copié ni exécuté : aucune nouvelle dépendance.
Les instantanés, licences, SHA et métadonnées GitHub sont conservés dans le
lot privé, documentés dans `provenance-repos.md`.

## Tests

`python3 -B -m unittest discover -s tests -p 'test_dates_rss_editoriales.py' -v`

Le lot historique du 22 fournit rouge/vert, suites liées et complète et deux
builds complets hors réseau ; ces résultats restent datés du 22.
La vague préparatoire du 23 a rejoué le rouge/vert et des contrats liés,
comparé les flux et testé la combinaison avec le patch clavier, sans build
complet. **L'intégration croissance a ensuite rejoué 200 tests Python et
4 tests Node**, puis `engine/run.py --essai --sans-redaction` dans une copie
isolée : 1 685 pages + assets, aucune rédaction payante, aucun envoi ni annonce.
Quatre flux tiers étaient indisponibles pendant cette collecte (502/403/429) ;
le build a néanmoins abouti. Les données de production sont intactes, les
sceaux de recette inchangés et le préfixe du journal conservé.

Comparaison sur les données réelles du SHA d'intégration, à horloge commune :
60/20 entrées ; seuls les `item/pubDate` sont retirés, tous les autres octets
conservés. XML contrôlé avec ElementTree et `xmllint`. Hors `feed_xml`, l'AST de
`construction.py` est identique. La suite des six nouveaux tests a été vue en
échec avant application du correctif (trois méthodes en échec, dont une avec
sous-cas ; les autres passent déjà), puis entièrement verte.

Le dépôt `lkiesow/python-feedgen` a été recherché et recontrôlé le 23 : API
BSD-2-Clause, dernier push `2024-07-04T10:19:12Z`, SHA `97260abb1793eb164c458c10b493690beb413f6d`.
L'en-tête du fichier mentionne FreeBSD/LGPL ; aucune ligne n'est copiée ni
aucune dépendance ajoutée. Réemploi du patch interne préparé, de la stdlib et
des contrats, plutôt qu'installation d'un nouveau générateur.

Preuves privées : `crabe-chantiers/croissance/2026-10-23-rss/` (rouge,
suites, essai, flux avant/après, `recette.py`, `resultat-local.json`).
Le lot préparatoire d'origine reste intact : 115 fichiers contrôlés contre
son manifeste avant intégration. Bureau inaccessible dans le contexte cron ;
worktree indépendant sur `origin/main`, commit local divergent préservé.

## Sources

[1] https://www.rssboard.org/rss-specification
[4] https://raw.githubusercontent.com/lkiesow/python-feedgen/97260abb1793eb164c458c10b493690beb413f6d/feedgen/entry.py
[9] https://raw.githubusercontent.com/django/django/79502d08405dbf24efa39e8731320f31035b9e9c/django/utils/feedgenerator.py
