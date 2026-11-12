# `borrar_completadas(e)`

**Para qué sirve:** elimina todas las tareas marcadas.

| Recibe | `e` (no se usa) |
|---|---|
| La llama | botón «Borrar completadas» (`on_click=borrar_completadas`) |
| Toca | `tareas.controls`, y vía `actualizar_contador` la pantalla |

```python
def borrar_completadas(e):
    for fila in list(tareas.controls):
        if fila.controls[0].value:
            tareas.controls.remove(fila)
    actualizar_contador()
```

| Código | Qué hace |
|---|---|
| `def borrar_completadas(e):` | Manejador del botón: recibe el evento `e` (no se usa). |
| `for fila in list(tareas.controls):` | Recorre una **copia** de la lista de filas, para poder borrar de la original sin saltarse ninguna. |
| `if fila.controls[0].value:` | Si el Checkbox de la fila está marcado (`True`)… |
| `tareas.controls.remove(fila)` | …quita esa fila de la lista. |
| `actualizar_contador()` | Recalcula el contador y redibuja (esa función hace `page.update()`). |

!!! danger "`list(...)` es imprescindible"
    Recorrer una lista y borrar de ella a la vez salta elementos. `list(tareas.controls)` crea una copia para recorrer.

Alternativa equivalente en una sola línea:

```python
tareas.controls = [f for f in tareas.controls if not f.controls[0].value]
actualizar_contador()
```

| Código | Qué hace |
|---|---|
| `[f for f in tareas.controls ...]` | Lista por comprensión: crea una lista nueva con las filas… |
| `if not f.controls[0].value` | …que **no** están marcadas. |
| `tareas.controls = ...` | Sustituye la lista vieja por la nueva (las marcadas desaparecen). |
| `actualizar_contador()` | Recalcula y redibuja. |
