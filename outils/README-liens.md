# Vérifier les liens locaux d'un build statique

`verifier_liens_hors_ligne.py` est un CLI Python standard, sans dépendance ni réseau, pour un **snapshot local immobile**. Il n'appelle ni constructeur, collecte, rédaction, FTP, DNS, paiement ou formulaire. POSIX requis (Linux/macOS, `O_NOFOLLOW`). Le pipeline réemploie sa fonction `check` avant FTP ; le CLI autonome et ses plafonds par défaut restent inchangés.

## Utilisation

Construire au préalable le site dans une **copie isolée**, jamais en écrasant un `_site` en cours de déploiement, puis :

```sh
python3 outils/verifier_liens_hors_ligne.py /chemin/absolu/du/build \
  --canonical-host communaute-ia.fr \
  --max-bytes 100000000 --max-links 200000 > /chemin/rapport-liens.json
```

- **0** : aucun défaut détecté dans le périmètre déclaré.
- **1** : défaut ou couverture incomplète (quota, fichier illisible, symlink, etc.).
- **2** : arguments invalides, avant scan ; pas de JSON produit.

Lire `complete`, `errors`, `exemptions`, `stats`, `budgets` et `limits`. `complete=true` décrit la complétude de l'inventaire/parsing, **pas l'absence d'erreurs de liens**. Les exemptions ne sont jamais des validations. Les fragments non HTML et directives texte sont exemptés après vérification du fichier ; leurs références figurent donc aussi dans `checked` : ne pas additionner aveuglément les compteurs.

Par défaut : 10 000 entrées fichier/dossier, 20 000 000 octets HTML cumulés, 2 000 000 par HTML, 100 000 références, profondeur 32. Les plafonds d'admission sont 50 000 / 128 000 000 / 4 000 000 / 200 000 / 64. Le média dépasse le budget par défaut de 20 Mo : les options explicites ci-dessus ont été éprouvées sur les builds figés des 17 et 22 novembre, sans relever les défauts. Cela ne préjuge pas du volume des builds suivants. En cas de `budget_exceeded`, le scan partiel peut annoncer des cibles manquantes parce que l'inventaire n'est pas complet : **ne pas corriger des pages à partir de ces seuls diagnostics**. Ne pas ignorer le code non nul ni étendre les plafonds sans nouvelle qualification du volume.

## Garde du pipeline

`engine/run.py` appelle directement `check` sur `config.DOSSIER_SORTIE`, après le retour du build complet et l'écriture locale de la clé IndexNow, avant le premier appel FTP. L'hôte est dérivé de `URL_SITE` (origine HTTP(S), nom DNS explicite, port standard, sans sous-chemin ni identifiants). Aucun sous-processus CLI, transport JSON ou dépendance supplémentaire.

Les cinq budgets sont explicites : **10 000 entrées / 100 000 000 octets HTML / 2 000 000 par page / 200 000 références / profondeur 32**. Qualification du 22 novembre sur `a5ab769` : **7 930 entrées, 2 631 HTML, 95 534 564 octets HTML, plus grosse page 861 098 octets, 129 154 références**, zéro erreur. Réserve HTML : **4 465 436 octets seulement** ; ce budget volontairement borné devra être requalifié avant saturation, jamais relevé automatiquement. Deux builds identiques ; [recette et limites](../docs/garde-liens-pipeline.md). Ne pas déployer sur un diagnostic partiel.

La garde exige un rapport de schéma 1 complet, au moins un HTML, sans erreur, avec compteurs, hôte et budgets conformes. Défaut, exception ou rapport invalide rejoint la voie d'échec du déploiement : code processus **1**, aucune tentative FTP, aucun signal IndexNow, archivage Wayback ni diffusion Bluesky. Le bilan d'échec et la routine de preuves existante restent exécutés ; les données éditoriales ne sont ni restaurées ni effacées. Un événement `verification_liens` avec compteurs/budgets est ajouté au journal seulement après acceptation. Pour le diagnostic détaillé, rejouer le CLI autonome sur le même snapshot immobile.

`--essai` et `--sans-deploiement` restent sans FTP/annonces et **ne déclenchent pas cette garde de déploiement** ; un code 0 dans ces modes ne certifie pas les liens. `--sans-redaction` ne contourne pas la garde lorsqu'un déploiement est demandé. Le succès incrémental FTP `(0, 0)` demeure un succès, mais seulement après le contrôle des liens.

Cette garde ne verrouille pas les écrivains et ne fige pas le répertoire entre le scan et FTP : l'isolation du build et la coordination local/cloud demeurent des prérequis distincts. Elle ne garantit ni sauvegarde distante ni arrêt borné du pipeline.

## Périmètre

- HTML UTF-8, `href`/`src`, chemins relatifs et absolus de l'hôte explicite, `index.html`, fragments `id` et anciens `a[name]` ; casse conservée.
- Une seule passe de percent-decoding UTF-8 ; entités traitées par le parseur HTML ; query ignorée pour le fichier.
- Cibles d'URL jamais passées aux lectures disque : inventaire lexical préalable, composants racine sans symlink, liens symboliques/fichiers spéciaux refusés. Pas de garantie contre un écrivain hostile, des montages ou hardlinks ; snapshot immobile obligatoire.
- `title`/`textarea` sont du texte, `script`/`style` également pour ce contrôle ; leur slash autofermant ne crée pas de fausses ancres. Contenu de `template` inerte ; `base[href]` refuse la qualification de la page plutôt que deviner ses cibles.
- Hôtes externes, ports non standard, mailto et autres schémas exemptés ; **aucune requête externe**.

Hors périmètre : disponibilité HTTPS, redirections/réécritures Apache, CSS `url()`, `srcset`, `poster`, actions de formulaires, JavaScript dynamique, XML/RSS/sitemap, Markdown, JSON-LD, validité HTML5/récupération complète d'un navigateur, accessibilité et qualité éditoriale. Les éléments exotiques/malformés ne sont pas une validation d'arbre DOM. Aucun téléchargement de kit ni preuve d'installation, aucune indexation/vente/inscription déduite d'un code 0.

## Tests et provenance

```sh
python3 -m unittest discover -s tests
```

Contrats dédiés : `test_verifier_liens_hors_ligne.py`, `test_liens_media_capacity.py`, `test_liens_contenu_texte.py` (27 tests). Qualification réelle : [liens-hors-ligne.md](../docs/liens-hors-ligne.md).

Réemploi du candidat privé des 16–17 novembre, pas de copie de code tiers. Concepts examinés dans [Lychee](https://github.com/lycheeverse/lychee/blob/f10ac2774dac100dfdbf014647487520a8ffe08d/lychee-lib/src/utils/fragment_checker/mod.rs#L58-L145), révision `f10ac2774dac100dfdbf014647487520a8ffe08d`, licences MIT/Apache-2.0, push API observé le 16 novembre 2026 à 12:44:27 UTC ; et [Linkinator](https://github.com/JustinBeckwith/linkinator/blob/62ba21965daddd9db2a451e8eacc510a010d6762/src/links.ts#L8-L104), révision `62ba21965daddd9db2a451e8eacc510a010d6762`, MIT, push observé le 17 à 01:03:16 UTC. Métadonnées recontrôlées le 17. Ni bibliothèque installée/exécutée ni source amont incorporée ; les couvertures plus larges de ces outils ne sont pas revendiquées.
