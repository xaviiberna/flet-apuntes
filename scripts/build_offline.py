"""Genera la versión OFFLINE del sitio (se abre con doble clic, sin internet).
Uso:  python3 scripts/build_offline.py        ->  crea  dist/flet-apuntes-offline/
Cambios respecto a la versión web (solo en una copia temporal):
  - se sirve con un servidor local de Python (el buscador necesita http://, no file://)
  - URLs relativas a archivos .html
  - sin fuentes de Google ni mermaid (se usan diagramas de texto)
"""
import re, shutil, subprocess, sys, tempfile, pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent
tmp = pathlib.Path(tempfile.mkdtemp())
shutil.copytree(RAIZ / "docs", tmp / "docs")
shutil.copytree(RAIZ / "codigo", tmp / "codigo")
cfg = (RAIZ / "mkdocs.yml").read_text(encoding="utf8")

# --- diagramas mermaid -> texto
DIAG = {
"empezar/vocabulario.md": """```text
 El usuario hace algo
        │
        ▼
 Se ejecuta un manejador
        │
        ▼
 El manejador cambia controles o datos
        │
        ▼
   page.update()
        │
        ▼
 Se ve el cambio
```""",
"funciones/index.md": """```text
 añadir_tarea ───────┐
 eliminar_tarea ─────┤
 borrar_completadas ─┼──► actualizar_contador ──► page.update() ──► pantalla
 Checkbox on_change ─┘

 modificar_tarea ────┐
 ordenar_tareas ─────┴──► page.update() ──► pantalla
```""",
"ordenar/donde-va.md": """```text
 main
  ├─ 1/3  CRITERIOS = {...}              (diccionario de lambdas)
  ├─ 2/3  def ordenar_tareas(...)        (la función que ordena)
  ├─ 3/3  fila_ordenar = ft.Row(...)     (botones con lambda e: ordenar_tareas(...))
  └─ page.add(... fila_ordenar ...)      (se añaden a la página)
```""",
}
for rel, txt in DIAG.items():
    f = tmp / "docs" / rel
    s = f.read_text(encoding="utf8")
    s2 = re.sub(r"```mermaid\n.*?```", txt, s, count=1, flags=re.S)
    assert s != s2, rel
    f.write_text(s2, encoding="utf8")

# --- configuración offline
cfg = re.sub(r"site_url:.*\n", "", cfg)
cfg = re.sub(r"repo_url:.*\n", "", cfg)
cfg = re.sub(r"repo_name:.*\n", "", cfg)
cfg = re.sub(r"      custom_fences:.*?format: !!python/name:pymdownx.superfences.fence_code_format\n", "", cfg, flags=re.S)
cfg = cfg.replace("theme:\n  name: material\n", "use_directory_urls: false\n\ntheme:\n  name: material\n  font: false\n", 1)
assert "font: false" in cfg
(tmp / "mkdocs.yml").write_text(cfg, encoding="utf8")

salida = RAIZ / "dist" / "flet-apuntes-offline"
if salida.exists():
    shutil.rmtree(salida)
salida.parent.mkdir(exist_ok=True)
subprocess.run([sys.executable, "-m", "mkdocs", "build", "-q", "-f", str(tmp / "mkdocs.yml"), "-d", str(salida / "web")], check=True)
shutil.copytree(RAIZ / "codigo", salida / "codigo")
(salida / "abrir.sh").write_text(r"""#!/bin/sh
# Abre los apuntes SIN internet: arranca un servidor local con Python y abre el navegador.
# Para cerrarlo: Ctrl+C en esta terminal.
cd "$(dirname "$0")/web" || exit 1
PUERTO=8000
while python3 -c "import socket,sys;s=socket.socket();sys.exit(s.connect_ex(('127.0.0.1',$PUERTO))!=0)" 2>/dev/null; do
  PUERTO=$((PUERTO+1))
done
python3 -m http.server "$PUERTO" --bind 127.0.0.1 >/dev/null 2>&1 &
SERVIDOR=$!
trap 'kill $SERVIDOR 2>/dev/null' EXIT INT TERM
sleep 1
URL="http://127.0.0.1:$PUERTO/index.html"
echo "Apuntes en: $URL   (Ctrl+C para cerrar)"
xdg-open "$URL" 2>/dev/null || firefox "$URL" 2>/dev/null || google-chrome "$URL" 2>/dev/null &
wait $SERVIDOR
""", encoding="utf8")
(salida / "abrir.sh").chmod(0o755)
(salida / "LEEME.txt").write_text(
"""APUNTES DE FLET (versión sin internet)

Abrir:   ./abrir.sh   (arranca un servidor local y abre el navegador; Ctrl+C para cerrar)
         Si no te deja ejecutarlo:  sh abrir.sh
         A mano:  cd web && python3 -m http.server 8000   y abre http://127.0.0.1:8000

También puedes abrir web/index.html con doble clic: se navega igual,
pero el BUSCADOR solo funciona con el servidor (abrir.sh).
Código:  carpeta codigo/   ->  flet run codigo/ordenar_funcional.py

El buscador (lupa de arriba) funciona sin conexión.
""", encoding="utf8")
shutil.rmtree(tmp)
print("OK ->", salida)
