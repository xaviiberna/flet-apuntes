# Paso 4 · Eventos: reaccionar al clic

**Archivo:** `codigo/paso4_eventos.py` · **Objetivo:** que el botón añada una tarea a la pantalla.

**Novedades:** `ft.Column` como contenedor · funciones manejadoras y el parámetro `e` · `on_click` · **regla de oro: modificar → `page.update()`**

```python title="paso4_eventos.py" hl_lines="12 15-18 20"
--8<-- "codigo/paso4_eventos.py"
```

| Código | Qué hace y por qué |
|---|---|
| `tareas = ft.Column()` | Columna vacía. Sus hijos están en `tareas.controls`, una **lista normal de Python**. |
| `def añadir_tarea(e):` | Manejador. Flet le pasa siempre `e` (el evento). Aunque no se use, debe existir. |
| `tareas.controls.append(ft.Text(nueva_tarea.value))` | Lee el campo, crea un `Text` y lo añade a la lista de hijos. |
| `nueva_tarea.value = ""` | Vacía el campo. |
| `page.update()` | Envía los cambios a la pantalla. |
| `on_click=añadir_tarea` | Asocia el clic con la función. **Sin paréntesis**: Flet la ejecuta cuando haya clic. |

!!! note "Idea clave"
    El flujo siempre es: **usuario hace algo → manejador → modifica datos → `page.update()`**. La función está dentro de `main` para poder usar `nueva_tarea`, `tareas` y `page` sin pasarlos como parámetros.

!!! failure "Errores típicos"
    - `on_click=añadir_tarea()` con paréntesis: se ejecuta al arrancar.
    - Olvidar `page.update()`.
    - `def añadir_tarea():` sin `e`.

!!! question "Prueba tú"
    1. `print(nueva_tarea.value)` dentro del manejador: mira la consola.
    2. Añade un `Text` llamado `mensaje` en verde: «Tarea XXX, añadida correctamente».
    3. Añade un `Text` llamado `contenido_evento` que muestre el contenido de `e`.
