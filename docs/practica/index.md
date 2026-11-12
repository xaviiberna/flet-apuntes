# Práctica · Modificaciones de MiPrimerApp

Partimos de la app del paso 8 **comentada línea a línea** (`codigo/practica_base_comentada.py`) y le añadimos funcionalidades. El resultado final es `codigo/practica_app_final.py`.

| # | Modificación | Dónde se toca |
|---|---|---|
| 1 | [Control de tareas repetidas](repetidas.md) | variable `mensaje` + bucle en `añadir_tarea` |
| 2 | [Color del contador (rojo/verde)](color-contador.md) | `contador` al crearlo + `if/else` en `actualizar_contador` |
| 3 | [Borrar completadas](borrar-completadas.md) | función `borrar_completadas` + botón |
| 4 | [Botón Modificar](modificar.md) | función `modificar_tarea` + `IconButton` en cada fila |
| 5 | [Publicar](publicar.md) | web, APK, Windows y Linux con `flet build` |

??? example "Código base comentado (antes de las modificaciones)"
    ```python title="practica_base_comentada.py"
    --8<-- "codigo/practica_base_comentada.py"
    ```

??? example "Código final de la práctica"
    ```python title="practica_app_final.py"
    --8<-- "codigo/practica_app_final.py"
    ```

!!! tip "Para encontrar cada cosa en el código final"
    Cada modificación tiene su página con **la línea exacta** y el motivo de ese lugar. Para ver qué hace cada función por separado, ve a [Función por función](../funciones/index.md).
