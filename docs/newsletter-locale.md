# Compositeur local de La Brève du Crabe — 20 octobre 2026

## Une intégration, sans lancement d'envoi

Le relais P4 de la roadmap et la vague du 20/10 désignent ce lot comme première
intégration en attente. Les actions SEO majeures #1–#4 et le catalogue de #5 sont
déjà dans le moteur ; la recette des anciennes pages est reprise séparément,
sans nouvelle modification du catalogue. Les arbitrages historiques et les
listings hors archives ne sont pas masqués par ce choix. Pas d'adoption de CSS,
de nouveau service ou du second patch hub dans cette mission.

Trois fichiers du lot newsletter réemployés :

- `outils/compose_breve.py` : CLI standard-library, entrée JSON locale figée,
  date et SHA explicites, déduplication, sources exactes, résultat déterministe.
- `outils/README-breve.md` : utilisation et verrous ; la documentation clarifie
  la borne de 400 candidats, distincte du catalogue désormais complet.
- `tests/test_compose_breve.py` : 17 contrats autonomes, données synthétiques
  explicitement marquées, sous-processus de CLI protégés du réseau.

Le code et les tests sont identiques au patch préparé ; pas de nouveau moteur.
Aucun formulaire, transport, destinataire, pixel, appel IA, branchement de cron
ou du pipeline. Le brouillon n'est ni ajouté au dépôt ni publié dans `_site`.
L'absence de lancement est intentionnelle, pas un envoi partiellement livré.

## Réemploi vérifié

Métadonnées API GitHub relues le 20/10 :

| Dépôt | Licence API | Dernier push | Décision |
|---|---|---|---|
| [KarenSpinner/substack-digest](https://github.com/KarenSpinner/substack-digest) | MIT | 17/10/2025 17:16:52 UTC | Dédup et limites déjà couvertes par le compositeur interne ; pas d'ajout de scraping/LLM. |
| [iloveitaly/listmonk-newsletter](https://github.com/iloveitaly/listmonk-newsletter) | non renseignée | 19/10/2026 01:02:38 UTC | Aucune copie sans droits établis ; campagnes mutatives exclues. |

Provenance préparatoire relue ; aucun code tiers installé ou exécuté.

## Recette réelle sur le SHA courant

Base après pull : `ea0c0b49047348698765c5455daa735520725648`.
73 pièces du lot vérifiées contre leur manifeste ; patch SHA-256
`bdaedec7f4cd42e6af59c07a75c088d86040cb166b773ef42e4c664639a9f75d`.

- Contrat CLI rendu rouge avant ajout du programme, puis vert : **17 tests**.
- `python3 -B -m unittest discover -s tests` : **164 tests réussis**.
  Suite Node de copie du pack : **4 réussis**, sans changement de ce module.
- Deux builds réels par `construction.construire()`, isolés, caches froids et
  horloge technique commune : **2 642 sorties identiques octet pour octet**.
- **521 fichiers préexistants préservés, dont 343 fichiers de données**.
  Aucune donnée de test réimportée ; journal et manifestes historiques intacts.
- JSON exact du commit vérifié via `git show` : **983 brèves**. Les 400 candidats
  sont un sous-ensemble construit, pas le nombre total de pages du site.
- Deux compositions identiques avec trois IDs explicitement sélectionnés :
  destinations présentes, canoniques et sources exactes vérifiées dans le build.
- Builds et compositeur sous garde Python refusant réseau et sous-processus ;
  aucun événement interdit. Ce garde-fou n'est pas une sandbox OS certifiée.

Preuves privées : `crabe-chantiers/newsletter/integration-2026-10-20/`
(`qualifier.py`, `resultat.json`, journaux rouge/vert/suites, inventaires et brut).
Le brouillon brut reprend le moteur ; l'édition privée corrigée et la revue
factuelle du lot du 20/10 restent séparées et ne constituent pas une relecture
humaine. Ne pas envoyer le brut comme une édition approuvée.

## Livraison

**Livraison vérifiée le 20/10 à 11:22 CEST.** Code `e59c543`, cinq blobs
relus sur `main` distant après push. [Run 39396533847 réussi](https://github.com/mael-ctrl/openclaw-france-communaute/actions/runs/39396533847) :
**164 tests cloud**, 1 363 fichiers envoyés ; sauvegarde `a08f3ef`, fusion
`ac63c1d`. Le délai du premier observateur local n'était pas un échec du run :
le statut final et les logs ont été relus. Aucun workflow ni cron modifié.

Après déploiement : **509 HTML HTTPS entièrement identiques** au rebuild isolé
de `a08f3ef8f81a56cf6551040b0453b1db71fd90fc` — 492 anciennes brèves,
les trois destinations du brouillon, dix pages de catalogue et quatre du fil.
**988 liens uniques du catalogue = 988 brèves du sitemap = données cloud**,
sans doublon entre pages. Version et sitemap stables aux deux bornes ; accueil,
podcast, news-sitemap et robots également 200. **517 GET conservés**, corps,
en-têtes, horodatages et empreintes sous `https-apres-cloud/` dans les preuves
privées. La vérification du catalogue de la veille est ainsi complétée, sans
prétendre avoir lu les 988 HTML ni toutes les URL historiques.

Le pipeline **ne compose ni n'envoie de newsletter**. Les 2 642 sorties
identiques avant/après prouvent l'absence de modification publique due à ce lot ;
la collecte cloud régulière a ensuite produit ses propres changements.

## Limites et suite

Compte/propriété, responsable et confidentialité, consentement, expéditeur,
transport et désinscription bout en bout non éprouvés : **envoi et inscription
fermés**. La présence de ce CLI ne valide pas ces prérequis. Aucune hausse
d'abonnés, de trafic, de chiffre d'affaires ou de dons revendiquée.
