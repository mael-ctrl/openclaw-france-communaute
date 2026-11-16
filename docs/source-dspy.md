# Veille DSPy — 16 novembre 2026

## Une amélioration

Ajout du flux officiel `https://github.com/stanfordnlp/dspy/releases.atom` :
« DSPy (releases, préversions incluses) », anglais, priorité 3. Les **34 sources
antérieures** restent identiques et dans le même ordre ; catalogue et export OPML
comptent maintenant **35 sources**. Réemploi du collecteur, du générateur OPML
et du compteur de Transparence, sans nouveau moteur ni dépendance.

Effet attendu : mieux couvrir les évolutions de DSPy, outil de programmation et
d'optimisation de systèmes à modèles de langage, depuis ses notes de versions
primaires. Ni hausse de trafic mesurée ni recommandation d'installation.
Fenêtre de trois jours, dates, filtres, quotas et plafond DeepSeek de 30 €/mois
inchangés. La priorité ne départage que les dates égales.

## Qualification

- Dépôt [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy), non archivé ;
  dernier push observé `2026-11-13T14:13:09Z`, consultation le 16 à 13:02 UTC.
- Révision `2c07ebbee3a66f6e04b71e141c6c198f1b31a129` ; licence MIT confirmée
  par l'API et le [LICENSE épinglé](https://github.com/stanfordnlp/dspy/blob/2c07ebbee3a66f6e04b71e141c6c198f1b31a129/LICENSE),
  conforme au blob Git `be3f5c0e3fc7e6b0e7c9dddd9db313ab15bfa62b`.
  Aucun code amont installé, copié ou exécuté ; seule l'adresse du flux est référencée.
- Flux HTTPS strict : HTTP 200, MIME `application/atom+xml`, 751 375 octets,
  SHA256 `2d99b813b70d01fe637f5c75e513839b098c5d4102f3c436243bc3e9a2bdb900`.
- Dix entrées lues par le vrai parseur du collecteur sur les octets conservés,
  toutes datées et liées au dépôt ; date la plus récente `2026-11-10T16:25:47+00:00`.
  **Aucun candidat récent dans la fenêtre de trois jours** : ajout prospectif,
  aucune date réécrite ni fenêtre élargie pour forcer une publication.

## Validation locale

Base `4a628545a5b3bf5d67808cc7d900655c0e8b39ac`, worktree propre hors Bureau,
pull rebase réussi sur ce seul worktree. Bureau inaccessible et conflits du clone
partagé constatés avant toute intervention : laissés intacts.

`tests/test_source_dspy.py` : échec attendu avant ajout, réussite après ; contrat
source unique, libellé explicite, export fidèle et compteur cohérent.
**364 tests Python réussis**, puis `engine/run.py --essai --sans-redaction`
dans une copie isolée : code 0, 2 588 pages, aucune rédaction payante, aucun
transfert ni message social. Clé chargée uniquement pour la lecture du solde,
sans affichage. HN OpenClaw a expiré et L'Usine Digitale a répondu 403 :
la disponibilité de tous les flux n'est pas garantie par la réussite du build.

59 fichiers de preuves/publications préservés, préfixe du journal intact ; aucune
donnée de la recette reprise en production. Export OPML égal au générateur,
SHA256 `664c52c5adea3eef60e92157a38d2fbaf26a09a28e3899c551c2b556fa896612`.
Pièces privées : `crabe-chantiers/croissance/2026-11-16-dspy/evidence/`.

Au commit initial, la publication HTTPS et le relais cloud restaient à confirmer.

## Publication vérifiée à 13:09 UTC

Commit de configuration `c2e95deadbf972b8f4e1ef1f40fd4e930c15e534` : les trois
fichiers livrés ont été relus identiques par l'API GitHub sur `main`.

Livraison SFTP bornée à `/veille/sources.opml` et au seul compteur **34 → 35**
de `/transparence/`, sans remplacer ses autres statistiques. Avant transfert :
clé hôte épinglée vérifiée avant secret, sauvegardes privées, base OPML exactement
égale au catalogue parent et égalité HTTPS/SFTP. Liste paginée des runs actifs :
un seul run, déjà sur le nouveau catalogue. Ce contrôle n'est pas un verrou
transactionnel. Staging `.part`, comparaison avant renommage et relecture SFTP
exacte ; transformation inverse du compteur conforme à tous les octets antérieurs.

La première lecture HTTPS immédiatement après transfert a différé et la commande
a correctement terminé avec code 1 : corps conservé, aucune réécriture de secours.
Deux nouvelles lectures canoniques à **13:09:10–13:09:11 UTC** correspondent ensuite
exactement aux deux fichiers attendus : **35 flux, DSPy une seule fois**, compteur
35 présent une fois. La cause du décalage initial n'est pas établie.

Pièces privées : `livraison-ciblee/{preflight,sftp-result}.json`, corps avant/après,
corps HTTPS initial divergent, puis `recontrole-https/result.json` et ses quatre
corps vérifiés. Le dispatch cloud `43872806460` porte le commit de configuration ;
au relevé de 13:09 UTC, les contrats sont encore en cours. L'export public livré
ne prouve ni fin du pipeline cloud, ni sauvegarde de son état, ni publication
d'une brève DSPy. Les conflits du clone partagé restent distincts et inchangés.
