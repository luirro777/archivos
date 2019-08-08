import hashlib
import linecache

def registro():
    usuario = input("Ingrese usuario a registrar: ")
    password = input("Ingrese contraseña: ")
    pass_hash = hashlib.md5(password.encode())
    with open("users.txt", "a") as ufile:
        ufile.write(usuario + "\n")
    with open("passwords.txt", "a")as pfile:
        pfile.write(pass_hash.hexdigest() + "\n")
   
def lectura():
    print("Archivo de usuarios:")
    with open("users.txt", "r") as ufile:
        for linea in ufile.readlines():
            print(linea)
    print("Archivo de contraseñas:")
    with open("passwords.txt", "r")as pfile:
        for linea in pfile.readlines():
            print(linea)     

def login():
    n_linea = 0
    flag = 0
    usuario = input("Usuario: ")

    with open("users.txt", "r") as ufile:
        for linea in ufile.readlines():
            n_linea += 1
            if(usuario in linea):
                flag = 1                
                break
        if (flag == 0):
            print("Usuario no encontrado")
        else:            
            password = input("Password: ")
            pass_hash = hashlib.md5(password.encode())
            linea = linecache.getline("passwords.txt", n_linea)
            if(pass_hash.hexdigest() in linea):
                print("Login exitoso")
            else:
                print("Contraseña incorrecta")
                                    

opcion = "99"

while(opcion != "4"):
    print('''
          SELECCIONE UNA OPCION:
              1 - Registrar usuario
              2 - Mostrar contenido de los archivos
              3 - Login
              4 - Exit
        '''
            )
    opcion = input("Opcion: ")
    if(opcion == "1"):
        registro()
    elif(opcion == "2"):
        lectura()
    elif(opcion == "3"):
        login()
    elif(opcion == "4"):
        break
    else:
        print("Opcion no valida")

        


              
