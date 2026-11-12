# Paso 2 · Propiedades de la página y estilo de un Text

**Archivo:** `codigo/paso2_pagina_y_texto.py` · **Objetivo:** configurar la página y dar formato a un control.

**Novedades:** `page.title`, `padding`, `theme_mode` · argumentos con nombre (`size`, `weight`) · enumeraciones.

```python linenums="1" title="paso2_pagina_y_texto.py"
--8<-- "codigo/paso2_pagina_y_texto.py"
```

| Código | Qué hace y por qué |
|---|---|
| `page.title = "Lista de tareas"` | Texto de la barra de la ventana (o pestaña del navegador). |
| `page.padding = 20` | Espacio interior entre el borde y el contenido (20 px). |
| `page.theme_mode = ft.ThemeMode.LIGHT` | Tema claro. Otras opciones: `DARK`, `SYSTEM`. `ThemeMode` es una **enumeración**: lista cerrada de valores válidos. |
| `ft.Text("Mis tareas", size=30, weight=ft.FontWeight.BOLD)` | `size` = tamaño, `weight` = grosor (`BOLD` = negrita). |
| `titulo = ...` | Guardamos el control en una variable para poder modificarlo luego. |
| `page.add(titulo)` | Añade el control ya creado. |

!!! note "Idea clave"
    Todo se configura con **propiedades**, al crear el control o después (`titulo.size = 20`). Si el valor debe ser de una lista cerrada, se usa una **enumeración** (`ft.FontWeight.` + autocompletar).

!!! failure "Errores típicos"
    - `weight="bold"` como texto: usa `ft.FontWeight.BOLD`.
    - Cambiar una propiedad y no ver el cambio: falta `page.update()` ([paso 4](paso4.md)).

!!! question "Prueba tú"
    Pon `ft.ThemeMode.DARK` y añade `color=ft.Colors.BLUE` al título.
