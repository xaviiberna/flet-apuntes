# Paso 9 · Clases: cada tarea es un control propio

Misma app, pero organizada con **POO**. Son tres versiones; cada una mejora la anterior.

=== "9a · Clase `Tarea`"

    **Archivo:** `codigo/paso9a_clase_tarea.py`. Cada tarea ya es una clase; `main` sigue siendo funcional.

    ```python linenums="1" title="paso9a_clase_tarea.py" hl_lines="8-9 16-17 36-41 73-75"
    --8<-- "codigo/paso9a_clase_tarea.py"
    ```

    | Líneas | Qué hacen |
    |---|---|
    | 1-2 | Comentarios: qué es este paso. |
    | 3 | `from typing import Callable`: tipo «función», para anotar los callbacks. |
    | 5 | Importa Flet. |
    | 8 | `@ft.control`: convierte la clase en un control de Flet. |
    | 9 | `class Tarea(ft.Column)`: una tarea **es** una columna (hereda de `Column`). |
    | 10 | `nombre: str = ""`: campo; se rellena al crear `Tarea(nombre="Pan")`. |
    | 13-14 | `on_borrar` y `on_cambio`: funciones que le pasa `main` (callbacks). `None` = ninguna por defecto. |
    | 16 | `def init(self)`: se ejecuta al crear la tarea; aquí se construye lo que se ve. |
    | 18 | `self.completada = False`: dato propio; la tarea empieza pendiente. |
    | 19-21 | `self.casilla`: el `Checkbox` con el nombre; al marcarlo llama a `self.cambio_estado`. |
    | 22-34 | `self.controls`: lo que se dibuja. Una `Row` con la casilla y la papelera; `SPACE_BETWEEN` las separa a los extremos. |
    | 27-31 | `IconButton` papelera con `tooltip` (texto al pasar el ratón). `on_click=self.clic_borrar`: no hace falta lambda, `self` ya es la tarea. |
    | 36-38 | `cambio_estado`: guarda si está marcada en `self.completada` y avisa a `main` con `self.on_cambio()`. |
    | 40-41 | `clic_borrar`: avisa a `main` pasándole **la propia tarea** (`self`). |
    | 44-53 | `main`: página, título, campo (Enter con lambda), contador y columna de tareas, igual que en el paso 8. |
    | 55-58 | `actualizar_contador`: cuenta las tareas con `tarea.completada` en vez de `fila.controls[0].value`. |
    | 60-62 | `eliminar_tarea(tarea)`: quita la tarea que le pasa `clic_borrar` y recalcula. |
    | 64-70 | `añadir_tarea`: lee el texto y, si está vacío, muestra error y sale. |
    | 72-75 | Crea `Tarea(...)` pasándole el texto y las dos funciones (callbacks) y la añade a la lista. |
    | 76-77 | Vacía el campo y recalcula el contador. |
    | 79-81 | Botón «Añadir» y `page.add` con todo. |
    | 84 | Arranca la app. |

=== "9b · Clase `AppTareas`"

    **Archivo:** `codigo/paso9b_clase_apptareas.py`. **Toda** la app es un control; `main` solo hace `page.add(AppTareas())`. Incluye el contador «Total de tareas creadas».

    ```python linenums="1" title="paso9b_clase_apptareas.py" hl_lines="44-45 70-89"
    --8<-- "codigo/paso9b_clase_apptareas.py"
    ```

    | Líneas | Qué hacen |
    |---|---|
    | 1-41 | Clase `Tarea`: igual que en 9a (ver esa pestaña). |
    | 44-45 | `class AppTareas(ft.Column)`: **toda la app** es un control. |
    | 46 | `init`: construye la app. |
    | 47-49 | `self.nueva_tarea`: campo de texto; Enter llama a `self.clic_añadir` (sin lambda: el método ya existe). |
    | 50-51 | `self.tareas` (columna de tareas) y `self.contador` (texto de pendientes). |
    | 53-54 | `self.total_creadas = 0`: número de tareas creadas; `self.texto_total_creadas`: el texto que lo muestra. |
    | 57-68 | `self.controls`: lo que se ve, en orden: título, fila campo+botón, contador, total y lista. |
    | 70-76 | `clic_añadir`: lee el texto; si está vacío, error y `return`. Usa `self.update()` en vez de `page.update()`. |
    | 78-85 | Crea `Tarea` pasando **métodos** como callbacks: `self.eliminar_tarea` y `self.actualizar_contador`. |
    | 86 | Vacía el campo. |
    | 87-88 | Suma 1 al total y actualiza su texto. |
    | 89 | Recalcula el contador (que hace `self.update()`). |
    | 91-93 | `eliminar_tarea`: quita la tarea y recalcula. |
    | 95-98 | `actualizar_contador`: cuenta pendientes, cambia el texto y `self.update()`. |
    | 102-105 | `main`: solo configura la página y añade `AppTareas()`. |
    | 108 | Arranca la app. |

=== "9c · `before_update`"

    **Archivo:** `codigo/paso9c_before_update.py`. Un **único sitio** donde se recalcula lo derivado; los manejadores solo cambian datos y llaman a `self.update()`.

    ```python linenums="1" title="paso9c_before_update.py" hl_lines="74-77 85-88"
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

## Qué significa cada pieza nueva

| Pieza | Qué es |
|---|---|
| `@ft.control` | Decorador: convierte la clase en un control de Flet (como una dataclass). Los campos con tipo (`nombre: str = ""`) se pueden pasar al crear: `Tarea(nombre="Pan")`. |
| `class Tarea(ft.Column)` | La clase **hereda** de `Column`: es una columna con tus propias cosas. |
| `def init(self)` | Se ejecuta **al crear** el control: aquí se construye su interfaz (no es `__init__`). |
| `on_borrar`, `on_cambio` | **Callbacks**: funciones que pasa el «dueño» de la lista. Prefijo `on_` = convención de Flet. |
| `Callable \| None = None` | Tipo: «una función o nada». |
| `self.casilla`, `self.completada` | Datos propios de cada tarea: ya no hace falta `fila.controls[0].value`. |
| `before_update(self)` | Flet lo llama **justo antes de cada `self.update()`**. |
| `on_cambio=self.update` | Se pasa el método **sin paréntesis** como callback. |

!!! note "Qué se gana"
    - `t.completada` y `t.nombre` en lugar de `fila.controls[0].value` / `.label` (se acabaron los índices mágicos).
    - Cada tarea sabe pintarse y reaccionar a sus eventos.
    - Con `before_update`, **añadir/borrar/marcar** solo hacen `self.update()` y el contador se recalcula solo.

!!! tip "Ordenar aquí es más fácil"
    Con clases la lambda queda más corta: `sort(key=lambda t: t.nombre.lower())` → [Ordenar en la versión con clases](../ordenar/clases.md).
