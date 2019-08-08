import csv

with open("datos.csv", "r") as csvfile:
    recolector = csv.reader(csvfile, delimiter=',', quotechar='"')
    for linea in recolector:
        nombre = linea[0]
        apellido = linea[1]
        edad = linea[2]
        print("Nombre: " + nombre + ", Apellido: " + apellido + ", Edad: " + edad)

