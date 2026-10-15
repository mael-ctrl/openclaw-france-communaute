# Métadonnées de partage des pages éditoriales — 15 octobre 2026

## Une amélioration, périmètre limité

Les brèves et articles individuels déclaraient tous `og:type=website`. Les articles portaient aussi une date sous `meta name="article:published_time"`, au lieu de l'attribut `property` attendu par Open Graph.

- Déclarer uniquement les deux gabarits éditoriaux en `og:type=article`.
- Conserver `website` pour l'accueil, les index et les annexes.
- Publier la date déjà enregistrée de l'article avec `property="article:published_time"` ; omettre la balise si cette date manque. Aucune date de build, de modification ou date de brève inventée.
- Conserver textes, liens, images, canoniques, données JSON-LD, sources, prix et paiements inchangés.

Effet attendu : donner aux services de partage une description correcte du type de contenu. Ce correctif ne prouve ni changement d'affichage sur un réseau social, ni gain de trafic ou de conversion. L'image reste la bannière générique existante ; les couvertures par article restent un chantier distinct.

## Remploi et provenance

Chasse GitHub : recherche `jekyll seo tag`, puis lecture de `jekyll/jekyll-seo-tag/lib/template.html` au SHA `ce38a841785d18dabb58443dd12d0616f39c2cc1`.

- Dépôt : https://github.com/jekyll/jekyll-seo-tag
- Licence constatée dans l'API GitHub : **MIT**.
- Dernier push constaté : **2026-09-29T23:58:38Z**.
- Référence normative : https://ogp.me/ — types `article` / `website`, attribut `property`, date `article:published_time`.
- Décision : reprendre le principe de distinction article/site et réutiliser le générateur maison. Aucun code tiers copié, aucune dépendance ajoutée, pas de migration Jekyll.

## Recette locale exécutée

Base : `37d92a48a3492c6655b632561d83ed8218571d37`.
Le Bureau n'était pas lisible comme dépôt dans le contexte cron ; clone isolé hors Bureau, synchronisé avec GitHub. Aucun changement local illisible repris.

- TDD : échec observé `website != article` pour chacun des deux gabarits, puis réussite ; échec sur date absente, puis omission vérifiée.
- Contrat : `python3 -B -m unittest discover -s tests -p test_open_graph_editorial.py -v` — **5 tests OK**.
- Suite entière dans une copie isolée : **78 tests Python OK** + **4 tests Node OK**.
- Comparaison sur les données réelles : **597 pages éditoriales** (400 brèves + 197 articles), corps et JSON-LD identiques avant/après ; seules les métadonnées ciblées changent.
- `python3 engine/run.py --essai --sans-redaction` dans cette copie : **code 0, 618 fichiers de pages/flux générés**, aucune rédaction payante, aucun FTP, aucune annonce, aucun sceau créé. Journal seulement complété ; manifestes identiques ; `data/` du dépôt conservé intact.
- Deux flux externes ont répondu 403 (Siècle Digital) et 429 (Reddit Claude) pendant cet essai ; cela ne constitue pas une validation exhaustive des sources RSS et n'a pas été modifié par ce chantier.

La production doit être vérifiée après le workflow cloud : type et unicité des métadonnées en HTTPS sur brève/article, date identique aux données sauvegardées, index toujours `website`, image existante disponible.
