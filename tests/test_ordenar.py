import runpy, sys, os
sys.path.insert(0, os.path.dirname(__file__))
import fake_flet

def cargar(nombre):
    ft = fake_flet.build()
    runpy.run_path(os.path.join(os.path.dirname(__file__), "..", "codigo", nombre))
    return ft.page

def find(controls, content):
    return next(c for c in controls if getattr(c, "content", None) == content)

# ---------------- versión funcional ----------------
page = cargar("ordenar_funcional.py")
titulo, fila_in, mensaje, contador, fila_ord, tareas, boton_borrar = page.controls
campo, boton_add = fila_in.controls
def añadir(t):
    campo.value = t; boton_add.on_click(None)
def etiquetas(): return [f.controls[0].label for f in tareas.controls]
def pulsar(txt): find(fila_ord.controls, txt).on_click(None)

for t in ["pera", "Manzana", "kiwi", "albaricoque", "Higo"]: añadir(t)
assert etiquetas() == ["pera","Manzana","kiwi","albaricoque","Higo"]
pulsar("A-Z");              assert etiquetas() == ["albaricoque","Higo","kiwi","Manzana","pera"], etiquetas()
pulsar("Z-A");              assert etiquetas() == ["pera","Manzana","kiwi","Higo","albaricoque"], etiquetas()
# marcar "kiwi" y "pera" como completadas
for f in tareas.controls:
    if f.controls[0].label in ("kiwi","pera"): f.controls[0].value = True
pulsar("Pendientes primero")
assert [f.controls[0].value for f in tareas.controls] == [False,False,False,True,True]
# estable: los pendientes mantienen el orden anterior (Z-A) -> Manzana, Higo, albaricoque
assert etiquetas()[:3] == ["Manzana","Higo","albaricoque"], etiquetas()
pulsar("Pendientes + A-Z"); assert etiquetas() == ["albaricoque","Higo","Manzana","kiwi","pera"], etiquetas()
pulsar("Cortas primero");   assert len(etiquetas()[0]) == 4 and len(etiquetas()[-1]) == 11, etiquetas()
# modificar una tarea y volver a ordenar usa el texto NUEVO
fila = next(f for f in tareas.controls if f.controls[0].label == "Higo")
campo.value = "Zarzamora"; fila.controls[1].on_click(None)
pulsar("A-Z"); assert etiquetas()[-1] == "Zarzamora", etiquetas()
print("funcional OK")

# ---------------- versión con clases ----------------
page = cargar("ordenar_clases.py")
app = page.controls[0]
campo, prio, boton = app.controls[1].controls
fila_ord = app.controls[3]
def add(t, p):
    campo.value = t; prio.value = p; boton.on_click(None)
for t, p in [("b","Baja"),("a","Media"),("c","Alta"),("d","Baja"),("e","Alta")]: add(t, p)
nom = lambda: [t.nombre for t in app.tareas.controls]
find(fila_ord.controls,"Por prioridad").on_click(None);     assert nom() == ["c","e","a","b","d"], nom()
find(fila_ord.controls,"Prioridad + A-Z").on_click(None);   assert nom() == ["c","e","a","b","d"], nom()
find(fila_ord.controls,"Z-A").on_click(None);               assert nom() == ["e","d","c","b","a"], nom()
app.tareas.controls[0].casilla.value = True; app.tareas.controls[0].cambio_estado(None)  # marca 'e'
assert app.contador.value == "Tareas pendientes: 4"
find(fila_ord.controls,"Pendientes primero").on_click(None); assert nom()[-1] == "e", nom()
print("clases OK")

# ---------------- por key de control ----------------
ft = fake_flet.build()
import runpy as r
# la versión key usa on_submit=añadir antes de definirlo? no: se define antes. Solo probamos ordenar.
page = cargar("ordenar_por_key_control.py")
nueva_row, botones, tareas = page.controls
nueva, add_btn = nueva_row.controls
for t in ["x","y","z"]: nueva.value = t; add_btn.on_click(None)
find(botones.controls,"Más nuevas primero").on_click(None)
assert [f.key for f in tareas.controls] == [3,2,1]
find(botones.controls,"Orden de creación").on_click(None)
assert [f.key for f in tareas.controls] == [1,2,3]
print("key OK")
