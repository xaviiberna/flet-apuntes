# PASO 6 - Borrar tareas: IconButton y lambda
# Objetivo: cada tarea es una Row con Checkbox + botón de borrar.
import flet as ft


def main(page: ft.Page):
    page.title = "Lista de tareas"
    page.padding = 20

    titulo = ft.Text("Mis tareas", size=30, weight=ft.FontWeight.BOLD)
    nueva_tarea = ft.TextField(label="Nueva tarea", expand=True)
    tareas = ft.Column()

    def eliminar_tarea(fila):
        tareas.controls.remove(fila)  # quitamos la fila concreta
        page.update()

    def añadir_tarea(e):
        fila = ft.Row()
        fila.controls = [
            ft.Checkbox(label=nueva_tarea.value, expand=True),
            ft.IconButton(
                icon=ft.Icons.DELETE,
                icon_color=ft.Colors.RED_400,
                # lambda nos permite pasar 'fila' a la función
                on_click=lambda e: eliminar_tarea(fila),
            ),
        ]
        tareas.controls.append(fila)
        nueva_tarea.value = ""
        page.update()

    boton = ft.Button(content="Añadir", on_click=añadir_tarea)

    page.add(titulo, ft.Row([nueva_tarea, boton]), tareas)


ft.run(main)
