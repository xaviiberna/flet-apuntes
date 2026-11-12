# PASO 3 - Controles de entrada: TextField y Button
# Objetivo: poner controles en pantalla (todavía no hacen nada).
import flet as ft


def main(page: ft.Page):
    page.title = "Lista de tareas"
    page.padding = 20

    titulo = ft.Text("Mis tareas", size=30, weight=ft.FontWeight.BOLD)
    nueva_tarea = ft.TextField(label="Nueva tarea")
    boton = ft.Button(content="Añadir")

    page.add(titulo, nueva_tarea, boton)


ft.run(main)
