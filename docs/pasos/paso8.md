# Paso 8 · App final: contador de tareas pendientes

**Archivo:** `codigo/paso8_app_final.py` · **Objetivo:** mantener un dato **derivado** (el contador) siempre sincronizado con el estado.

**Novedades:** `Checkbox(on_change=...)` · estado derivado · `e=None` · expresión generadora en `sum` · f-strings.

```python title="paso8_app_final.py" hl_lines="12 15-19 37 46"
--8<-- "codigo/paso8_app_final.py"
```

| Código | Qué hace y por qué |
|---|---|
| `contador = ft.Text("Tareas pendientes: 0")` | Texto en variable para poder cambiar su `value`. |
| `def actualizar_contador(e=None)` | `e=None` permite llamarla de dos formas: como manejador (Flet pasa `e`) o directamente sin argumentos. |
| `sum(1 for fila in tareas.controls if not fila.controls[0].value)` | Recorre las filas; `controls[0]` es el `Checkbox`; cuenta 1 por cada no marcado. |
| `f"Tareas pendientes: {pendientes}"` | f-string: mete el número dentro del texto. |
| `Checkbox(..., on_change=actualizar_contador)` | Se dispara al marcar/desmarcar. |
| `eliminar_tarea` / `añadir_tarea` → `actualizar_contador()` | Todo lo que puede cambiar el número lo recalcula. Esta función ya hace `page.update()`. |

La línea del `sum` sin comprimir:

```python
pendientes = 0
for fila in tareas.controls:
    checkbox = fila.controls[0]
    if not checkbox.value:
        pendientes += 1
```

!!! note "Idea clave"
    El contador **no es un dato independiente**: se deduce de las casillas. En vez de sumar/restar 1 en cada evento (fácil equivocarse), se **recalcula entero** cada vez. Una función hace el cálculo y la llaman todos los eventos.

!!! failure "Errores típicos"
    - Olvidar `on_change`: el contador no cambia al marcar.
    - Llamar a `actualizar_contador` **antes** de añadir la fila: va un paso por detrás.
    - `fila.controls[1]` en vez de `[0]`: el índice 1 es el `IconButton`, que no tiene `value`.

!!! question "Prueba tú"
    Añade «Borrar completadas» → [resuelto en la práctica](../practica/borrar-completadas.md).
