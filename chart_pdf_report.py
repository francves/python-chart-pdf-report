import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from matplotlib import pyplot as plt

# Abrimos el archivo JSON con los datos de los productos
with open("productos.json", "r") as archivo:
    data = json.load(archivo)

# Creamos una lista con las cantidades de productos
cantidades = [producto["cantidad"] for producto in data]

# Creamos una lista con los nombres de los productos
nombres = [producto["nombre"] for producto in data]

# Creamos una lista con las etiquetas de cada sección de la torta (solo el nombre y cantidad)
etiquetas = ["{} ({})".format(n, c) for n, c in zip(nombres, cantidades)]

# Creamos un gráfico de torta con las cantidades de productos y las etiquetas
plt.pie(cantidades, labels=etiquetas, autopct='%1.1f%%', textprops={'fontsize': 10})

# Guardamos el gráfico como una imagen PNG
plt.savefig("grafico.png")

# Creamos el PDF y agregamos la imagen del gráfico con las cantidades y nombres
doc = canvas.Canvas("reporte.pdf", pagesize=letter)

# Agregamos el título del gráfico
doc.drawString(100, 750, "Gráfico de torta de cantidades de productos con porcentajes")

# Agregamos la imagen del gráfico con las cantidades y nombres
doc.drawImage("grafico.png", 50, 50, width=500, height=500)

doc.save()
