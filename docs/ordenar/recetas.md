# Recetas: criterios de ordenación

Todas usan la fila de la práctica (`fila.controls[0]` = Checkbox). Cada una es solo la **lambda** que va en `key=`.

| Quiero ordenar por… | `key=` | Notas |
|---|---|---|
| Nombre A-Z | `lambda fila: fila.controls[0].label.lower()` | `.lower()` para que «pan» y «Pan» cuenten igual |
| Nombre Z-A | la de A-Z + `reverse=True` | |
| Pendientes primero | `lambda fila: fila.controls[0].value` | `False < True`: las no marcadas van antes |
| Completadas primero | la anterior + `reverse=True` | |
| Texto más corto primero | `lambda fila: len(fila.controls[0].label)` | |
| Pendientes y luego A-Z | `lambda fila: (fila.controls[0].value, fila.controls[0].label.lower())` | una **tupla**: se compara el 1.º y, si empatan, el 2.º |

## Varios criterios: la tupla

```python
tareas.controls.sort(
    key=lambda fila: (fila.controls[0].value, fila.controls[0].label.lower())
)
```

| Código | Qué hace |
|---|---|
| `(valor, texto)` | Una **tupla** con dos valores: se compara el primero y, si empatan, el segundo. |
| `fila.controls[0].value` | 1.º criterio: `False` (pendiente) va antes que `True` (hecha). |
| `fila.controls[0].label.lower()` | 2.º criterio: dentro de cada grupo, A-Z. |

Python compara tuplas elemento a elemento: primero el estado (pendientes antes), y **dentro de cada grupo** por nombre.

## Un criterio descendente dentro de una tupla

`reverse=True` invierte **todo**. Si quieres un campo ascendente y otro descendente con números, cambia el signo:

```python
# más largas primero, y a igualdad de longitud, A-Z
key=lambda fila: (-len(fila.controls[0].label), fila.controls[0].label.lower())
```

| Código | Qué hace |
|---|---|
| `-len(...)` | Longitud en **negativo**: las más largas dan números más pequeños y van primero. |
| `fila.controls[0].label.lower()` | A igual longitud, A-Z. |

(El truco del `-` solo vale para números, no para textos.)

## Ordenar en dos pasos (por estabilidad)

Equivale a la tupla, pero explícito:

```python
tareas.controls.sort(key=lambda f: f.controls[0].label.lower())   # 1.º: nombre
tareas.controls.sort(key=lambda f: f.controls[0].value)           # 2.º: estado (mantiene A-Z dentro de cada grupo)
```

| Código | Qué hace |
|---|---|
| `sort(key=lambda f: ...label.lower())` | 1.ª pasada: ordena A-Z. |
| `sort(key=lambda f: f.controls[0].value)` | 2.ª pasada: separa pendientes y hechas. Como `sort` es estable, el A-Z se mantiene dentro de cada grupo. |

El **último** `sort` es el criterio principal.

## Ordenar por prioridad (texto → número)

«Alta», «Media», «Baja» ordenadas alfabéticamente salen mal (Alta, Baja, Media). Se traduce a número con un diccionario:

```python
ORDEN_PRIORIDAD = {"Alta": 0, "Media": 1, "Baja": 2}
lista.sort(key=lambda t: ORDEN_PRIORIDAD[t.prioridad])
```

| Código | Qué hace |
|---|---|
| `ORDEN_PRIORIDAD = {...}` | Diccionario que traduce cada prioridad a un número. |
| `ORDEN_PRIORIDAD[t.prioridad]` | Para cada tarea `t`, busca su número: Alta=0, Media=1, Baja=2. |
| `lista.sort(key=...)` | Ordena por ese número: Alta primero. |

Necesitas guardar la prioridad en cada tarea → [versión con clases](clases.md).

## Tabla de criterios en un diccionario (lo que usa la app)

Para no escribir una lambda en cada botón, se guardan todas en un diccionario y se elige por nombre:

```python
CRITERIOS = {
    "az":        lambda fila: fila.controls[0].label.lower(),
    "estado":    lambda fila: fila.controls[0].value,
    "longitud":  lambda fila: len(fila.controls[0].label),
    "estado_az": lambda fila: (fila.controls[0].value, fila.controls[0].label.lower()),
}

def ordenar_tareas(criterio, inverso=False):
    tareas.controls.sort(key=CRITERIOS[criterio], reverse=inverso)
    page.update()
```

| Código | Qué hace |
|---|---|
| `CRITERIOS = {...}` | Diccionario: a cada nombre de criterio le corresponde su lambda. |
| `"az": lambda fila: ...` | Criterio A-Z. |
| `"estado": ...` | Pendientes primero. |
| `"longitud": ...` | Textos más cortos primero. |
| `"estado_az": ...` | Pendientes primero y A-Z dentro. |
| `def ordenar_tareas(criterio, inverso=False):` | Recibe el nombre del criterio y si se invierte. |
| `CRITERIOS[criterio]` | Coge la lambda de ese criterio y se la pasa a `sort`. |
| `reverse=inverso` | Orden descendente si `inverso` es `True`. |
| `page.update()` | Redibuja. |

Para **añadir un criterio nuevo** solo hay que añadir una línea al diccionario y un botón.
