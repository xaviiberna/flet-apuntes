# Práctica · Modificaciones de MiPrimerApp

Partimos de la app del paso 8 **comentada línea a línea** (`codigo/practica_base_comentada.py`) y le añadimos funcionalidades. El resultado final es `codigo/practica_app_final.py`.

| # | Modificación | Dónde se toca |
|---|---|---|
| 1 | [Control de tareas repetidas](repetidas.md) | variable `mensaje` + bucle en `añadir_tarea` |
| 2 | [Color del contador (rojo/verde)](color-contador.md) | `contador` al crearlo + `if/else` en `actualizar_contador` |
| 3 | [Borrar completadas](borrar-completadas.md) | función `borrar_completadas` + botón |
| 4 | [Botón Modificar](modificar.md) | función `modificar_tarea` + `IconButton` en cada fila |
| 5 | [Publicar](publicar.md) | web, APK, Windows y Linux con `flet build` |

??? example "Código base comentado (antes de las modificaciones)"
    ```python linenums="1" title="practica_base_comentada.py"
    --8<-- "codigo/practica_base_comentada.py"
    ```

    | Líneas | Qué hacen |
    |---|---|
    | 1-2 | Importa Flet con el alias `ft`. |
    | 6 | `main(page)`: función principal; recibe la ventana. |
    | 8-10 | Título de la ventana y margen interior de 20 px. |
    | 13 | Título «Mis tareas» grande y en negrita. |
    | 22 | Campo de texto que ocupa el espacio libre; Enter llama a `añadir_tarea` (lambda porque aún no está definida). |
    | 25 | Texto del contador de pendientes. |
    | 28 | Columna vacía donde se añaden las tareas. |
    | 32-39 | `actualizar_contador`: cuenta las casillas sin marcar, cambia el texto y `page.update()`. |
    | 42-45 | `eliminar_tarea(fila)`: quita esa fila y recalcula. |
    | 49-61 | `añadir_tarea`: lee el texto sin espacios; si está vacío, error y `return`. |
    | 64 | Quita el error anterior. |
    | 66-84 | Crea la fila: `Checkbox` (con `on_change`) y papelera (con lambda que captura la fila). |
    | 86-90 | Añade la fila, vacía el campo y recalcula. |
    | 93 | Botón «Añadir». |
    | 96 | Añade a la página: título, fila de entrada, contador y lista. |
    | 99 | Arranca la app. |

??? example "Código final de la práctica"
    ```python linenums="1" title="practica_app_final.py"
    --8<-- "codigo/practica_app_final.py"
    ```

    | Líneas | Qué hacen |
    |---|---|
    | 2 | Importa Flet. |
    | 6-13 | `main`: título y padding de la página, y el título «Mis tareas». |
    | 22 | Campo de texto; Enter llama a `añadir_tarea`. |
    | 26 | Contador, **rojo** al empezar (no hay tareas). |
    | 29 | `mensaje`: texto naranja para avisar de repetidas. |
    | 32 | Columna de tareas. |
    | 36-41 | `actualizar_contador`: cuenta pendientes y cambia el texto. |
    | 45-48 | Color: rojo si `pendientes == 0`, verde si hay alguna. |
    | 51 | Redibuja. |
    | 54-58 | `borrar_completadas`: recorre una copia (`list(...)`), quita las marcadas y recalcula. |
    | 61-64 | `eliminar_tarea(fila)`: quita una fila y recalcula. |
    | 68-77 | `modificar_tarea(fila)`: cambia el `label` del Checkbox por el texto del campo (si no está vacío). |
    | 81-83 | `añadir_tarea`: lee el texto sin espacios. |
    | 87-91 | Si está vacío: error en el campo y `return`. |
    | 94-100 | Si ya existe (comparando en minúsculas): aviso naranja y `return`. |
    | 102-103 | Tarea válida: borra el aviso y el error. |
    | 106-133 | Crea la fila: `Checkbox`, lápiz (`modificar_tarea`) y papelera (`eliminar_tarea`), cada uno con su lambda. |
    | 135-139 | Añade la fila, vacía el campo y recalcula el contador. |
    | 142 | Botón «Añadir». |
    | 145 | Botón «Borrar completadas». |
    | 148 | Añade todo a la página en orden. |
    | 151 | Arranca la app. |

!!! tip "Para encontrar cada cosa en el código final"
    Cada modificación tiene su página con **la línea exacta** y el motivo de ese lugar. Para ver qué hace cada función por separado, ve a [Función por función](../funciones/index.md).
