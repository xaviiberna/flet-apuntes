# Paso 7 · Validación y tecla Enter

**Archivo:** `codigo/paso7_validacion.py` · **Objetivo:** no permitir tareas vacías y añadir con Enter.

```python linenums="1" title="paso7_validacion.py" hl_lines="12 20-27"
--8<-- "codigo/paso7_validacion.py"
```

| Código | Qué hace y por qué |
|---|---|
| `on_submit=lambda e: añadir_tarea(e)` | Se dispara al pulsar **Enter**. Lambda porque `añadir_tarea` se define *después* del campo: Python la busca cuando ocurre el evento. |
| `.value.strip()` | Quita espacios sobrantes: una tarea con solo espacios cuenta como vacía. |
| `if not texto:` | Un texto vacío es «falso», así que `not texto` es verdadero si no hay nada. |
| `nueva_tarea.error = "Escribe una tarea"` | Muestra un error en rojo bajo el campo. |
| `page.update()` + `return` | Actualiza y **sale**: el código de debajo no se ejecuta. |
| `nueva_tarea.error = None` | Si es válida, quita el error anterior. |

!!! tip "Alternativa sin lambda"
    Se puede asignar **después** de definir la función: `nueva_tarea.on_submit = añadir_tarea`. (Así lo hace el paso 8 de los apuntes.)

!!! note "Idea clave"
    Validar = comprobar los datos **antes** de modificar el estado. Patrón: comprobar → si falla, avisar y `return` → si pasa, continuar (*return temprano*).

!!! failure "Errores típicos"
    - Olvidar `error = None`: el error se queda aunque ya escribas.
    - No poner `return` tras el error: se añade la tarea vacía.

!!! question "Prueba tú"
    Impide tareas **duplicadas** y muestra en naranja «Tarea XXX ya existe, no se puede añadir» → [resuelto en la práctica](../practica/repetidas.md).
