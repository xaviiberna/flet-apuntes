# PASO 9b - Segunda clase: AppTareas (la app completa es un control personalizado)
# main queda reducido a configurar la página y añadir AppTareas().
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
 
 
@ft.control
class AppTareas(ft.Column):
    def init(self):
        self.nueva_tarea = ft.TextField(
            label="Nueva tarea", expand=True, on_submit=self.clic_añadir
        )
        self.tareas = ft.Column()
        self.contador = ft.Text("Tareas pendientes: 0")

        self.total_creadas = 0
        self.texto_total_creadas = ft.Text("Total de tareas creadas: 0")
        
 
        self.controls = [
            ft.Text("Mis tareas", size=30, weight=ft.FontWeight.BOLD),
            ft.Row(
                [
                    self.nueva_tarea,
                    ft.Button(content="Añadir", on_click=self.clic_añadir),
                ]
            ),
            self.contador,
            self.texto_total_creadas,
            self.tareas,
        ]
 
    def clic_añadir(self, e):
        texto = self.nueva_tarea.value.strip()
 
        if not texto:
            self.nueva_tarea.error = "Escribe una tarea"
            self.update()
            return
 
        self.nueva_tarea.error = None
        self.tareas.controls.append(
            Tarea(
                nombre=texto,
                on_borrar=self.eliminar_tarea,
                on_cambio=self.actualizar_contador,
            )
        )
        self.nueva_tarea.value = ""
        self.total_creadas += 1
        self.texto_total_creadas.value= f"Total de tareas creadas: {self.total_creadas}"
        self.actualizar_contador()
 
    def eliminar_tarea(self, tarea):
        self.tareas.controls.remove(tarea)
        self.actualizar_contador()
 
    def actualizar_contador(self):
        pendientes = sum(1 for tarea in self.tareas.controls if not tarea.completada)
        self.contador.value = f"Tareas pendientes: {pendientes}"
        self.update()
    
 
 
def main(page: ft.Page):
    page.title = "Lista de tareas"
    page.padding = 20
    page.add(AppTareas())
 
 
ft.run(main)