file = open("ejemplo.txt", "a")
texto = input("Ingrese texto a insertar en el archivo: ")
file.write(texto + "\n")
file.close()

file = open("ejemplo.txt", "r")

for linea in file.readlines():
    print(linea)
file.close()
                
