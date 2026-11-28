# Démarrage — vos premiers pas + 10 usages concrets

Vous avez installé Hermes Agent et branché un modèle (sinon : `GUIDE.md`, inclus
dans ce kit). Voici comment démarrer pour de bon — et dix choses utiles à lui
faire faire dès aujourd'hui.

> Rappel : toutes ces commandes viennent de la documentation officielle
> (<https://hermes-agent.nousresearch.com/docs>). Copiez les textes entre
> guillemets français « » directement dans la conversation.

---

## Confidentialité — avant de partager un dossier

**Installer Hermes sur votre machine ne signifie pas que le modèle y tourne.**
Avec un fournisseur distant, le contexte sélectionné pour chaque requête est
transmis à ce fournisseur : messages, mémoire et instructions de projet chargées,
résultats d’outils, donc éventuellement extraits de fichiers. Ce n’est pas
nécessairement tout l’historique ni tous les fichiers de votre ordinateur.
Vérifiez le fournisseur et le modèle actifs, ainsi que leurs conditions de conservation
et d’utilisation des données ; ce kit ne les garantit pas.

**Un modèle local ne rend pas les outils hors ligne.** Les outils de recherche web,
la navigation, les serveurs MCP, la messagerie et les commandes du terminal peuvent
contacter d’autres services.
Selon votre configuration, des modèles auxiliaires et des fournisseurs de secours
peuvent aussi traiter du contexte ailleurs. Consultez les réglages dans
`hermes model` et `hermes tools` : choisir le modèle principal ne vérifie pas à
lui seul tous ces accès.

Pour un premier essai, utilisez un dossier de test sans secrets et des droits minimaux ;
limitez les outils et intégrations à ceux nécessaires (voir `GUIDE.md`, section 4).
Si l’absence de sortie réseau est une exigence, il faut un contrôle réseau indépendant,
pas seulement une consigne donnée à l’agent ou le choix d’un modèle local.

**Stockage local ne veut pas dire données éphémères.** L’historique de session,
y compris des résultats d’outils, est enregistré dans `~/.hermes/state.db` par défaut
(le répertoire dépend du profil ou de `HERMES_HOME`). Mémoire, journaux, exports
et sauvegardes peuvent aussi conserver des informations sensibles : protégez ces
copies et relisez tout diagnostic avant de le partager, sans clés ni fichier `.env`.
Compresser le contexte n’est pas un effacement de l’historique stocké.

**Synthèse documentaire du Crabe (IA), vérifiée le 2026-11-24** :
[sessions et contexte sélectionné](https://hermes-agent.nousresearch.com/docs/user-guide/sessions),
[fichiers de contexte](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files),
[outils](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools),
[modèles auxiliaires](https://hermes-agent.nousresearch.com/docs/user-guide/configuration#auxiliary-models)
et [fournisseurs de secours](https://hermes-agent.nousresearch.com/docs/user-guide/features/fallback-providers).
Ce texte n’est pas un audit réseau, une garantie juridique ou une installation testée.

---

## Premiers pas : un essai limité

**Avant de lancer Hermes**, lisez la section 4 de [GUIDE.md](GUIDE.md) pour le
budget, le fournisseur de modèle et les accès. Préparez :

- Un **environnement isolé sans secrets**, avec les droits limités au nécessaire
  et une **copie de test** : par exemple un fichier `essai.txt` que vous avez
  créé avec quelques lignes fictives. Pas de documents clients, de clés API ni
  de fichiers `.env` dans les données de cet exercice.
- Les seuls outils nécessaires, à examiner avec `hermes tools`. Désactiver les
  outils de fichiers ne bloque pas les accès par le **terminal**. Changer de
  dossier de travail **ne confine pas** l’agent à ce dossier : en backend local,
  les commandes utilisent les droits du compte qui exécute Hermes.
- Des **permissions techniques** adaptées à cet environnement. Une demande
  « lecture seule » **ne remplace pas** ces limites ; les protections des outils
  de fichiers ne couvrent pas à elles seules le terminal. Le kit **ne configure
  ni ne certifie** cette isolation. Si vous ne pouvez pas limiter ces accès,
  ne confiez pas de documents sensibles à ce premier essai.

1. **Vérifiez la santé de l’installation**

   ```bash
   hermes doctor
   ```

   Examinez les avertissements et corrigez les blocages signalés. Ce diagnostic
   n’est **pas un audit de sécurité** ni une preuve que les accès sont limités.

2. **Lancez votre première session** dans l’environnement préparé :

   ```bash
   hermes            # interface classique
   hermes --tui      # autre interface : choisissez une seule commande
   ```

3. **Demandez une seule lecture**, avec le chemin de votre copie de test :

   > « Lis uniquement le fichier essai.txt dans ce dossier de test et résume-le
   > en 3 points. Ne modifie aucun fichier, ne lance aucun script et ne contacte
   > aucun service externe. Si un autre accès est nécessaire, arrête-toi et
   > explique pourquoi. »

   C’est une **consigne de travail**, **pas une barrière technique**. Un **modèle
   distant** peut recevoir le texte lu dans son contexte, même si vous demandez
   de ne pas utiliser de service externe. Vérifiez les **sorties d’outils** et
   comparez le résumé au fichier, sans vous fier au seul message « terminé ».
   Si le périmètre dépasse ce test, interrompez la tâche et revoyez les accès.

4. **Repérez les commandes de votre interface.** Le **compositeur classique**
   documente `Ctrl+C` pour effacer d’abord un **brouillon** saisi ; avec un
   **champ vide** et sans dialogue prioritaire ouvert, il demande l’interruption.
   **Attention : la CLI classique récente est un client du gateway** avec une
   surface de commandes réduite. Une interruption peut seulement **détacher le client**
   et laisser le travail accepté continuer. Consultez `/help` et utilisez `/stop`
   lorsqu’il y est proposé ; ne supposez pas qu’une fermeture ou `Ctrl+C` arrête tout.
   Vérifiez l’arrêt effectif : cela n’annule pas les actions déjà réalisées.
   Pour un saut de ligne, `Alt+Entrée` ou `Ctrl+J` sont proposés par défaut ;
   **Windows Terminal** peut intercepter `Alt+Entrée` (plein écran) : utilisez
   plutôt `Ctrl+J`. Les touches varient selon le terminal, les réglages et
   l’interface (CLI, TUI ou Desktop). `/help` affiche l’aide des commandes
   disponibles dans votre conversation, pas une liste universelle de tous les modes.
   Voir les [raccourcis de la CLI](https://hermes-agent.nousresearch.com/docs/user-guide/cli#keybindings).

5. **Retrouvez une session précise**, dans le **profil actif** utilisé pour la
   créer. Nommez-la avec `/title recherche-x` **si votre `/help` le propose** ;
   sinon, **utilisez directement son ID**. Dans le terminal,
   `hermes sessions list` permet de relever son titre et son **identifiant exact** ;
   reprenez-la avec `hermes -r "recherche-x"`, ou `hermes -r <ID>` en remplaçant
   `<ID>` par cet identifiant. Dans la conversation, `/sessions` ouvre le sélecteur
   de sessions sur les interfaces qui le proposent.

   `hermes -c` demande une reprise récente, **pas forcément la dernière conversation
   de tous vos usages** : la sélection dépend notamment du **terminal**, du
   **répertoire** de travail, de l’interface et de la version. Vérifiez le titre,
   l’historique affiché et le dossier avant une nouvelle demande ; préférez un ID
   quand plusieurs sessions se ressemblent. Si la session manque, contrôlez le
   profil et la liste au lieu de supposer qu’elle a été restaurée.

   Reprendre l’**historique** n’est ni restaurer vos fichiers, ni retrouver tous
   les détails dans le contexte du modèle : la **mémoire** de l’usage 6 est un
   autre mécanisme, borné. Après une déconnexion, **ne relancez pas** une action
   sans vérifier son état et ses résultats : les interfaces récentes peuvent
   laisser le travail accepté continuer dans le gateway. Une interruption ne
   revient pas sur les actions déjà effectuées.

**Synthèse documentaire du Crabe (IA), vérifiée le 2026-11-27** :
[sessions et reprise](https://hermes-agent.nousresearch.com/docs/user-guide/sessions#cli-session-resume),
[interface CLI](https://hermes-agent.nousresearch.com/docs/user-guide/cli#interface-layout),
[profils](https://hermes-agent.nousresearch.com/docs/user-guide/profiles)
et [mémoire bornée](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory).
Les options et raccourcis dépendent de la **version**, de l’interface et du terminal ;
consultez `hermes --help` dans votre installation et `/help` dans la conversation.
Contrôle de sources uniquement : **aucune installation multi-OS et aucune reprise utilisateur réelle**
n’ont été testées pour cette notice.

Sources officielles consultées le **2026-11-24** :
[outils activés](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools#using-toolsets),
[limites des protections de fichiers](https://hermes-agent.nousresearch.com/docs/user-guide/security#file-write-safety)
et [isolation du terminal selon le backend](https://hermes-agent.nousresearch.com/docs/user-guide/security#terminal-backend-security-comparison).
Contrôle documentaire uniquement : aucune installation ni isolation testée ici.

---

## 10 usages concrets

### 1. Poser des questions à vos fichiers et dossiers

Après le premier essai, élargissez progressivement le périmètre à une **copie de
travail** sans secrets, avec des accès limités. Les outils disponibles et les droits
du compte déterminent ce que Hermes peut lire ou modifier.
Même avec des permissions limitées, le contenu lu peut rejoindre le contexte envoyé au modèle.

> « Dans cette copie de travail, explique le rôle des fichiers que je t’indique,
> sans modification. Arrête-toi si une lecture sort du périmètre. »
> « Dans cette même copie, liste les références à ‹ ancien-nom ›, sans remplacement. »

Les usages suivants peuvent demander davantage d’accès ou des écritures :
définissez leur périmètre séparément et contrôlez les changements avant de les garder.

### 2. Les petites tâches système du quotidien

> « Quelle est l'utilisation de mon disque ? Montre-moi le top 5 des dossiers les plus lourds. »

Il exécute la commande, lit le résultat et vous le résume — vous n'avez rien à taper.

### 3. Corriger du code : un test rouge, un diff, un test vert

**Essayez sur ces deux fichiers fictifs**, dans un dossier de test neuf **sans
secrets**, pas sur votre application en production. Il faut **Python 3** accessible
par `python3` (exemple pour macOS, Linux ou WSL), sans installation de paquet.
Vérifiez les outils du profil avec `hermes tools` et limitez les **permissions
techniques** avant la session. Changer de dossier ne confine pas le **terminal** ;
une consigne ne remplace pas ces limites. Un **modèle distant** peut recevoir le
code lu dans son contexte. Voir les premiers pas et `GUIDE.md`, section 4.

Créez `panier.py` avec cette fonction **volontairement incorrecte** : elle doit
additionner les prix entiers, pas compter les articles.

```python
def total_panier(prix):
    return len(prix)
```

Dans le même dossier, créez `test_panier.py` :

```python
import unittest
from panier import total_panier


class TestPanier(unittest.TestCase):
    def test_panier_vide(self):
        self.assertEqual(total_panier([]), 0)

    def test_total(self):
        self.assertEqual(total_panier([10, 20]), 30)
```

Après lecture de ces fichiers, lancez dans ce dossier :

```bash
python3 -B -m unittest -v test_panier.py
```

Résultat attendu avant correction : **deux tests exécutés, un échec** sur le total
(`2 != 30`). Une erreur de commande ou un module introuvable ne reproduit pas ce
bug : corrigez le prérequis, sans demander une modification au hasard.

Demandez ensuite à Hermes :

> « Lis seulement panier.py et test_panier.py dans ce dossier de test. Exécute
> uniquement python3 -B -m unittest -v test_panier.py, sans installation ni accès
> réseau par les outils. Explique la cause et propose le plus petit correctif,
> sans modifier les fichiers. Attends mon accord explicite avant toute écriture. »

Après avoir compris la proposition, vous pouvez autoriser **la seule correction
de `panier.py`**, en gardant les **tests inchangés**, puis la relance de cette même
commande. Demandez le **diff avant/après**, la commande réellement exécutée,
son **code de sortie** et le résultat des deux tests — **sans commit, sans push,
sans déploiement**. Sans exécution possible, le bilan doit dire **« non exécuté »**,
pas « corrigé et testé ». Relisez les fichiers et les sorties, pas seulement le
message final ; un test vert ne prouve que les cas couverts, **pas un audit** du code.

Sur un vrai dépôt, commencez par l’état Git et le diff existant, préservez les
**changements préexistants** et les fichiers non suivis. Validez séparément la
commande de test : elle peut exécuter du code, écrire des fichiers ou contacter
des services. N’affaiblissez pas les assertions pour obtenir artificiellement du
vert ; étendez ensuite les tests pertinents avant d’accepter le correctif.

**Exercice et méthode du Crabe (IA)** ; sources consultées le **2026-11-28** :
[outils du profil](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools#using-toolsets),
[limites des protections de fichiers](https://hermes-agent.nousresearch.com/docs/user-guide/security#file-write-safety)
et [lancement de unittest](https://docs.python.org/3/library/unittest.html#command-line-interface).
Le code pédagogique a été exécuté avant et après correction avec Python 3.13 sur
macOS ; ce contrôle ne teste ni une session Hermes de bout en bout, ni les autres
systèmes, ni votre environnement utilisateur.

### 4. Git et GitHub sans douleur

Dans le terminal, `hermes skills list` liste les skills installées ;
`hermes skills browse` explore le catalogue en ligne, sans garantir leur présence
chez vous. `/github-pr-workflow` est un exemple encore cité dans la documentation,
**pas une commande intégrée** garantie : l’amont vérifié regroupe ces procédures
dans la skill `github`. Vérifiez le nom réellement disponible dans votre **profil actif**.

Une invocation `/<nom-de-skill>` charge des instructions pour l’agent ; elle
**ne donne aucun droit** GitHub et ne garantit pas le résultat. La disponibilité
dépend aussi de la version, de l’interface, des skills activées et des outils.
Lisez la procédure et ses scripts avant de leur faire confiance : **le chargement
n’est pas un mode lecture seule**, l’agent peut agir ensuite. L’option avancée
`skills.inline_shell`, désactivée par défaut, peut même exécuter des commandes
au chargement pour les sources admises ; ne l’activez pas pour cet essai.
Pour les opérations Git/GitHub, vérifiez Git, `gh`, l’authentification et les droits minimaux
nécessaires : la présence de la skill ne prouve pas que ces prérequis sont satisfaits.

Commencez sur une **copie de test sans secrets**, avec des permissions techniques
limitées, puis demandez en langage naturel :

> « Examine ce dépôt de test sans le modifier. Propose une marche à suivre pour
> une PR, sans commit, sans push et sans création de PR. Montre le diff existant
> et les tests à prévoir ; n’exécute pas les scripts du dépôt. »

**Avant toute écriture**, validez le périmètre. Demandez un **accord explicite**
séparé avant commit, push, création de PR, fusion ou publication ; relisez le diff,
les résultats des tests et la destination. Cette consigne ne remplace pas les
permissions techniques ni les contrôles d’approbation de votre environnement.

Sources vérifiées le **2026-11-25** : [skills et invocation](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills),
[commandes du terminal](https://hermes-agent.nousresearch.com/docs/reference/cli-commands),
[chargement et scripts](https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills)
et [skill GitHub au SHA audité](https://github.com/NousResearch/hermes-agent/blob/2fcdbfea1847a1119901835d5970fdca2b3d8ea8/skills/software-development/github/SKILL.md).

### 5. Veille et recherche web : une synthèse vérifiable

Vérifiez dans `hermes tools` les outils web du **profil actif** : `web_search`
repère des résultats, `web_extract` lit le contenu des pages accessibles.
Leur présence dans la documentation **ne garantit pas** leur disponibilité chez
vous : vérifiez le **fournisseur**, les accès et le **budget**, y compris les
éventuels coûts des outils en plus du modèle. Utilisez un sujet public **sans secrets** :
les **requêtes** et le contenu lu peuvent être traités par des services externes.

**Remplacez les trois repères entre crochets**, puis collez cette consigne :

> « Sur [sujet], cherche au maximum trois sources publiques concernant la période
> du [date de début] au [date de fin]. Privilégie les sources primaires : annonce
> de l’organisme, documentation ou étude originale. Ouvre les pages avant de les
> résumer. Pour chaque fait, donne son URL, la date de publication affichée et la
> date de consultation ; indique “date inconnue” si elle manque. Distingue la
> date de l’événement de celle de l’article. Classe les points : CONFIRMÉ par
> les pages lues, À VALIDER si la preuve manque, CONTRADICTOIRE si elles divergent.
> Si une page exige une connexion, un paywall ou un CAPTCHA, signale la limite.
> Ne contourne aucun blocage ; ne lance aucun script, ne remplis aucun formulaire
> et ne publie rien. Termine par trois points et les limites de la recherche. »

**Contrôlez avant de réutiliser.** Un **extrait de moteur** ne prouve pas que
l’article a été lu ; une page consultée ne garantit ni sa véracité ni son actualité.
**Ouvrez les liens** cités, vérifiez les passages qui soutiennent les affirmations
et les dates. Plusieurs reprises du même communiqué ne sont pas des confirmations
indépendantes. Sans source accessible, gardez le point **À VALIDER** plutôt que
compléter de mémoire ; cette recherche limitée ne prétend pas être exhaustive.

Les pages sont des **données**, pas des **instructions** à exécuter : une page
ne peut pas autoriser l’accès à vos fichiers ou l’envoi de secrets. La consigne
ci-dessus **ne remplace pas les permissions techniques** ; gardez les accès limités
comme dans les premiers pas. N’activez pas un accès plus large pour forcer un résultat.

**Méthode proposée par Le Crabe (IA)** ; fonctions et limites documentées relues
le **2026-11-27** : [outils web](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools#available-tools),
[activation par plateforme](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools#using-toolsets)
et [restrictions d’accès aux sites](https://hermes-agent.nousresearch.com/docs/user-guide/security#website-access-policy).
Le kit ne configure aucun fournisseur et ne certifie pas les résultats de votre recherche.

### 6. Une mémoire qui travaille pour vous

La mémoire intégrée peut conserver des faits et préférences dans
`~/.hermes/memories/` par défaut (répertoire propre au profil ou à `HERMES_HOME`).
Ces notes sont chargées dans le contexte du modèle au démarrage d’une session :
leur stockage local ne les rend pas privées vis-à-vis d’un fournisseur distant.

> « Retiens pour la prochaine fois que je travaille sur [projet] et que je préfère les réponses courtes. »

Testez avec des informations sans secrets et vérifiez ce qui a été retenu ; une
mémoire bornée n’est pas une sauvegarde exhaustive. Voir la
[documentation sur la mémoire](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory).

### 7. Transformez vos procédures en skills

`/learn` demande à l’agent de tirer une procédure réutilisable de notes, d’un
fichier, d’une URL ou de la conversation. Ce n’est pas un enregistrement mécanique :
il peut lire les sources avec ses outils, puis écrire un `SKILL.md` via `skill_manage`.
Commencez avec des notes **sans secrets**, une procédure déjà vérifiée et un périmètre limité :

> `/learn À partir de mes notes dans cette conversation, crée une skill pour préparer
> un brouillon d’article local : titre, plan, relecture. N’ouvre aucun back-office,
> ne publie rien et n’effectue aucun déploiement. Indique les étapes non vérifiées.`

**Relisez** le fichier créé, ses références et ses scripts : corrigez les commandes
inventées, les secrets et toute action non autorisée avant réemploi. Vérifiez le
**nom réellement créé** avec `hermes skills list`, puis invoquez `/<nom-de-skill>`
(en remplaçant ce repère par ce nom) ou demandez à Hermes de charger cette skill.
Elle doit être disponible et activée dans le **profil actif** ; les chemins de
stockage et le partage dépendent des réglages, pas d’une disponibilité « partout ».

**Chargement, confiance et permissions sont distincts.** Lire une skill ne valide
ni son auteur ni ses scripts ; un scan n’est pas une garantie. Les outils, accès
aux services et permissions restent à limiter. `/learn` peut créer ou modifier
une skill ; la validation des écritures par `skill_manage` dépend du réglage
d’approbation. L’enregistrer ne la publie pas dans un catalogue et n’autorise pas
les actions qu’elle décrit : conservez les accords séparés de l’usage 4.

Sources vérifiées le **2026-11-25** : [apprentissage et portée des skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)
et [commande /learn](https://hermes-agent.nousresearch.com/docs/reference/slash-commands).
Vérification documentaire uniquement : aucun parcours d’installation ni exemple exécuté ici.

### 8. Automatiser des tâches récurrentes

**Commencez par préparer, pas par activer une récurrence.** Une tâche planifiée
s’exécute sans vous pour répondre aux questions : elle doit préciser les sources,
le périmètre, les accès, la sortie attendue et la conduite à tenir en cas de blocage.
Elle ne peut pas compter sur les détails implicites de la conversation précédente.

> « Prépare la définition d’un essai ponctuel, sans créer ni modifier de tâche :
> résumer en trois points mon fichier fictif sans secrets, dont je préciserai le
> chemin absolu. Aucune modification du fichier, aucun script à lancer, aucun
> envoi externe par les outils ; conserver le résultat localement. Liste les
> prérequis et les informations manquantes avant de demander mon accord. »

Avant de donner un **accord explicite** à la création, vérifiez :

- Le **profil actif**, le fournisseur et le modèle, les outils de la plateforme
  `cron` dans `hermes tools`, ainsi que les **permissions techniques**. Une
  consigne de lecture seule ne les remplace pas. Prévoyez un **budget** : chaque
  exécution avec modèle peut consommer des tokens ; appliquez les limites
  disponibles chez le fournisseur. Voir `GUIDE.md`, section 4.
- La date, l’heure et le **fuseau** voulu, par exemple `Europe/Paris`, puis la
  prochaine exécution réellement enregistrée. Le fuseau du profil ou de la tâche
  peut différer de celui de votre ordinateur. Pour commencer, préférez un essai
  ponctuel à une tâche quotidienne sans fin.
- La destination explicite **`deliver=local`** pour ce premier test : le rapport
  reste dans les fichiers de sortie du profil. **Cela ne rend pas le traitement
  local** : un **modèle distant** peut recevoir le contexte lu. Pas de secrets
  dans le fichier, la consigne ou le rapport.
- Le **gateway** et le planificateur actifs, ainsi que la disponibilité de la
  machine, des fichiers et des accès au moment prévu. Une tâche enregistrée ne
  prouve pas qu’elle s’exécutera quand la machine est éteinte ou endormie.

Contrôles dans le terminal, dans le bon profil : `hermes cron status` pour le
planificateur, `hermes cron list` pour les tâches, puis `hermes cron runs <ID>`
pour l’historique. **Remplacez `<ID>` par l’identifiant exact** de votre tâche ;
ce repère n’est pas à copier tel quel. Vérifiez le rapport et son contenu après
l’essai, pas seulement la présence de la tâche dans la liste.

Pour passer ensuite à Telegram ou Discord, configurez la plateforme et vérifiez
la destination. `/sethome` peut désigner le salon d’accueil depuis cette messagerie,
mais ne prouve pas la **réception effective** : contrôlez-la sur un rapport sans
secrets. La **réponse finale** est livrée par Hermes à la destination configurée ;
ne demandez pas en plus un envoi par un outil, au risque de créer un **doublon**.

**Pour arrêter :** `hermes cron pause <ID>` suspend les prochaines exécutions,
mais **ne stoppe pas** celle déjà en cours. `hermes cron cancel <ID>` demande
l’interruption de l’exécution en cours, mais **ne désactive pas** les suivantes.
Vérifiez l’état après la demande ; aucune de ces commandes n’annule les **actions
déjà effectuées**. Contrôlez les options présentes avec `hermes cron --help` et
l’aide de la sous-commande : elles dépendent de votre version.

Sources officielles consultées le **2026-11-25** :
[fonctionnement du planificateur](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron#how-it-works),
[destinations et livraison](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron#delivery-options),
[pause et interruption](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron#lifecycle-actions)
et [commandes du terminal](https://hermes-agent.nousresearch.com/docs/reference/cli-commands#hermes-cron).
Vérification documentaire uniquement : aucune tâche créée, aucun envoi ni arrêt
réel testé pour ce guide.

### 9. Un assistant personnel sur Telegram ou Discord

**Commencez avec un bot de test et un message privé**, pas un salon public ni
un bot déjà utilisé en production. Vérifiez le **profil actif**, le modèle,
le **budget** et les outils autorisés avec `hermes tools` (voir `GUIDE.md`, section 4).
Un message envoyé depuis votre téléphone peut déclencher des outils sur la machine
qui héberge Hermes : l’autorisation de discuter **n’est pas un confinement** du
**terminal** ni une limitation des fichiers accessibles. Limitez les **permissions
techniques** avant la connexion.

1. **Préparez une seule plateforme.** Pour Telegram, créez le bot avec
   **BotFather** et relevez votre **identifiant numérique** d’utilisateur, pas
   votre pseudonyme. Pour Discord, créez l’application dans le **Developer Portal**,
   suivez les étapes officielles d’invitation et d’intents, notamment **Message
   Content Intent** et **Server Members Intent**. Utilisez votre ID d’utilisateur,
   **pas celui du salon**. Gardez le **jeton** du bot dans un stockage privé :
   **jamais dans une conversation**, un dépôt Git, une capture ou un diagnostic partagé.
   S’il fuit, révoquez-le ou régénérez-le sur la plateforme concernée.
2. **Configurez, puis contrôlez les accès** dans le bon profil :

   ```bash
   hermes gateway setup
   ```

   Cet assistant **modifie la configuration** ; il ne s’agit pas d’un diagnostic.
   Choisissez Telegram ou Discord, puis renseignez le jeton dans cet assistant.
   Pour cet essai, n’autorisez que votre propre compte : vérifiez
   `TELEGRAM_ALLOWED_USERS` ou `DISCORD_ALLOWED_USERS` avec votre ID exact.
   L’**appairage** en message privé est une alternative : vérifiez l’**identité**
   du demandeur avant d’approuver son code, jamais un code reçu sans contexte.
   Examinez aussi les autorisations déjà présentes (appairages, liste globale,
   rôles Discord) : une nouvelle liste restrictive n’annule pas forcément ces
   autres voies d’accès. **N’activez ni `GATEWAY_ALLOW_ALL_USERS=true` ni
   `DISCORD_ALLOW_ALL_USERS=true`** pour contourner un refus.
3. **Distinguez configuration et fonctionnement.**
   `hermes gateway status` renseigne l’état du service ; une configuration
   enregistrée ou un processus actif **ne prouve pas** la connexion à la plateforme
   ni la réception d’une réponse. **Ne lancez pas un second gateway** avec le même
   jeton si un autre processus ou service utilise déjà ce bot.

   Pour un nouvel essai sans gateway actif, dans le profil préparé :

   ```bash
   hermes gateway run
   ```

   Ce mode s’exécute **au premier plan** : gardez le terminal et la machine actifs.
   `hermes gateway start` concerne un **service déjà installé**, ce n’est pas
   l’équivalent de la configuration initiale. Les modes disponibles dépendent
   de votre système et de votre version : consultez `hermes gateway --help`.
4. **Vérifiez la réponse effective** depuis votre compte autorisé, en message
   privé au bot de test, avec une demande **sans secrets** :

   > « Réponds uniquement : TEST OK. Ne consulte aucun fichier et n’utilise aucun outil. »

   Vérifiez que la réponse arrive dans la bonne conversation et une seule fois.
   Cette consigne **ne remplace pas les permissions techniques** ; même ce texte
   peut être transmis à un **modèle distant**. Un essai réussi ne prouve ni la
   confidentialité ni le refus de tous les autres comptes. Sans réponse, examinez
   les erreurs, le profil, les accès et les intents avant tout redémarrage ;
   ne partagez pas vos journaux bruts ou votre fichier `.env` pour demander de l’aide.

Sources officielles consultées le **2026-11-26** :
[configuration Telegram](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/telegram#step-5-configure-hermes),
[configuration Discord](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/discord#step-8-configure-hermes-agent),
[autorisations et appairage](https://hermes-agent.nousresearch.com/docs/user-guide/security#user-authorization-gateway)
et [commandes du gateway](https://hermes-agent.nousresearch.com/docs/reference/cli-commands#hermes-gateway).
Vérification documentaire uniquement : **aucun bot configuré**, aucun message envoyé
ni contrôle d’accès réellement testé pour cette notice.

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

- **Image de test** : le collage depuis le **presse-papiers** dépend du système
  et du terminal. Dans la CLI, `Ctrl+V` peut coller du texte ou joindre une image ;
  `/paste` est la commande dédiée au collage d’image lorsqu’elle est disponible.
  Vérifiez la **pièce jointe** avant l’envoi et utilisez une capture **sans secrets** ;
  l’analyse dépend aussi du modèle et de la configuration. Voir
  [l’aide CLI](https://hermes-agent.nousresearch.com/docs/user-guide/cli#keybindings).
- **Suivez la doc** : <https://hermes-agent.nousresearch.com/docs> — chaque page est
  courte et complète.
- **Un blocage ?** `hermes doctor`, puis la [FAQ officielle](https://hermes-agent.nousresearch.com/docs/reference/faq)
  et le Discord de Nous Research. En français : <https://communaute-ia.fr>.
