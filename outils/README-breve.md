# La Brève du Crabe — composition locale uniquement

`python3 -B outils/compose_breve.py` reprend le compositeur livré le 15/10/2026. Python 3.11+, bibliothèque standard, aucune dépendance d'envoi. Aucun import du moteur, réseau, sous-processus, LLM, secret, horloge courante, destinataire ou collecte. **Ne pas le brancher au pipeline, à un formulaire ou à un cron.**

## Exécution

Préparer hors du dépôt un instantané authentique : `git show <SHA-complet>:data/breves.json`, en conservant ses octets et son SHA-256. Ne pas filtrer ou retrier ce JSON avant composition. Vérifier séparément le rattachement commit→octets : l'outil valide la syntaxe du SHA, pas son existence Git.

```bash
python3 -B -m unittest discover -s tests -p test_compose_breve.py -v
python3 -B outils/compose_breve.py --help
```

Exemple d'édition avec données figées le 17/10/2026 (le fichier `breves.json` est à fournir hors dépôt) :

```bash
python3 -B outils/compose_breve.py \
  --input /chemin/hors-depot/breves.json --date 2026-10-17 \
  --sha 12b60dc0ed4179fe2c568b2a8fb2309e381ae8b3 \
  --expect-sha256 2feef9565f915dd3417dd93fe844cfdc144f1e150c6711bb446193dadde2d62b \
  --days 7 --limit 2 \
  --only-id 07ad9ae53fcdeb92 --only-id 116a65f219d1169c
```

Stdout seulement par défaut ; `--output /chemin/hors-depot/nouveau.md` crée un fichier neuf, jamais écrasé. Code 0 : composé ; 2 : paramètres/JSON/entrée/sortie refusés. Pour vérifier un fichier déjà livré, relancer sans `--output` et comparer les octets ; ne pas réécrire le fichier. Aucun numéro d'envoi n'est inventé : le titre porte la date d'édition.

## Sélection et schéma

- Entrée : tableau non vide UTF-8, 8 Mio maximum ; clés dupliquées, NaN, placeholders connus et champs inconnus rejetés. Toute entrée invalide bloque le fichier entier, y compris hors fenêtre.
- Champs requis : `id` (16 hex minuscules), `slug` (ASCII alphanumérique/tirets, 1–200), `titre`, `resume`, `source`, `lien_source`, `date_redac`, `date_source`. Les dates sont ISO à secondes avec fuseau explicite ; `date_source` peut être null. Champs optionnels : `importance` entier 1–5, `tags` liste de textes, `gen` objet. Pas de champ de contacts.
- La borne **400 premières entrées dans l'ordre du JSON** précède tout tri. Depuis le catalogue du 19/10, ce n'est plus le total des pages construites : c'est le plafond prudent des **candidats du compositeur**. La recette du 20/10 au SHA `ea0c0b49047348698765c5455daa735520725648` vérifie leur inclusion dans les 983 brèves construites et les trois destinations choisies. Les anciens messages CLI « 400 pages construites » désignent ce sous-ensemble, pas tout le site. Une collision de slug dans ces 400 entrées est refusée ; le constructeur contrôle désormais aussi les autres entrées. Une évolution du moteur exige une nouvelle recette ; le compositeur n'interroge pas le site.
- Fenêtre UTC de `--days` (1–31), se terminant à minuit après `--date`. Date source si renseignée, sinon rédaction ; rédaction future exclue. Pour l'exemple : 11/10 inclus → 18/10 exclu. Ce n'est pas une date de première publication.
- Tri par rédaction décroissante puis slug et JSON stable. Dédup ID/slug/titre normalisé/URL hors fragment/libellé de source ; pas de dédup inter-numéros. Maximum `--limit` 1–10, cinq par défaut ; jamais de remplissage artificiel.
- `--only-id` répétable permet une **sélection éditoriale explicite sans retoucher le snapshot**. Chaque ID doit être unique, admissible dans la fenêtre et les 400 pages, non ambigu et survivre à la déduplication. Si la limite supprimerait un ID, l'outil refuse. Sans cette option, sélection automatique inchangée. L'option ne certifie aucun fait.
- Canonique média fixe `https://communaute-ia.fr/breves/{slug}/`. Sources exactes conservées ; URL HTTPS de forme publique, sans identifiant ni suivi connu. Contrôle syntaxique uniquement, sans DNS. Markdown/HTML de contenu rendu inerte ; aucune image/pixel ajoutée.

## Revue obligatoire et lancement désactivé

Le brouillon attribue les résumés au moteur et indique une reprise non vérifiée indépendamment. Relire les sources publiques séparément ; classer confirmé / à valider / contradictoire et écarter les entrées insuffisantes via `--only-id`. Un HTTP 200, un tag Git ou un résumé IA ne prouvent pas une annonce, une build téléchargeable, une disponibilité régionale ni une performance. Ne pas transformer une date de rédaction en nouveauté du jour.

IA explicitée ; engagement de 100 % des **bénéfices**, pas du CA, vers les associations : aucun don réalisé n'est affirmé. Aucun chiffre d'audience/financier ajouté.

**Envoi et inscription restent désactivés** : compte/propriété, offre contractuelle, responsable et confidentialité avant collecte, consentement/double confirmation, expéditeur, absence de suivi, droits/rétention et désinscription bout en bout ne sont pas éprouvés. Aucune adresse ni action de formulaire ancienne n'est réutilisable comme preuve. Un mandat séparé est nécessaire pour toute activation ; cet outil restera sans transport.

## Provenance du remploi

Code interne du lot newsletter du 15/10, conservé et adapté, pas un nouveau système. Deux dépôts réévalués en lecture le 17/10 : `KarenSpinner/substack-digest` (MIT, push API 2025-10-17T17:16:52Z, SHA `5a29e6ba382ea227868be9464044a1fa9a0a80c4`) : dédup/limites déjà couvertes, scraping/LLM/horloge écartés.[1][2]

`iloveitaly/listmonk-newsletter` (licence API null, push 2026-10-13T12:18:09Z, SHA `c635dace19f344918bfde0199fd8630d6274cc71`) : droits non établis, campagnes mutantes hors périmètre.[4][5]

Aucun code tiers incorporé, dépôt installé ou exécuté.

Détails et preuves : lot privé `crabe-chantiers/newsletter/2026-10-17/provenance-repos.md`. Le patch ne contient ni snapshot, brouillon, capture publique, `data/`, `_site/`, ni ancien formulaire. La recette réelle sur snapshot est dans le vérificateur du lot ; la suite intégrée est entièrement synthétique et autonome, sans le snapshot historique du 15/10.

## Sources

[1] https://api.github.com/repos/KarenSpinner/substack-digest
[2] https://raw.githubusercontent.com/KarenSpinner/substack-digest/5a29e6ba382ea227868be9464044a1fa9a0a80c4/create_digest.py
[4] https://api.github.com/repos/iloveitaly/listmonk-newsletter
[5] https://raw.githubusercontent.com/iloveitaly/listmonk-newsletter/c635dace19f344918bfde0199fd8630d6274cc71/listmonk_newsletter/__init__.py
