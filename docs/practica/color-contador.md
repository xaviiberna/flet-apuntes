# Color del contador (rojo / verde)

**Objetivo:** rojo si no hay tareas pendientes, verde si hay alguna.

## 1. Color inicial (al crear el contador)

Empezamos sin tareas, así que arranca en rojo:

```python
contador = ft.Text("Tareas pendientes: 0", color=ft.Colors.RED)
```

| Código | Qué hace |
|---|---|
| `ft.Text("Tareas pendientes: 0", ...)` | Texto del contador con el valor inicial. |
| `color=ft.Colors.RED` | Empieza en rojo porque al arrancar hay 0 pendientes. |

## 2. Cambio de color (dentro de `actualizar_contador`, tras calcular `pendientes`)

```python
if pendientes == 0:
    contador.color = ft.Colors.RED
else:
    contador.color = ft.Colors.GREEN
```

| Código | Qué hace |
|---|---|
| `if pendientes == 0:` | Si no queda ninguna tarea pendiente… |
| `contador.color = ft.Colors.RED` | …pone el texto en rojo. |
| `else:` | Si queda alguna… |
| `contador.color = ft.Colors.GREEN` | …lo pone en verde. Se verá al hacer el `page.update()` del final de la función. |

!!! note "Por qué en `actualizar_contador`"
    Es la función que **todos los eventos** (añadir, borrar, marcar) ya llaman. Poniendo ahí el color, siempre está sincronizado con el número. Es el mismo principio del [estado derivado](../pasos/paso8.md).

| Sin tareas | 1 pendiente | Todo marcado |
|---|---|---|
| ![](../assets/img/contador-rojo.png){ width=200 } | ![](../assets/img/contador-verde.png){ width=200 } | ![](../assets/img/contador-rojo-marcado.png){ width=200 } |
