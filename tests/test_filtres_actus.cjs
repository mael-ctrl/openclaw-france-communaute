/* Contrats du vrai app.js ; DOM minimal, clavier natif testé au navigateur. */
const {test} = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

function element(attrs = {}, hidden = false) {
  const classes = new Set((attrs.class || '').split(' ').filter(Boolean));
  return {hidden, value: '', textContent: '', handlers: {},
    getAttribute: name => attrs[name] ?? null,
    setAttribute: (name, value) => { attrs[name] = String(value); },
    classList: {add: v => classes.add(v), remove: v => classes.delete(v),
      contains: v => classes.has(v), toggle: (v, on) => on ? classes.add(v) : classes.delete(v)},
    addEventListener(event, fn) { this.handlers[event] = fn; },
    fire(event) { this.handlers[event](); },
  };
}
function mount({empty = false, restored = ''} = {}) {
  const cards = empty ? [] : [
    element({'data-tags': 'IA', 'data-texte': 'alpha modèle'}),
    element({'data-tags': 'Robot', 'data-texte': 'beta robot'}),
    element({'data-tags': 'IA,Robot', 'data-texte': 'gamma robot'}),
  ];
  const buttons = ['', 'IA', 'Robot'].map(tag => element({'data-tag': tag, 'aria-pressed': 'false', class: 'filtre'}));
  const ids = {'outils-actus': element({}, true), 'recherche': element(),
    'aucun-resultat': element({}, true), 'resultats-actus': element(),
    'liste-actus': {querySelectorAll: () => cards}};
  ids.recherche.value = restored;
  let ready;
  let clock = 0;
  let id = 0;
  const timers = new Map();
  const context = {
    document: {getElementById: n => ids[n] || null, querySelectorAll: () => buttons,
      querySelector: () => null, addEventListener: (_, fn) => { ready = fn; }},
    window: {setTimeout: (fn, delay) => {timers.set(++id, {fn, at: clock + delay}); return id;},
      clearTimeout: id => timers.delete(id)},
  };
  vm.runInNewContext(fs.readFileSync(path.join(__dirname, '../assets/app.js'), 'utf8'), context);
  ready();
  return {cards, buttons, ids, timers,
    tick(ms) {clock += ms; for (const [id, timer] of [...timers]) if (timer.at <= clock) {timers.delete(id); timer.fn();}},
    input(value) {ids.recherche.value = value; ids.recherche.fire('input');},
    visible() {return cards.filter(c => !c.hidden).length;},
  };
}

test('montage : outils révélés et Tout seul pressé ; changement de tag synchronisé', () => {
  const h = mount();
  assert.equal(h.ids['outils-actus'].hidden, false);
  const selected = index => h.buttons.forEach((b, i) => {
    assert.equal(b.getAttribute('aria-pressed'), String(i === index));
    assert.equal(b.classList.contains('actif'), i === index);
  });
  selected(0);
  h.buttons[1].fire('click'); selected(1); assert.equal(h.visible(), 2);
  h.buttons[2].fire('click'); selected(2); assert.equal(h.visible(), 2);
  h.buttons[0].fire('click'); selected(0); assert.equal(h.visible(), 3);
  assert.equal(mount({empty: true}).ids['outils-actus'].hidden, true);
});

test('statut local : silencieux au montage, annonce après interaction et zéro puis retour', () => {
  const h = mount();
  const status = h.ids['resultats-actus'];
  h.tick(1000); assert.equal(status.textContent, '');
  h.buttons[1].fire('click'); h.tick(0);
  assert.equal(status.textContent, '2 résultats sur cette page.');
  h.input('  ALpHa  '); h.tick(249);
  assert.equal(h.visible(), 1);
  assert.equal(status.textContent, '2 résultats sur cette page.');
  h.tick(1); assert.equal(status.textContent, '1 résultat sur cette page.');
  h.input('absent'); h.tick(250);
  assert.equal(h.visible(), 0); assert.equal(h.ids['aucun-resultat'].hidden, false);
  assert.equal(status.textContent, '0 résultat sur cette page.');
  h.input('  '); h.tick(250);
  assert.equal(h.visible(), 2); assert.equal(h.ids['aucun-resultat'].hidden, true);
  h.buttons[0].fire('click'); h.tick(0);
  assert.equal(status.textContent, '3 résultats sur cette page.');
});

test('saisie rapide : une annonce finale ; clic annule toute annonce obsolète', () => {
  const h = mount();
  h.input('a'); h.tick(100); h.input('alpha'); h.tick(100); h.input('beta');
  assert.equal(h.timers.size, 1);
  h.buttons[1].fire('click'); h.tick(0);
  assert.equal(h.ids['resultats-actus'].textContent, '0 résultat sur cette page.');
  h.tick(1000);
  assert.equal(h.ids['resultats-actus'].textContent, '0 résultat sur cette page.');
  assert.equal(h.timers.size, 0);
});

test('valeur restaurée au montage : filtre cohérent sans annonce automatique', () => {
  const h = mount({restored: '  ALpHa  '});
  assert.equal(h.visible(), 1);
  h.tick(1000);
  assert.equal(h.ids['resultats-actus'].textContent, '');
});
