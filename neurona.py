# -*- coding: utf-8 -*-
""" 

"""

import neurolab as nl
import numpy as np
import scipy as sp


datos = np.matrix(sp.genfromtxt("datos-entrenamiento.csv", delimiter=" "))

entrada = datos[:,:-1]

print otro
print entrada

objetivo = datos[:,-1]

# Crear red neuronal con 2 capas
rna = nl.net.newff([[-5, 5], [-5,5]], [14999, 5000, 1000, 100, 10, 1])

#Cambio de algoritmo a back progation simple
rna.trainf = nl.train.train_gd

#Datos para la RNA
error = rna.train(entrada, objetivo, epochs=75000, show=100, goal=0.02)

# Simulacion RNA
salida = rna.sim(entrada)

print rna.layers[0].np['w']
print rna.layers[1].np['w']

