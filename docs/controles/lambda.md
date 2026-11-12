# `lambda` explicada: los 3 usos en la app

Una **lambda** es una función de una línea sin nombre: `lambda argumentos: expresión`.

```python
def doble(x):          # equivale a:   doble = lambda x: x * 2
    return x * 2
```

## Uso 1 · Pasar un dato extra a un manejador

Flet solo entrega `e`. Para pasar además la `fila`:

```python
ft.IconButton(icon=ft.Icons.DELETE, on_click=lambda e: eliminar_tarea(fila))
```

La lambda recibe `e` y llama a tu función con lo que necesitas. Cada fila tiene su propia variable `fila`, por eso cada papelera borra la suya.

## Uso 2 · Retrasar la llamada a una función que aún no existe

```python
nueva_tarea = ft.TextField(on_submit=lambda e: añadir_tarea(e))   # añadir_tarea se define más abajo
```

Python busca `añadir_tarea` **cuando se pulsa Enter**, no al crear el campo. Alternativa sin lambda: asignar después de definirla, `nueva_tarea.on_submit = añadir_tarea`.

## Uso 3 · Función `key` para ordenar

```python
tareas.controls.sort(key=lambda fila: fila.controls[0].label.lower())
```

Aquí la lambda **no recibe `e`**: recibe **cada elemento de la lista** y devuelve el valor por el que comparar. → [Ordenar listas](../ordenar/index.md)

| | Parámetro de la lambda | Quién la llama |
|---|---|---|
| Uso 1 y 2 (`on_click`, `on_submit`) | `e` (el evento) | Flet, al ocurrir el evento |
| Uso 3 (`key=`) | cada elemento de la lista | `sort`, una vez por elemento |

!!! failure "Error típico"
    `on_click=lambda: eliminar_tarea(fila)` — falta `e`. Flet le pasa un argumento y la lambda no lo acepta → `TypeError`.
