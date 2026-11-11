  ['precios', 'detallado', 'pulido', 'ceramico', 'report', 'nosotros', 'contacto', 'ubicacion'].forEach((t, k) => {
    const h = document.createElement('header'); h.className = 'land-h';
    h.innerHTML = `<span class="land-n">${String(k + 1).padStart(2, '0')}</span><h2>${PAGES[t]}</h2>`;
    panels[t].prepend(h); $('land').append(panels[t]);
  });
  $('land').append($('sheet-cta'));
  document.querySelector('#report details.report').open = true;
  const onScroll = () => {
    document.body.classList.toggle('scrolled', scrollY > innerHeight * .6);
    const y = innerHeight * .4; let cur = null, best = -1e9;
    for (const t of TABS) { const top = panels[t].getBoundingClientRect().top; if (top <= y && top > best) { best = top; cur = t; } }
    document.querySelectorAll('.lnav a.l').forEach(a => a.classList.toggle('on', a.getAttribute('href') === '#tp-' + cur));
  };
  addEventListener('scroll', onScroll, { passive: true });
  $('down').onclick = () => $('land').scrollIntoView({ behavior: 'smooth' });
  document.querySelectorAll('.lnav a[href="#"], .foot a[href="#"]').forEach(a => a.onclick = e => { e.preventDefault(); scrollTo({ top: 0, behavior: 'smooth' }); });
  // Bajar a la información cuesta un poco: desde el escenario hay que insistir con la rueda (la barrita del aviso se va llenando)
  let gate = 0, gateT = 0;
  const paintGate = () => $('down').style.setProperty('--g', Math.min(1, gate / 650));
  addEventListener('wheel', e => {
    if (scrollY > 4 || e.deltaY <= 0) return;
    if (e.target.closest && e.target.closest('.xside')) return;
    e.preventDefault();
    if (loading || demo) return;
    clearTimeout(gateT); gateT = setTimeout(() => { gate = 0; paintGate(); }, 450);
    gate += Math.min(Math.abs(e.deltaY), 110); paintGate();
    if (gate >= 650) { gate = 0; paintGate(); $('land').scrollIntoView({ behavior: 'smooth' }); }
  }, { passive: false });
