# Ordenar por la `key` del control

!!! question "¿Sort `key` o propiedad `key`?"
    Son dos cosas distintas con el mismo nombre:

    | | Qué es |
    |---|---|
    | `sort(key=...)` | El **argumento de Python** que dice por qué comparar (lo de las páginas anteriores). |
    | `ft.Row(key=...)` | Una **propiedad de los controles de Flet**: un identificador que tú eliges. |

Todos los controles de Flet tienen la propiedad `key`. Sirve para **identificar** un control concreto, y como es un dato más, también se puede usar de criterio de orden.

## Ejemplo: orden de creación

Asigna a cada fila un número según se crea, y ordena por él para **volver al orden original**:

```python linenums="1" title="codigo/ordenar_por_key_control.py"
--8<-- "codigo/ordenar_por_key_control.py"
```

| Pieza | Qué hace |
|---|---|
| `contador_id = {"n": 0}` | Contador de ids. Es un diccionario para poder modificarlo desde la función interna sin `nonlocal`. |
| `ft.Row(key=contador_id["n"], ...)` | Marca cada fila con su número de creación. |
| `sort(key=lambda fila: fila.key)` | Ordena por esa marca → orden de creación. |
| `reverse=True` | Las más nuevas primero. |

## Cuándo conviene

- Quieres poder **volver al orden original** después de ordenar de otras formas.
- Quieres un id estable que no cambie si modificas el texto de la tarea.

!!! warning "Usa un tipo que se pueda comparar"
    Todas las `key` de las filas que ordenes deben ser del **mismo tipo** (todas números o todas textos). Mezclar `int` y `str` da `TypeError`. Comprueba en la documentación de tu versión qué tipos admite `key`.

!!! tip "Más simple si usas clases"
    Con la [versión con clases](clases.md) puedes guardar un campo `numero` en `Tarea` y ordenar con `lambda t: t.numero`, sin depender de `key`.
