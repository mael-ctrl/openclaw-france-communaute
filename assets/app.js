/* La Communauté 🦀 — petites interactions, zéro dépendance. */
document.addEventListener('DOMContentLoaded', function () {
  'use strict';

  /* ---- Filtres + recherche (page actus) ---- */
  var grille = document.getElementById('liste-actus');
  if (grille) {
    var cartes = Array.prototype.slice.call(grille.querySelectorAll('.carte'));
    var filtres = Array.prototype.slice.call(document.querySelectorAll('#filtres .filtre'));
    var recherche = document.getElementById('recherche');
    var outils = document.getElementById('outils-actus');
    var aucun = document.getElementById('aucun-resultat');
    var statut = document.getElementById('resultats-actus');
    var annonceEnAttente;
    var tagActif = '';
    var requete = recherche ? recherche.value.trim().toLowerCase() : '';

    function appliquer(delaiAnnonce) {
      window.clearTimeout(annonceEnAttente);
      filtres.forEach(function (bouton) {
        var actif = (bouton.getAttribute('data-tag') || '') === tagActif;
        bouton.classList.toggle('actif', actif);
        bouton.setAttribute('aria-pressed', String(actif));
      });
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
      if (statut && typeof delaiAnnonce === 'number') {
        annonceEnAttente = window.setTimeout(function () {
          var message = visibles + (visibles > 1 ? ' résultats' : ' résultat') + ' sur cette page.';
          if (statut.textContent !== message) { statut.textContent = message; }
        }, delaiAnnonce);
      }
    }

    filtres.forEach(function (bouton) {
      bouton.addEventListener('click', function () {
        tagActif = bouton.getAttribute('data-tag') || '';
        appliquer(0);
      });
    });

    if (recherche) {
      recherche.addEventListener('input', function () {
        requete = recherche.value.trim().toLowerCase();
        appliquer(250);
      });
    }
    if (outils && cartes.length) {
      appliquer();
      outils.hidden = false;
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
