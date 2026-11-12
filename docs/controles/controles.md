# Controles usados en la app

| Control | Para qué | Propiedades que usamos |
|---|---|---|
| `ft.Text` | Mostrar texto | `value`, `size`, `weight`, `color` |
| `ft.TextField` | Escribir texto | `label`, `value`, `expand`, `error`, `on_submit` |
| `ft.Button` | Botón con texto | `content`, `on_click` |
| `ft.Checkbox` | Casilla marcable | `label`, `value`, `expand`, `on_change` |
| `ft.IconButton` | Botón con icono | `icon`, `icon_color`, `tooltip`, `on_click` |
| `ft.Row` | Colocar en **horizontal** | `controls`, `alignment`, `wrap`, `spacing` |
| `ft.Column` | Colocar en **vertical** | `controls`, `spacing` |
| `ft.Dropdown` | Elegir una opción | `value`, `options`, `width`, `on_select` |

## `Text`

```python
ft.Text("Mis tareas", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.RED)
```

Cambiar el texto: `contador.value = "..."`. Cambiar el color: `contador.color = ft.Colors.GREEN`.

## `TextField`

| Propiedad | Qué hace |
|---|---|
| `label` | Etiqueta flotante. |
| `hint_text` | Pista que desaparece al escribir. |
| `value` | Lo que hay escrito (leer y escribir). |
| `error` | Mensaje de error en rojo bajo el campo. `None` lo quita. |
| `expand=True` | Ocupa el espacio libre de su fila. |

## `Checkbox`

`value` es `True` / `False`. `label` es el texto. `on_change` se dispara al marcar/desmarcar.

## `IconButton`

Los iconos están en `ft.Icons` (`DELETE`, `EDIT`, `CLOSE`, `DELETE_OUTLINE`…). Escribe `ft.Icons.` en el editor y verás todos. Los colores, en `ft.Colors`.

## `Row` y `Column`

Reciben una lista de hijos (`controls`). Los hijos de una `Column` están en `tareas.controls`: una **lista normal de Python** que puedes `append`, `remove`, `sort`…

| Propiedad | Para qué |
|---|---|
| `expand=True` (en un hijo) | Reparte el espacio libre |
| `alignment=ft.MainAxisAlignment.SPACE_BETWEEN` | Separa los hijos a los extremos |
| `wrap=True` | Salta de línea si no caben |
| `spacing=20` | Separación entre hijos |

## `Dropdown`

```python
ft.Dropdown(
    value="Media",
    options=[ft.DropdownOption(key="Alta"), ft.DropdownOption(key="Media"), ft.DropdownOption(key="Baja")],
)
```

`value` es la `key` de la opción elegida. Evento de selección: `on_select` (en versiones antiguas, `on_change`).

!!! note "El índice `controls[0]`"
    En la fila de tarea: `[0]` = Checkbox, `[1]` = lápiz, `[2]` = papelera. Las funciones leen `fila.controls[0]`, por eso **el Checkbox debe ir primero**.
