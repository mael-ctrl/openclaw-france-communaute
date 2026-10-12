/* Extraits du pack : copie sur demande, sans dépendance ni envoi de données. */
document.addEventListener('DOMContentLoaded', function () {
  'use strict';

  document.querySelectorAll('.extrait-pack').forEach(function (bloc) {
    var texte = bloc.querySelector('pre');
    var titre = bloc.querySelector('summary');
    var bouton = document.createElement('button');
    bouton.type = 'button';
    bouton.className = 'bouton fantome';
    bouton.textContent = 'Copier le prompt';
    bouton.setAttribute('aria-label', 'Copier le prompt : ' + titre.textContent.trim());
    bouton.style.font = 'inherit';
    bouton.style.minHeight = '48px';
    bouton.style.cursor = 'pointer';
    var statut = document.createElement('p');
    statut.className = 'petit-texte';
    statut.setAttribute('role', 'status');
    statut.setAttribute('aria-live', 'polite');
    bloc.insertBefore(bouton, texte);
    bloc.insertBefore(statut, texte);

    bouton.addEventListener('click', async function () {
      bouton.disabled = true;
      statut.textContent = '';
      try {
        await navigator.clipboard.writeText(texte.textContent);
        statut.textContent = 'Prompt copié. Collez-le dans votre assistant IA.';
      } catch (erreur) {
        statut.textContent = 'Copie indisponible. Sélectionnez le texte du prompt et copiez-le manuellement.';
      } finally {
        bouton.disabled = false;
      }
    });
  });
});
