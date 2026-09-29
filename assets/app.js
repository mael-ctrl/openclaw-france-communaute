/* La Communauté 🦀 — petites interactions, zéro dépendance. */
document.addEventListener('DOMContentLoaded', function () {
  'use strict';

  /* ---- Filtres + recherche (page actus) ---- */
  var grille = document.getElementById('liste-actus');
  if (grille) {
    var cartes = Array.prototype.slice.call(grille.querySelectorAll('.carte'));
    var filtres = Array.prototype.slice.call(document.querySelectorAll('#filtres .filtre'));
    var recherche = document.getElementById('recherche');
    var aucun = document.getElementById('aucun-resultat');
    var tagActif = '';
    var requete = '';

    function appliquer() {
      var visibles = 0;
      cartes.forEach(function (carte) {
        var tags = (carte.getAttribute('data-tags') || '').split(',');
        var texte = carte.getAttribute('data-texte') || '';
        var okTag = !tagActif || tags.indexOf(tagActif) !== -1;
        var okQ = !requete || texte.indexOf(requete) !== -1;
        var visible = okTag && okQ;
        carte.hidden = !visible;
        if (visible) { visibles += 1; }
      });
      if (aucun) { aucun.hidden = visibles > 0; }
    }

    filtres.forEach(function (bouton) {
      bouton.addEventListener('click', function () {
        filtres.forEach(function (b) { b.classList.remove('actif'); });
        bouton.classList.add('actif');
        tagActif = bouton.getAttribute('data-tag') || '';
        appliquer();
      });
    });

    if (recherche) {
      recherche.addEventListener('input', function () {
        requete = recherche.value.trim().toLowerCase();
        appliquer();
      });
    }
  }

  /* ---- Barre de progression de lecture ---- */
  if (document.querySelector('.corps-article, .prose')) {
    var barre = document.createElement('div');
    barre.className = 'progression';
    document.body.appendChild(barre);
    var maj = function () {
      var total = document.documentElement.scrollHeight - window.innerHeight;
      barre.style.width = (total > 0 ? Math.min(100, (window.scrollY / total) * 100) : 0) + '%';
    };
    window.addEventListener('scroll', maj, { passive: true });
    window.addEventListener('resize', maj);
    maj();
  }

  /* ---- Bandeau : adoucir la vitesse selon la longueur ---- */
  var piste = document.querySelector('.bandeau-piste');
  if (piste) {
    var largeur = piste.scrollWidth / 2;
    if (largeur > 0) {
      piste.style.animationDuration = Math.max(38, Math.round(largeur / 42)) + 's';
    }
  }
});
