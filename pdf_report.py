from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import json

# Abrimos el archivo JSON con los datos de los productos
with open("productos.json", "r") as archivo:
    data = json.load(archivo)

# Convertimos los datos en una lista de listas para crear la tabla
tabla_datos = [["Nombre", "Precio", "Cantidad", "Imagen"]]

for producto in data:
    tabla_datos.append([producto["nombre"], producto["precio"], producto["cantidad"], producto["imagen"]])

# Creamos el PDF y agregamos la tabla de datos
doc = SimpleDocTemplate("reporte.pdf", pagesize=letter)

estilos = getSampleStyleSheet()
tabla_estilo = TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    ("ALIGN", (0, 0), (-1, 0), "CENTER"),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, 0), 14),
    ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
    ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
    ("TEXTCOLOR", (0, 1), (-1, -1), colors.black),
    ("ALIGN", (0, 1), (-2, -1), "LEFT"),
    ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
    ("FONTSIZE", (0, 1), (-1, -1), 12),
    ("TOPPADDING", (0, 1), (-1, -1), 12),
    ("BOTTOMPADDING", (0, -1), (-1, -1), 12),
    ("LINEABOVE", (0, 0), (-1, 0), 1, colors.black),
    ("LINEBELOW", (0, 0), (-1, 0), 1, colors.black),
    ("GRID", (0, 1), (-1, -1), 1, colors.grey)
])

tabla = Table(tabla_datos)

tabla.setStyle(tabla_estilo)

contenido = [tabla]

doc.build(contenido)
