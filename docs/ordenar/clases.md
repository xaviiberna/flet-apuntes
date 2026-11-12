# Ordenar en la versión con clases

Archivo: `codigo/ordenar_clases.py` (basado en el [paso 9c](../pasos/paso9.md)). Aquí cada `Tarea` guarda sus propios datos, así que las lambdas son **más cortas y más claras**:

| Versión funcional | Versión con clases |
|---|---|
| `lambda fila: fila.controls[0].label.lower()` | `lambda t: t.nombre.lower()` |
| `lambda fila: fila.controls[0].value` | `lambda t: t.completada` |
| (no hay dónde guardar prioridad) | `lambda t: ORDEN_PRIORIDAD[t.prioridad]` |

## Los 4 cambios sobre el paso 9c

=== "1 · Diccionario de prioridades (arriba del todo)"

    ```python
    ORDEN_PRIORIDAD = {"Alta": 0, "Media": 1, "Baja": 2}
    ```

    | Código | Qué hace |
    |---|---|
    | `ORDEN_PRIORIDAD = {...}` | Traduce prioridad → número para que Alta (0) vaya antes que Baja (2). |

=== "2 · Campo nuevo en `Tarea`"

    ```python
    @ft.control
    class Tarea(ft.Column):
        nombre: str = ""
        prioridad: str = "Media"      # NUEVO: para poder ordenar por prioridad
    ```

    | Código | Qué hace |
    |---|---|
    | `@ft.control / class Tarea(ft.Column)` | La clase de la tarea (ver paso 9). |
    | `nombre: str = ""` | Campo con el texto. |
    | `prioridad: str = "Media"` | Campo nuevo; se pasa al crear: `Tarea(nombre=..., prioridad="Alta")`. |

    Y se muestra en la fila: `ft.Text(self.prioridad)`.

=== "3 · Dropdown en `AppTareas.init`"

    ```python
    self.prioridad = ft.Dropdown(
        value="Media",
        width=130,
        options=[ft.DropdownOption(key=p) for p in ORDEN_PRIORIDAD],
    )
    ```

    | Código | Qué hace |
    |---|---|
    | `ft.Dropdown(...)` | Desplegable para elegir la prioridad de la tarea nueva. |
    | `value="Media"` | Opción elegida al empezar. |
    | `width=130` | Ancho fijo en píxeles. |
    | `[ft.DropdownOption(key=p) for p in ORDEN_PRIORIDAD]` | Crea una opción por cada clave del diccionario: Alta, Media, Baja. |

    Y se lee al añadir: `Tarea(nombre=texto, prioridad=self.prioridad.value, ...)`.

    !!! info "Versión de Flet"
        En Flet 1.0 se usa `ft.DropdownOption`. En versiones antiguas era `ft.dropdown.Option`. Para **leer** el valor basta `self.prioridad.value`; no hace falta ningún evento.

=== "4 · Método `ordenar` + botones"

    ```python linenums="111" title="Método de AppTareas (líneas 111-121)"
    --8<-- "codigo/ordenar_clases.py:111:121"
    ```

    | Código | Qué hace |
    |---|---|
    | `def ordenar(self, criterio, inverso=False):` | Método de `AppTareas` que ordena. |
    | `criterios = {...}` | Criterios: nombre → lambda. Aquí `t` es una `Tarea`. |
    | `lambda t: t.nombre.lower()` | A-Z por nombre. |
    | `lambda t: t.completada` | Pendientes primero. |
    | `lambda t: ORDEN_PRIORIDAD[t.prioridad]` | Por prioridad: Alta, Media, Baja. |
    | `lambda t: (ORDEN_PRIORIDAD[...], t.nombre.lower())` | Por prioridad y, dentro, A-Z. |
    | `self.tareas.controls.sort(...)` | Ordena la lista de tareas. |
    | `self.update()` | Redibuja (antes se ejecuta `before_update`). |

    ```python linenums="71" title="Botones dentro de self.controls (líneas 71-83)"
    --8<-- "codigo/ordenar_clases.py:71:83"
    ```

    | Código | Qué hace |
    |---|---|
    | `ft.Row(wrap=True, controls=[...])` | Fila de botones que salta de línea si no cabe. |
    | `lambda e: self.ordenar("nombre")` | A-Z. |
    | `self.ordenar("nombre", True)` | Z-A (segundo argumento = `inverso`). |
    | `self.ordenar("estado")` | Pendientes primero. |
    | `self.ordenar("prioridad")` | Por prioridad. |
    | `self.ordenar("prioridad_nombre")` | Prioridad y A-Z. |

## Dónde va cada cosa

| Pieza | Dentro de… | Posición |
|---|---|---|
| `ORDEN_PRIORIDAD` | el módulo | fuera de las clases, arriba |
| campo `prioridad` | `class Tarea` | junto a `nombre` |
| `Dropdown` y fila de botones | `AppTareas.init` | y se añaden a `self.controls` |
| `def ordenar(...)` | `class AppTareas` | como método, junto a `eliminar_tarea` |

!!! note "`self.update()` y `before_update`"
    `ordenar` termina con `self.update()`. Como el contador se recalcula en `before_update`, no hay que tocarlo: el número seguirá bien tras ordenar.

!!! tip "Lambda para pasar el criterio"
    `on_click=lambda e: self.ordenar("nombre")`: aquí **sí** hace falta lambda porque el método necesita un argumento extra (el criterio).

## Resultado esperado (prueba)

Añade: `b`(Baja), `a`(Media), `c`(Alta), `d`(Baja), `e`(Alta) y pulsa **Por prioridad** → `c, e, a, b, d`. Fíjate en que `c` va antes que `e` y `b` antes que `d`: la ordenación es **estable**, mantiene el orden de inserción entre iguales.
