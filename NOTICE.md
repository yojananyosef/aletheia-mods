# Fuentes y licencias del catálogo

Aletheia distribuye contenido de **dominio público**, **CC BY 4.0** y
**CC BY-SA 4.0**, además de contenido propio. Todas estas licencias permiten
uso comercial y distribución; no se incluye material con licencia
No-Comercial (NC) ni activos de la aplicación original. Esta nota registra la
procedencia, la atribución y la base de licencia de los recursos publicados en
este repositorio (`docs/v1/`) y de la geometría de mapas que acompaña a la app.

## 1. Recursos incluidos

| Recurso | Fuente / atribución | Licencia | Verificación |
|---|---|---|---|
| Reina-Valera 1909 (`bible.rv1909`) | [eBible.org — spaRV1909](https://ebible.org/spaRV1909/) · [zip USFM](https://ebible.org/Scriptures/spaRV1909_usfm.zip) | Dominio público | `copr.htm` del paquete de eBible declara Public Domain. |
| King James Version (`bible.kjv`) | [eBible.org — eng-kjv](https://ebible.org/Scriptures/eng-kjv_usfm.zip) | Dominio público | Texto de 1611/1769; paquete de eBible con licencia Public Domain. |
| American Standard Version 1901 (`bible.asv`) | [eBible.org — eng-asv](https://ebible.org/Scriptures/eng-asv_usfm.zip) | Dominio público | `copr.htm` del paquete declara Public Domain. |
| Santa Biblia libre Latinoamericano (`bible.bll`) | [eBible.org — spabll](https://ebible.org/Scriptures/spabll_usfm.zip) | Dominio público | `copr.htm` del paquete declara Public Domain; el propio paquete se identifica como borrador de traducción. |
| Santa Biblia libre para el mundo (`bible.sblm`) | [eBible.org — spablm](https://ebible.org/Scriptures/spablm_usfm.zip) | Dominio público | `copr.htm` del paquete declara Public Domain. Es un borrador de traducción de 2026. |
| La Biblia en Español Sencillo (`bible.bes`) | [eBible.org — spabes](https://ebible.org/Scriptures/spabes_usfm.zip) | Dominio público | `copr.htm` del paquete declara Public Domain. |
| Versión Biblia Libre (`bible.vbl`) | [eBible.org — spavbl](https://ebible.org/Scriptures/spavbl_usfm.zip) · Jonathan Gallagher y Shelly Barrios de Ávila | **CC BY-SA 4.0** | El paquete y su ficha declaran Creative Commons Atribución-CompartirIgual 4.0. Se distribuye el texto sin etiquetas Strong por la alineación irregular de la fuente. |
| Texto hebreo TAHOT (`bible.tahot`) | [STEPBible.org / STEPBible-Data](https://github.com/STEPBible/STEPBible-Data) · Tyndale House Cambridge | **CC BY 4.0** | La distribución de STEPBible declara CC BY 4.0. Se conserva la atribución en el manifiesto y en la ficha del recurso. |
| Texto griego TAGNT (`bible.tagnt`) | [STEPBible.org / STEPBible-Data](https://github.com/STEPBible/STEPBible-Data) · Tyndale House Cambridge | **CC BY 4.0** | La distribución de STEPBible declara CC BY 4.0. Se usa la referencia KJV entre corchetes cuando la versificación difiere. |
| Léxico Strong (`lexicon.strongs`) | [STEPBible.org / STEPBible-Data](https://github.com/STEPBible/STEPBible-Data) (TBESH/TBESG) · [CrossWire StrongsHebrew](https://www.crosswire.org/sword/modules/ModInfo.jsp?modName=StrongsHebrew) (definiciones hebreas) | **CC BY 4.0** para TBESH/TBESG; **dominio público** para Strong's Hebrew Dictionary | Las glosas y la morfología proceden de STEPBible (CC BY 4.0). Las definiciones hebreas son el *Strong's Hebrew Dictionary* de CrossWire, de dominio público. Las definiciones griegas son TBESG (CC BY 4.0). |
| Matthew Henry, comentario conciso (`commentary.matthew-henry-concise`) | [lyteword/mhenry-concise](https://github.com/lyteword/mhenry-concise) · [mhenry-complete](https://github.com/lyteword/mhenry-complete) | CC0-1.0 en la edición Markdown; texto original de dominio público | GitHub API del repositorio declara `CC0-1.0`; 2 Reyes 1 se toma de la edición completa, también CC0. |
| Diccionario bíblico de Easton, 1897 (`dictionary.easton`) | [JWBickel/BibleDictionaries](https://huggingface.co/datasets/JWBickel/BibleDictionaries) · `Easton's Bible Dictionary.jsonl` | Texto original de dominio público | Matthew George Easton (1823–1894); el diccionario se publicó en 1897 y la transcripción JSONL reproduce ese texto. El repositorio de la transcripción no declara una licencia adicional. |
| Treasury of Scripture Knowledge (TSK) | [ariseshinestudio/TSK](https://github.com/ariseshinestudio/TSK) · [JustVerses.com](https://www.justverses.com/) | Dominio público | La ficha del repositorio indica “Provider: JustVerses.com · License: Public Domain”; el TSK original es una obra del siglo XIX. |
| Geometría de mapas (`app/assets/maps/`) | [Natural Earth](https://www.naturalearthdata.com/) — `ne_110m_land`, `ne_110m_lakes` | Dominio público | Natural Earth declara sus datos en dominio público; no se exige atribución, pero se conserva en la app y en este aviso. |
| Coordenadas de lugares bíblicos | [OpenBible.info Bible Geocoding](https://github.com/openbibleinfo/Bible-Geocoding-Data) | **CC BY 4.0** | La ficha del repositorio declara CC BY 4.0. Se usan las coordenadas de los lugares, no las imágenes ni las teselas. La atribución aparece al pie de cada mapa. |
| Devocional diario (`devotional.daily`) | Contenido propio de Aletheia | Propio | Lecturas y temas originales; los versículos citados son de la RV1909. |
| Factbook (`factbook.core`) | Contenido propio de Aletheia | Propio | 32 artículos originales (19 con mapa); las referencias bíblicas son de dominio público. |

## 2. Atribución exigida por las licencias CC BY

Al reutilizar o redistribuir los textos de STEPBible, TBESH/TBESG o la VBL debe
conservarse, como mínimo:

- **TAHOT/TAGNT/TBESH/TBESG:** «Fuente: STEPBible.org / Tyndale House
  Cambridge, CC BY 4.0». Enlace:
  <https://github.com/STEPBible/STEPBible-Data>. Se indica si se han hecho
  cambios de formato o de versificación; el texto y el etiquetado se conservan
  sin alterar su contenido.
- **VBL:** «Versión Biblia Libre, Jonathan Gallagher y Shelly Barrios de Ávila,
  CC BY-SA 4.0». Enlace:
  <https://ebible.org/Scriptures/spavbl_usfm.zip>. Las adaptaciones del texto
  deben distribuirse bajo CC BY-SA 4.0.
- **Strong's Hebrew Dictionary:** «Strong's Hebrew Dictionary, dominio
  público, módulo StrongsHebrew de CrossWire».
- **OpenBible.info:** «Coordenadas de lugares: OpenBible.info Bible Geocoding,
  CC BY 4.0». Enlace:
  <https://github.com/openbibleinfo/Bible-Geocoding-Data>. La app no altera
  las coordenadas; solo las usa para situar marcadores.
- **Natural Earth:** «Geometría: Natural Earth, dominio público». Enlace:
  <https://www.naturalearthdata.com/>.

Las fichas de recurso de la interfaz muestran el autor y la licencia; los
manifiestos guardan `source` y `license`. La app no reclama derechos sobre
estos textos.

## 3. Qué se distribuye

- Texto normalizado en formato JSON del contrato del catálogo; no se incluyen
  escaneos, portadas ni activos de las fuentes.
- Los libros de las Biblias y los índices de secciones grandes se comprimen
  como `.json.gz`; la app los descomprime en memoria. No se altera el texto.
- El endpoint `/v1/cross-references` devuelve `source` y `license` junto a los
  enlaces del TSK. En modo local, la etiqueta «Tesoro de conocimiento bíblico»
  identifica la fuente en «Ideas».
- Los mapas no incluyen teselas ni imágenes de terceros: se dibujan localmente
  con la geometría de Natural Earth y las coordenadas de OpenBible.info. La
  atribución se muestra al pie de cada mapa.
- Las fuentes crudas (`catalog/sources/`) y los artefactos de construcción
  (`catalog/data/`) no se versionan; solo se versiona el resultado necesario
  para ejecutar la app.

## 4. Recuentos de la edición actual

- **14 recursos:** 9 Biblias (5 en español, 2 en inglés, TAHOT y TAGNT),
  2 diccionarios (Easton y léxico Strong), 1 comentario, 1 devocional y
  1 Factbook de **32 artículos** (19 con mapa).
- **248 870 versículos indexados** y **23 633 secciones no bíblicas**;
  **272 503 entradas FTS5** en total.
- **376 083 enlaces** de referencias cruzadas del TSK.
- TAHOT: 39 libros, 929 capítulos, 23 261 versículos (incluidos los títulos de
  los salmos como versículo 0) y 305 417 palabras.
- TAGNT: 27 libros, 260 capítulos, 7 953 versículos y 138 140 palabras.
- Léxico Strong: 18 085 entradas (8 723 hebreas y 9 362 griegas).
- Los assets ocupan **92 MB**, de los cuales 48,8 MB son el índice FTS5
  comprimido. La geometría de los mapas añade unos 171 KB.

La fecha de verificación de estas fuentes es **2026-10-20**. Para reproducir el
catálogo, véase [`catalog/README.md`](catalog/README.md) y
[`docs/spec/05-fuentes-contenido.md`](docs/spec/05-fuentes-contenido.md).
