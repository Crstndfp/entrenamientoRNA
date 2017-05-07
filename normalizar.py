import neurolab as nl
import numpy as np
import scipy as sp
import os, sys
from tempfile import TemporaryFile

def normalizar(x):
    salida = (x*10.)/255.
    return np.fromstring(salida)


def normalized(a, axis=-1, order=2):
    l2 = np.atleast_1d(np.linalg.norm(a, order, axis))
    l2[l2==0] = 1
    return a / np.expand_dims(l2, axis)

def mandar(archivo):
    archivo_entrenamiento = open("normalizado.csv", "a")
    global cont
    for x1 in range(len(archivo[:, 0])):
        for x2 in range(archivo.shape[1]):
            # print np.fromstring(normalizar(archivo[:,x2]))
            # print archivo[:,x2]
            outfile = TemporaryFile()
            np.save(archivo_entrenamiento,normalizar(archivo[:,x2]))

            # a= str(n)
            # print a[:a.find(".")+5]

            #archivo_entrenamiento.write(np.save(normalizar(archivo[:,x2]), outfile))
            # archivo_entrenamiento.write(" ")
    print "fin"
            #normalizar
    #    normalizado = normalized(archivo[x1, :])
    #    for x2 in range(normalizado.shape[1]):

    #        archivo_entrenamiento.write(b[:b.find(".")+5])
    #        archivo_entrenamiento.write(" ")
    #    archivo_entrenamiento.write(salida)
    #    archivo_entrenamiento.write("\n")
    # archivo_entrenamiento.close()




# A = np.array([252 1],[180, 230],[255, 180])
# print (A)
if(os.path.exists("normalizado.csv")== True):
    os.remove("normalizado.csv")
dato = np.matrix(sp.genfromtxt("tomates-recortados-bueno.csv", delimiter=" "))
# dato2 = np.matrix(sp.genfromtxt("tomates-recortados-malos.csv", delimiter=" "))
# salida1 = "0.09 0 0 0 0"
#salida2 = "0 0.09 0 0 0"
mandar(dato)
# mandar(dato2,salida2)
