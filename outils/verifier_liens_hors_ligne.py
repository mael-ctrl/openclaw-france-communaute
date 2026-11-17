#!/usr/bin/env python3
"""Vérifier href/src et fragments d'un site local UTF-8, sans réseau (stdlib POSIX)."""
import argparse
from html.parser import HTMLParser
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
from urllib.parse import unquote, urlsplit

HTML_EXTENSIONS = {'.html', '.htm'}
DEFAULTS = {'files': 10000, 'bytes': 20000000, 'page_bytes': 2000000,
            'links': 100000, 'depth': 32}
CAPS = {'files': 50000, 'bytes': 128000000, 'page_bytes': 4000000,
        'links': 200000, 'depth': 64}
LIMITS = [
    'HTML UTF-8 statique seulement ; HTMLParser, pas un navigateur ni un validateur HTML.',
    'href/src uniquement ; pas CSS url(), srcset, poster, action, srcdoc, JS, XML, Markdown ou JSON-LD.',
    'Aucun réseau, DNS, mail, paiement, redirection serveur, réécriture extensionless ou exécution de script.',
    'Hôte explicite unique ; autres hôtes/ports et schémas exemptés, jamais contactés.',
    'Query ignorée pour le fichier ; décodage percent UTF-8 unique, entités HTML décodées par le parseur uniquement.',
    'Fragments non HTML et directives texte exemptés après contrôle du fichier ; pas de preuve de leur validité.',
    'base[href] rend la page non vérifiable ; contenu template inerte exempté.',
    'Tous symlinks refusés, y compris internes et composants de la racine ; fichiers spéciaux refusés.',
    'Snapshot local immobile requis ; pas une garantie contre un écrivain hostile, montages ou hardlinks.',
    'Existence locale, pas disponibilité HTTP, SEO, accessibilité, performance ou qualité éditoriale.',
]


class Problem(ValueError):
    pass


class Budget(Problem):
    def __init__(self, dimension):
        super().__init__('budget_exceeded')
        self.dimension = dimension


class Document(HTMLParser):
    # RCDATA : nous ne lisons pas le texte, seulement les vraies balises.
    TEXT_ELEMENTS = ('script', 'style', 'title', 'textarea')

    def handle_startendtag(self, tag, attrs):
        # En HTML, le slash ne ferme pas ces éléments non void.
        if tag in self.TEXT_ELEMENTS or tag == 'template':
            self.handle_starttag(tag, attrs)
        else:
            super().handle_startendtag(tag, attrs)

    def __init__(self, text, consume_link):
        super().__init__(convert_charrefs=True)
        self.ids, self.refs = set(), []
        self.base_line = None
        self.template_depth = 0
        self.consume_link = consume_link
        self.feed(text)
        self.close()

    def handle_starttag(self, tag, attrs):
        if tag in self.TEXT_ELEMENTS:
            self.set_cdata_mode(tag)
        if tag == 'template':
            self.template_depth += 1
        for key, value in attrs:
            if tag == 'base' and key == 'href' and not self.template_depth:
                self.base_line = self.getpos()[0]
            if not self.template_depth and (key == 'id' or (tag == 'a' and key == 'name')) and value:
                self.ids.add(value)
            if key in ('href', 'src') and value is not None:
                self.consume_link()
                self.refs.append({'line': self.getpos()[0], 'tag': tag,
                                  'attribute': key, 'url': value,
                                  'inert': bool(self.template_depth)})

    def handle_endtag(self, tag):
        if tag == 'template' and self.template_depth:
            self.template_depth -= 1


def decode(value):
    if re.search(r'%(?![0-9a-fA-F]{2})', value):
        raise Problem('invalid_encoding')
    try:
        return unquote(value, encoding='utf-8', errors='strict')
    except UnicodeError:
        raise Problem('invalid_encoding') from None


def resolve_url(value, source, host):
    value = value.strip(' \t\r\n\f')
    if any(ord(c) < 32 or ord(c) == 127 for c in value) or '\\' in value or value.startswith('///'):
        raise Problem('invalid_url')
    try:
        url = urlsplit(value)
        port = url.port
    except ValueError:
        raise Problem('invalid_url') from None
    if url.scheme and url.scheme not in ('http', 'https'):
        return None, 'scheme', None
    if url.netloc or url.scheme:
        if not url.hostname or url.username is not None or url.password is not None:
            raise Problem('invalid_url')
        if url.hostname.lower() != host:
            return None, 'external_host', None
        if port is not None and port != (80 if url.scheme == 'http' else 443):
            return None, 'external_port', None
    path, fragment = decode(url.path), decode(url.fragment)
    if any(ord(c) < 32 or ord(c) == 127 for c in path + fragment) or '\\' in path:
        raise Problem('invalid_url')
    if not path:
        path = '/' if url.netloc else '/' + source
    stack = [] if path.startswith('/') else list(PurePosixPath(source).parent.parts)
    for part in path.split('/'):
        if part in ('', '.'):
            continue
        if part == '..':
            if not stack:
                raise Problem('outside_root')
            stack.pop()
        else:
            stack.append(part)
    return '/'.join(stack), None, (url.fragment, fragment, path.endswith('/'))


def open_root(root):
    """Open each component without symlink resolution or ancestor file reads."""
    if os.name != 'posix' or not hasattr(os, 'O_NOFOLLOW'):
        raise Problem('unsupported_platform')
    parts = (Path.cwd() / root).parts
    if '..' in parts:
        raise Problem('unsafe_root')
    fd = os.open('/', os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        for part in parts[1:]:
            child = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = child
        return fd
    except OSError:
        os.close(fd)
        raise Problem('unsafe_root') from None


def snapshot(root, budgets):
    """Index lexical paths: URL targets are NEVER passed to file I/O."""
    pages, entries, errors = {}, {'': 'directory'}, []
    used = {'files': 0, 'bytes': 0, 'links': 0}

    def consume_link():
        used['links'] += 1
        if used['links'] > budgets['links']:
            raise Budget('links')

    def walk(fd, parent, depth):
        if depth > budgets['depth']:
            raise Budget('depth')
        names = []
        # Bound the listing itself, not merely the processing after listdir().
        with os.scandir(fd) as iterator:
            for entry in iterator:
                used['files'] += 1
                if used['files'] > budgets['files']:
                    raise Budget('files')
                names.append(entry.name)
        for name in sorted(names):
            path = parent + '/' + name if parent else name
            try:
                info = os.stat(name, dir_fd=fd, follow_symlinks=False)
                if stat.S_ISLNK(info.st_mode):
                    entries[path] = 'symlink_refused'
                    raise Problem('symlink_refused')
                if stat.S_ISDIR(info.st_mode):
                    entries[path] = 'directory'
                    child = os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
                    try:
                        walk(child, path, depth + 1)
                    finally:
                        os.close(child)
                elif stat.S_ISREG(info.st_mode):
                    entries[path] = 'file'
                    if PurePosixPath(name).suffix.lower() in HTML_EXTENSIONS:
                        if info.st_size > budgets['page_bytes']:
                            raise Budget('page_bytes')
                        if used['bytes'] + info.st_size > budgets['bytes']:
                            raise Budget('bytes')
                        child = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=fd)
                        with os.fdopen(child, 'rb') as stream:
                            current = os.fstat(stream.fileno())
                            if not stat.S_ISREG(current.st_mode) or (info.st_dev, info.st_ino) != (current.st_dev, current.st_ino):
                                raise Problem('changed_during_scan')
                            ceiling = min(budgets['page_bytes'], budgets['bytes'] - used['bytes'])
                            raw = stream.read(ceiling + 1)
                            if len(raw) > ceiling:
                                raise Budget('bytes')
                            final = os.fstat(stream.fileno())
                            if (current.st_size, current.st_mtime_ns) != (final.st_size, final.st_mtime_ns):
                                raise Problem('changed_during_scan')
                        used['bytes'] += len(raw)
                        pages[path] = Document(raw.decode('utf-8'), consume_link)
                else:
                    entries[path] = 'special_file'
                    raise Problem('special_file')
            except Budget:
                raise
            except Problem as exc:
                errors.append({'source': path, 'code': str(exc)})
            except UnicodeError:
                errors.append({'source': path, 'code': 'html_encoding'})
            except OSError:
                errors.append({'source': path, 'code': 'unreadable_or_changed'})

    try:
        fd = open_root(root)
        try:
            walk(fd, '', 1)
        finally:
            os.close(fd)
    except Budget as exc:
        errors.append({'source': '.', 'code': str(exc), 'dimension': exc.dimension})
    except Problem as exc:
        errors.append({'source': '.', 'code': str(exc)})
    except OSError:
        errors.append({'source': '.', 'code': 'unreadable_or_changed'})
    if not pages and not errors:
        errors.append({'source': '.', 'code': 'no_html'})
    return pages, entries, errors, used


def check(root, host, budgets=None):
    budgets = dict(DEFAULTS if budgets is None else budgets)
    pages, entries, errors, used = snapshot(root, budgets)
    complete = not errors
    exemptions = []
    checked = references = 0
    for source, doc in sorted(pages.items()):
        if doc.base_line is not None:
            errors.append({'source': source, 'line': doc.base_line, 'code': 'base_unsupported'})
            complete = False
        for ref in doc.refs:
            references += 1
            entry = {'source': source, **{k: v for k, v in ref.items() if k != 'inert'}}
            if ref['inert'] or doc.base_line is not None:
                exemptions.append({**entry, 'code': 'inert_template' if ref['inert'] else 'base_unsupported'})
                continue
            try:
                target, exempt, fragment_data = resolve_url(ref['url'], source, host)
                if exempt:
                    exemptions.append({**entry, 'code': exempt})
                    continue
                checked += 1
                raw_fragment, fragment, trailing_slash = fragment_data
                parts = target.split('/') if target else []
                for i in range(1, len(parts) + 1):
                    status = entries.get('/'.join(parts[:i]))
                    if status in ('symlink_refused', 'special_file'):
                        raise Problem(status)
                if trailing_slash or entries.get(target) == 'directory':
                    target = (PurePosixPath(target) / 'index.html').as_posix()
                entry['target'] = target
                status = entries.get(target)
                if status in ('symlink_refused', 'special_file'):
                    raise Problem(status)
                if status != 'file':
                    raise Problem('missing_target')
                if fragment:
                    entry['fragment'] = fragment
                    if PurePosixPath(target).suffix.lower() not in HTML_EXTENSIONS:
                        exemptions.append({**entry, 'code': 'non_html_fragment'})
                    elif target not in pages:
                        raise Problem('target_html_unchecked')
                    elif ':~:' in raw_fragment:
                        exemptions.append({**entry, 'code': 'text_fragment'})
                    elif raw_fragment not in pages[target].ids and fragment not in pages[target].ids and fragment.lower() != 'top':
                        raise Problem('missing_fragment')
            except Problem as exc:
                errors.append({**entry, 'code': str(exc)})
    return {'schema': 1, 'canonical_host': host, 'complete': complete,
            'stats': {'html_files': len(pages), 'references': references, 'checked': checked,
                      'errors': len(errors), 'exemptions': len(exemptions),
                      'entries_seen': used['files'], 'html_bytes': used['bytes']},
            'budgets': budgets, 'limits': LIMITS, 'errors': errors, 'exemptions': exemptions}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', type=Path, help='copie locale immobile du site publié')
    parser.add_argument('--canonical-host', required=True, help='hôte DNS ASCII sans schéma ni port')
    for key, default in DEFAULTS.items():
        parser.add_argument('--max-' + key.replace('_', '-'), type=int, default=default)
    args = parser.parse_args()
    host = args.canonical_host.lower()
    if len(host) > 253 or not re.fullmatch(r'[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(?:\.[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)*', host) or any(len(label) > 63 for label in host.split('.')):
        parser.error('--canonical-host attend un nom DNS ASCII explicite, sans schéma, port ni chemin')
    budgets = {key: getattr(args, 'max_' + key) for key in DEFAULTS}
    for key, value in budgets.items():
        if not 1 <= value <= CAPS[key]:
            parser.error('--max-' + key.replace('_', '-') + ' attendu entre 1 et ' + str(CAPS[key]))
    report = check(args.root, host, budgets)
    print(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2))
    return 1 if report['errors'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
