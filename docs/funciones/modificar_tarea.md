# `modificar_tarea(fila)`

**Para qué sirve:** cambia el texto de una tarea por lo que haya escrito en el campo «Nueva tarea».

| Recibe | `fila`: la fila cuyo lápiz se pulsó |
|---|---|
| La llama | el `IconButton` EDIT, mediante `lambda e: modificar_tarea(fila)` |
| Toca | `fila.controls[0].label`, `nueva_tarea.error/value` |

```python
def modificar_tarea(fila):
    texto = nueva_tarea.value.strip()
    if not texto:
        nueva_tarea.error = "Escribe el texto nuevo"
        page.update()
        return
    fila.controls[0].label = texto
    nueva_tarea.error = None
    nueva_tarea.value = ""
    page.update()
```

| Código | Qué hace |
|---|---|
| `def modificar_tarea(fila):` | Recibe la fila cuyo lápiz se ha pulsado. |
| `texto = nueva_tarea.value.strip()` | Lee el texto nuevo del campo «Nueva tarea», sin espacios. |
| `if not texto:` | Si está vacío… |
| `nueva_tarea.error = "Escribe el texto nuevo"` | …muestra un error bajo el campo, |
| `page.update() / return` | …lo dibuja y sale sin cambiar nada. |
| `fila.controls[0].label = texto` | Cambia el texto del Checkbox (`controls[0]`) de **esa** fila. |
| `nueva_tarea.error = None` | Quita el error si lo había. |
| `nueva_tarea.value = ""` | Vacía el campo. |
| `page.update()` | Redibuja para que se vea el texto nuevo. |

!!! note "No llama a `actualizar_contador`"
    Cambiar el texto no cambia cuántas hay pendientes ni su estado, así que basta `page.update()`.

!!! tip "Mejora propuesta"
    Comprobar también que el texto nuevo no coincide con otra tarea (el mismo bucle de [repetidas](../practica/repetidas.md), saltándose la propia fila).
