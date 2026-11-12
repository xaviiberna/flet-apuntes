# Instalación y entorno

Siempre se trabaja dentro de un **entorno virtual**: una carpeta con su propio Python y sus propias librerías, para no mezclar proyectos.

=== "Linux"

    ```bash
    ls /usr/bin/python*          # ver versiones instaladas y usar la más moderna
    mkdir todo && cd todo        # carpeta del proyecto
    python3 -m venv env          # crea el entorno (python3.12 -m venv env para una versión concreta)
    source env/bin/activate      # lo activa
    pip install flet             # instala Flet
    ```

=== "Windows (PowerShell)"

    ```powershell
    mkdir todo; cd todo
    py -m venv env               # crea el entorno
    env\Scripts\Activate.ps1     # lo activa
    pip install flet
    ```

    !!! warning "Si PowerShell no deja activar el entorno"
        Ejecuta una vez `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` y vuelve a activar.

## Ejecutar un archivo

```bash
flet run paso1_hola_mundo.py     # recarga sola cada vez que guardas
python3 paso1_hola_mundo.py      # alternativa (sin recarga automática)
```

| Comando | Para qué |
|---|---|
| `flet run archivo.py` | Abre la app y la **recarga al guardar** |
| `flet run --web archivo.py` | Ábrela en el navegador |
| `pip install flet` | Instala la librería |

!!! danger "No llames a tu archivo `flet.py`"
    Python importaría tu archivo en vez de la librería.
