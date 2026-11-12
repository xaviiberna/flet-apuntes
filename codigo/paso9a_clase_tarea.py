# PASO 9a - Primera clase: Tarea (cada tarea es un control personalizado)
# La app sigue siendo funcional (main), pero cada tarea ya es una clase.
from typing import Callable
 
import flet as ft
 
 
@ft.control
class Tarea(ft.Column):
    nombre: str = ""  # campo: texto de la tarea
    # Callbacks: funciones que pasa el "dueño" de la lista.
    # Se llaman on_...: convención de Flet para funciones y eventos
    on_borrar: Callable | None = None  # al pulsar borrar
    on_cambio: Callable | None = None  # al marcar/desmarcar
 
    def init(self):
        # Se ejecuta al crear la tarea: aquí se construye su interfaz
        self.completada = False
        self.casilla = ft.Checkbox(
            value=False, label=self.nombre, on_change=self.cambio_estado
        )
        self.controls = [
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    self.casilla,
                    ft.IconButton(
                        icon=ft.Icons.DELETE_OUTLINE,
                        tooltip="Eliminar tarea",
                        on_click=self.clic_borrar,
                    ),
                ],
            )
        ]
 
    def cambio_estado(self, e):
        self.completada = self.casilla.value
        self.on_cambio()
 
    def clic_borrar(self, e):
        self.on_borrar(self)
 
 
def main(page: ft.Page):
    page.title = "Lista de tareas"
    page.padding = 20
 
    titulo = ft.Text("Mis tareas", size=30, weight=ft.FontWeight.BOLD)
    nueva_tarea = ft.TextField(
        label="Nueva tarea", expand=True, on_submit=lambda e: añadir_tarea(e)
    )
    contador = ft.Text("Tareas pendientes: 0")
    tareas = ft.Column()
 
    def actualizar_contador():
        pendientes = sum(1 for tarea in tareas.controls if not tarea.completada)
        contador.value = f"Tareas pendientes: {pendientes}"
        page.update()
 
    def eliminar_tarea(tarea):
        tareas.controls.remove(tarea)
        actualizar_contador()
 
    def añadir_tarea(e):
        texto = nueva_tarea.value.strip()
 
        if not texto:
            nueva_tarea.error = "Escribe una tarea"
            page.update()
            return
 
        nueva_tarea.error = None
        tareas.controls.append(
            Tarea(nombre=texto, on_borrar=eliminar_tarea, on_cambio=actualizar_contador)
        )
        nueva_tarea.value = ""
        actualizar_contador()
 
    boton = ft.Button(content="Añadir", on_click=añadir_tarea)
 
    page.add(titulo, ft.Row([nueva_tarea, boton]), contador, tareas)
 
 
ft.run(main)