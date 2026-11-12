# Dónde va cada trozo en el código

En `codigo/ordenar_funcional.py` (la app final de la práctica) hay **3 sitios**, marcados con `# >>> ORDENAR`.

```mermaid
flowchart TD
    subgraph main
    A["1/3 · CRITERIOS (diccionario de lambdas)"] --> B["2/3 · def ordenar_tareas"]
    B --> C["3/3 · botones con lambda e: ordenar_tareas(...)"]
    C --> D["page.add(... fila_ordenar ...)"]
    end
```

## 1/3 y 2/3 · Criterios y función

**Dentro de `main`, después de `modificar_tarea` y antes de `añadir_tarea`.**

```python title="Líneas 81-101"
--8<-- "codigo/ordenar_funcional.py:81:101"
```

!!! note "Por qué aquí"
    - Tiene que estar **dentro de `main`** para ver `tareas` y `page`.
    - Va **después de `tareas = ft.Column()`**, porque la usa.
    - No necesita estar antes que `añadir_tarea` (solo se ejecuta cuando se pulsa un botón), pero juntarla con las demás funciones mantiene el código ordenado.
    - Las lambdas del diccionario **no se ejecutan** al crearlo; solo cuando `sort` las llama.

## 3/3 · Los botones

**Después de definir `ordenar_tareas`, junto a los demás botones** (`boton`, `boton_borrar`).

```python title="Líneas 172-184"
--8<-- "codigo/ordenar_funcional.py:172:184"
```

!!! note "Por qué lambda aquí"
    `on_click` solo entrega `e`, pero `ordenar_tareas` necesita el criterio. `lambda e: ordenar_tareas("az")` hace de intermediaria ([lambda explicada](../controles/lambda.md)).

!!! tip "`wrap=True`"
    Con 5 botones en una `Row`, `wrap=True` hace que salten de línea si no caben.

## Añadirlos a la página

En el `page.add(...)` del final, en la posición donde quieras verlos (aquí entre el contador y la lista):

```python
page.add(titulo, ft.Row([nueva_tarea, boton]), mensaje, contador, fila_ordenar, tareas, boton_borrar)
#                                                                  ^^^^^^^^^^^^ nuevo
```

## Resumen de 30 segundos

1. Pega `CRITERIOS` y `ordenar_tareas` **dentro de `main`**, tras `modificar_tarea`.
2. Crea `fila_ordenar` con los botones, junto a los otros botones.
3. Añade `fila_ordenar` a `page.add(...)`.
4. Prueba: añade «pera», «Manzana», «kiwi» y pulsa **A-Z**.

## ¿Y si quiero ordenar automáticamente al añadir?

Llama a `ordenar_tareas("az")` al final de `añadir_tarea`, **antes** de `actualizar_contador()` (que hace el `page.update()`):

```python
    tareas.controls.append(fila)
    nueva_tarea.value = ""
    tareas.controls.sort(key=CRITERIOS["az"])   # mantiene la lista siempre ordenada
    actualizar_contador()
```

(No uses `ordenar_tareas(...)` aquí si no quieres un `page.update()` extra: `actualizar_contador` ya lo hace.)

## Cosas que se rompen si cambias la fila

Las lambdas usan `fila.controls[0]`. Si metes otro control **antes** del Checkbox, o cambias la estructura de la fila, hay que actualizar el índice en `CRITERIOS`, `actualizar_contador`, `borrar_completadas` y `modificar_tarea`. Con la [versión con clases](clases.md) este problema desaparece.
