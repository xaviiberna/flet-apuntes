# PASO 4 - Eventos: reaccionar al clic
# Objetivo: que el botón añada una tarea (como texto) a la pantalla.
import flet as ft


def main(page: ft.Page):
    page.title = "Lista de tareas"
    page.padding = 20

    titulo = ft.Text("Mis tareas", size=30, weight=ft.FontWeight.BOLD)
    nueva_tarea = ft.TextField(label="Nueva tarea")
    tareas = ft.Column()  # contenedor vertical donde irán las tareas

    # Función manejadora del evento. 'e' es el objeto del evento.
    def añadir_tarea(e):
        tareas.controls.append(ft.Text(nueva_tarea.value))  # modificamos la lista
        nueva_tarea.value = ""  # vaciamos el campo
        page.update()  # ¡sin esto no se ve el cambio!

    boton = ft.Button(content="Añadir", on_click=añadir_tarea)

    page.add(titulo, nueva_tarea, boton, tareas)


ft.run(main)
