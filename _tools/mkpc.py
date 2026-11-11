#!/usr/bin/env python3
"""Genera index.html (versión de ordenador) a partir de la web del móvil (~/topdetail/index.html).
Mismo contenido, textos, menú, animaciones y tutorial; cambia el escenario (fotos 16:9 a pantalla completa) y la colocación.
Volver a ejecutarlo cada vez que cambie la del móvil:  python3 _tools/mkpc.py"""
import os
SRC = os.path.expanduser('~/topdetail/index.html'); OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'index.html')
s = open(SRC, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90]); s = s.replace(old, new)

CSS = r'''
/* ══════════ Versión de ordenador (generada con _tools/mkpc.py; no editar aquí) ══════════
   Escenario a pantalla completa con fotos 16:9, ficha grande abajo a la izquierda, opciones a la derecha,
   menú en cápsula abajo en el centro y las páginas de información en un panel lateral. */
.phone { width: 100%; height: 100%; }
#phone button, #phone summary { cursor: pointer; }
#phone .layer, #phone .seq {
  inset: 0; top: 0; left: 0; width: 100%; height: 100%; -webkit-mask-image: none; mask-image: none;
  translate: var(--px, 0px) var(--py, 0px); scale: 1.04; transition: translate .9s cubic-bezier(.2,.8,.2,1), scale 1.1s cubic-bezier(.2,.8,.2,1);
}
/* Dentro de un servicio la cámara se acerca y se va a la derecha: deja sitio a la ficha */
#phone.in-cat .layer, #phone.in-cat .seq { scale: 1.13; translate: calc(5.5cqw + var(--px, 0px)) var(--py, 0px); }
#phone .shade {
  background:
    radial-gradient(120% 90% at 50% 45%, rgba(0,0,0,0) 55%, rgba(0,0,0,.55) 100%),
    linear-gradient(to bottom, rgba(0,0,0,.62) 0, rgba(0,0,0,0) 20%),
    linear-gradient(to top, rgba(3,3,4,.9) 0, rgba(3,3,4,.5) 16%, rgba(3,3,4,0) 34%);
  transition: background .6s;
}
#phone.in-cat .shade {
  background:
    linear-gradient(to right, rgba(3,3,4,.86) 0, rgba(3,3,4,.55) 24%, rgba(3,3,4,0) 46%),
    linear-gradient(to left, rgba(3,3,4,.6) 0, rgba(3,3,4,0) 20%),
    linear-gradient(to bottom, rgba(0,0,0,.62) 0, rgba(0,0,0,0) 20%),
    linear-gradient(to top, rgba(3,3,4,.8) 0, rgba(3,3,4,0) 30%);
}
/* Cabecera */
#phone .top { padding: 22px 44px; }
#phone .logo img { height: 66px; }
#phone .where { grid-column: 1; grid-row: 1; justify-self: start; font: 400 11px/1 var(--ui); letter-spacing: .42em; text-transform: uppercase; color: rgba(233,220,199,.72); transition: opacity .5s; }
#phone.loading .where, #phone.in-cat .where, #phone.in-serv .where { opacity: 0; }
#phone .cita { padding: 15px 24px; font-size: 12px; letter-spacing: .2em; transition: opacity .5s, filter .25s, transform .25s; }
#phone .cita:hover { filter: brightness(1.15); transform: translateY(-1px); }
#phone .back { top: 34px; left: 44px; height: 46px; padding: 0 22px 0 14px; font-size: 12px; }
#phone .back:hover { background: rgba(233,220,199,.12); }
/* Menú */
#phone .side.l, #phone .side.s { bottom: calc(34px + env(safe-area-inset-bottom, 0px)); gap: 16px; }
#phone .side .dock { padding: 8px; gap: 4px; }
#phone .side.l .dock button, #phone .side.s .dock button { width: 124px; height: 76px; font-size: 11.5px; letter-spacing: .16em; gap: 7px; transition: background .25s, color .25s, transform .25s; }
#phone .side .dock button small { font-size: 9.5px; }
#phone .side .dock svg { width: 26px; height: 26px; }
#phone .side.l .dock button.star { width: 108px; height: 108px; margin: -36px 8px 0; font-size: 12px; }
#phone .side.l .dock button.star svg { width: 30px; height: 30px; }
#phone .side .dock button:not(.star):hover { background: rgba(233,220,199,.1); color: #fff; }
#phone .side.l .dock button.star:hover { filter: brightness(1.15); transform: scale(1.04); }
#phone .side.s .dock button { width: 132px; }
#phone .side.l .links { gap: 10px; }
#phone .side.l .links button { height: 42px; padding: 0 20px; font-size: 11px; letter-spacing: .2em; transition: background .25s, border-color .25s, color .25s; }
#phone .side.l .links button:hover { background: rgba(233,220,199,.12); border-color: rgba(233,220,199,.5); color: #fff; }
/* Ficha: abajo a la izquierda; en el menú de servicios, centrada sobre el menú */
#phone .hud { inset: auto auto 36px 36px; width: min(560px, 40cqw); padding: 26px 28px 24px; gap: 8px; border-radius: 30px; }
#phone h1 { font-size: clamp(38px, 3.9cqw, 64px); line-height: 1; gap: 6px 16px; }
#phone .eyebrow { font-size: 11px; letter-spacing: .36em; }
#phone .desc { font-size: clamp(16px, 1.25cqw, 19px); max-width: none; margin-top: 6px; }
#phone .price { font-size: 16px; margin-top: 6px; }
#phone .price .k { font-size: 24px; }
#phone .spec { gap: 7px; margin-top: 10px; }
#phone .spec li { font-size: 11px; padding: 7px 13px 6px; letter-spacing: .12em; }
#phone .tag { font-size: 12px; padding: 6px 12px 5px; }
#phone .ab { margin-top: 20px; max-width: 400px; }
#phone .ab button { height: 46px; font-size: 11.5px; transition: background .25s, color .25s; }
#phone .ab button:not([aria-pressed="true"]):hover { color: #fff; }
#phone .glass { margin-top: 20px; max-width: 420px; }
#phone .add { max-width: 400px; height: 46px; margin-top: 10px; }
#phone .add:hover { background: rgba(233,220,199,.14); }
#phone .add.on:hover { background: var(--red); filter: brightness(1.15); }
#phone .more { height: 36px; padding: 0 12px 0 16px; font-size: 10.5px; transition: background .25s; }
#phone .more:hover { background: rgba(233,220,199,.18); }
#phone.in-serv .hud { inset: 128px auto auto 50%; translate: -50% 0; width: max-content; max-width: 90%; justify-items: center; text-align: center; padding: 22px 40px 20px; }
#phone.in-serv .desc { text-shadow: 0 1px 12px #000; }
#phone.in-serv .hud .row { justify-content: center; gap: 18px; }
#phone.in-serv .hud .eyebrow { flex: none; }
#phone.in-serv h1 { justify-content: center; }
/* Opciones: columna a la derecha */
#phone .xside.l { right: 44px; top: 118px; gap: 8px; max-height: calc(100cqh - 118px - 48px); padding: 8px 4px 8px 12px; }
#phone .xside.l p { font-size: 10px; letter-spacing: .36em; margin: 10px 4px 2px 0; }
#phone .xside button { min-width: 176px; min-height: 44px; padding: 8px 20px; font-size: 11px; letter-spacing: .18em; transition: background .25s, border-color .25s, transform .25s; }
#phone .xside button:not([aria-current="true"]):hover { background: rgba(233,220,199,.14); border-color: rgba(233,220,199,.5); transform: translateX(-3px); }
#phone .xside button .badge { font-size: 8px; padding: 3px 7px 2px; top: -8px; right: -6px; }
/* Tutorial: la cápsula, abajo en el centro (sobre el menú cuando lo hay) */
#phone .island { bottom: calc(232px + env(safe-area-inset-bottom, 0px)); min-height: 52px; padding-left: 20px; }
#phone.in-serv .island { bottom: calc(150px + env(safe-area-inset-bottom, 0px)); }
#phone.in-cat .island { bottom: calc(44px + env(safe-area-inset-bottom, 0px)); }
#phone .island.tip { padding: 12px 22px; }
#phone .isl-t { font-size: 14px; }
/* Páginas de información: panel lateral sobre el escenario oscurecido */
.scrim { position: absolute; inset: 0; z-index: 5; background: rgba(0,0,0,.52); -webkit-backdrop-filter: blur(5px); backdrop-filter: blur(5px); opacity: 0; pointer-events: none; transition: opacity .35s; }
.sheet-open .scrim { opacity: 1; pointer-events: auto; }
#phone .sheet {
  inset: 0 0 0 auto; width: min(620px, 100%); padding-left: 40px; padding-right: 40px;
  border-left: 1px solid rgba(233,220,199,.16); box-shadow: -50px 0 90px rgba(0,0,0,.6);
  background: linear-gradient(to bottom, rgba(10,8,8,.94), rgba(6,5,5,.98) 26%);
  transform: translateX(60px);
}
#phone .sheet.open { transform: none; }
#phone .sheet-head { padding-top: 26px; }
#phone .sheet h2 { font-size: 24px; }
#phone .close:hover, #phone .btn:hover { filter: brightness(1.25); }
#phone .rail { margin: 0 -40px; padding: 4px 40px 14px; overflow-x: auto; scrollbar-width: thin; }
#phone .rail > * { flex: 0 0 58%; }
#phone .hero { min-height: 250px; }
/* Bienvenida */
#phone .loader { inset: auto auto 0 50%; width: min(460px, 90%); transform: translateX(-50%); padding: 0 0 30px; gap: 6px; }
#phone .loader.done { transform: translate(-50%, -36px); }
#phone .brand { width: 250px; max-width: 100%; }
#phone .welcome { margin-bottom: 0; }
#phone .hello { font-size: 12px; }
/* Pantallas bajas: opciones más compactas. Pantallas grandes: toda la interfaz crece en proporción */
@media (max-height: 860px) { #phone .xside.l { gap: 6px; } #phone .xside button { min-height: 38px; padding: 6px 18px; } #phone .xside.l p { margin-top: 6px; } }
@media (min-width: 1700px) and (min-height: 900px) { #phone .top, #phone .side, #phone .hud, #phone .xside, #phone .back, #phone .island, #phone .loader { zoom: 1.2; } #phone .sheet { zoom: 1.12; } }
@media (min-width: 2300px) and (min-height: 1200px) { #phone .top, #phone .side, #phone .hud, #phone .xside, #phone .back, #phone .island, #phone .loader { zoom: 1.5; } #phone .sheet { zoom: 1.35; } }
@media (prefers-reduced-motion: reduce) { #phone .layer, #phone .seq { translate: none; transition: none; } }
'''
rep('</style>\n</head>', CSS + '</style>\n<script>\n// En un móvil en vertical, mejor la web hecha para móvil\nif (innerWidth < 700 && innerHeight > innerWidth) location.replace(\'https://topdetail.puntozerosl.es/\');\n</script>\n</head>')
rep('<title>Top Detail Garage</title>', '<title>Top Detail Garage</title>\n<!-- Versión de ordenador: generada con _tools/mkpc.py a partir de ~/topdetail/index.html -->')

# ── HTML ──
rep('      <button class="logo" id="logo"', '      <span class="where">Fernán Núñez · Córdoba</span>\n      <button class="logo" id="logo"')
rep('    <section class="sheet" id="sheet"', '    <div class="scrim" id="scrim"></div>\n    <section class="sheet" id="sheet"')
rep('<b>Desliza hacia arriba</b><span>para comenzar a ver todos nuestros servicios</span>', '<b>Haz clic para entrar</b><span>y descubre todos nuestros servicios</span>')

# ── JS ──
# Fotos: 1920×1080 con la foto original del móvil (1080 px de ancho) en el centro
rep("  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;",
    "  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;\n  const PC = { w: 1920, h: 1080, photo: 1080 };   // medidas de las fotos de ordenador y ancho de la foto original dentro de ellas")
# Vídeos de Veo: los del móvil son verticales; hasta tener los horizontales, las transiciones son fundidos y animaciones por código
rep("  const VIDEO = true;", "  const VIDEO = false;   // ORDENADOR: faltan los clips horizontales (vid/p_, t_, c_, e_ en 16:9); al tenerlos, poner true")
# Tamaño de las herramientas: en proporción a la foto original, no al ancho de la pantalla
rep("    const c = { W, H, top, tx, dpr: W / phone.clientWidth, dm,", "    const c = { W, H, PW: PC.photo * Math.max(W / PC.w, H / PC.h), top, tx, dpr: W / phone.clientWidth, dm,")
rep("      const k = W / 720 * (o.scale || 1);", "      const k = c.PW / 720 * (o.scale || 1);")
rep("      const r = Math.max(W * .075, Math.min(W * .15, Math.min(bw, bh) * .26));", "      const r = Math.max(c.PW * .075, Math.min(c.PW * .15, Math.min(bw, bh) * .26));")
rep("      const k = W * .17 / BRU.bw,", "      const k = c.PW * .17 / BRU.bw,")
# Panel lateral: el fondo oscurecido lo cierra
rep("    sheet.inert = false; sheet.classList.add('open'); sheet.scrollTop = 0;", "    sheet.inert = false; sheet.classList.add('open'); phone.classList.add('sheet-open'); sheet.scrollTop = 0;")
rep("    sheet.classList.remove('open'); sheet.inert = true;", "    sheet.classList.remove('open'); phone.classList.remove('sheet-open'); sheet.inert = true;")
rep("  $('sheet-x').onclick = closeSheet;", """  $('sheet-x').onclick = closeSheet;
  $('scrim').onclick = closeSheet;
  // Paralaje: el escenario se mueve un poco con el ratón (no durante el comparador de la cera)
  if (!reduce && matchMedia('(pointer: fine)').matches) phone.addEventListener('pointermove', e => {
    if (sliding) { phone.style.setProperty('--px', '0px'); phone.style.setProperty('--py', '0px'); return; }
    const r = phone.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
    phone.style.setProperty('--px', (-x * r.width * .018).toFixed(1) + 'px'); phone.style.setProperty('--py', (-y * r.height * .014).toFixed(1) + 'px');
  });""")
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'land_patch.py'), encoding='utf-8').read())
open(OUT, 'w', encoding='utf-8').write(s); print('ok', len(s))
