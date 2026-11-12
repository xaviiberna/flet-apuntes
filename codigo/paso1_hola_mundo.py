# PASO 1 - Hola mundo
# Objetivo: entender la estructura mínima de una app Flet.
import flet as ft


def main(page: ft.Page):
    # 'page' es la ventana/pestaña de la app. Todo se añade a ella.
    page.add(ft.Text("¡Hola, Flet!"))


ft.run(main)
