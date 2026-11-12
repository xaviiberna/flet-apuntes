# `eliminar_tarea(fila)`

**Para qué sirve:** quita **una** fila concreta de la lista.

| Recibe | `fila`: la `Row` que hay que borrar (no es `e`) |
|---|---|
| La llama | el `IconButton` de la papelera, mediante `lambda e: eliminar_tarea(fila)` |
| Toca | `tareas.controls`, y vía `actualizar_contador` la pantalla |

```python
def eliminar_tarea(fila):
    tareas.controls.remove(fila)
    actualizar_contador()
```

!!! note "Por qué no es un manejador directo"
    Un manejador solo recibe `e`. Aquí hace falta saber **qué** fila: por eso el botón usa una [lambda](../controles/lambda.md) que captura `fila`.

!!! failure "Error típico"
    `on_click=eliminar_tarea(fila)` (sin lambda): se ejecuta al crear el botón.
