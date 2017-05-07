import neurolab as nl
import numpy as np
import scipy as sp
import os


def normalized(a, axis=-1, order=2):
    l2 = np.atleast_1d(np.linalg.norm(a, order, axis))
    l2[l2==0] = 1
    return a / np.expand_dims(l2, axis)

def mandar(archivo, salida):
    archivo_entrenamiento = open("normalizado.csv", "a")
    global cont
    for x1 in range(len(archivo[:, 0])):
        normalizado = normalized(archivo[x1, :])
        for x2 in range(normalizado.shape[1]):
            b = str(normalizado[0, x2])
            archivo_entrenamiento.write(b[:b.find(".")+5])
            archivo_entrenamiento.write(" ")
        archivo_entrenamiento.write(salida)
        archivo_entrenamiento.write("\n")
    archivo_entrenamiento.close()


# A = np.array([252 1],[180, 230],[255, 180])
# print (A)
if(os.path.exists("normalizado.csv")== True):
    os.remove("normalizado.csv")
dato = np.matrix(sp.genfromtxt("tomates-recortados-bueno.csv", delimiter=" "))
dato2 = np.matrix(sp.genfromtxt("tomates-recortados-malos.csv", delimiter=" "))
salida1 = "0.09 0 0 0 0"
salida2 = "0 0.09 0 0 0"
mandar(dato,salida1)
mandar(dato2,salida2)
