# Veille LiteLLM — 20 novembre 2026

## Une amélioration

Ajout du flux primaire `https://github.com/BerriAI/litellm/releases.atom`,
libellé « LiteLLM (releases, préversions incluses) », anglais, priorité 3.
Les **38 sources précédentes** restent identiques et dans le même ordre ;
le catalogue, l'OPML et le compteur de Transparence passent à **39**.
Le collecteur et les générateurs existants sont réemployés, sans nouvelle dépendance.

Effet attendu : compléter la veille des agents par les évolutions d'une passerelle
multi-fournisseurs de modèles (compatibilité, routage et suivi des coûts).
Il ne s'agit ni d'une recommandation de sécurité ni d'une adoption de son logiciel.
Aucun gain d'audience ou de ventes n'est mesuré par cet ajout.
Fenêtre de trois jours, filtres, quotas et budget de 30 €/mois inchangés.
La priorité départage seulement les dates égales ; les préversions sont signalées.

## Qualification GitHub et flux

- Dépôt : [BerriAI/litellm](https://github.com/BerriAI/litellm).
- Révision consultée : `995ec7955edf194e6bdbe55acbc6eda113fbd6dd`.
  Dernier push observé à 19:46 UTC : `2026-11-20T19:46:44Z`.
- API licence : `NOASSERTION`. Le [LICENSE épinglé](https://github.com/BerriAI/litellm/blob/995ec7955edf194e6bdbe55acbc6eda113fbd6dd/LICENSE)
  applique MIT au contenu hors `litellm/enterprise/` ; ce répertoire relève d'une
  licence séparée. Ne pas qualifier tout le dépôt de MIT.
  Octets vérifiés contre le blob Git `2ffbfec19ad5a1fd2a489d1f4f7ce81a899eb77b`.
  Aucun code amont copié, installé ou exécuté : seule l'adresse Atom est ajoutée.
- Flux HTTPS strict : HTTP 200, `application/atom+xml`, 519 770 octets,
  SHA256 `f1a9a0ac5d44c261aa2613ab01090e702ec9f8ccf168f886bf1a4929cd09e1df`.
- Vrai parseur exécuté sur les octets conservés : dix entrées liées au dépôt,
  dix candidates dans la fenêtre de trois jours ; date maximale lue :
  `2026-11-20T06:18:30+00:00`. Ce ne sont pas dix articles publiés.
  Le flux comporte notamment des versions `rc` et `dev`, non assimilées à du stable.

## Recette locale

Base : `87310d935c09fc30042c0a848d1b45c048d28263`.
Le Bureau est inaccessible au cron ; le clone partagé diverge (23 commits locaux,
146 distants lors du relevé). Le pull explicite `--ff-only origin main` y a refusé.
Un worktree neuf sur `origin/main` a réussi ce même pull ; aucune fusion de données,
réécriture de sceau ou modification du clone actif n'a été faite.

`tests/test_source_litellm.py` échoue avant l'ajout, puis réussit : source unique,
projection OPML exacte de tout le catalogue, compteur cohérent.
**402 tests Python réussis** dans une copie séparée. Le premier essai a échoué
sur ENOSPC pendant la copie des couvertures, pas sur le catalogue. Trace conservée.
Après nouveau contrôle de l'espace disponible, le même essai
`engine/run.py --essai --sans-redaction` a réussi : **2 624 pages**,
zéro rédaction payante, transfert ou publication sociale. Aucun nettoyage des
anciens lots n'a été effectué. Les échecs tiers (Simon Willison timeout,
LocalLLaMA 404, L'Usine Digitale 403, Reddit Claude 429) restent distincts.
LiteLLM a fourni dix candidats au collecteur. La clé n'est utilisée que pour
la lecture du solde et n'est pas affichée.

Les 62 fichiers de preuves/publications contrôlés sont inchangés ; le préfixe du
journal est intact. Aucune donnée de recette importée dans le dépôt.
Export construit : SHA256 `bc24e18c20c4493d383aef4fb63cd3f87958ac6d202dc5b8e48e309faa506f2b`.
Pièces privées : `crabe-chantiers/croissance/2026-11-20-litellm/evidence/`.

La publication HTTPS et l'issue du relais cloud sont à vérifier séparément.
