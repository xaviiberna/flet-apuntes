# `main(page)`

**Para qué sirve:** es la función que Flet ejecuta al arrancar. Crea los controles, define las demás funciones y lo añade todo a la página.

| Recibe | `page`: la ventana de la app |
|---|---|
| Devuelve | nada |
| La llama | Flet, a través de `ft.run(main)` |

## Orden de las cosas dentro de `main`

1. **Propiedades de la página** (`title`, `padding`).
2. **Controles** que luego se usarán (`titulo`, `nueva_tarea`, `contador`, `mensaje`, `tareas`).
3. **Funciones internas** (`actualizar_contador`, `eliminar_tarea`, …).
4. **Botones** (después de definir las funciones que usan).
5. **`page.add(...)`** con todo en el orden en que se verá.

```python
def main(page: ft.Page):
    page.title = "Lista de tareas"
    page.padding = 20
    titulo = ft.Text("Mis tareas", size=30, weight=ft.FontWeight.BOLD)
    ...
    page.add(titulo, ft.Row([nueva_tarea, boton]), mensaje, contador, tareas, boton_borrar)

ft.run(main)
```

| Código | Qué hace |
|---|---|
| `def main(page: ft.Page):` | Define la función principal; `page` es la ventana. |
| `page.title = "Lista de tareas"` | Título de la ventana. |
| `page.padding = 20` | Margen interior de 20 px. |
| `titulo = ft.Text(...)` | Crea el título; el `...` representa el resto de controles y funciones. |
| `page.add(...)` | Añade todo a la página en el orden en que se verá. |
| `ft.run(main)` | Arranca la app con esa función. |

!!! note "Por qué las funciones están *dentro* de `main`"
    Así pueden usar `page`, `tareas`, `nueva_tarea`, `contador`… sin recibirlos como parámetros. A cambio, `main` crece. Con clases ([paso 9](../pasos/paso9.md)) esto se ordena.
