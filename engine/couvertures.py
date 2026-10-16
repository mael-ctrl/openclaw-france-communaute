"""Illustrations procédurales locales, sans photo, texte raster ni réseau."""
import hashlib
import io
import json
import os
import re
import tempfile
import unicodedata
from pathlib import Path

from PIL import Image, ImageDraw, __version__, features

LARGEUR, HAUTEUR = 1280, 720
VERSION = "1"
BUDGET = 120_000
THEMES = {
    "securite": (r"\b(securite|cyber\w*|faille\w*|pirat\w*|confidential\w*|voles)\b", "sécurité", "bouclier et verrou", "#f1b875"),
    "materiel": (r"\b(gpu\w*|vram|puce\w*|materiel|processeur\w*|nvidia|rtx)\b", "matériel", "puce et circuits", "#70dac1"),
    "robotique": (r"\b(robot\w*|humanoide\w*)\b", "robotique", "bras articulé symbolique", "#9ac5f7"),
    "agents": (r"\b(agent\w*|outil\w*|workflow\w*|automatisation)\b", "agents et outils", "modules reliés", "#b5a5ee"),
    "modeles": (r"\b(modele\w*|llm\w*|inference|langage|qwen\w*|llama\w*)\b", "modèles", "couches de calcul", "#f19a8d"),
    "generique": (r"", "réseau numérique (repli générique)", "réseau abstrait générique", "#87cbd1"),
}


def _theme(item):
    texte = " ".join([item.get("titre", ""), *(item.get("tags") or [])])
    texte = unicodedata.normalize("NFKD", texte).encode("ascii", "ignore").decode().lower()
    return next(nom for nom, (motif, *_) in THEMES.items() if re.search(motif, texte))


def _dessiner(cle, theme):
    """Motifs originaux par famille, jamais représentation d'un événement."""
    image = Image.new("RGB", (LARGEUR, HAUTEUR), "#101e2b")
    d = ImageDraw.Draw(image)
    accent = THEMES[theme][3]
    graine = bytes.fromhex(cle)
    # Cadre et satellites varient avec le contenu ; aucun graphe de données.
    d.ellipse((310, 25, 970, 685), outline="#213545", width=2)
    d.ellipse((350, 65, 930, 645), outline="#213545", width=1)
    for i in range(12):
        x = 65 + (i % 6) * 220 + graine[i] % 40
        y = 80 + (i // 6) * 510 + graine[16 + i] % 30
        d.line((x - 16, y, x + 16, y), fill="#385263", width=2)
        d.line((x, y - 16, x, y + 16), fill="#385263", width=2)
        d.ellipse((x - 3, y - 3, x + 3, y + 3), fill=accent)
    if theme == "materiel":
        d.rounded_rectangle((410, 155, 870, 565), radius=40, fill="#213a4c", outline=accent, width=5)
        for i in range(8):
            y = 195 + i * 46
            d.line((310, y, 408, y), fill=accent, width=7)
            d.line((872, y, 970, y), fill=accent, width=7)
        d.rounded_rectangle((515, 245, 765, 475), radius=15, fill=accent)
        for x in range(550, 750, 40):
            d.line((x, 280, x, 440), fill="#294451", width=3)
    elif theme == "securite":
        d.polygon([(640, 120), (865, 205), (840, 425), (770, 530), (640, 600),
                   (510, 530), (440, 425), (415, 205)], fill="#283e4e", outline=accent, width=6)
        d.arc((555, 220, 725, 420), 180, 360, fill=accent, width=16)
        d.rounded_rectangle((530, 325, 750, 475), radius=22, fill=accent)
        d.ellipse((625, 365, 655, 395), fill="#101e2b")
        d.line((640, 385, 640, 430), fill="#101e2b", width=10)
    elif theme == "robotique":
        d.rounded_rectangle((445, 540, 745, 575), radius=15, fill=accent)
        points = [(590, 540), (520, 345), (735, 210), (830, 320)]
        d.line(points, fill=accent, width=42, joint="curve")
        for x, y in points[:-1]:
            d.ellipse((x-34, y-34, x+34, y+34), fill="#243b4b", outline=accent, width=7)
        d.line([(830, 320), (800, 395), (835, 425)], fill=accent, width=15)
        d.line([(830, 320), (895, 350), (890, 395)], fill=accent, width=15)
    elif theme == "agents":
        for x, y in [(355, 230), (925, 230), (355, 490), (925, 490)]:
            d.line((x, y, 640, 360), fill="#597487", width=8)
            d.rounded_rectangle((x-80, y-60, x+80, y+60), radius=24, fill="#294352", outline=accent, width=3)
            d.ellipse((x-16, y-16, x+16, y+16), fill=accent)
        d.rounded_rectangle((535, 255, 745, 465), radius=36, fill=accent)
        d.line((590, 360, 630, 400, 690, 320), fill="#243346", width=12)
    elif theme == "modeles":
        for y in (455, 340, 225):
            d.polygon([(380, y+30), (640, y-85), (900, y+30), (640, y+145)],
                      fill="#263d4d", outline=accent, width=5)
        d.polygon([(520, 250), (640, 195), (760, 250), (640, 305)], fill=accent)
    else:
        points = [(380, 245), (640, 155), (890, 255), (850, 490), (570, 550), (420, 435)]
        for i, (x, y) in enumerate(points):
            d.line((x, y, 640, 350), fill="#496575", width=5)
            d.line([(x, y), points[(i+1) % len(points)]], fill="#294352", width=3)
        for x, y in points + [(640, 350)]:
            d.ellipse((x-33, y-33, x+33, y+33), fill=accent)
            d.ellipse((x-18, y-18, x+18, y+18), fill="#1e3547")
    return image


def verifier_chemin(chemin):
    """Refuse les liens symboliques existants, sans normaliser un slug."""
    chemin = Path(chemin).absolute()
    if any(p.is_symlink() for p in (chemin, *chemin.parents)):
        raise ValueError(f"Lien symbolique interdit : {chemin}")
    return chemin


def valider(item, genre):
    if genre not in ("breves", "articles"):
        raise ValueError("Genre éditorial inconnu")
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,199}", item.get("slug", "")):
        raise ValueError("Slug éditorial non sûr")


def _atomique(chemin, octets):
    verifier_chemin(chemin)
    with tempfile.NamedTemporaryFile(dir=chemin.parent, delete=False) as f:
        temporaire = Path(f.name)
        try:
            f.write(octets)
            f.close()
            os.replace(temporaire, chemin)
        finally:
            temporaire.unlink(missing_ok=True)


def generer(item, genre, cache):
    """Retourne les métadonnées d'un JPEG ; les données éditoriales sont intactes."""
    valider(item, genre)
    identite = json.dumps([VERSION, __version__, features.version_codec("jpg"),
                          features.version_feature("libjpeg_turbo"), genre, item],
                         ensure_ascii=False, sort_keys=True).encode()
    cle = hashlib.sha256(identite).hexdigest()
    cache = verifier_chemin(cache)
    cache.mkdir(parents=True, exist_ok=True)
    fichier, meta = cache / (cle + ".jpg"), cache / (cle + ".json")
    verifier_chemin(fichier)
    verifier_chemin(meta)
    theme = _theme(item)
    attendu = {"path": f"/assets/couvertures/{cle}.jpg", "width": LARGEUR, "height": HAUTEUR,
               "type": "image/jpeg", "theme": theme,
               "alt": "Illustration générée : " + THEMES[theme][2] + ".",
               "caption": "Illustration générée localement — " + THEMES[theme][1]
                          + ". Schéma symbolique, pas une photographie."}
    try:
        if meta.stat().st_size > 4096 or fichier.stat().st_size >= BUDGET:
            raise ValueError("Cache hors budget")
        info = json.loads(meta.read_text(encoding="utf-8"))
        octets = fichier.read_bytes()
        if (info["sha256"] == hashlib.sha256(octets).hexdigest()
                and info["bytes"] == len(octets) < BUDGET
                and {k: v for k, v in info.items() if k not in ("sha256", "bytes")} == attendu):
            with Image.open(io.BytesIO(octets)) as verification:
                if verification.format == "JPEG" and verification.size == (LARGEUR, HAUTEUR):
                    verification.load()
                    # Nom adressé par contenu : empreinte FTP stable même sans cache.
                    # Horodatage technique uniquement, jamais une date de publication.
                    if fichier.stat().st_mtime != 946684800:
                        os.utime(fichier, (946684800, 946684800))
                    return info
    except (OSError, ValueError, KeyError, TypeError):
        pass
    image = _dessiner(cle, theme)
    flux = io.BytesIO()
    image.save(flux, format="JPEG", quality=84, subsampling=0, optimize=True, progressive=False)
    octets = flux.getvalue()
    if len(octets) >= BUDGET:
        raise ValueError("Couverture hors budget")
    info = dict(attendu, bytes=len(octets), sha256=hashlib.sha256(octets).hexdigest())
    _atomique(fichier, octets)
    os.utime(fichier, (946684800, 946684800))  # asset immuable, pas une date éditoriale
    _atomique(meta, json.dumps(info, ensure_ascii=False, sort_keys=True).encode())
    return info
