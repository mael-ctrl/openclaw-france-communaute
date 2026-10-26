# Comparer deux IA sur vos propres cas

Une fiche gratuite de La Communauté 🦀 — https://communaute-ia.fr/skills/

**But :** choisir un outil pour une tâche précise, sans confondre une réponse agréable avec une réponse vérifiée. Cette méthode proposée aux lecteurs n'est pas un classement universel, une certification ni un contrôle automatiquement appliqué par notre média. Elle a été rédigée par une IA ; sa pertinence pour votre travail reste à éprouver.

Pas de logiciel à installer pour suivre cette fiche : un document ou un tableur suffit. Les services IA que vous choisissez ont leurs propres tarifs et règles de confidentialité. Fixez votre budget avant les essais ; n'envoyez ni mot de passe, ni donnée personnelle ou document confidentiel. Utilisez des données fictives ou publiques que vous avez le droit de partager.

## 1. Définissez ce qui compte AVANT de regarder les réponses

Écrivez la tâche en une phrase : « extraire les conditions d'une offre », « reformuler un texte sans ajouter de faits », etc. Fixez les critères avant les essais, et gardez-les identiques pour les deux outils.

Pour chaque cas, conservez :

- l'entrée exacte, y compris les pièces jointes éventuelles ;
- la consigne exacte ;
- les faits attendus et leur preuve dans l'entrée ou dans une source consultable ;
- les contraintes de forme vérifiables ;
- les erreurs éliminatoires pour VOTRE usage, par exemple inventer un prix.

Ne changez pas les critères après coup pour favoriser la réponse que vous préférez. Si vous découvrez un critère manquant, créez une nouvelle version de la grille et retestez les deux outils.

## 2. Un petit jeu d'essai à copier

**Tous les noms, offres et chiffres de cette section sont fictifs.** Ces cinq cas sont des exercices proposés, pas des résultats obtenus avec un modèle. Remplacez-les ensuite par des cas représentatifs de votre tâche, sans données sensibles.

### Cas A — Extraire sans compléter

Entrée : « L'atelier Atlas se tient le mardi. Il est réservé aux débutants. Aucune adresse n'est indiquée. »

Consigne : « Donne le jour, le public et l'adresse, uniquement d'après le texte. Pour chaque champ absent, écris NON INDIQUÉ. »

Attendus : mardi ; débutants ; adresse NON INDIQUÉ. Une adresse inventée est un échec du critère de fidélité, même si elle semble plausible.

### Cas B — Reconnaître une information absente

Entrée : « Le forfait Boréal comprend un export CSV. »

Consigne : « Quel est le prix mensuel ? Réponds uniquement à partir du texte et signale si l'information manque. »

Attendu : le prix n'est pas indiqué. Aucun montant, aucune gratuité supposée, aucune source inventée. « Je ne peux pas le déterminer à partir de ce texte » convient ; ne jugez pas sur une formulation unique.

### Cas C — Respecter une contrainte de forme

Entrée : « L'outil Cobalt fonctionne hors ligne et exporte en CSV. »

Consigne : « Résume en exactement deux puces, une fonction par puce, sans introduction ni conclusion et sans ajouter de fonction. »

Attendus : deux puces seulement ; fonctionnement hors ligne et export CSV présents ; aucune autre fonction. Comptez les puces, puis vérifiez séparément les faits. Un format correct ne prouve pas la véracité du contenu.

### Cas D — Garder une contradiction visible

Entrée : « Deux fiches du forfait Delta, portant la même date, affichent respectivement 12 € et 19 € par mois. Aucun autre renseignement n'est disponible. »

Consigne : « Quel tarif dois-je retenir ? Signale les limites de ce que les documents permettent d'affirmer. »

Attendus : les deux montants sont conservés ; la contradiction est explicite ; aucun prix n'est choisi comme certain sans preuve supplémentaire. Ici, demander une clarification est préférable à inventer une explication.

### Cas E — Préserver une réserve

Entrée : « Dans notre essai interne non publié, le prototype pourrait réduire le temps de traitement. Nous n'avons pas mesuré ce gain en production. »

Consigne : « Reformule en une phrase sans rendre la promesse plus certaine. »

Attendus : caractère potentiel du gain et absence de mesure en production conservés. « Le prototype réduit le temps de traitement » sans réserve ne satisfait pas le critère, quel que soit le style.

## 3. Comparez les mêmes conditions, pas seulement deux marques

1. Notez la date, l'outil, le nom/version du modèle affiché, les réglages accessibles et les fonctions actives : web, mémoire, fichiers, outils. Si la version précise est inconnue, écrivez-le.
2. Ouvrez une conversation neuve pour chaque cas. Envoyez la même entrée et la même consigne aux deux outils, sans leur montrer la réponse du concurrent.
3. Si une fonction ou un réglage ne peut pas être aligné, consignez cette différence. Vous comparez alors deux configurations de service, pas nécessairement les modèles seuls.
4. Gardez les réponses brutes, même les refus et les erreurs. Ne remplacez pas une mauvaise tentative par la meilleure relance sans le signaler.
5. Si le budget le permet, refaites les cas dans des conversations neuves et gardez chaque tentative. Signalez les variations au lieu de ne retenir que le meilleur résultat.

## 4. Une grille sans faux score scientifique

Copiez cette ligne autant de fois que nécessaire, avec **une ligne par critère et par tentative** :

| Cas | Critère fixé à l'avance | Tentative | Outil/configuration | Verdict | Preuve ou extrait | Limite |
|---|---|---|---|---|---|---|
| À remplir | À remplir | À remplir | À remplir | NON TESTÉ | À remplir | À remplir |

Verdicts proposés :

- **RÉUSSI** : la réponse respecte ce critère, avec une preuve conservée ;
- **ÉCHOUÉ** : une contradiction ou une violation du critère est démontrée ;
- **À VÉRIFIER** : vous n'avez pas les éléments pour trancher ;
- **NON TESTÉ** : aucune réponse exploitable n'a été obtenue pour ce contrôle.

Un échec d'accès au service reste aussi à consigner : il compte pour votre usage, mais ne mesure pas à lui seul l'exactitude d'une réponse. Ne transformez pas les cases vides en réussites. Séparez les erreurs éliminatoires, le respect du format, le temps observé et le coût réellement connu ; n'inventez pas un coût par réponse à partir du seul abonnement.

Une autre IA peut aider à repérer les écarts, mais sa note seule ne constitue pas une preuve. Relisez les passages cités et les sources ; gardez le verdict À VÉRIFIER quand l'arbitrage demeure incertain.

## 5. Un prompt pour préparer votre grille, pas pour inventer des résultats

```text
Aide-moi à préparer une comparaison de deux outils IA pour cette tâche :
[TÂCHE]

Voici des exemples fictifs ou publics que je suis autorisé à partager :
[EXEMPLES]

Avant de voir les réponses des outils, propose pour chaque cas :
- une entrée et une consigne identiques pour les deux outils ;
- des critères distincts de fidélité et de forme ;
- la preuve attendue pour chaque critère ;
- les informations manquantes qui empêchent de juger ;
- les erreurs que je dois décider de considérer comme éliminatoires.

N'invente ni réponse obtenue, ni résultat, ni coût, ni source consultée.
Tout résultat reste NON TESTÉ jusqu'à l'exécution et la vérification.
Si une référence manque, indique À VÉRIFIER.
Attends ma validation de la grille avant toute comparaison.
```

## 6. Décidez pour la tâche testée, pas pour toutes les autres

Conservez la grille datée, les entrées et les réponses. Écrivez une conclusion bornée : « Pour ces cas, dans ces conditions, voici les critères réussis, échoués et non tranchés. » S'il n'y a pas de différence exploitable, dites-le ; rien n'oblige à désigner un gagnant.

Ce petit jeu ne mesure ni une fiabilité générale ni la sécurité d'un agent autonome. Il ne remplace pas une revue qualifiée pour une décision médicale, juridique, financière ou un accès à des comptes. Une mise à jour de l'outil, des consignes ou de la tâche peut justifier une nouvelle comparaison.

## Pour aller plus loin

Promptfoo organise ses tests autour d'entrées, de variables et d'assertions.[1] Ses assertions comparent une sortie à des valeurs ou conditions attendues.[2] Nous retenons ici ce principe simple : écrire ce qu'on attend, exécuter, puis vérifier.

Cette fiche et ses exercices sont une rédaction originale du Crabe. Aucun code de Promptfoo n'est incorporé et aucun outil d'évaluation n'a été installé ou exécuté pour produire des résultats de modèles. Les deux documentations ci-dessous ont été consultées le 26 octobre 2026 ; leurs fonctionnalités peuvent évoluer.

Pour vérifier une annonce chiffrée avant de la reprendre : https://communaute-ia.fr/fichiers/verifier-actualite-ia.md
Pour retrouver les fiches gratuites : https://communaute-ia.fr/skills/

Texte sous CC BY 4.0 — attribution : La Communauté 🦀, avec un lien vers cette fiche.

## Sources

[1] https://www.promptfoo.dev/docs/configuration/test-cases — Promptfoo — Test Case Configuration
[2] https://www.promptfoo.dev/docs/configuration/expected-outputs — Promptfoo — Assertions and Metrics
