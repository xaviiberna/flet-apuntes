# Paso 6 · Borrar tareas: IconButton y lambda

**Archivo:** `codigo/paso6_borrar_tareas.py` · **Objetivo:** cada tarea es una fila con casilla + botón de borrar.

```python title="paso6_borrar_tareas.py" hl_lines="14-16 19-28"
--8<-- "codigo/paso6_borrar_tareas.py"
```

| Código | Qué hace y por qué |
|---|---|
| `def eliminar_tarea(fila):` | Función normal que recibe **qué fila** borrar. No es un manejador directo (esos solo reciben `e`). |
| `tareas.controls.remove(fila)` | `remove` de las listas de Python: quita esa fila. |
| `fila = ft.Row()` y luego `fila.controls = [...]` | Se crea vacía primero para que el botón pueda referirse a **su propia fila**. |
| `Checkbox(..., expand=True)` | La casilla ocupa el espacio y empuja el icono a la derecha. |
| `IconButton(icon=ft.Icons.DELETE, icon_color=...)` | Botón con icono en vez de texto. |
| `on_click=lambda e: eliminar_tarea(fila)` | La **lambda** recibe `e` y llama a `eliminar_tarea` con la fila correcta. Más en [lambda explicada](../controles/lambda.md). |
| `tareas.controls.append(fila)` | Añade la fila completa. |

!!! note "Idea clave"
    Flet solo entrega `e`, pero aquí necesitamos más datos (qué fila). La **lambda** hace de intermediaria. Cada fila creada tiene su propia variable `fila`, por eso cada botón borra la suya.

!!! failure "Errores típicos"
    - `on_click=eliminar_tarea(fila)`: se ejecuta al crear el botón.
    - Olvidar `page.update()` tras `remove`.

!!! question "Prueba tú"
    1. Cambia el icono por `ft.Icons.CLOSE` o `DELETE_OUTLINE`.
    2. Muestra en rojo «Tarea XXX, Borrada Correctamente».
