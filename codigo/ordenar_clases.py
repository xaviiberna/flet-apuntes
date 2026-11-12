# EXTRA - Ordenar con sort(key=lambda ...) en la versión con CLASES (paso 9c + prioridad)
# Aquí la lambda es más corta porque Tarea ya guarda sus datos: t.nombre, t.completada, t.prioridad.
from typing import Callable

import flet as ft

# Diccionario para convertir texto en número: la prioridad "Alta" debe ir ANTES que "Baja".
ORDEN_PRIORIDAD = {"Alta": 0, "Media": 1, "Baja": 2}


@ft.control
class Tarea(ft.Column):
    nombre: str = ""
    prioridad: str = "Media"  # NUEVO: campo para poder ordenar por prioridad
    on_borrar: Callable | None = None
    on_cambio: Callable | None = None

    def init(self):
        self.completada = False
        self.casilla = ft.Checkbox(
            value=False, label=self.nombre, on_change=self.cambio_estado
        )
        self.controls = [
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    self.casilla,
                    ft.Text(self.prioridad),  # se muestra la prioridad a la derecha
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
        # Dropdown: elegir la prioridad de la tarea que se va a añadir
        self.prioridad = ft.Dropdown(
            value="Media",
            width=130,
            options=[ft.DropdownOption(key=p) for p in ORDEN_PRIORIDAD],
        )
        self.tareas = ft.Column()
        self.contador = ft.Text("Tareas pendientes: 0")

        self.controls = [
            ft.Text("Mis tareas", size=30, weight=ft.FontWeight.BOLD),
            ft.Row(
                [
                    self.nueva_tarea,
                    self.prioridad,
                    ft.Button(content="Añadir", on_click=self.clic_añadir),
                ]
            ),
            self.contador,
            # >>> ORDENAR: botones. lambda e: ... para poder pasar argumentos al método
            ft.Row(
                wrap=True,
                controls=[
                    ft.Text("Ordenar:"),
                    ft.Button(content="A-Z", on_click=lambda e: self.ordenar("nombre")),
                    ft.Button(content="Z-A", on_click=lambda e: self.ordenar("nombre", True)),
                    ft.Button(content="Pendientes primero", on_click=lambda e: self.ordenar("estado")),
                    ft.Button(content="Por prioridad", on_click=lambda e: self.ordenar("prioridad")),
                    ft.Button(content="Prioridad + A-Z", on_click=lambda e: self.ordenar("prioridad_nombre")),
                ],
            ),
            # <<< ORDENAR
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
                prioridad=self.prioridad.value,
                on_borrar=self.eliminar_tarea,
                on_cambio=self.update,
            )
        )
        self.nueva_tarea.value = ""
        self.update()

    def eliminar_tarea(self, tarea):
        self.tareas.controls.remove(tarea)
        self.update()

    # >>> ORDENAR: método de la clase (sustituye a la función suelta de la versión funcional)
    def ordenar(self, criterio, inverso=False):
        criterios = {
            "nombre": lambda t: t.nombre.lower(),
            "estado": lambda t: t.completada,
            "prioridad": lambda t: ORDEN_PRIORIDAD[t.prioridad],
            "prioridad_nombre": lambda t: (ORDEN_PRIORIDAD[t.prioridad], t.nombre.lower()),
        }
        self.tareas.controls.sort(key=criterios[criterio], reverse=inverso)
        self.update()  # before_update recalcula el contador y Flet redibuja
    # <<< ORDENAR

    def before_update(self):
        pendientes = sum(1 for tarea in self.tareas.controls if not tarea.completada)
        self.contador.value = f"Tareas pendientes: {pendientes}"


def main(page: ft.Page):
    page.title = "Lista de tareas"
    page.padding = 20
    page.add(AppTareas())


ft.run(main)
