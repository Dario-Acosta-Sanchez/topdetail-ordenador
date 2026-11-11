# Top Detail · versión de ordenador

`index.html` se GENERA: `python3 _tools/mkpc.py` lo crea a partir de `~/topdetail/index.html` (la web del móvil)
y le añade la capa de ordenador (CSS + pequeños cambios de JS). Si cambia la del móvil, volver a ejecutarlo.

Fotos (`img/`, 1920×1080): `python3 _tools/pc.py lienzos | montar | comprobar <grupo>`.
Cada grupo de fotos con el mismo encuadre comparte un fondo ampliado por Gemini (`_tools/fondos/<grupo>.jpeg`);
el centro original del móvil se pega encima, así antes y después calcan. Sin fondo → relleno provisional desenfocado.

Vídeos: `VIDEO = false` hasta tener los clips de Veo en horizontal (vid/p_, t_, c_, e_).
Ver en local: `python3 -m http.server 8790 --bind 127.0.0.1`.
