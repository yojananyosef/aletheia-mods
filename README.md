# aletheia-mods

Catálogo de contenido desacoplado de **Aletheia**, publicado como sitio
estático para que la aplicación pueda descargar únicamente los recursos que
necesita y cachearlos.

- **Catálogo publicado:** <https://yojananyosef.github.io/aletheia-mods/>
- **Base de datos:** <https://yojananyosef.github.io/aletheia-mods/v1/>
- **Manifiesto:** <https://yojananyosef.github.io/aletheia-mods/v1/mods.json>
- **Aplicación:** <https://yojananyosef.github.io/aletheia/>

## Qué contiene

`docs/v1/` reproduce el árbol que consume la app:

```text
v1/
  mods.json                 manifiesto de versión y archivos principales
  index.json                fichas de los 27 recursos
  search.meta.json          hash, tamaño y conteos del índice FTS5
  search.sqlite.gz          índice FTS5 comprimido (~48,8 MB)
  morphology.json           descripciones de morfología
  rv1909/
    manifest.json
    books/GEN.json.gz
    ...
  kjv/, asv/, ...
  lexicon.strongs/
  matthew-henry-concise/
  easton/
  devotional.daily/
  factbook.core/
```

Los libros y los índices de secciones se sirven comprimidos con gzip. Los
manifiestos y las secciones individuales permanecen en JSON. GitHub Pages
sirve los archivos con `Access-Control-Allow-Origin: *` y `Accept-Ranges:
bytes`, así que la app web puede descargarlos directamente y cachearlos.

## Versionado

- `v1` es el contrato actual del catálogo.
- Los cambios de contenido compatibles se publican dentro de `v1` y se
  identifican por `mods.json.version` y por el hash de `search.meta.json`.
- Un cambio incompatible del formato debe publicarse en `v2` y la app debe
  elegir la versión que entiende.
- La app no debe asumir que el catálogo está empaquetado: el índice de
  búsqueda y los recursos se descargan bajo demanda y se reutilizan desde la
  caché del navegador o del sistema.

## Publicar una actualización

Desde un clon de los dos repositorios:

```bash
cd aletheia-mods
python3 tools/import_assets.py --source ../aletheia/app/assets/catalog
python3 -m json.tool docs/v1/mods.json > /dev/null
git add docs/v1
git commit -m "Catálogo: actualiza a $(python3 -c 'import json; print(json.load(open("docs/v1/mods.json"))["version"])')"
git push
```

El script reemplaza `docs/v1/` para que no queden recursos obsoletos. No
incluye las fuentes crudas ni `catalog/data/`; esos artefactos se generan en
el repositorio de la aplicación.

GitHub Pages publica la carpeta `docs/` de la rama `main`. No hay servidor:
todo el contenido es estático.

## Licencias y atribución

El catálogo distribuye contenido de **dominio público**, **CC BY 4.0**,
**CC BY-SA 4.0** y contenido propio. La procedencia, los enlaces y las
obligaciones de atribución están en [`NOTICE.md`](NOTICE.md). No se incluye
contenido con licencia No-Comercial, marcas ni activos de aplicaciones de
terceros.

La app muestra la fuente y la licencia en la ficha de cada recurso. Si se
reutiliza el contenido de este repositorio, deben conservarse las atribuciones
de `NOTICE.md`.

## Estado

- **27 recursos:** 12 Biblias (RV1909, KJV, ASV, BLL, SBLM, BES, VBL, TAHOT,
  TAGNT, BSB, WEB y la Biblia Platense con canon amplio), léxico Strong,
  6 comentarios (Matthew Henry conciso, Wesley, Clarke, Calvino, Catena Aurea
  y Lutero), 3 diccionarios (Easton, Webster 1828 y Strong), 2 devocionales
  (diario propio y Morning and Evening de Spurgeon), 2 documentos (Josefo y
  Didaché en griego), gazetteer y Factbook.
- **346 798 versículos** y **94 335 secciones no bíblicas** en el índice FTS5.
- **376 083 referencias cruzadas** del TSK.
- **18 mapas** dibujados por la app con geometría de Natural Earth y
  coordenadas de OpenBible.info; la geometría se empaqueta con la app porque
  es pequeña y se necesita sin conexión.
