# Todo el código

Archivos en `codigo/`. Cada uno es completo y ejecutable: `flet run codigo/<archivo>.py`.

??? example "paso1 → paso8"
    ```python linenums="1" title="paso8_app_final.py"
    --8<-- "codigo/paso8_app_final.py"
    ```

    | Líneas | Qué hacen |
    |---|---|
    | 3 | Importa Flet. |
    | 6-13 | `main`: página, título, campo (Enter), contador y columna. |
    | 15-19 | `actualizar_contador`: cuenta pendientes y redibuja. |
    | 21-23 | `eliminar_tarea`: quita la fila y recalcula. |
    | 25-31 | `añadir_tarea`: valida que no esté vacío. |
    | 33-46 | Crea la fila (Checkbox + papelera), la añade y recalcula. |
    | 48-50 | Botón y `page.add`. |
    | 53 | Arranca. |
    |  | Explicación detallada: [Paso 8](../pasos/paso8.md). |

??? example "paso9c · clases + before_update"
    ```python linenums="1" title="paso9c_before_update.py"
    --8<-- "codigo/paso9c_before_update.py"
    ```

    | Líneas | Qué hacen |
    |---|---|
    | 1-41 | Clase `Tarea`: igual que en 9a. |
    | 44-63 | `AppTareas.init`: campo, columna, contador y `self.controls` (sin total de creadas). |
    | 65-71 | `clic_añadir`: validación de texto vacío. |
    | 73 | Quita el error si lo había. |
    | 74-77 | Crea la tarea con `on_cambio=self.update`: al marcar una casilla se llama a `self.update()`, que dispara `before_update`. |
    | 78-79 | Vacía el campo y `self.update()`. |
    | 81-83 | `eliminar_tarea`: quita la tarea y `self.update()`. |
    | 85-88 | `before_update`: Flet lo ejecuta **justo antes de cada** `self.update()`. Aquí se recalcula el contador; ya no existe `actualizar_contador`. |
    | 91-94 | `main`: configura la página y añade `AppTareas()`. |
    | 97 | Arranca la app. |

    Más detalle: [Paso 9](../pasos/paso9.md).

??? example "practica_app_final.py"
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

    Más detalle: [Función por función](../funciones/index.md).

??? example "ordenar_funcional.py (práctica + ordenar)"
    ```python linenums="1" title="ordenar_funcional.py"
    --8<-- "codigo/ordenar_funcional.py"
    ```

    | Líneas | Qué hacen |
    |---|---|
    | 1-79 | Igual que `practica_app_final.py`, pero 2 líneas más abajo (por la cabecera de 2 comentarios). |
    | 81-93 | `CRITERIOS`: diccionario de lambdas de ordenación. |
    | 95-101 | `ordenar_tareas(criterio, inverso)`: `sort` + `page.update()`. |
    | 106-164 | `añadir_tarea`: validación, repetidas y creación de la fila. |
    | 167-170 | Botones «Añadir» y «Borrar completadas». |
    | 172-184 | `fila_ordenar`: botones de ordenar con lambda. |
    | 187 | `page.add` con la fila de ordenar entre el contador y la lista. |
    | 190 | Arranca. |

    Más detalle: [Dónde va en el código](../ordenar/donde-va.md).

??? example "ordenar_clases.py"
    ```python linenums="1" title="ordenar_clases.py"
    --8<-- "codigo/ordenar_clases.py"
    ```

    | Líneas | Qué hacen |
    |---|---|
    | 3-5 | Imports. |
    | 8 | `ORDEN_PRIORIDAD`: prioridad → número. |
    | 11-44 | Clase `Tarea` con el campo `prioridad` y su texto en la fila. |
    | 46-85 | `AppTareas.init`: campo, Dropdown de prioridad, contador, botones de ordenar (71-83) y lista. |
    | 87-105 | `clic_añadir`: valida y crea `Tarea` con la prioridad elegida. |
    | 107-109 | `eliminar_tarea`. |
    | 111-121 | `ordenar`: criterios con lambda y `sort`. |
    | 123-125 | `before_update`: recalcula el contador. |
    | 128-131 | `main`. |
    | 134 | Arranca. |

    Más detalle: [Versión con clases](../ordenar/clases.md).
