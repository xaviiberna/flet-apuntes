# PASO 7 - Validación y tecla Enter
# Objetivo: no permitir tareas vacías y añadir con Enter.
import flet as ft


def main(page: ft.Page):
    page.title = "Lista de tareas"
    page.padding = 20

    titulo = ft.Text("Mis tareas", size=30, weight=ft.FontWeight.BOLD)
    # on_submit se dispara al pulsar Enter dentro del campo
    nueva_tarea = ft.TextField(label="Nueva tarea", expand=True, on_submit=lambda e: añadir_tarea(e))
    tareas = ft.Column()

    def eliminar_tarea(fila):
        tareas.controls.remove(fila)
        page.update()

    def añadir_tarea(e):
        texto = nueva_tarea.value.strip()  # strip() quita espacios sobrantes

        if not texto:
            nueva_tarea.error = "Escribe una tarea"
            page.update()
            return  # salimos sin añadir nada

        nueva_tarea.error = None  # quitamos el error si lo había
        fila = ft.Row()
        fila.controls = [
            ft.Checkbox(label=texto, expand=True),
            ft.IconButton(
                icon=ft.Icons.DELETE,
                icon_color=ft.Colors.RED_400,
                on_click=lambda e: eliminar_tarea(fila),
            ),
        ]
        tareas.controls.append(fila)
        nueva_tarea.value = ""
        page.update()

    boton = ft.Button(content="Añadir", on_click=añadir_tarea)

    page.add(titulo, ft.Row([nueva_tarea, boton]), tareas)


ft.run(main)
