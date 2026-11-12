# `ordenar_tareas(criterio, inverso=False)` · nueva

**Para qué sirve:** reordena las tareas en pantalla según un criterio (A-Z, pendientes primero, longitud…).

| Recibe | `criterio`: nombre del criterio (clave del diccionario `CRITERIOS`) · `inverso`: `True` para orden descendente |
|---|---|
| Devuelve | nada |
| La llaman | los botones de ordenar, mediante `lambda e: ordenar_tareas("az")` |
| Toca | el **orden** de `tareas.controls` (no cambia las filas, solo su posición) |

```python linenums="81" title="codigo/ordenar_funcional.py (líneas 81-101)"
--8<-- "codigo/ordenar_funcional.py:81:101"
```

| Línea | Qué hace |
|---|---|
| `CRITERIOS = {"az": lambda fila: ..., ...}` | Diccionario de **funciones key**: cada una recibe una fila y devuelve el valor por el que se compara. |
| `tareas.controls.sort(key=CRITERIOS[criterio], reverse=inverso)` | Ordena la lista **en el sitio**. `key` dice *por qué* ordenar; `reverse` *en qué sentido*. |
| `page.update()` | La lista de Python ya está ordenada, pero la pantalla no se entera sin esto. |

!!! note "No llama a `actualizar_contador`"
    Ordenar no cambia cuántas hay pendientes. Basta `page.update()`.

Todo el detalle (qué es `key`, recetas, dónde pegarlo) está en la sección **[Ordenar listas](../ordenar/index.md)**.
