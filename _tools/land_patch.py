# Página larga bajo el escenario (lo ejecuta mkpc.py): las páginas de información dejan de ir en un panel
# y pasan a ser secciones a lo ancho; los botones del menú bajan hasta la suya.
T = os.path.dirname(os.path.abspath(__file__)) + '/'
rd = lambda n: open(T + n, encoding='utf-8').read()
rep('</style>\n<script>\n// En un móvil', rd('land.css') + '</style>\n<script>\n// En un móvil')
rep('    <nav class="xside l" id="opt-l"', '    <button class="down" id="down" type="button">Toda la información<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button>\n    <nav class="xside l" id="opt-l"')
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
