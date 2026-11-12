# EXTRA - Ordenar la lista con sort(key=lambda ...)
# Es la app final de la práctica + botones de ordenar. Lo nuevo está entre marcas  # >>> ORDENAR  y  # <<< ORDENAR
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
    # color=ft.Colors.RED: el texto empieza en rojo porque empezamos sin tareas pendientes.
    contador = ft.Text("Tareas pendientes: 0", color=ft.Colors.RED)

    # mensaje: Text para avisar al usuario cuando intenta añadir una tarea repetida (en naranja).
    mensaje = ft.Text("", color=ft.Colors.ORANGE)

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

        # Revisa la variable de tareas pendientes y cambia el color,
        # rojo si no hay tareas pendientes, verde si hay alguna.
        if pendientes == 0:
            contador.color = ft.Colors.RED
        else:
            contador.color = ft.Colors.GREEN

        # Redibuja la pantalla para que se vea el cambio.
        page.update()

    
    def borrar_completadas(e): # creamos la función borrar_completadas que se ejecuta al pulsar el botón "Borrar completadas"
        for fila in list(tareas.controls): # Recorremos una copia de la lista de tareas (tareas.controls) para poder eliminar elementos mientras iteramos.
            if fila.controls[0].value: # Si el checkbox de la fila está marcado (value=True), significa que la tarea está completada.
                tareas.controls.remove(fila) # Eliminamos la fila de la lista de tareas.
        actualizar_contador() # Llamamos a actualizar_contador para que se actualice el número de tareas pendientes después de eliminar las completadas.

    # La función eliminar tarea recibe la fila a eliminar y la quita del contenedor de tareas.
    def eliminar_tarea(fila):
        tareas.controls.remove(fila)
        # Llama a actualizar_contador para que se actualice el número de tareas pendientes.
        actualizar_contador()


    # Cambia el texto de una tarea por el que haya escrito en el campo "Nueva tarea".
    def modificar_tarea(fila):
        texto = nueva_tarea.value.strip()  # Recoge el texto nuevo del campo.
        if not texto:  # Si está vacío, avisa y no modifica nada.
            nueva_tarea.error = "Escribe el texto nuevo"
            page.update()
            return
        fila.controls[0].label = texto  # Cambia el texto del checkbox de esa fila.
        nueva_tarea.error = None  # Borra el error si lo había.
        nueva_tarea.value = ""  # Vacía el campo.
        page.update()  # Redibuja la pantalla.

    # >>> ORDENAR (1/3): criterios de ordenación -------------------------------------
    # Cada criterio es una función "key": recibe UNA fila y devuelve el valor por el que se compara.
    # fila.controls[0] es el Checkbox de la fila (igual que en actualizar_contador).
    CRITERIOS = {
        # texto en minúsculas: así "pan" y "Pan" se ordenan igual
        "az": lambda fila: fila.controls[0].label.lower(),
        # False < True, así que las no marcadas (pendientes) quedan primero
        "estado": lambda fila: fila.controls[0].value,
        # primero las tareas con el texto más corto
        "longitud": lambda fila: len(fila.controls[0].label),
        # varios criterios a la vez: una tupla. Pendientes primero y, dentro de cada grupo, A-Z
        "estado_az": lambda fila: (fila.controls[0].value, fila.controls[0].label.lower()),
    }

    # >>> ORDENAR (2/3): la función que ordena ----------------------------------------
    def ordenar_tareas(criterio, inverso=False):
        # .sort() ordena la lista tareas.controls "en el sitio" (no devuelve nada nuevo).
        # key=...     -> función que saca el valor de comparación de cada fila.
        # reverse=... -> True para orden descendente (Z-A).
        tareas.controls.sort(key=CRITERIOS[criterio], reverse=inverso)
        # La lista de Python ya está ordenada, pero la pantalla no se entera sin update.
        page.update()

    # Se ejecuta cuando ocurre un evento (Enter en el campo o clic en "Añadir").
    # e es el evento que Flet pasa automáticamente; aquí no se usa.
    def añadir_tarea(e):
        # texto: recoge el valor del campo de texto, eliminando espacios al principio y al final.
        texto = nueva_tarea.value.strip()

        # Comprueba si el campo está vacío.
        # Un texto vacío ("") cuenta como False, así que "not texto" es True y entra en el if.
        if not texto:
            # muestra un mensaje de error en el TextField y no añade la tarea.
            nueva_tarea.error = "Escribe una tarea"
            page.update()  # Redibuja la pantalla para que se vea el mensaje de error.
            return  # sale de la función sin añadir la tarea

                # Recorre las tareas existentes para detectar duplicados.
        for fila_existente in tareas.controls:
            # .lower() pasa a minúsculas ambos textos, así no se distingue entre mayúsculas y minúsculas.
            # controls[0].label es el texto del checkbox de esa fila.
            if fila_existente.controls[0].label.lower() == texto.lower():
                mensaje.value = f"La tarea '{texto}' ya existe, no se puede añadir"
                page.update()
                return  # sale sin añadir la tarea

        mensaje.value = ""
        nueva_tarea.error = None  # Si el campo no está vacío, se borra el mensaje de error.
  
        #crea una fila (Row) vacia que contendrá el checkbox y el botón de eliminar.
        fila = ft.Row()
        # controls: lista de controles que contiene la fila.
        fila.controls = [
            # Checkbox: control que muestra un checkbox con el texto de la tarea.
            # on_change se dispara al marcar/desmarcar el checkbox
            ft.Checkbox(label=texto, expand=True, on_change=actualizar_contador),

            # IconButton: botón con un icono (EDIT)
            # icon es el icono que se muestra; icon_color es el color del icono.
            # on_click se dispara al pulsar el botón; llama a modificar_tarea pasando la fila como argumento.
            # Se usa lambda porque Flet solo envía el evento (e) y aquí hace falta pasar también la fila.
            ft.IconButton(
                icon=ft.Icons.EDIT,
                icon_color=ft.Colors.BLUE_400,
                on_click=lambda e: modificar_tarea(fila),
            ),
            
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

    # Crea un botón que llama a borrar_completadas al pulsarlo.
    boton_borrar = ft.Button(content="Borrar completadas", on_click=borrar_completadas)

    # >>> ORDENAR (3/3): botones. Se usa lambda para pasar el criterio al manejador -----
    fila_ordenar = ft.Row(
        wrap=True,
        controls=[
            ft.Text("Ordenar:"),
            ft.Button(content="A-Z", on_click=lambda e: ordenar_tareas("az")),
            ft.Button(content="Z-A", on_click=lambda e: ordenar_tareas("az", inverso=True)),
            ft.Button(content="Pendientes primero", on_click=lambda e: ordenar_tareas("estado")),
            ft.Button(content="Cortas primero", on_click=lambda e: ordenar_tareas("longitud")),
            ft.Button(content="Pendientes + A-Z", on_click=lambda e: ordenar_tareas("estado_az")),
        ],
    )
    # <<< ORDENAR

    # Añade los controles a la página en el orden que se quieren mostrar.
    page.add(titulo, ft.Row([nueva_tarea, boton]), mensaje, contador, fila_ordenar, tareas, boton_borrar)

# Llamada a ft.run() para ejecutar la app, pasando la función main como argumento.
ft.run(main)
