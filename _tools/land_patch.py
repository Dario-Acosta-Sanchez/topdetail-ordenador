# Página larga bajo el escenario (lo ejecuta mkpc.py): las páginas de información dejan de ir en un panel
# y pasan a ser secciones a lo ancho; los botones del menú bajan hasta la suya.
T = os.path.dirname(os.path.abspath(__file__)) + '/'
rd = lambda n: open(T + n, encoding='utf-8').read()
rep('</style>\n<script>\n// En un móvil', rd('land.css') + '</style>\n<script>\n// En un móvil')
rep('    <nav class="xside l" id="opt-l"', '    <button class="down" id="down" type="button"><span>Desliza para más información</span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg><i aria-hidden="true"></i></button>\n    <nav class="xside l" id="opt-l"')
# Sin pantalla de «entrar»: al acabar la carga se entra sola (la rueda ya no arrastra la página nada más empezar)
rep("    S.onclick = go;\n", "    S.onclick = go;\n    setTimeout(go, reduce ? 0 : 650);\n")
rep('<script>\n(() => {', rd('land.html') + '<script>\n(() => {')
rep("pn.setAttribute('role', 'tabpanel'); pn.hidden = true; panels[t] = pn;", "pn.hidden = false; panels[t] = pn;")
rep("  $('sheet-cta').before(...TABS.map(t => panels[t]));\n", rd('land.js'))
a = s.index("  function openSheet(page, focusId) {"); b = s.index("  function closeSheet() {")
s = s[:a] + """  // Los botones de información bajan hasta su sección
  function openSheet(page, focusId) {
    if (loading) return;
    const el = (focusId && $(focusId)) || panels[page];
    if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
""" + s[b:]
a = s.index("  function showTab(t) {"); b = s.index("  showTab('nosotros');")
s = s[:a] + "  function showTab(t) { tab = 'contacto'; renderPicks(); }\n" + s[b:]
rep("    const [c, i] = b.dataset.go.split(':'); closeSheet(); play(c, +i);", "    const [c, i] = b.dataset.go.split(':'); scrollTo({ top: 0, behavior: 'smooth' }); play(c, +i);")
rep("  $('demo-btn').onclick = () => { closeSheet(); setTimeout(runDemo, 500); };", "  $('demo-btn').onclick = () => { scrollTo({ top: 0, behavior: 'smooth' }); setTimeout(runDemo, 900); };")
rep("{ root: sheet, rootMargin: '-38% 0px -38% 0px' }", "{ root: null, rootMargin: '-38% 0px -38% 0px' }")
rep("{ root: sheet, threshold: .25 }", "{ root: null, threshold: .15 }")
# La rueda baja por la página (el acercamiento con la rueda volverá con los vídeos horizontales)
rep("    if (e.target.closest && (e.target.closest('.xside') || e.target.closest('.sheet'))) return;\n    e.preventDefault();", "    return;   // ORDENADOR: la rueda baja por la página\n    e.preventDefault();")
# Los elementos ya no están dentro del panel: se buscan en todo el documento
s = s.replace("sheet.querySelectorAll('.reveal')", "document.querySelectorAll('.reveal')").replace("sheet.querySelectorAll('.steps li')", "document.querySelectorAll('.steps li')").replace("sheet.querySelectorAll('#teoria .acc')", "document.querySelectorAll('#teoria .acc')")
assert "sheet.querySelectorAll('.reveal')" not in s
# ── Tutorial de ordenador: puntero de ratón, textos de clic, un paso que enseña la información de abajo y botón para repetirlo ──
rep("      say('Empieza por Servicios', 1, N);", "      say('Haz clic en Servicios', 1, N);")
rep("      say('Elige uno: el pulido, por ejemplo', 2, N);", "      say('Elige un servicio: el pulido, por ejemplo', 2, N);")
rep("      say('Ahora te toca a ti');\n", """      say('Y abajo, toda la información y los precios', 6, N);
      await moveTo($('down'), 650);
      $('down').classList.add('pulse'); await sleep(1700); live();
      say('Ahora te toca a ti');
""")
rep("  function hint() { say('Empieza por Servicios');", "  function hint() { say('Haz clic en Servicios');")
rep('    <button class="down" id="down"', '    <button class="tuto" id="tuto" type="button"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5.5v13l11-6.5z"/></svg>Ver tutorial</button>\n    <button class="down" id="down"')
rep("  $('isl-x').onclick = endDemo;", "  $('isl-x').onclick = endDemo;\n  $('tuto').onclick = () => { if (!demo) runDemo(); };")
