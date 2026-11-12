# PASO 5 - Layouts (Row/Column) y Checkbox
# Objetivo: campo y botón en la misma fila; cada tarea es un Checkbox.
import flet as ft


def main(page: ft.Page):
    page.title = "Lista de tareas"
    page.padding = 20

    titulo = ft.Text("Mis tareas", size=30, weight=ft.FontWeight.BOLD)
    nueva_tarea = ft.TextField(label="Nueva tarea", expand=True)  # ocupa el espacio libre
    tareas = ft.Column()

    def añadir_tarea(e):
        tareas.controls.append(ft.Checkbox(label=nueva_tarea.value))
        nueva_tarea.value = ""
        page.update()

    boton = ft.Button(content="Añadir", on_click=añadir_tarea)

    # Row coloca los controles en horizontal
    fila_entrada = ft.Row([nueva_tarea, boton])

    page.add(titulo, fila_entrada, tareas)


ft.run(main)
