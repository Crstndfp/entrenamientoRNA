# -*- coding: utf-8 -*-
"""
Programa que entrena una RNA
algoritmo que utiliza backpropagation
3 neuronas en la capa de salida 
n neuronas en la capa de entrada
n datos de entrada 
el numero de neuronas en la primera capa oculta es igual al
nuero de neuronas en la capa de entrada
el numero de neuronas en la segunda capa es n/2
factor de correcion 0.01
error aceptado 0.02

"""

import neurolab as nl
import numpy as np
import scipy as sp

#lectura de la matrix de datos
datos = np.matrix(sp.genfromtxt("datos-entrenamiento.csv", delimiter=" "))

#salida de la neurona 
columanas_salida = 3

#datos de entrada a la neurona
entrada = datos[:,:-3]
#datos de salida de la neurona
objetivo = datos[:,-3:]

#max min para cada dato de entrada a la neurona 
maxmin = np.matrix([[ -5, 5] for i in range(len(entrada[1,:].T))])

# valores para las capas de la neurona 
capa_entrada = entrada.shape[0]
capa_oculta1 = int(capa_entrada*0.5)
capa_oculta2 = int(capa_entrada*0.33)
capa_salida = 3


# Crear red neuronal con 4 capas 1 de entrada 2 ocultas y 1 de salida 
rna = nl.net.newff(maxmin, [ capa_entrada, capa_entrada, capa_oculta1, capa_salida])

#Cambio de algoritmo a back progation simple
rna.trainf = nl.train.train_gd

#Datos para la RNAd
error = rna.train(entrada, objetivo, epochs=7500000, show=100, goal=0.02, lr=0.01)


#rna.save("neurona.tmt")
# Simulacion RNA
rna.save("red-neuronal-artificial.tmt")
salida = rna.sim(entrada)


#print rna.layers[0].np['w']
#print rna.layers[1].np['w']

print salida

