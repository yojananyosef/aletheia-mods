#!/usr/bin/env python3
"""Publica el catálogo construido de Aletheia en `docs/v1/`.

El repositorio `aletheia-mods` distribuye artefactos, no las fuentes crudas.
El origen habitual es `app/assets/catalog/` del repositorio `aletheia`:

    python3 tools/import_assets.py --source ../aletheia/app/assets/catalog

El script copia los recursos, el índice FTS5 y la morfología a `docs/v1/`, y
genera `docs/v1/mods.json` con la versión, las sumas de los archivos de nivel
superior y los metadatos del índice. Los recursos y sus licencias se documentan
en `NOTICE.md`.

El contenido es estático: GitHub Pages lo sirve con CORS y `Accept-Ranges`.
La app puede descargar solo lo que necesita y cachearlo.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
TARGET = DOCS / "v1"

# Archivos de nivel superior que forman parte del contrato del catálogo.
TOP_LEVEL = (
    "index.json",
    "search.meta.json",
    "search.sqlite.gz",
    "morphology.json",
)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def version_from(meta: dict) -> str:
    built = str(meta.get("builtAt") or "").strip()
    if built:
        try:
            parsed = datetime.fromisoformat(built.replace("Z", "+00:00"))
            return parsed.astimezone(timezone.utc).strftime("%Y.%m.%d.%H%M%S")
        except ValueError:
            pass
    return datetime.now(timezone.utc).strftime("%Y.%m.%d.%H%M%S")


def copy_tree(source: Path, target: Path) -> None:
    """Reemplaza el árbol publicado para no dejar recursos eliminados."""
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(source, target)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("../aletheia/app/assets/catalog"),
        help="Directorio app/assets/catalog de Aletheia",
    )
    args = parser.parse_args()
    source = args.source.expanduser().resolve()
    if not (source / "index.json").exists():
        raise SystemExit(f"ERROR: no parece un catálogo de Aletheia: {source}")

    copy_tree(source, TARGET)

    index = read_json(TARGET / "index.json")
    meta = read_json(TARGET / "search.meta.json")
    version = version_from(meta)

    files = {}
    for name in TOP_LEVEL:
        path = TARGET / name
        if not path.exists():
            raise SystemExit(f"ERROR: falta {path}")
        files[name] = {
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }

    # v2: cada recurso publica el listado de sus archivos (ruta relativa al
    # raíz del catálogo, tamaño y sha256). Es lo que permite que la app de
    # escritorio instale el módulo desde la Tienda y verifique cada archivo,
    # en vez de tener todo el contenido dentro del ejecutable.
    def module_files(resource_id: str, size: bytes) -> dict:
        root = dir_for(resource_id)
        base = TARGET / root
        if not base.exists():
            raise SystemExit(f"ERROR: el recurso {resource_id} no tiene carpeta en el catálogo")
        entries = [
            {
                "path": f"{root}/{path.relative_to(base).as_posix()}",
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
            for path in sorted(base.rglob("*"))
            if path.is_file()
        ]
        return {
            "id": resource_id,
            "size": sum(entry["bytes"] for entry in entries),
            "files": entries,
        }

    def dir_for(resource_id: str) -> str:
        # Espeja `DocumentRepository.dirFor` de la app.
        overrides = {"devotional.daily", "factbook.core", "lexicon.strongs"}
        if resource_id in overrides:
            return resource_id
        return resource_id.split(".")[-1]

    resources = []
    for item in index:
        resource_id = item.get("id")
        entry = module_files(resource_id, 0)
        listing = {
            "id": resource_id,
            "type": item.get("type"),
            "title": item.get("title"),
            "language": item.get("language"),
            "license": item.get("license"),
            "stats": item.get("stats", {}),
            "size": entry["size"],
            "files": entry["files"],
        }
        resources.append(listing)
    # El índice FTS5 es su propio módulo: la app lo instala aparte (con
    # progreso y cancelación) y sigue igual de útil sin él.
    search_files = [
        {
            "path": name,
            "bytes": files[name]["bytes"],
            "sha256": files[name]["sha256"],
        }
        for name in ("search.sqlite.gz", "search.meta.json")
        if name in files
    ]
    resources.append(
        {
            "id": "catalog.search",
            "type": "dataset",
            "title": "Búsqueda local (índice FTS5)",
            "language": "mul",
            "license": {"kind": "public-domain", "text": "Ver NOTICE.md: dominio público/CC"},
            "stats": {
                "entries": meta.get("indexedEntries", 0),
                "verses": meta.get("indexedVerses", 0),
                "sections": meta.get("indexedSections", 0),
            },
            "size": sum(file_["bytes"] for file_ in search_files),
            "files": search_files,
        },
    )
    resources.sort(key=lambda item: str(item.get("id") or ""))

    manifest = {
        "schema": 2,
        "name": "Aletheia Mods",
        "version": version,
        "builtAt": meta.get("builtAt"),
        "publishedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "basePath": "/aletheia-mods/v1/",
        "license": "Ver NOTICE.md: dominio público, CC BY 4.0, CC BY-SA 4.0 y contenido propio.",
        "search": meta,
        "resources": resources,
        "files": files,
    }
    write_json(TARGET / "mods.json", manifest)

    total = sum(path.stat().st_size for path in TARGET.rglob("*") if path.is_file())
    print(
        f"OK: {len(resources)} recursos, {len(files)} archivos de nivel superior, "
        f"{total / 1_000_000:.1f} MB en {TARGET}"
    )
    print(f"   versión {version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
