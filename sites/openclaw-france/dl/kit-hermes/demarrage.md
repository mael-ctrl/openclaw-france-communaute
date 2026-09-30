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

### 10. Le faire tourner 100 % en local (gratuit)

Sans clé API, sans compte, sans coût : un modèle sur votre machine via Ollama.

```bash
curl -fsSL https://ollama.com/install.sh | sh   # installer Ollama (guide officiel)
ollama pull qwen3.5:27b                          # ou un modèle plus petit selon votre RAM
```

Puis `hermes model` → **Custom endpoint** → `http://localhost:11434/v1`, laissez la
clé vide (ou tapez « no-key »), indiquez le nom du modèle. Tout reste chez vous —
parfait pour tester sans dépenser. (Détails au `GUIDE.md`, section 4.)

---

## Et après ?

- **Astuce bonus** : `Ctrl+V` colle une capture d'écran directement dans le chat —
  Hermes analyse l'image (utile pour les messages d'erreur ou les maquettes).
- **Suivez la doc** : <https://hermes-agent.nousresearch.com/docs> — chaque page est
  courte et complète.
- **Un blocage ?** `hermes doctor`, puis la [FAQ officielle](https://hermes-agent.nousresearch.com/docs/reference/faq)
  et le Discord de Nous Research. En français : <https://communaute-ia.fr>.
