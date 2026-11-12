"""Mini-sustituto de Flet SOLO para probar la lógica (sin ventana). No es parte del temario."""
import sys, types

class Control:
    def __init__(self, *args, **kw):
        self.controls = []
        for a in args:
            if isinstance(a, list): self.controls = list(a)
            elif isinstance(a, str): self.value = a
        for k, v in kw.items(): setattr(self, k, v)
        self.__dict__.setdefault("value", None)
    def update(self):
        if hasattr(self, "before_update"): self.before_update()

class Page(Control):
    def add(self, *c): self.controls.extend(c)
    def update(self): pass

class Checkbox(Control):
    def __init__(self, *a, **k):
        super().__init__(*a, **k); self.value = k.get("value", False)

def control(cls):
    def __init__(self, **kw):
        Control.__init__(self)
        for klass in reversed(cls.__mro__):
            for k in getattr(klass, "__annotations__", {}): setattr(self, k, getattr(klass, k, None))
        for k, v in kw.items(): setattr(self, k, v)
        self.init()
    cls.__init__ = __init__
    return cls

class _Enum:
    def __getattr__(self, n): return n

def build():
    ft = types.ModuleType("flet")
    for n in ["Text","TextField","Button","Row","Column","IconButton","Dropdown","DropdownOption"]:
        setattr(ft, n, type(n, (Control,), {}))
    ft.Checkbox = Checkbox; ft.Page = Page; ft.control = control
    ft.Colors = _Enum(); ft.Icons = _Enum(); ft.FontWeight = _Enum(); ft.MainAxisAlignment = _Enum()
    ft.DropdownOption = type("DropdownOption", (Control,), {})
    def run(main):
        p = Page(); main(p); ft.page = p
    ft.run = run
    sys.modules["flet"] = ft
    return ft
