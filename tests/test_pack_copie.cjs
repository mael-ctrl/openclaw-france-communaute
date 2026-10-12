/* Contrat du script réel ; DOM minimal et presse-papiers remplacé à la frontière. */
const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const fichier = path.join(__dirname, '..', 'assets', 'pack-copie.js');

function element(tag, text = '') {
  return {
    tag, textContent: text, attrs: {}, style: {}, children: [], listeners: {},
    setAttribute(key, value) { this.attrs[key] = value; },
    addEventListener(event, handler) { this.listeners[event] = handler; },
    insertBefore(child, ref) { this.children.splice(this.children.indexOf(ref), 0, child); },
  };
}

function charger(clipboard) {
  const extraits = ['Texte avec [champ] & <exemple>\nDeuxième ligne.', 'Autre prompt.'].map(text => {
    const bloc = element('details');
    const pre = element('pre', text);
    const summary = element('summary', 'Un titre');
    bloc.children.push(summary, pre);
    bloc.querySelector = selector => ({ pre, summary }[selector] || null);
    return bloc;
  });
  const document = {
    querySelectorAll(selector) {
      assert.equal(selector, '.extrait-pack');
      return extraits;
    },
    createElement: element,
    addEventListener(event, handler) {
      assert.equal(event, 'DOMContentLoaded');
      handler();
    },
  };
  // Sans script, le HTML reste lisible mais aucun bouton n'est créé.
  vm.runInNewContext(fs.existsSync(fichier) ? fs.readFileSync(fichier, 'utf8') : '', {
    document, navigator: { clipboard },
  });
  return extraits;
}

function bouton(bloc) { return bloc.children.find(el => el.tag === 'button'); }
function statut(bloc) { return bloc.children.find(el => el.attrs.role === 'status'); }

test('copie seulement le prompt choisi, sans titre, en conservant caractères et lignes', async () => {
  const copies = [];
  const blocs = charger({ writeText: async texte => { copies.push(texte); } });
  assert.equal(blocs.filter(b => bouton(b)).length, 2, 'Un bouton par extrait');
  assert.deepEqual(copies, [], 'Aucune écriture au chargement');
  for (const bloc of blocs) {
    const b = bouton(bloc);
    assert.equal(b.type, 'button');
    assert.equal(b.textContent, 'Copier le prompt');
    assert.ok(bloc.children.indexOf(b) < bloc.children.indexOf(bloc.querySelector('pre')));
    await b.listeners.click();
    assert.equal(copies.at(-1), bloc.querySelector('pre').textContent);
    assert.match(statut(bloc).textContent, /Prompt copié/);
    assert.equal(b.disabled, false);
  }
  assert.equal(copies.length, 2);
});

test('un refus du presse-papiers propose la copie manuelle sans annoncer un succès', async () => {
  const [bloc] = charger({ writeText: async () => { throw new Error('Permission refusée'); } });
  const texteAvant = bloc.querySelector('pre').textContent;
  await bouton(bloc).listeners.click();
  assert.match(statut(bloc).textContent, /Sélectionnez le texte/);
  assert.doesNotMatch(statut(bloc).textContent, /Prompt copié/);
  assert.equal(bouton(bloc).disabled, false, 'Une nouvelle tentative reste possible');
  assert.equal(bloc.querySelector('pre').textContent, texteAvant);
});

test('navigateur sans API clipboard : le texte reste disponible pour copie manuelle', async () => {
  const [bloc] = charger(undefined);
  await bouton(bloc).listeners.click();
  assert.match(statut(bloc).textContent, /copiez-le manuellement/);
  assert.equal(bouton(bloc).disabled, false);
});

test('aucun faux succès avant résolution, statut propre à chaque extrait', async () => {
  let terminer;
  const blocs = charger({ writeText: () => new Promise(resolve => { terminer = resolve; }) });
  const enCours = bouton(blocs[0]).listeners.click();
  assert.equal(bouton(blocs[0]).disabled, true);
  assert.equal(statut(blocs[0]).textContent, '');
  assert.equal(statut(blocs[1]).textContent, '');
  assert.equal(statut(blocs[0]).attrs['aria-live'], 'polite');
  terminer();
  await enCours;
  assert.match(statut(blocs[0]).textContent, /Prompt copié/);
  assert.equal(statut(blocs[1]).textContent, '');
  assert.equal(bouton(blocs[0]).disabled, false);
});
