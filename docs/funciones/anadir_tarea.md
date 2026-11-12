# `añadir_tarea(e)`

**Para qué sirve:** valida el texto, evita repetidas, crea la fila (casilla + lápiz + papelera) y la añade a la lista.

| Recibe | `e`: el evento (no se usa) |
|---|---|
| La llaman | botón «Añadir» (`on_click`) y tecla Enter en el campo (`on_submit`) |
| Toca | `nueva_tarea.error/value`, `mensaje.value`, `tareas.controls` |

## Las 5 fases de la función

```python
def añadir_tarea(e):
    texto = nueva_tarea.value.strip()                    # 1. leer y limpiar

    if not texto:                                        # 2. validar vacío
        nueva_tarea.error = "Escribe una tarea"
        page.update()
        return

    for fila_existente in tareas.controls:               # 3. validar repetida
        if fila_existente.controls[0].label.lower() == texto.lower():
            mensaje.value = f"La tarea '{texto}' ya existe, no se puede añadir"
            page.update()
            return

    mensaje.value = ""
    nueva_tarea.error = None                             # 4. limpiar avisos

    fila = ft.Row()                                      # 5. crear y añadir la fila
    fila.controls = [
        ft.Checkbox(label=texto, expand=True, on_change=actualizar_contador),
        ft.IconButton(icon=ft.Icons.EDIT, icon_color=ft.Colors.BLUE_400,
                      on_click=lambda e: modificar_tarea(fila)),
        ft.IconButton(icon=ft.Icons.DELETE, icon_color=ft.Colors.RED_400,
                      on_click=lambda e: eliminar_tarea(fila)),
    ]
    tareas.controls.append(fila)
    nueva_tarea.value = ""
    actualizar_contador()
```

| Fase | Por qué |
|---|---|
| 1. `strip()` | Quita espacios; «   » cuenta como vacío. |
| 2. `return` si vacío | *Return temprano*: no se crea nada. |
| 3. Bucle de repetidas | Compara en minúsculas con el `label` de cada fila. Ver [repetidas](../practica/repetidas.md). |
| 4. Limpiar avisos | Si llegamos aquí, la tarea es válida. |
| 5. Crear la fila | Se crea `fila` **vacía primero** para que las lambdas puedan capturarla. |

!!! warning "Orden de los botones en la fila"
    `controls[0]` **tiene que ser el Checkbox**: `actualizar_contador`, `borrar_completadas`, `ordenar_tareas`… leen `fila.controls[0]`. Si metes otro control antes, hay que cambiar el índice en todas.
