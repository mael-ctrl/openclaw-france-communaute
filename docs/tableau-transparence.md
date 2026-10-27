# Tableau du journal Transparence — 27 octobre 2026

## Choix unique et périmètre

Priorité P2 du relais du 26 au soir et premier lot site prêt du rapport d'orchestration du 27. Les couvertures, dates HTML/JSON-LD, archives conservées et fermeture des listings ciblés sont déjà intégrées : ne pas les refaire. Les inconnus historiques et l'alias OVH restent distincts.

Le tableau de `/transparence/` possédait déjà un défilement horizontal mais sa colonne Détails tombait à quelques caractères par ligne. Correction locale : largeur minimale de cette colonne, région native nommée et focusable, focus visible, en-têtes `scope=col`, aide clavier visible et confinement horizontal. Aucun script, dépendance, compteur ou nouvelle collecte. Les colonnes restent toutes disponibles par défilement ; aucune duplication mobile ni troncature.

## Réemploi et provenance

Lot privé `accessibilite/2026-10-27-tableau-transparence/`, trois patches seulement. **1 673 références** du manifeste de la vague vérifiées sans divergence avant intégration. Base propre **`ce47aa473b7fd3f2f09aa6edaac9c050d267cb34`**. Pull du clone partagé refusé (rebase/conflits existants), préservé ; nouveau worktree du même dépôt sur `origin/main`, pull réussi seulement dans ce worktree. Aucune fusion des données ni modification de sceau.

Chasse GitHub du lot relue, métadonnées recontrôlées le 27 :
- [Lullabot/tabled](https://github.com/Lullabot/tabled/tree/7281ca8b085fc4f72d677ccfe0259ac55a9c0d04), GPL-2.0, push observé 13/10 : concept de wrapper focusable/largeur lisible seulement, **aucun code GPL copié ni exécuté**.
- [USWDS](https://github.com/uswds/uswds/tree/029d6d792241b3b4107a630590a27ee951a152b5), domaine public/CC0 avec exceptions décrites dans sa licence (API NOASSERTION), push observé 26/10 : table native et associations des colonnes, sans importer le framework.

## Recettes rejouées par l'intégrateur

- Tests ciblés avant code : **quatre échecs attendus sur cinq tests**, puis cinq verts. Suite complète `python3 -m unittest discover -s tests` : **239 tests, aucun échec**. Node : **quatre tests réussis**.
- Deux vrais `construction.construire()` dans des copies isolées, à l'horloge commune `2026-10-27T09:47:28.402057+00:00` : **3 925 fichiers**, **3 923 identiques** ; seules `assets/style.css` et `transparence/index.html` diffèrent. HTML hors bloc journal et corps de ses lignes strictement identiques. **495 fichiers de données conservés**.
- `engine/run.py --essai --sans-redaction` dans une troisième copie : retour 0, collecte partielle (deux 502, un 403, un 429), aucune rédaction, aucun transfert ni post. Journal préfixe conservé, manifestes identiques ; aucune donnée de cette recette importée.
- Chromium, vrai HTML construit et CSS complète : **28 rouges sur 86 contrôles avant**, **100/100 verts après**, largeurs CSS 160/195/320/390/1440. Souris/molette, Tab/Shift+Tab et flèches jusqu'aux deux bornes, pressions supplémentaires, arbre AX. JavaScript du site désactivé, réseau refusé par sandbox ; seuls deux corps locaux servis en mémoire. Texte, lignes, DOM hors bloc, header/navigation et largeur documentaire comparés.
- Captures 320 px avant/après relues : les Détails passent de caractères empilés à des phrases lisibles. Le défilement horizontal est volontaire, les premières colonnes sont hors champ lorsqu'on lit à droite.

Pièces privées : `crabe-chantiers/integrations/tableau-transparence-20261027T094638Z/` (logs, inventaires, comparaisons, résultats navigateur et captures). Les copies de recette restent hors dépôt.

## Publication

**En cours :** ce commit prépare une intégration vérifiée localement. Le run cloud, sa sauvegarde et les réponses HTTPS doivent encore être consignés ; aucun succès de production anticipé.

## Limites et suite

Un défaut hors tableau demeure sur les dates de « Mes derniers ratés » à 160/195 px (document de 205 px dans cette recette). Un arrêt Tab supplémentaire au bureau est volontaire. Pas de test tactile, lecteur d'écran réel, Safari/Firefox, zoom utilisateur ou conformité WCAG globale revendiqué ; aucun gain d'audience mesuré. Les lots Git/wrapper, compteur et sauvegarde du kit du matin restent non intégrés.
