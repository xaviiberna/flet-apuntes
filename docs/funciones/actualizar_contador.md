# `actualizar_contador(e=None)`

**Para qué sirve:** recalcula cuántas tareas están pendientes, actualiza el texto del contador y su color.

| Recibe | `e` (opcional): el evento, si lo llama Flet. Vale `None` si la llamas tú. |
|---|---|
| Devuelve | nada |
| La llaman | `Checkbox` (`on_change`), `añadir_tarea`, `eliminar_tarea`, `borrar_completadas` |
| Toca | `contador.value`, `contador.color`, `page.update()` |

```python
def actualizar_contador(e=None):
    pendientes = sum(1 for fila in tareas.controls if not fila.controls[0].value)
    contador.value = f"Tareas pendientes: {pendientes}"

    if pendientes == 0:
        contador.color = ft.Colors.RED
    else:
        contador.color = ft.Colors.GREEN

    page.update()
```

| Línea | Qué hace |
|---|---|
| `e=None` | Se puede usar como manejador **y** llamar sin argumentos. |
| `sum(1 for ... if not ...value)` | Cuenta las filas cuyo Checkbox (`controls[0]`) está **sin marcar**. |
| `contador.value = f"..."` | Cambia el texto con el número. |
| `if pendientes == 0` | Rojo si no queda nada, verde si queda algo. |
| `page.update()` | Redibuja. Como está aquí, quien la llame **no** necesita su propio `update`. |

!!! tip "Por qué se recalcula entero"
    Más fiable que sumar/restar 1 en cada evento. Ver [Paso 8](../pasos/paso8.md).
