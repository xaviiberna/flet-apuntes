# Errores frecuentes

| Síntoma | Causa probable | Dónde |
|---|---|---|
| Un cambio **no aparece** en pantalla | Falta `page.update()` | [Paso 4](../pasos/paso4.md) |
| La función se ejecuta **al arrancar** la app | `on_click=funcion()` con paréntesis | [Eventos](../controles/eventos.md) |
| Error al pulsar un botón | El manejador no tiene el parámetro `e` | [Eventos](../controles/eventos.md) |
| Todos los botones de borrar actúan sobre la misma fila | La lambda no captura la fila correcta | [Paso 6](../pasos/paso6.md) |
| `AttributeError` con un control o propiedad | Nombre incorrecto para la versión de Flet | — |
| El contador va un paso por detrás | Llamas a `actualizar_contador` antes de añadir la fila | [Paso 8](../pasos/paso8.md) |
| `AttributeError: ... has no attribute 'value'` en el contador | `controls[1]` en vez de `controls[0]` (es el IconButton) | [Paso 8](../pasos/paso8.md) |
| «Borrar completadas» deja alguna marcada | Borras de la lista mientras la recorres: usa `list(...)` | [borrar_completadas](../funciones/borrar_completadas.md) |
| La app falla tras ordenar: `'NoneType'...` | `tareas.controls = tareas.controls.sort(...)` | [Cómo funciona sort](../ordenar/como-funciona.md) |
| Ordenar «no hace nada» | Falta `page.update()` después de `sort` | [ordenar_tareas](../funciones/ordenar_tareas.md) |
| A-Z pone «Zeta» antes que «arbol» | Falta `.lower()` en la key | [Recetas](../ordenar/recetas.md) |
| `TypeError` al ordenar por `key` del control | `key` de tipos distintos (int y str) | [Ordenar por key](../ordenar/key-control.md) |
| `ModuleNotFoundError: flet` | El entorno virtual no está activado | [Instalación](../empezar/instalacion.md) |
| Un archivo llamado `flet.py` rompe todo | Python importa tu archivo en vez de la librería | [Instalación](../empezar/instalacion.md) |

!!! note "Sobre versiones"
    La API de Flet cambió bastante entre versiones (`ft.app` → `ft.run`, `text=` → `content=` en `Button`, `ft.dropdown.Option` → `ft.DropdownOption`, `Dropdown.on_change` → `on_select`). Si un nombre falla, mira la documentación de **tu** versión: `pip show flet`.
