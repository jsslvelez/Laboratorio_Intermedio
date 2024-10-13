#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:45:03 2024

ERROR PROPAGATION

La idea de este código es dejar colocado funciones para calcular el error absoluto o relativo
de cantidades obtenidas en el laboratorio intermedio. De esta forma, podemos acelerar los cálculos
en el futuro y ahorrarnos mucho tiempo.

@author: jessielvelez
"""

# ERROR RELATIVO

"""
Como esta es una expresión porcentual del valor original, una de las entradas de la función debe ser el 
valor de la medida. Adicional, debe tomar el error absoluto de la medida y de alguna forma especificar 
la operación que se desea realizar.
"""

import numpy as np

data = np.loadtxt('Data_Exp3.txt', skiprows=1)

V = data[:,3]
I = data[:,1]

errporV = 0.001/V
errporI = 0.001/I

#Error de los valores de R

errporR = (errporV + errporI)*100
R = V/I
errR = (errporR/100)*R

Results = np.column_stack((R,errporR))

'''
Cálculo de error para el primer método
'''

errTref = 1
errTrefrel = 1/294 
errRref = 0.1
errRrefrel = 0.1/0.5

#Esto es complicado, so lo voy a hacer paralelo a los calculos de T

#Error para el primer método
ErrT = ((R*(errporR/100) + errRref)/(R-0.5) + errRrefrel)*((R-0.5)/(4.5e-3*0.5)) + errTref

'''
Cálculo de error para el segundo método (Método de Tabla)
'''



