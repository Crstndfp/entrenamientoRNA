# -*- coding: utf-8 -*-
"""

"""

import neurolab as nl
import numpy as np
import scipy as sp

<<<<<<< HEAD
# 
datos = np.matrix(sp.genfromtxt("datos-entrenamiento.csv", delimiter=" "))
=======

datos = np.matrix(sp.genfromtxt("normalizado.csv", delimiter=" "))

entrada = datos[:,:-5]
objetivo = datos[:,-5]

>>>>>>> refs/remotes/origin/master


maxmin = np.matrix([[ -5, 5] for i in range(len(entrada[1,:].T))])


# Crear red neuronal con 2 capas
rna = nl.net.newff(maxmin, [15000, 5000, 5])

#Cambio de algoritmo a back progation simple
rna.trainf = nl.train.train_gd

#Datos para la RNAd
error = rna.train(entrada, objetivo, epochs=75000, show=10, goal=0.02)


#rna.save("neurona.tmt")
# Simulacion RNA
salida = rna.sim(entrada)

<<<<<<< HEAD
print rna.layers[0].np['w']
print rna.layers[1].np['w']
=======
print salida
>>>>>>> refs/remotes/origin/master
