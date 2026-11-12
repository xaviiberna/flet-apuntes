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

    | Código | Qué hace |
    |---|---|
    | `ls /usr/bin/python*` | Lista las versiones de Python instaladas, para usar la más moderna. |
    | `mkdir todo && cd todo` | Crea la carpeta del proyecto (`todo`) y entra en ella. `&&` = ejecuta lo segundo si lo primero va bien. |
    | `python3 -m venv env` | Crea el entorno virtual en la carpeta `env`. `-m venv` ejecuta el módulo que crea entornos. |
    | `source env/bin/activate` | Activa el entorno: desde ahora `python` y `pip` son los de `env`. Verás `(env)` en el prompt. |
    | `pip install flet` | Descarga e instala Flet **dentro del entorno**. |

=== "Windows (PowerShell)"

    ```powershell
    mkdir todo; cd todo
    py -m venv env               # crea el entorno
    env\Scripts\Activate.ps1     # lo activa
    pip install flet
    ```

    | Código | Qué hace |
    |---|---|
    | `mkdir todo; cd todo` | Crea la carpeta y entra. En PowerShell se separan comandos con `;`. |
    | `py -m venv env` | Crea el entorno virtual. `py` es el lanzador de Python en Windows. |
    | `env\Scripts\Activate.ps1` | Activa el entorno (en Windows está en `Scripts`, no en `bin`). |
    | `pip install flet` | Instala Flet dentro del entorno. |

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
