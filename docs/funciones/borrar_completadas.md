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

!!! danger "`list(...)` es imprescindible"
    Recorrer una lista y borrar de ella a la vez salta elementos. `list(tareas.controls)` crea una copia para recorrer.

Alternativa equivalente en una sola línea:

```python
tareas.controls = [f for f in tareas.controls if not f.controls[0].value]
actualizar_contador()
```
