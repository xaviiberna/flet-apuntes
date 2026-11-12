# Ordenar listas de controles con `key` y `lambda`

Las tareas viven en una **lista normal de Python**: `tareas.controls`. Ordenarlas es ordenar esa lista y luego decirle a Flet que redibuje.

```python
tareas.controls.sort(key=lambda fila: fila.controls[0].label.lower())
page.update()
```

Dos líneas. Todo lo demás es decidir **por qué** criterio ordenar y **dónde** poner el código.

<div class="grid cards" markdown>

-   :material-help-circle: **[Cómo funciona `sort` y `key`](como-funciona.md)**

    Qué es `key`, qué hace la `lambda`, `sort` vs `sorted`, `reverse`.

-   :material-book-open-variant: **[Recetas](recetas.md)**

    A-Z, Z-A, pendientes primero, por longitud, varios criterios, prioridad.

-   :material-map-marker: **[Dónde va en el código](donde-va.md)**

    Los 3 sitios exactos en la app de la práctica y por qué.

-   :material-cube-outline: **[Versión con clases](clases.md)**

    El mismo orden con `Tarea.nombre` y `Tarea.completada`.

-   :material-key: **[Ordenar por la `key` del control](key-control.md)**

    La propiedad `key` que tienen todos los controles de Flet.

</div>

!!! success "Código completo y probado"
    - `codigo/ordenar_funcional.py` — la práctica + 5 botones de ordenar
    - `codigo/ordenar_clases.py` — versión con clases y prioridad
    - `codigo/ordenar_por_key_control.py` — con la `key` del control

    La lógica de los tres está comprobada con pruebas automáticas (`tests/test_ordenar.py`).
