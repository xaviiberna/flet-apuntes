# Cómo funciona `sort` y `key`

## 1. `sort` ordena una lista

```python
numeros = [3, 1, 2]
numeros.sort()          # [1, 2, 3]  (cambia la lista, no devuelve nada)
```

| Código | Qué hace |
|---|---|
| `numeros = [3, 1, 2]` | Una lista de números desordenada. |
| `numeros.sort()` | La ordena de menor a mayor. Cambia la propia lista y no devuelve nada. |

Con números o textos simples funciona sin más. Pero una **fila de Flet** no es un número: es un objeto con muchas cosas dentro. Python no sabe por cuál comparar. Por eso existe `key`.

## 2. `key` = «dime por qué valor comparar»

`key` es una **función** que Python llama **una vez por cada elemento**; el valor que devuelve es el que se usa para ordenar.

```python
palabras = ["pera", "Manzana", "kiwi"]
palabras.sort(key=len)                      # por longitud → ['pera', 'kiwi', 'Manzana']
palabras.sort(key=str.lower)                # sin distinguir mayúsculas
```

| Código | Qué hace |
|---|---|
| `palabras = [...]` | Lista de textos. |
| `palabras.sort(key=len)` | `len` se aplica a cada palabra: ordena por **longitud**. |
| `palabras.sort(key=str.lower)` | Compara cada palabra en minúsculas: ordena A-Z sin distinguir mayúsculas. |

## 3. La `lambda` es esa función escrita en una línea

Una lambda es una función **sin nombre**. Estas dos cosas son equivalentes:

=== "Con lambda"

    ```python
    tareas.controls.sort(key=lambda fila: fila.controls[0].label.lower())
    ```

    | Código | Qué hace |
    |---|---|
    | `lambda fila:` | Función sin nombre que recibe una fila. |
    | `fila.controls[0].label.lower()` | Devuelve su texto en minúsculas; `sort` ordena por ese valor. |

=== "Con def"

    ```python
    def texto_de(fila):
        return fila.controls[0].label.lower()

    tareas.controls.sort(key=texto_de)
    ```

    | Código | Qué hace |
    |---|---|
    | `def texto_de(fila):` | La misma función, pero con nombre. |
    | `return fila.controls[0].label.lower()` | Devuelve el texto de la fila en minúsculas. |
    | `sort(key=texto_de)` | Se pasa la función **sin paréntesis**: `sort` la llamará para cada fila. |

Se lee: *«para cada `fila`, compara por `fila.controls[0].label.lower()`»*.

!!! note "No es la misma lambda que en `on_click`"
    En `on_click=lambda e: eliminar_tarea(fila)` la lambda recibe el **evento** `e`. En `key=lambda fila: ...` recibe **cada elemento de la lista**. Misma sintaxis, distinto papel. Ver [lambda explicada](../controles/lambda.md).

## 4. `fila.controls[0]` — de dónde sale

En la app de la práctica cada fila es `Row([Checkbox, IconButton(lápiz), IconButton(papelera)])`:

| Expresión | Es… |
|---|---|
| `fila` | la `Row` completa |
| `fila.controls[0]` | el `Checkbox` (siempre el primero) |
| `fila.controls[0].label` | el **texto** de la tarea |
| `fila.controls[0].value` | `True` si está marcada, `False` si no |

## 5. `reverse` y estabilidad

```python
tareas.controls.sort(key=..., reverse=True)   # descendente (Z-A)
```

| Código | Qué hace |
|---|---|
| `key=...` | El criterio, como siempre. |
| `reverse=True` | Invierte el orden: de mayor a menor (Z-A). |

`sort` es **estable**: si dos elementos tienen el mismo valor de `key`, **mantienen el orden que ya tenían**. Esto permite ordenar en dos pasos (ver [recetas](recetas.md)).

## 6. `.sort()` vs `sorted()`

| | `lista.sort(key=...)` | `sorted(lista, key=...)` |
|---|---|---|
| Cambia la lista original | **Sí** | No |
| Devuelve | `None` | una lista nueva |
| Uso en Flet | `tareas.controls.sort(key=...)` | `tareas.controls = sorted(tareas.controls, key=...)` |

!!! danger "El error clásico"
    ```python
    tareas.controls = tareas.controls.sort(key=...)   # ❌ sort devuelve None
    ```

    | Código | Qué hace |
    |---|---|
    | `tareas.controls.sort(...)` | Ordena la lista… y devuelve `None`. |
    | `tareas.controls = ...` | …así que guardas `None` en `tareas.controls` y la app falla. Escribe solo `tareas.controls.sort(...)`. |
    Dejas `tareas.controls` en `None` y la app falla. Usa `.sort(...)` **solo**, o `sorted(...)` **con** asignación.

## 7. Y después, `page.update()`

Ordenar cambia la lista de Python. La pantalla **no** se entera hasta que llamas a `page.update()` (o `self.update()` en una clase). Es la misma [regla de oro](../pasos/paso4.md) de siempre.
