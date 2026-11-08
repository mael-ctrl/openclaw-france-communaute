# Dépendance vendored : RCSSmin

`rcssmin.py` est une copie **non modifiée** de
[ndparker/rcssmin](https://github.com/ndparker/rcssmin/blob/7e457c8163324f02d2df10ed1612c91b53dcf276/rcssmin.py),
révision `7e457c8163324f02d2df10ed1612c91b53dcf276`, version déclarée 1.3.0.
Licence Apache-2.0, copyright André Malo et ses concédants, texte intégral dans
`RCSSMIN-LICENSE`. Aucun NOTICE présent dans l'arbre amont de cette révision.
Dernier push API observé le 7 novembre 2026 : 10 octobre 2026 à 16:36:38 UTC.
Blob source vérifié : `d49b69c2fa8e9023946fa067e0db326aeb60337e`.

Le moteur appelle explicitement la variante Python, sans extension C requise,
sans commande réseau ni modification de l'interpréteur local/cloud.
Compression syntaxique seulement, pas optimisation sémantique des styles.
`wilsonzlin/minify-html` (MIT, dernier push observé 18 novembre 2025) a été
considéré puis écarté : le HTML éditorial, les espaces des scripts/prompt et les
fichiers téléchargeables ne doivent pas être réécrits pour ce chantier CSS.
