# Paso 5 · Layouts (Row y Column) y Checkbox

**Archivo:** `codigo/paso5_layouts_checkbox.py` · **Objetivo:** campo y botón en la misma fila; cada tarea es una casilla.

```python linenums="1" title="paso5_layouts_checkbox.py" hl_lines="11 15 22"
--8<-- "codigo/paso5_layouts_checkbox.py"
```

| Código | Qué hace y por qué |
|---|---|
| `TextField(..., expand=True)` | Ocupa **todo el espacio libre** de su fila; el botón queda a la derecha. |
| `ft.Checkbox(label=...)` | Cada tarea es una casilla. Su estado está en `.value` (`True` = marcada). |
| `ft.Row([nueva_tarea, boton])` | Coloca los controles **en horizontal**. `Column` hace lo mismo en vertical. |
| `page.add(titulo, fila_entrada, tareas)` | Ya no añadimos `nueva_tarea` y `boton` sueltos: están dentro de la fila. |

!!! note "Idea clave"
    Una interfaz Flet es un **árbol**: la página contiene controles y los layouts (`Row`, `Column`) contienen más controles. `expand=True` solo funciona **dentro** de una `Row` o `Column`.

!!! failure "Errores típicos"
    - Añadir el mismo control a `page` y a una `Row`: solo puede estar en un sitio.
    - `expand=True` en un control suelto de la página: no hace nada.

!!! question "Prueba tú"
    Cambia `ft.Row` por `ft.Column` en `fila_entrada`. Prueba `spacing=20`.
