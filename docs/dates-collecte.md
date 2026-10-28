# Dates de collecte RSS — correction ciblée

Mission croissance du 27 octobre 2026, recette terminée le **28 octobre** : une seule correction du collecteur, aucune nouvelle source.

## Défaut et effet

L'ancien test `"T" in brut` envoyait aussi les dates RSS contenant **Tue**, **Thu** ou **GMT** au parseur ISO. Leur lecture échouait et renvoyait `None`, malgré une date source valide. Ces dépêches pouvaient échapper au filtre de fraîcheur de trois jours et être mal classées avant rédaction.

Reproduction sur le flux Google AI déjà configuré : `Tue, 13 Oct 2026 16:00:00 +0000` devient `None` avant correctif, puis `2026-10-13T16:00:00+00:00`. Ce n'est pas une preuve que cette dépêche a été republiée : la déduplication peut déjà l'exclure. Le flux CNIL a servi de témoin complémentaire, **sans ajout au catalogue**.

## Modification bornée

`engine/collecte.py`, `_date_depuis_item()` : essayer le parseur ISO existant, puis `email.utils.parsedate_to_datetime` si le format est refusé. Priorité des champs, normalisation UTC, filtre IA, fenêtre de fraîcheur, déduplication, quotas et budget inchangés. Dates absentes/illisibles toujours absentes ; la convention héritée « date naïve → UTC » est conservée, pas validée comme vérité du fuseau source.

Aucun `data/`, journal, sceau ou contenu publié n'est réécrit. La correction porte sur les **collectes futures**, pas sur la réparation rétrospective des dates de brèves, des métadonnées ou des archives.

## Contrats et recette

- `tests/test_collecte_dates.py` : six tests, dont le cas mardi/jeudi rouge avant correction ; jours de semaine, GMT/décalages numériques, Atom/ISO, précision, dates invalides, repli et priorité des champs.
- Vraie boucle téléchargement/parsing/collecte sur un transport simulé : mardi ancien exclu, mardi récent conservé et trié avant lundi, seconde collecte vide par déduplication. Le témoin ancien échoue réellement.
- Première suite isolée : **245 tests réussis**. `engine/run.py --essai --sans-redaction` réussi, sans rédaction payante, FTP ni diffusion. 497 fichiers de données du worktree inchangés, 32 manifestes de la copie inchangés, préfixe du journal intact. Deux refus de flux tiers observés (403/429), non corrigés par ce lot.
- Captures et logs privés : `crabe-chantiers/croissance/2026-10-27/preuves/`. Les heures des recettes sont celles réellement observées, notamment le 28/10 ; pas d'antidatage.

Le Bureau était illisible et le clone automatisé en rebase/conflit. Le correctif est préparé dans un worktree propre, sans résoudre ni écraser leurs données. La première base était `4d7b45fa2ace920ea86e0ae40846a9b06997ab37` ; la reprise sur main à jour et la publication sont vérifiées séparément.

## Réemploi / chasse GitHub

Dépôt consulté : [kurtmckee/feedparser](https://github.com/kurtmckee/feedparser), révision `a22c5521cbb109871f1a2318948581901bd47e26`, dernier push observé `2026-10-06T00:52:50Z`. API licence `NOASSERTION` ; fichier [LICENSE](https://github.com/kurtmckee/feedparser/blob/a22c5521cbb109871f1a2318948581901bd47e26/LICENSE) effectivement lu : licence de redistribution à deux clauses pour code/tests, notice distincte pour documentation.

Les fichiers [datetimes/__init__.py](https://github.com/kurtmckee/feedparser/blob/a22c5521cbb109871f1a2318948581901bd47e26/feedparser/datetimes/__init__.py) et [rfc822.py](https://github.com/kurtmckee/feedparser/blob/a22c5521cbb109871f1a2318948581901bd47e26/feedparser/datetimes/rfc822.py) séparent les parseurs et essaient d'autres formats en cas de refus. Leurs blobs et la licence ont été vérifiés par empreinte Git. **Aucun code copié, aucune dépendance installée** : réemploi des parseurs stdlib déjà présents, correction maison minimale.

## Effet attendu

Une veille mieux datée : éviter que des dépêches anciennes passent pour non datées et mieux prioriser l'actualité. Aucun gain de trafic ou d'abonnés mesuré. La réussite des tests ne vaut pas, seule, preuve de déploiement.
