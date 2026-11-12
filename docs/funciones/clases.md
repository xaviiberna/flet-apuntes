# Clases `Tarea` y `AppTareas`

Versión con clases ([paso 9](../pasos/paso9.md)). Las funciones de la app pasan a ser **métodos**:

| En la versión funcional | En la versión con clases |
|---|---|
| `fila` (una `Row`) | `Tarea` (clase que hereda de `Column`) |
| `fila.controls[0].value` | `tarea.completada` |
| `fila.controls[0].label` | `tarea.nombre` |
| `eliminar_tarea(fila)` + lambda | callback `on_borrar` → `AppTareas.eliminar_tarea(tarea)` |
| `Checkbox(on_change=actualizar_contador)` | callback `on_cambio` |
| `actualizar_contador()` | `before_update()` (se ejecuta solo antes de cada `self.update()`) |
| `añadir_tarea(e)` | `AppTareas.clic_añadir(e)` |
| `ordenar_tareas(criterio)` | `AppTareas.ordenar(criterio)` → [ver](../ordenar/clases.md) |

## Métodos de `Tarea`

| Método | Qué hace |
|---|---|
| `init(self)` | Construye la interfaz de la tarea (casilla + papelera). |
| `cambio_estado(self, e)` | Guarda `self.completada = self.casilla.value` y avisa al dueño con `self.on_cambio()`. |
| `clic_borrar(self, e)` | Avisa al dueño: `self.on_borrar(self)` (le pasa **la propia tarea**, sin lambda). |

## Métodos de `AppTareas`

| Método | Qué hace |
|---|---|
| `init(self)` | Crea campo, contador, columna de tareas y arma `self.controls`. |
| `clic_añadir(self, e)` | Valida, crea `Tarea(...)` pasándole los callbacks y hace `self.update()`. |
| `eliminar_tarea(self, tarea)` | Quita la tarea y `self.update()`. |
| `before_update(self)` | Recalcula el contador. Flet lo llama justo antes de cada `update`. |

!!! tip "Sin lambda"
    Dentro de una clase, `on_click=self.clic_borrar` ya sabe qué tarea es (`self`). Por eso aquí casi no hacen falta lambdas, salvo para pasar un argumento extra (por ejemplo el criterio de ordenar).
