# Botón «Modificar»

**Objetivo:** cambiar el texto de una tarea existente. El texto nuevo se escribe en el campo «Nueva tarea» y se pulsa el lápiz de esa tarea.

## 1. La función (dentro de `main`, antes de `añadir_tarea`)

```python
def modificar_tarea(fila):
    texto = nueva_tarea.value.strip()        # texto nuevo del campo
    if not texto:                            # vacío: avisa y no modifica
        nueva_tarea.error = "Escribe el texto nuevo"
        page.update()
        return
    fila.controls[0].label = texto           # cambia el texto del checkbox de ESA fila
    nueva_tarea.error = None
    nueva_tarea.value = ""
    page.update()
```

## 2. El botón en cada fila (dentro de `añadir_tarea`, en `fila.controls`, **entre el Checkbox y el de eliminar**)

```python
ft.IconButton(
    icon=ft.Icons.EDIT,
    icon_color=ft.Colors.BLUE_400,
    on_click=lambda e: modificar_tarea(fila),   # lambda para pasar la fila
),
```

!!! note "Por qué se puede modificar así"
    `fila.controls[0]` es el `Checkbox`; cambiar su `label` cambia el texto. Como el botón está **dentro** de cada fila y la lambda captura `fila`, cada lápiz modifica **su** tarea (igual que cada papelera borra la suya).

!!! warning "Limitación"
    `modificar_tarea` no comprueba si el texto nuevo ya existe (como sí hace `añadir_tarea`). Es una buena mejora para hacer.

![Modificar](../assets/img/app-modificar.png){ width=600 }
