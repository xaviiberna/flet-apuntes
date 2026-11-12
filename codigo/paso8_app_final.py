# PASO 8 - App final: contador de tareas pendientes
# Objetivo: mantener un dato derivado (el contador) sincronizado con el estado.
import flet as ft


def main(page: ft.Page):
    page.title = "Lista de tareas"
    page.padding = 20

    titulo = ft.Text("Mis tareas", size=30, weight=ft.FontWeight.BOLD)
    nueva_tarea = ft.TextField(label="Nueva tarea", expand=True, on_submit=lambda e: añadir_tarea(e))
    contador = ft.Text("Tareas pendientes: 0")
    tareas = ft.Column()

    def actualizar_contador(e=None):
        # controls[0] de cada fila es el Checkbox; value=False => pendiente
        pendientes = sum(1 for fila in tareas.controls if not fila.controls[0].value)
        contador.value = f"Tareas pendientes: {pendientes}"
        page.update()

    def eliminar_tarea(fila):
        tareas.controls.remove(fila)
        actualizar_contador()

    def añadir_tarea(e):
        texto = nueva_tarea.value.strip()

        if not texto:
            nueva_tarea.error = "Escribe una tarea"
            page.update()
            return

        nueva_tarea.error = None
        fila = ft.Row()
        fila.controls = [
            # on_change se dispara al marcar/desmarcar el checkbox
            ft.Checkbox(label=texto, expand=True, on_change=actualizar_contador),
            ft.IconButton(
                icon=ft.Icons.DELETE,
                icon_color=ft.Colors.RED_400,
                on_click=lambda e: eliminar_tarea(fila),
            ),
        ]
        tareas.controls.append(fila)
        nueva_tarea.value = ""
        actualizar_contador()

    boton = ft.Button(content="Añadir", on_click=añadir_tarea)

    page.add(titulo, ft.Row([nueva_tarea, boton]), contador, tareas)


ft.run(main)
