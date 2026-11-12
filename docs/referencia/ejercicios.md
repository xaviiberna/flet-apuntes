# Ejercicios

Marca lo que ya tienes hecho y mira dónde está explicado.

| Ejercicio | Dónde |
|---|---|
| Color del título y tema oscuro | [Paso 2](../pasos/paso2.md) |
| Mensaje verde al añadir; mostrar el contenido del evento | [Paso 4](../pasos/paso4.md) |
| Mensaje rojo al borrar | [Paso 6](../pasos/paso6.md) |
| Impedir tareas repetidas | [Repetidas](../practica/repetidas.md) |
| Botón «Borrar completadas» | [Borrar completadas](../practica/borrar-completadas.md) |
| Mensaje «¡No tienes tareas pendientes!» cuando el contador llegue a 0 | *(propuesto)* en `actualizar_contador`: `if pendientes == 0:` |
| Botón Modificar | [Modificar](../practica/modificar.md) |
| Dropdown de prioridad (Alta, Media, Baja) | [Ordenar con clases](../ordenar/clases.md) |
| Total de tareas creadas junto al contador | [Paso 9b](../pasos/paso9.md) |
| **Ordenar** A-Z, pendientes primero, por prioridad | [Ordenar](../ordenar/index.md) |
| Versión web, APK, Windows y Linux | [Publicar](../practica/publicar.md) |

## Retos nuevos (ordenar)

1. Añade un botón **«Completadas primero»** (una línea en `CRITERIOS` + un botón).
2. Haz un **único botón A-Z / Z-A** que alterne el sentido cada vez que se pulsa (pista: una variable booleana que invierta `inverso`; en una función interna necesitarás `nonlocal` o un diccionario).
3. Ordena por **longitud descendente y, a igualdad, A-Z** (pista: signo `-` en una tupla).
4. Mantén la lista **siempre ordenada** al añadir una tarea nueva.
5. En la versión con clases, añade el criterio **«Por número de creación»**.
