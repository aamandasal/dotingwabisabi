# La Casa de Tinta

*(nombre provisional — cámbialo en `pelicanconf.py`, línea `SITENAME`)*

Un blog literario construido con Pelican: papel crema, tipografía
EB Garamond (la de los libros bien editados), ornamentos tipográficos,
y tratamiento especial para poesía.

---

## Para empezar (primera vez, con ayuda de tu ingeniero de cabecera)

```bash
python3 -m venv .venv
source .venv/bin/activate
make install
make serve
```

Abre `http://localhost:8000` en el navegador. Cada vez que guardes un
texto, refresca y ahí está.

---

## Escribir una entrada nueva

Crea un archivo `.md` dentro de `content/`. Todo texto empieza con esta
ficha (los datos de arriba) y luego el texto:

```
Title: El título de tu texto
Date: 2026-07-10
Category: Poemas
Tags: inéditos, serie de las cosas quietas
Slug: titulo-corto-para-la-direccion
Summary: Una línea que aparece en la portada como invitación.

Aquí empieza el texto...
```

- **Category** organiza el menú: usa `Poemas` o `Prosa` (o crea nuevas
  solo con escribirlas — no hay que registrarlas en ningún lado).
- **Slug** es la dirección: `tusitio.com/titulo-corto/`.
- Para un **borrador** que no se publique: agrega la línea `Status: draft`.

## Cómo publicar POESÍA (importante)

La prosa fluye sola, pero los versos necesitan que se respete cada salto
de línea. Envuelve el poema así:

```
<div class="poema">
Primer verso
segundo verso
tercer verso

nueva estrofa tras línea en blanco
</div>
```

El tema centra el poema, airea el interlineado y respeta cada salto tal
como lo escribiste. Las *cursivas* funcionan normal dentro del poema.

## Ornamentos disponibles

- `---` (tres guiones solos) se convierte en un asterismo dorado ⁂
- Las citas con `>` aparecen centradas con un fleurón ❦ arriba

---

## Cambiar el aspecto

Abre `theme/tinta/static/css/style.css`. Al inicio está la
**ZONA DE PERSONALIZACIÓN** con los colores y tipografías comentados.
Cambia un valor y todo el sitio cambia:

- `--papel` — el color de fondo (crema)
- `--tinto` — el rojo editorial de los enlaces
- `--dorado` — los ornamentos
- `--tamano` — el tamaño de letra base

## Cambiar el nombre del blog

En `pelicanconf.py`: `SITENAME` (el nombre) y `SITESUBTITLE` (la frase
bajo el nombre). El menú está en `MENUITEMS`.

---

## Publicar en internet

El proyecto trae el mismo sistema automático que el blog de tu esposo:

1. Crear una cuenta de GitHub propia
2. Subir este proyecto a un repositorio
3. Activar GitHub Pages (Settings → Pages → Source: GitHub Actions)
4. Conectar un dominio propio si se quiere

Cada vez que se suba un cambio (`git push`), el sitio se publica solo.
Los pasos detallados están en el manual PDF que acompaña al proyecto —
o mejor: pídele el tour a quien ya lo hizo una vez. 😉

---

## El ritual de cada sesión

```bash
cd ruta/a/casa-tinta
source .venv/bin/activate
make serve
```
Escribir. Guardar. Refrescar. Y cuando el texto esté listo:
```bash
git add .
git commit -m "Publica: [título del texto]"
git push
```
