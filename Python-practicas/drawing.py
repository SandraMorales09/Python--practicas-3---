import turtle as tu
import re
import docx

# Leer el documento Word
data = docx.Document("Source/tulips.docx")
coordinates = []
colors = []

# Procesar los párrafos del documento
for i in data.paragraphs:
    try:
        patron = r'[-+]?\d*\.\d+(?:[eE][-+]?\d+)?'
        patron_coord = r'\(' + patron + r'\s*,\s*' + patron + r'\)'
        patron_color = patron_coord + r'\s*,\s*' + patron + r'\)'

        # Buscar coordenadas y colores en los párrafos
        coord_str_top = re.findall(patron_coord, i.text)
        color_str_top = re.findall(patron_color, i.text)

        coord_num_top = []
        if color_str_top:
            color_val = re.findall(r'[-+]?\d*\.\d+', color_str_top[0])
            color_val_list = [float(k) for k in color_val]
            colors.append(tuple(color_val_list))

        for j in coord_str_top:
            coord_pos = re.findall(r'[-+]?\d*\.\d+', j)
            coord_num_list = [float(k) for k in coord_pos]
            coord_num_top.append(tuple(coord_num_list))

        coordinates.append(coord_num_top)
    except Exception as e:
        print(f"Error procesando un párrafo: {e}")
        pass

# Configuración de la pantalla y la pluma de dibujo
pen = tu.Turtle()
screen = tu.Screen()

tu.tracer(2)
pen.hideturtle()
pen.speed(10)
screen.getcanvas().winfo_toplevel().attributes("-fullscreen", True)

# Dibujar las figuras
for i in range(len(coordinates)):
    draw = True
    path = coordinates[i]
    col = colors[i] if i < len(colors) else (0, 0, 0)  # Color por defecto negro si no hay colores
    pen.color(col)
    pen.begin_fill()
    for order_pair in path:
        x, y = order_pair
        y = -1 * y  # Invertir la coordenada Y para la pantalla de turtle
        if draw:
            pen.up()
            pen.goto(x, y)
            pen.down()
            draw = False
        else:
            pen.goto(x, y)
    pen.end_fill()

pen.hideturtle()
screen.mainloop()