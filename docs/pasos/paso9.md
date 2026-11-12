# Paso 9 · Clases: cada tarea es un control propio

Misma app, pero organizada con **POO**. Son tres versiones; cada una mejora la anterior.

=== "9a · Clase `Tarea`"

    **Archivo:** `codigo/paso9a_clase_tarea.py`. Cada tarea ya es una clase; `main` sigue siendo funcional.

    ```python title="paso9a_clase_tarea.py" hl_lines="8-9 16-17 36-41 73-75"
    --8<-- "codigo/paso9a_clase_tarea.py"
    ```

=== "9b · Clase `AppTareas`"

    **Archivo:** `codigo/paso9b_clase_apptareas.py`. **Toda** la app es un control; `main` solo hace `page.add(AppTareas())`. Incluye el contador «Total de tareas creadas».

    ```python title="paso9b_clase_apptareas.py" hl_lines="44-45 70-89"
    --8<-- "codigo/paso9b_clase_apptareas.py"
    ```

=== "9c · `before_update`"

    **Archivo:** `codigo/paso9c_before_update.py`. Un **único sitio** donde se recalcula lo derivado; los manejadores solo cambian datos y llaman a `self.update()`.

    ```python title="paso9c_before_update.py" hl_lines="74-77 85-88"
    --8<-- "codigo/paso9c_before_update.py"
    ```

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
