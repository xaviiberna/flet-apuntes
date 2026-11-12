# Paso 1 · Hola mundo

**Archivo:** `codigo/paso1_hola_mundo.py` · **Objetivo:** entender la estructura mínima de una app Flet.

**Novedades:** `main(page)` · `page.add(...)` · `ft.run(main)`

```python title="paso1_hola_mundo.py"
--8<-- "codigo/paso1_hola_mundo.py"
```

| Código | Qué hace y por qué |
|---|---|
| `import flet as ft` | Importa la librería con el alias `ft` (verás `ft.` delante de casi todo). |
| `def main(page: ft.Page):` | Función principal. Flet la llama al arrancar y le entrega la **página**. `: ft.Page` es solo una pista de tipo para el editor. |
| `page.add(ft.Text("¡Hola, Flet!"))` | Crea un control `Text` y lo añade a la página. `page.add` además refresca la pantalla. |
| `ft.run(main)` | Arranca la app. Se pasa `main` **sin paréntesis**: le damos la función, no su resultado. |

!!! note "Idea clave"
    Flet llama a tu función `main` y te da la página. `page` es un lienzo en blanco y `main` son las instrucciones para dibujar.

**Qué deberías ver:** una ventana con «¡Hola, Flet!».

!!! failure "Errores típicos"
    - Olvidar el parámetro `page` en `main`.
    - Escribir `ft.run(main())` con paréntesis.
    - Llamar al archivo `flet.py`.

!!! question "Prueba tú"
    Cambia el texto y añade un segundo `ft.Text` en la misma llamada a `page.add(...)`. ¿En qué orden aparecen?
