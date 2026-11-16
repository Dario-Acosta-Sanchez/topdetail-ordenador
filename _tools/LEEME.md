# Top Detail · versión de ordenador

**Desde el 16-11-2026 hay UNA sola dirección: https://topdetail.puntozerosl.es** (repo `topdetail`).
Su `index.html` (móvil) lleva arriba el selector `#td-version`: en ordenador o tablet manda a `pc/`, y la página de `pc/`
enseña en la barra la dirección de siempre (replaceState + `<base href="../">`). `?movil` y `?pc` fuerzan una u otra.
Este repo es solo el taller (herramientas y fotos 16:9); su `index.html` redirige a la dirección única.

La versión de ordenador se GENERA: `python3 _tools/mkpc.py` lee `~/topdetail/index.html` (la del móvil), le añade la capa
de ordenador (CSS + pequeños cambios de JS) y escribe `~/topdetail/pc/index.html`, copiando `img/` → `~/topdetail/pc/img/`
(las rutas pasan a `pc/img/`). Si cambia la del móvil o alguna foto de aquí, volver a ejecutarlo y publicar `topdetail`.

Fotos (`img/`, 1920×1080): `python3 _tools/pc.py lienzos | montar | comprobar <grupo>`.
Cada grupo de fotos con el mismo encuadre comparte un fondo ampliado por Gemini (`_tools/fondos/<grupo>.jpeg`);
el centro original del móvil se pega encima, así antes y después calcan. Sin fondo → relleno provisional desenfocado.

Vídeos: `VIDEO = false` hasta tener los clips de Veo en horizontal (vid/p_, t_, c_, e_).
Ver en local: en `~/topdetail`, `python3 -m http.server 8790 --bind 127.0.0.1` (la raíz elige la versión).
