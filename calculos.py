import csv
import numpy as np


n_linea = 0

with open("coeficientes.txt","r") as coef:
    recolector = csv.reader(coef, delimiter=',', quotechar='"')
    for linea in recolector:
        coef1 = int(linea[0])
        coef2 = int(linea[1])
        n_linea += 1
        if (n_linea ==1):            
            coef3 = int(linea[2])
            coef4 = int(linea[3])
            a = np.array([[coef1, coef2],[coef3,coef4]])
        elif(n_linea == 2):
            b = np.array([coef1, coef2])


c = np.linalg.solve(a,b)

print(c)


            
    