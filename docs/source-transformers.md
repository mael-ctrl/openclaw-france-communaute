# Veille Transformers — 23 novembre 2026

## Une amélioration

Ajout du flux primaire `https://github.com/huggingface/transformers/releases.atom`,
libellé « Transformers (releases, préversions incluses) », anglais, priorité 3.
Les **40 sources précédentes** restent identiques et dans le même ordre ;
le catalogue, l'OPML et le compteur de Transparence passent à **41**.
Le collecteur et les générateurs existants sont réemployés, sans dépendance ajoutée.

Effet attendu : compléter le blog Hugging Face par les notes de versions de sa
bibliothèque Transformers, notamment les nouveaux modèles pris en charge.
Cet ajout n'est ni une adoption du logiciel ni une recommandation de sécurité ;
aucun gain d'audience mesuré. Fenêtre de trois jours, filtres, quotas et budget
DeepSeek de 30 €/mois inchangés. La priorité départage seulement les dates égales ;
les préversions sont signalées, pas filtrées implicitement.

## Qualification GitHub et flux

- Dépôt : [huggingface/transformers](https://github.com/huggingface/transformers).
- Révision consultée : `2f6f6912aff24e5d31b20a129a19b6c1819bca60`.
  Dernier push API observé : `2026-11-23T13:00:24Z`.
- Licence API et [LICENSE épinglé](https://github.com/huggingface/transformers/blob/2f6f6912aff24e5d31b20a129a19b6c1819bca60/LICENSE) : Apache-2.0.
  Octets vérifiés contre le blob Git `68b7d66c97d66c58de883ed0c451af2b3183e6f3`.
  Aucun code amont copié, installé ou exécuté : seule l'adresse Atom est ajoutée.
- Candidat alternatif consulté : `langflow-ai/langflow`, licence API MIT,
  dernier push `2026-11-23T00:27:24Z` ; non ajouté pour limiter la mission à une source.
- Flux HTTPS strict à **13:03 UTC** : HTTP 200, `application/atom+xml`,
  **1 029 847 octets**, SHA256
  `d973b7eae000a39f390336a1a26a926ed304262adc75951e4fafbe2fc18c74c3`.
- Vrai parseur exécuté sur les octets conservés : dix entrées,
  **une dans la fenêtre de trois jours** : « Release v5.24.0 »,
  date lue `2026-11-21T12:43:39+00:00`. Aucune redatation ni fenêtre élargie.
  Un candidat récent n'est pas une brève publiée : le tri et le plafond globaux
  restent applicables.

## Recette locale

Base : `d7687ef18249a652292f48063b42dfcc07b1b073`.
Le Bureau n'est pas lisible comme dépôt depuis ce cron ; le clone de secours
partagé a six fichiers en conflit. Son index, ses variantes et ses preuves
restent intacts. Pull réussi seulement dans un worktree neuf sur `origin/main`,
sans reprise du rebase interrompu. Rapport/manifeste de la vague du 23 lus ;
aucun patch préparatoire de cette vague importé.

`tests/test_source_transformers.py` échoue avant l'ajout puis réussit :
source unique, projection OPML exacte du catalogue et compteur cohérent.
**429 tests Python réussis** dans une copie séparée ; vrai
`engine/run.py --essai --sans-redaction` réussi ensuite : **2 638 pages**,
un candidat Transformers collecté avant plafonnement global, zéro rédaction
payante, transfert ou publication sociale. Clé utilisée uniquement pour lire
le solde, jamais affichée. Échecs tiers HN (502), LocalLLaMA (404),
L'Usine Digitale (403) et Reddit Claude (429) conservés dans les logs.

Les **63 fichiers de preuves/publications** contrôlés restent identiques ;
préfixe du journal intact. Aucune donnée de recette importée dans le dépôt.
OPML construit : SHA256 `bc7a2c555cd13f150c35a521434033899ec2e55727b2cfc27589194f75d25fac`.
Pièces privées : `crabe-chantiers/croissance/2026-11-23-transformers/preuves/`.

## Publication vérifiée, clôture cloud distincte

Code **`55294d0bd7837d8b49079507e122ee0e318f42c2`**, trois fichiers relus par
l'API GitHub et identiques aux octets locaux. Dispatch unique du workflow
**`45181163972`**, sur ce SHA ; aucun run actif annulé par cette mission.

Premier préflight SFTP refusé sans écriture : l'OPML et le compteur servis étaient
revenus à **28 sources**, et non 40. Catalogue exactement rattaché au commit
`0bcc84f0cb89cf2847d31e2b5496c23f416f2789` ; douze ajouts déjà versionnés manquaient.
Le refus et les corps initiaux sont conservés. Aucune cause de cette régression
n'est déduite du seul constat, aucune fusion de données ni réparation du clone.

Requalification distincte à **13:10 UTC**, base historique exacte et sauvegardée,
égalité SFTP/HTTPS avant écriture. Inventaire paginé des cinq statuts actifs :
seul le nouveau run, avec le catalogue 41, était actif ; aucun pipeline local
concurrent détecté. Ce contrôle ponctuel n'est pas un verrou transactionnel.

Deux cibles seulement transférées par SFTP après vérification de clé hôte :
`veille/sources.opml` et `transparence/index.html`. Dans Transparence, seul le
compteur **28 → 41** change ; toutes les autres statistiques/octets sont préservés.
OPML aligné sur le catalogue Git courant, rétablissant les ajouts antérieurs et
ajoutant Transformers. Fichiers intermédiaires exclusifs puis renommage atomique
par cible ; témoins `.htaccess` racine, veille et CORS Skool inchangés.

À **13:10:34 UTC**, relecture SFTP exacte et **deux passages HTTPS canoniques
identiques** : OPML de 5 065 octets, 41 couples nom/URL ; page de 20 705 octets,
compteur 41. Preuves privées : `livraison-02/https-result.json`, captures et
sauvegardes du même chantier. Nouveau relevé **13:12:43 UTC** : mêmes octets HTTPS.
Les **contrats cloud ont réussi à 13:12:30 UTC** ; pipeline encore en cours,
sauvegarde en attente au dernier relevé. La publication ciblée est vérifiée,
mais ce n'est ni une clôture de la sauvegarde cloud ni une validation du reste du site.

Le rebase partagé, la régression observée et les interruptions cloud restent des
dettes d'exploitation séparées, non réparées par l'ajout d'une source.
