# Démarrage — vos premiers pas + 10 usages concrets

Vous avez installé Hermes Agent et branché un modèle (sinon : `GUIDE.md`, inclus
dans ce kit). Voici comment démarrer pour de bon — et dix choses utiles à lui
faire faire dès aujourd'hui.

> Rappel : toutes ces commandes viennent de la documentation officielle
> (<https://hermes-agent.nousresearch.com/docs>). Copiez les textes entre
> guillemets français « » directement dans la conversation.

---

## Premiers pas (5 minutes)

1. **Vérifiez la santé de l'installation**

   ```bash
   hermes doctor
   ```

   Tout doit être vert. Sinon, il vous dit quoi corriger.

2. **Lancez votre première session**

   ```bash
   hermes            # interface classique
   hermes --tui      # interface moderne (recommandée)
   ```

3. **Faites connaissance.** Demandez par exemple :

   > « Résume ce dossier en 5 points et dis-moi quel fichier semble être le point d'entrée. »

   Hermes va utiliser ses outils (lecture de fichiers, terminal) pour répondre.

4. **Apprenez les trois raccourcis vitaux** : `Ctrl+C` interrompt l'agent,
   `Alt+Entrée` (ou `Ctrl+J`) fait un saut de ligne sans envoyer, `/help` liste
   toutes les commandes.

5. **Reprenez où vous en étiez** : quittez, puis relancez avec `hermes -c` — votre
   dernière session revient intacte. Nommez vos sessions avec `/title recherche-x`
   pour les retrouver ensuite via `hermes sessions list` et `hermes -r "recherche-x"`.

---

## 10 usages concrets

### 1. Poser des questions à vos fichiers et dossiers

Hermes lit votre machine comme vous. Idéal pour s'y retrouver dans un projet ou un
dossier en désordre.

> « Explique-moi ce que fait ce projet, fichier par fichier. »
> « Trouve toutes les références à ‹ ancien-nom › dans ce dossier et liste-les. »

### 2. Les petites tâches système du quotidien

> « Quelle est l'utilisation de mon disque ? Montre-moi le top 5 des dossiers les plus lourds. »

Il exécute la commande, lit le résultat et vous le résume — vous n'avez rien à taper.

### 3. Coder et corriger sans se battre

> « Ce test échoue. Trouve pourquoi et corrige-le. »
> « Ajoute une validation des entrées dans cette fonction, en respectant le style du fichier. »

Il cherche, lit, modifie, relance les tests. Vous validez les changements.

### 4. Git et GitHub sans douleur

Des skills dédiées existent — par exemple `/github-pr-workflow`, cité dans la doc.
Elles s'utilisent comme des commandes.

> `/github-pr-workflow crée une PR propre pour la refonte de l'authentification`

Ou, en langage naturel : « Aide-moi à mettre en place un workflow PR propre pour ce
dépôt. » Explorez le reste avec `hermes skills browse`.

### 5. Veille et recherche web

> « Cherche les actualités récentes sur [sujet] et fais-moi une synthèse avec les sources. »

Hermes dispose d'outils de recherche et d'extraction web natifs ; demandez-lui de
citer les pages consultées, et faites-le creuser une source précise si besoin.

### 6. Une mémoire qui travaille pour vous

Au fil des sessions, Hermes retient vos faits et préférences (dans `~/.hermes/`).

> « Retiens pour la prochaine fois que je travaille sur [projet] et que je préfère les réponses courtes. »

À la session suivante, il s'en souvient. (Sa mémoire est volontairement bornée ;
il fait le ménage en consolidant — vous pouvez l'aider : « nettoie ta mémoire ».)

### 7. Transformez vos procédures en skills

Répétez-vous les mêmes explications ? Apprenez-les-lui une fois :

> `/learn comment publier un article : ouvrir le back-office, nouveau brouillon, relire, publier`

Ensuite, la skill (par exemple `/publier-un-article`) recharge la procédure
partout. Vous pouvez aussi dire : « sauvegarde ce que tu viens de faire en skill
`deploy-staging` ».

### 8. Automatiser des tâches récurrentes

Hermes sait planifier des tâches en langage naturel. Demandez et il met en place le
rappel ou le rapport :

> « Chaque matin à 8 h, fais-moi la synthèse de ma journée et envoie-la-moi. »

Pour recevoir les résultats sur Telegram ou Discord, désignez le salon d'accueil avec
`/sethome` dedans. Conseil de la doc : ne mettez ça en place qu'après avoir une
configuration de base stable.

### 9. Un assistant personnel sur Telegram ou Discord

```bash
hermes gateway setup     # configuration interactive de la plateforme
hermes gateway status    # vérifier que ça tourne
```

Votre agent devient un bot joignable depuis votre téléphone. **Sécurité** (doc) :
verrouillez l'accès avec des listes d'utilisateurs autorisés
(`TELEGRAM_ALLOWED_USERS`, `DISCORD_ALLOWED_USERS`) ou le système d'appairage ;
jamais `GATEWAY_ALLOW_ALL_USERS=true` pour un bot avec accès au terminal.

### 10. Utiliser un modèle local : coûts et limites du hors-ligne

Le kit et le logiciel Hermes sont **gratuits**. Exécuter un modèle sur votre
machine avec Ollama évite la **facturation API de ce modèle**, pas les coûts de
**matériel**, d’**électricité**, d’un éventuel **hébergement** ou des **outils externes**
activés. **Ollama Cloud** est une offre distincte : choisir Ollama ne suffit pas
à prouver que le modèle tourne sur votre machine.

1. Suivez le [démarrage officiel Ollama](https://docs.ollama.com/quickstart)
   pour votre système, puis choisissez et téléchargez un **modèle local**, pas
   un modèle cloud. Installation et téléchargement nécessitent normalement
   une connexion ; prévoyez-les avant un essai déconnecté.
2. Vérifiez l’**appel d’outils**, les ressources matérielles et le contexte du
   modèle. La documentation Hermes demande **64 000 tokens** de contexte au
   minimum pour l’usage agent avec outils. Configurez le contexte côté serveur
   Ollama et indiquez la même valeur dans Hermes ; un réglage Hermes seul ne
   suffit pas. Le [guide officiel local](https://hermes-agent.nousresearch.com/docs/integrations/providers#ollama--local-models-zero-config)
   explique comment contrôler le contexte effectif avec `ollama ps`.
   Aucun minimum de RAM universel ni fonctionnement sur votre machine n’est garanti.
3. Lorsque le serveur local est prêt : `hermes model` → **Custom endpoint** →
   `http://localhost:11434/v1`, puis le nom exact du modèle installé. L’API locale
   Ollama ne demande pas de clé ; la FAQ Hermes utilise `ollama` comme valeur
   de remplacement si le client en demande une. Ne fournissez pas une clé cloud
   pour ce serveur local et ne l’exposez pas publiquement.

**Un modèle local ne garantit pas le hors-ligne de tout l’agent.** Vérifiez les
**modèles auxiliaires**, les **fournisseurs de secours**, les outils connectés et
les extensions : ils peuvent utiliser d’autres services selon leur configuration.
Examinez les outils avec `hermes tools` ; désactiver le web ne bloque pas à lui seul
le réseau du **terminal**, des scripts ou des extensions.

Commencez avec une copie de test **sans secrets**. Si aucune sortie réseau n’est
acceptable, utilisez un environnement isolé avec un **contrôle réseau indépendant**
et vérifiez les connexions ; le kit n’effectue **pas un audit réseau** et ne
certifie pas ce confinement. Lisez aussi [GUIDE.md](GUIDE.md), section 4,
pour le budget et la confidentialité avant votre premier essai.

Sources officielles consultées le **2026-11-23** :
[modèle local et endpoint](https://hermes-agent.nousresearch.com/docs/reference/faq#can-i-use-it-offline--with-local-models),
[modèles auxiliaires](https://hermes-agent.nousresearch.com/docs/user-guide/configuration#auxiliary-models)
et [fournisseurs de secours](https://hermes-agent.nousresearch.com/docs/integrations/providers#fallback-providers).
C’est un contrôle documentaire, pas une installation ni un test hors-ligne réalisé.

---

## Et après ?

- **Astuce bonus** : `Ctrl+V` colle une capture d'écran directement dans le chat —
  Hermes analyse l'image (utile pour les messages d'erreur ou les maquettes).
- **Suivez la doc** : <https://hermes-agent.nousresearch.com/docs> — chaque page est
  courte et complète.
- **Un blocage ?** `hermes doctor`, puis la [FAQ officielle](https://hermes-agent.nousresearch.com/docs/reference/faq)
  et le Discord de Nous Research. En français : <https://communaute-ia.fr>.
