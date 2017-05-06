import neurolab as nl
import numpy as np
import scipy as sp
import os



def normalized(a, axis=-1, order=2):
    l2 = np.atleast_1d(np.linalg.norm(a, order, axis))
    l2[l2==0] = 1
    return a / np.expand_dims(l2, axis)

# A = np.array([252 1],[180, 230],[255, 180])
# print (A)
if(os.path.exists("normalizado.csv")== True):
    os.remove("normalizado.csv")
datos = np.matrix(sp.genfromtxt("datos-entrenamiento.csv", delimiter=" "))
entrada = datos[:,:-1]

archivo_entrenamiento = open("normalizado.csv", "a")
for x1 in range(len(entrada[:, 0])):
    normalizado = normalized(entrada[x1, :])
    for x2 in range(normalizado.shape[1]):
        b = str(normalizado[0, x2])
        archivo_entrenamiento.write(b[:b.find(".")+5])
        archivo_entrenamiento.write(" ")
    archivo_entrenamiento.write("1")
    archivo_entrenamiento.write("\n")
