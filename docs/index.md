# Flet · Lista de tareas

Apuntes y prácticas de **Flet** explicados desde cero: de «Hola mundo» a una app completa con clases, publicada como web, APK, Windows y Linux.

!!! tip "Buscador"
    Usa la lupa de arriba (o pulsa ++s++ o ++slash++). Busca por **función** (`actualizar_contador`), por **control** (`Checkbox`), por **evento** (`on_click`) o por **error** (`page.update`).

<div class="grid cards" markdown>

-   :material-rocket-launch: **Empezar**

    Entorno virtual, instalación y vocabulario.

    [:octicons-arrow-right-24: Instalación](empezar/instalacion.md)

-   :material-stairs: **Pasos 1 → 9**

    Cada paso añade una cosa nueva, con el código completo y cada línea explicada.

    [:octicons-arrow-right-24: Tutorial](pasos/index.md)

-   :material-clipboard-check: **Práctica: Modificaciones**

    Repetidas, color del contador, borrar completadas, modificar, web/APK/exe.

    [:octicons-arrow-right-24: Práctica](practica/index.md)

-   :material-function: **Función por función**

    Qué hace cada función, de dónde la llaman y por qué está donde está.

    [:octicons-arrow-right-24: Funciones](funciones/index.md)

-   :material-sort: **Ordenar con `key` y `lambda`**

    Cómo ordenar las tareas, todos los criterios y **dónde va cada trozo en el código**.

    [:octicons-arrow-right-24: Ordenar](ordenar/index.md)

-   :material-puzzle: **Controles y eventos**

    Qué es cada control y cada evento, y la `lambda` explicada.

    [:octicons-arrow-right-24: Controles](controles/index.md)

</div>

## Mapa del código

| Archivo | Qué contiene |
|---|---|
| `codigo/paso1…paso8` | El tutorial: cada archivo añade una novedad |
| `codigo/paso9a/9b/9c` | La misma app con clases |
| `codigo/practica_app_final.py` | App de la práctica (repetidas, colores, borrar completadas, modificar) |
| `codigo/ordenar_funcional.py` | La práctica + botones de ordenar |
| `codigo/ordenar_clases.py` | Ordenar en la versión con clases (con prioridad) |
| `codigo/ordenar_por_key_control.py` | Ordenar usando la propiedad `key` de los controles |

!!! info "Versión"
    Apuntes escritos con **Flet 0.86 / 1.0** (`ft.run`, `ft.Button(content=...)`). La API cambió respecto a versiones anteriores (`ft.app`, `ElevatedButton`, `text=`).
