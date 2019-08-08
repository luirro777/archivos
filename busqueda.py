texto = input("Ingrese texto a buscar en el archivo: ")
n_linea = 0
flag = 0

with open("ejemplo.txt", "r") as file:
    for linea in file.readlines():
        n_linea += 1
        if(texto in linea):
            print("Texto encontrado en la linea " + str(n_linea))
            flag = 1
            break

if (flag == 0):
    print("Texto no encontrado")

                
