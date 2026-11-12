# Eventos y manejadores

Un **evento** es algo que pasa en la interfaz. Un **manejador** es la función que se ejecuta. Se conectan asignando la función a la propiedad del evento (**sin paréntesis**).

| Evento | Control | Cuándo ocurre | En la app |
|---|---|---|---|
| `on_click` | `Button`, `IconButton` | clic | Añadir, borrar, modificar, ordenar |
| `on_submit` | `TextField` | pulsar Enter | añadir con Enter |
| `on_change` | `Checkbox` | marcar / desmarcar | actualizar contador |
| `on_select` | `Dropdown` | elegir opción | (opcional) |

```python
boton = ft.Button(content="Añadir", on_click=añadir_tarea)   # ✅ sin paréntesis
boton = ft.Button(content="Añadir", on_click=añadir_tarea()) # ❌ se ejecuta ya
```

| Código | Qué hace |
|---|---|
| `on_click=añadir_tarea` | Se pasa la **función**: Flet la ejecuta al hacer clic. |
| `on_click=añadir_tarea()` | Se ejecuta **ya**, al crear el botón, y a `on_click` le llega su resultado (`None`). |

## El parámetro `e`

Flet pasa **siempre** un objeto evento al manejador. Aunque no lo uses, la función debe aceptarlo:

```python
def añadir_tarea(e): ...                # ✅
def actualizar_contador(e=None): ...    # ✅ sirve de manejador Y se puede llamar sin argumentos
def añadir_tarea(): ...                 # ❌ falla al pulsar
```

| Código | Qué hace |
|---|---|
| `def añadir_tarea(e)` | Correcto: acepta el evento que manda Flet. |
| `def actualizar_contador(e=None)` | Acepta el evento o nada: sirve de manejador y para llamarla tú. |
| `def añadir_tarea()` | Mal: Flet le pasa `e` y da error. |

## `page.update()`

Envía los cambios a la pantalla. **Todo manejador que cambie algo debe terminar en un `update`** (directo o a través de otra función que lo haga, como `actualizar_contador`).

!!! info "En Flet 1.0"
    Se añadió actualización automática tras los manejadores en algunos casos, pero en estos apuntes se usa `page.update()` explícito: es más claro y funciona igual en todas las versiones.
