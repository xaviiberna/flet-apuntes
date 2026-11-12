# Importamos la librería Flet con el alias "ft" para usar sus controles (Text, TextField, Column...).
import flet as ft

# Función principal: Flet la ejecuta al arrancar y le pasa "page", la ventana de la app.
# Aquí se crean los controles y se añaden a la página.
def main(page: ft.Page):
    # title: texto que aparece en la barra de título de la ventana.
    page.title = "Lista de tareas"
    # padding: espacio interior entre el borde de la ventana y los controles (20 px).
    page.padding = 20

    # Text: control que muestra texto. size = tamaño de letra; weight = grosor (BOLD = negrita).
    titulo = ft.Text("Mis tareas", size=30, weight=ft.FontWeight.BOLD)

    # TextField: campo de texto donde se escribe la nueva tarea.
    #  - label: texto descriptivo que se muestra dentro del campo como pista.
    #  - expand=True: ocupa todo el espacio horizontal libre de su fila.
    #  - on_submit: evento que se dispara al pulsar Enter; recibe el evento "e".
    #  - lambda e: añadir_tarea(e): función anónima que llama a añadir_tarea cuando ocurre el evento.
    #    Se usa lambda porque añadir_tarea aún no está definida en este punto del código;
    #    así la llamada se retrasa hasta que se pulsa Enter, cuando la función ya existe.
    nueva_tarea = ft.TextField(label="Nueva tarea", expand=True, on_submit=lambda e: añadir_tarea(e))

    # contador: Text que muestra cuántas tareas quedan pendientes (empieza en 0).
    contador = ft.Text("Tareas pendientes: 0")

    # tareas: Column, contenedor vertical donde se irán añadiendo las filas de tareas.
    tareas = ft.Column()

    # La función actualizar_contador cuenta las tareas sin marcar y actualiza el texto del contador.
    # e=None: recibe el evento si lo llama Flet; vale None si la llamo yo.
    def actualizar_contador(e=None):
        # controls[0] de cada fila es el Checkbox; value=False => pendiente.
        # pendientes, recorre todas las filas y suma 1 por cada una sin marcar. y fila controls[0] es el checkbox de esa fila.
        pendientes = sum(1 for fila in tareas.controls if not fila.controls[0].value)
        # Actualiza el texto del contador con el número de tareas pendientes.
        contador.value = f"Tareas pendientes: {pendientes}"
        # Redibuja la pantalla para que se vea el cambio.
        page.update()

    # La función eliminar tarea recibe la fila a eliminar y la quita del contenedor de tareas.
    def eliminar_tarea(fila):
        tareas.controls.remove(fila)
        # Llama a actualizar_contador para que se actualice el número de tareas pendientes.
        actualizar_contador()

    # Se ejecuta cuando ocurre un evento (Enter en el campo o clic en "Añadir").
    # e es el evento que Flet pasa automáticamente; aquí no se usa.
    def añadir_tarea(e):
        # texto: recoge el valor del campo de texto, eliminando espacios al principio y al final.
        texto = nueva_tarea.value.strip()

        # Comprueba si el campo está vacío.
        # Un texto vacío ("") cuenta como False, así que "not texto" es True y entra en el if.
        if not texto:
            #muestra un mensaje de error en el TextField y no añade la tarea.
            nueva_tarea.error = "Escribe una tarea"
            # Redibuja la pantalla para que se vea el cambio.
            page.update()
            #sale de la función sin añadir la tarea.
            return

        # Si el campo no está vacío, se borra el mensaje de error.
        nueva_tarea.error = None
        #crea una fila (Row) vacia que contendrá el checkbox y el botón de eliminar.
        fila = ft.Row()
        # controls: lista de controles que contiene la fila.
        fila.controls = [
            # Checkbox: control que muestra un checkbox con el texto de la tarea.
            # on_change se dispara al marcar/desmarcar el checkbox
            ft.Checkbox(label=texto, expand=True, on_change=actualizar_contador),

            
            # IconButton: botón con un icono (DELETE)
            # icon es el icono que se muestra; icon_color es el color del icono.
            # on_click se dispara al pulsar el botón; llama a eliminar_tarea pasando la fila como argumento.
            # Se usa lambda porque Flet solo envía el evento (e) y aquí hace falta pasar también la fila.
            ft.IconButton(
                icon=ft.Icons.DELETE,
                icon_color=ft.Colors.RED_400,
                on_click=lambda e: eliminar_tarea(fila),
            ),
            
        ]
        # Añade la fila a la lista de tareas, al final (tareas.controls).
        tareas.controls.append(fila)
        # Vacía el campo de texto para poder escribir otra tarea.
        nueva_tarea.value = ""
        # Recalcula el contador (esta función ya hace page.update()).
        actualizar_contador()

    # Crea un botón que llama a añadir_tarea al pulsarlo, no hace falta lambda porque la función ya está definida.
    boton = ft.Button(content="Añadir", on_click=añadir_tarea)

    # Añade los controles a la página en el orden que se quieren mostrar.
    page.add(titulo, ft.Row([nueva_tarea, boton]), contador, tareas)

# Llamada a ft.run() para ejecutar la app, pasando la función main como argumento.
ft.run(main)
