# EXTRA - Ordenar usando la propiedad `key` de los controles de Flet
# Todos los controles tienen `key` (un identificador que TÚ eliges). Sirve para
# reconocer un control y también se puede usar como criterio de ordenación.
import flet as ft


def main(page: ft.Page):
    tareas = ft.Column()
    contador_id = {"n": 0}  # contador de ids: la tarea 1, 2, 3... según se crean

    def añadir(e):
        contador_id["n"] += 1
        # key = número de orden de creación. Lo guardamos en la fila, no en el texto.
        fila = ft.Row(key=contador_id["n"], controls=[ft.Checkbox(label=nueva.value or "sin nombre")])
        tareas.controls.append(fila)
        nueva.value = ""
        page.update()

    def orden_creacion(e):
        # Vuelve al orden original: ordena por la key de cada fila
        tareas.controls.sort(key=lambda fila: fila.key)
        page.update()

    def orden_inverso(e):
        tareas.controls.sort(key=lambda fila: fila.key, reverse=True)
        page.update()

    nueva = ft.TextField(label="Nueva tarea", expand=True, on_submit=añadir)
    page.add(
        ft.Row([nueva, ft.Button(content="Añadir", on_click=añadir)]),
        ft.Row([
            ft.Button(content="Orden de creación", on_click=orden_creacion),
            ft.Button(content="Más nuevas primero", on_click=orden_inverso),
        ]),
        tareas,
    )


ft.run(main)
