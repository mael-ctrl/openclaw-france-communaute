# Veille FastMCP — 19 novembre 2026

## Une amélioration

Ajout du flux primaire `https://github.com/PrefectHQ/fastmcp/releases.atom`,
libellé « FastMCP (releases, préversions incluses) », anglais, priorité 3.
Les **37 sources précédentes** restent identiques et dans le même ordre ;
le catalogue, l'export OPML et le compteur de Transparence passent à **38**.
Réemploi du collecteur et des générateurs existants, sans dépendance nouvelle.

Effet attendu : mieux couvrir les outils de construction de serveurs et clients
MCP, depuis leurs notes de versions primaires, en complément des SDK MCP déjà
suivis. Cela ne prouve ni trafic supplémentaire ni publication de chaque release.
Fenêtre de trois jours, filtres, quotas et plafond de 30 €/mois inchangés.
La priorité ne départage que les dates égales ; les préversions ne sont pas
présentées comme stables.

## Qualification GitHub et flux

- Dépôt canonique : [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp).
  L'ancien chemin `jlowin/fastmcp` redirige : seule l'adresse canonique est ajoutée.
- Révision lue : `adbb3862ce98c5ca13834b4dd14a6c09a512328d` ; dernier push
  observé via l'API : `2026-11-19T13:02:49Z`.
- Licence Apache-2.0 lue dans le [LICENSE épinglé](https://github.com/PrefectHQ/fastmcp/blob/adbb3862ce98c5ca13834b4dd14a6c09a512328d/LICENSE),
  octets contrôlés contre le blob `f49a4e16e68b128803cc2dcea614603632b04eac`.
  Aucun code amont copié, installé ou exécuté : seule l'adresse Atom est ajoutée.
- HTTPS strict à 13:03 UTC : HTTP 200, `application/atom+xml`, 1 073 858 octets,
  SHA256 `d24e00db382031e333b339f391abe26d0980bd84277f0d9cb8618e3f83536e0a`.
- Dix entrées datées et liées au dépôt, lues par le vrai parseur sur les octets
  conservés. Dernière date : `2026-11-18T19:12:03+00:00` ; **deux candidats
  dans la fenêtre de trois jours**. Ce ne sont pas deux articles publiés.
- Alternatives repérées : Aider (Apache-2.0, dernière release API du 09/08/2025)
  et MLX (MIT, dernière release API du 14/10/2026). Non ajoutées : priorité donnée
  à un flux actuellement récent et complémentaire aux SDK déjà suivis.

## Recette locale et préservation

Base `39aef322899a7cde3a7b7c4039d9df67386f9b6c`. Bureau inaccessible depuis le cron ;
pull refusé dans le clone partagé en conflit. Ces fichiers ont été préservés.
Un worktree propre de `origin/main`, hors Bureau, a réellement réussi son pull
`--ff-only`. Aucune résolution automatique ni import de données locales en conflit.

`tests/test_source_fastmcp.py` : rouge avant ajout, vert après ; source canonique
unique, export fidèle de tout le catalogue et compteur cohérent.
**401 tests Python réussis**, puis `engine/run.py --essai --sans-redaction`
dans une copie isolée : code 0, 2 610 pages, zéro rédaction payante, transfert
ou publication sociale. Clé chargée uniquement pour consulter le solde, sans
l'afficher. Deux flux HN ont répondu 502, LocalLLaMA 404, L'Usine Digitale 403
et Reddit Claude 429 : le build réussi ne valide pas les flux tiers indisponibles.
FastMCP a effectivement fourni deux candidats au collecteur lors de l'essai.

Les 60 fichiers de preuves/publications contrôlés restent identiques et le
préfixe du journal est intact ; aucune donnée de recette importée en production.
Export construit identique au générateur, SHA256
`b1474f9a5f6ea237c5804a4c7429b17115ab30692be78f554b57e2200c89aebb`.
Pièces privées : `crabe-chantiers/croissance/2026-11-19-1300/evidence/`.

## Publication vérifiée

Code poussé : `39f5d3515a1321168f8d91a71829543f1e3e109f`.
Le dispatch cloud `44530446524` a été retrouvé sur ce SHA. Au contrôle du
19 à 13:09 UTC, ce run était en cours ; il n'est pas déclaré terminé.

Livraison SFTP ciblée de deux fichiers seulement : `/veille/sources.opml` et
le compteur de `/transparence/`. La base distante correspondait exactement
au catalogue parent de 37 sources. Les autres octets de Transparence et les
trois témoins `.htaccess` (racine, veille, Skool) sont préservés. Aucun ancien
catalogue dans les runs actifs paginés, ni pipeline local détecté lors des
préflights ; cette observation n'est pas un verrou transactionnel.

Relectures SFTP exactes puis **deux lectures HTTPS canoniques identiques** à
13:09:33 UTC : **38 sources**, dont FastMCP. OPML : empreinte ci-dessus ;
Transparence : `241f98567aea0f47bd5b7d47f80914925d8cf9569bb1051cf752c8e3c528e073`.
Sauvegardes et résultats hors dépôt : `crabe-chantiers/croissance/2026-11-19-1300/livraison/`.
Cette publication de l'export et du compteur ne clôt pas le pipeline cloud,
sa sauvegarde d'état ni la divergence préexistante du clone partagé.
