#!/usr/bin/env python3
"""Fotos de ordenador (1920×1080) a partir de las del móvil (~/topdetail/img, 1080×1935).
Cada «grupo» de fotos con el mismo encuadre comparte un fondo: del móvil se toma una franja cuadrada de 1080 px
(la que contiene lo que cambia) y los lados los pinta Gemini (outpainting, una vez por grupo, _tools/fondos/<grupo>.jpeg).
Luego el centro ORIGINAL de cada foto se pega encima con un fundido, así antes y después siguen calcando.
  pc.py lienzos   → _tools/lienzos/<grupo>.jpg (centro + franjas verdes) y _tools/grupos.json
  pc.py montar    → img/<foto>.webp (con el fondo de Gemini si existe; si no, relleno provisional de espejo desenfocado)
"""
import sys, os, json, glob
from PIL import Image, ImageChops, ImageFilter, ImageOps
SRC = os.path.expanduser('~/topdetail/img/')
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
W, H, S = 1920, 1080, 1080; X0 = (W - S) // 2
def band(d, n):
    """Franja de la foto n del grupo d, escalada a la altura del lienzo (hb = alto de la franja en la foto del móvil)."""
    hb = d.get('hb', S); w = round(S * H / hb)
    return load(n).crop((0, d['y0'], S, d['y0'] + hb)).resize((w, H), Image.LANCZOS)
def load(n): return Image.open(f'{SRC}{n}.webp').convert('RGB').resize((1080, 1935), Image.LANCZOS)
G = {  # grupo: (fotos, foto del centro del lienzo, y0 o None = automático)
  'coche': (['00-base_porsche_limpio', '01-intro_porsche_sucio', '06-limpieza_basico', '06-limpieza_premium', '06-limpieza_integral', '04-ceramica_mantenimiento'], '00-base_porsche_limpio', 400, 1300),
  'perfil': (['02-tintado_lunas_sin', '02-tintado_lunas_50', '02-tintado_lunas_30', '02-tintado_lunas_5'], '02-tintado_lunas_sin', 400, 1300),
  'macro': (['03-correccion_pintura_swirls', '03-correccion_pintura_1paso', '03-correccion_pintura_2pasos', '04-ceramica_perlado'], '03-correccion_pintura_2pasos', None),
}
for f in sorted(glob.glob(SRC + '05-extras_*_antes.webp')):
    a = os.path.basename(f)[:-5]; b = a[:-5] + 'despues'
    G[a.split('_')[2]] = ([a, b], b, None)
def auto_y0(names):
    """Franja centrada en lo que cambia entre las fotos del grupo (centroide de la diferencia)."""
    ims = [load(n).convert('L').resize((108, 194)) for n in names]
    rows = [0.0] * 194
    for im in ims[1:]:
        d = ImageChops.difference(ims[0], im); px = d.load()
        for y in range(194):
            rows[y] += sum(v for v in (px[x, y] for x in range(108)) if v > 18)
    tot = sum(rows) or 1
    cy = sum(y * r for y, r in enumerate(rows)) / tot * 10
    return int(max(0, min(1935 - S, cy - S / 2)))
def groups():
    out = {}
    for g, (names, c, y0, *hb) in G.items():
        out[g] = dict(fotos=names, centro=c, y0=auto_y0(names) if y0 is None else y0, hb=hb[0] if hb else S)
    return out
def lienzos():
    os.makedirs(f'{HERE}/lienzos', exist_ok=True)
    gs = groups(); json.dump(gs, open(f'{HERE}/grupos.json', 'w'), indent=1, ensure_ascii=False)
    for g, d in gs.items():
        c = Image.new('RGB', (W, H), (0, 255, 0))
        ce = band(d, d['centro']); c.paste(ce, ((W - ce.width) // 2, 0))
        c.save(f'{HERE}/lienzos/{g}.jpg', quality=95)
    print(len(gs), 'lienzos')
def mask(w, f=70):
    m = Image.new('L', (w, 1), 255); px = m.load()
    for x in range(f):
        v = int(255 * (x / f) ** 2 * (3 - 2 * x / f)); px[x, 0] = v; px[w - 1 - x, 0] = v
    return m.resize((w, H))
def provisional(center):
    """Sin fondo de Gemini todavía: los lados son el borde del centro en espejo, desenfocado y oscurecido."""
    c = Image.new('RGB', (W, H)); w = center.width; x0 = (W - w) // 2; m = ImageOps.mirror(center)
    for x in range(x0 - w, -w, -w): c.paste(m if ((x0 - x) // w) % 2 else center, (x, 0))
    for k, x in enumerate(range(x0 + w, W, w)): c.paste(center if k % 2 else m, (x, 0))
    c.paste(center, (x0, 0))
    b = c.filter(ImageFilter.GaussianBlur(22)).point(lambda v: int(v * .72))
    return b
def montar(only=None):
    gs = json.load(open(f'{HERE}/grupos.json')); os.makedirs(f'{ROOT}/img', exist_ok=True); rep = []
    for g, d in gs.items():
        if only and g not in only: continue
        f = next((p for p in (f'{HERE}/fondos/{g}.{e}' for e in ('jpeg', 'jpg', 'png')) if os.path.exists(p)), None)
        bg0 = Image.open(f).convert('RGB').resize((W, H), Image.LANCZOS) if f else None
        for n in d['fotos']:
            ce = band(d, n)
            bg = (bg0 or provisional(band(d, d['centro']))).copy()
            bg.paste(ce, ((W - ce.width) // 2, 0), mask(ce.width))
            bg.save(f'{ROOT}/img/{n}.webp', quality=88, method=5)
        rep.append(f"{g}:{'gemini' if f else 'provisional'}")
    print(' '.join(rep))
def comprobar(g):
    """¿Gemini ha respetado el centro? Diferencia media (0–255) entre el centro del lienzo y el del fondo generado."""
    d = json.load(open(f'{HERE}/grupos.json'))[g]
    f = next(p for p in (f'{HERE}/fondos/{g}.{e}' for e in ('jpeg', 'jpg', 'png')) if os.path.exists(p))
    im = Image.open(f).convert('RGB'); ar = im.width / im.height
    ce = band(d, d['centro']); x0 = (W - ce.width) // 2
    b = im.resize((W, H), Image.LANCZOS).crop((x0 + 80, 0, x0 + ce.width - 80, H)).resize((230, 270))
    a = ce.crop((80, 0, ce.width - 80, H)).resize((230, 270))
    h = ImageChops.difference(a, b).convert('L').histogram(); dif = sum(i * v for i, v in enumerate(h)) / sum(h)
    # ¿queda verde en los lados?
    side = im.resize((W, H)).crop((0, 0, x0 - 20, H)).resize((40, 108)); gr = sum(1 for r, g2, b2 in side.getdata() if g2 > 150 and g2 - max(r, b2) > 70) / (40 * 108)
    print(f'{g}: tamaño {im.size} (proporción {ar:.3f}, debe ser ~1.778) · diferencia del centro {dif:.1f} (bien < 12) · verde en el lado {gr:.0%} (debe ser 0 %)')
if __name__ == '__main__':
    a = sys.argv[1:]
    {'lienzos': lienzos, 'montar': lambda: montar(a[1:] or None), 'comprobar': lambda: [comprobar(g) for g in a[1:]]}[a[0]]()
