# Paso 3 · TextField y Button

**Archivo:** `codigo/paso3_controles.py` · **Objetivo:** poner en pantalla los controles de entrada (todavía no hacen nada).

```python title="paso3_controles.py"
--8<-- "codigo/paso3_controles.py"
```

| Código | Qué hace y por qué |
|---|---|
| `ft.TextField(label="Nueva tarea")` | Campo de texto. `label` es la etiqueta flotante. Lo escrito se guarda en `nueva_tarea.value`. |
| `ft.Button(content="Añadir")` | Botón. `content` es lo que se muestra dentro. |
| `page.add(titulo, nueva_tarea, boton)` | Añade varios controles de una vez, uno debajo de otro. |

!!! note "Idea clave"
    Guardamos cada control en una **variable** porque lo necesitaremos para leer lo que escribió el usuario (`nueva_tarea.value`) o modificarlo. Un control sin variable es un control al que no podrás volver.

!!! failure "Errores típicos"
    - Esperar que el botón haga algo: falta el evento ([paso 4](paso4.md)).
    - `ft.Button("Añadir")` o `text=`: según la versión; en la de referencia es `content=`.

!!! question "Prueba tú"
    Añade `hint_text="Ej: comprar pan"` al `TextField`. ¿Qué diferencia hay con `label`?
