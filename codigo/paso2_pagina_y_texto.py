# PASO 2 - Propiedades de la página y estilo de un Text
# Objetivo: configurar la página y dar formato a un control.
import flet as ft


def main(page: ft.Page):
    # Propiedades de la página
    page.title = "Lista de tareas"
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT

    # Un Text con estilo
    titulo = ft.Text("Mis tareas", size=30, weight=ft.FontWeight.BOLD)

    page.add(titulo)


ft.run(main)
