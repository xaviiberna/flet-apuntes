# Flet · Lista de tareas

Apuntes y prácticas de **Flet** explicados paso a paso y **función por función**, con buscador. Incluye la práctica *Modificaciones de MiPrimerApp* y una sección nueva sobre **ordenar listas de controles con `key` y `lambda`**.

## Contenido

| Carpeta | Qué hay |
|---|---|
| `docs/` | El sitio (Markdown) |
| `codigo/` | Todos los `.py`, completos y ejecutables |
| `tests/` | Pruebas de la lógica de ordenar (sin ventana) |
| `mkdocs.yml` | Configuración del sitio (MkDocs Material) |

## Ver el sitio en tu equipo

```bash
python3 -m venv env && source env/bin/activate     # en Windows: env\Scripts\Activate.ps1
pip install -r requirements.txt
mkdocs serve                                        # http://127.0.0.1:8000
```

## Publicarlo en GitHub Pages

1. `mkdocs.yml` ya apunta a `xaviiberna/flet-apuntes` (campos `site_url` y `repo_url`); cámbialo si usas otro usuario o nombre.
2. Crea el repositorio `flet-apuntes` en GitHub y sube todo a la rama `main`.
3. El workflow `.github/workflows/deploy.yml` construye y publica solo en la rama `gh-pages`.
4. En **Settings → Pages**: *Deploy from a branch* → `gh-pages` / `/ (root)`.

La web quedará en `https://xaviiberna.github.io/flet-apuntes/`.

## Ejecutar las apps

```bash
pip install flet
flet run codigo/ordenar_funcional.py
```

## Probar la lógica de ordenar

```bash
python3 tests/test_ordenar.py
```
