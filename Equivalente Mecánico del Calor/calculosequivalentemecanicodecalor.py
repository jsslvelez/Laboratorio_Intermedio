#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:12:00 2024

Cálculos para Lab de Equivalente Mecánico del Calor

@author: jessielvelez
"""

import numpy as np
from scipy.constants import pi, g

M, errorM = 4.3809, 0.0005
R, errorR = 2.375, 0.005 # radio del cilindro
N = np.array([260,273,223])

#Cálculo de Trabajo

W = (M*g*R* 10**(-2))*(2*pi*N) # En julios (J)

m, errorm = np.array([201.650, 202.239, 200]), np.array([0.005,0.005, 1.5])
c = 0.220
Tf, errorTf = np.array([33.5 ,33.9 ,32.0]), np.array([0.3, 0.3, 0.3])
Ti, errorTi = np.array([25.2, 25.0, 23.7]), np.array([0.2, 0.2, 0.2])

#Cálculo de Calor

Q = m*c*(Tf-Ti) #En calorias (c)

#Cálculo del Equivalente Mecánico del Calor

J = (W/Q)

# Actual Value and Comparison

J_actual = 4.186 # Valor del libro de texto (Citar Serway)

#Porcentaje de error

PorError = np.abs((J-J_actual)/J_actual)*100

'''
ANÁLISIS DE ERROR
'''

#Para el trabajo, los únicos contribuyentes al error será la masa del objeto y el valor de R, puesto
# que las constantes se tomaron a suficientes espacios decimales y los demás valores no contribuyen error.

errorW = (errorM/M)+(errorR/R)*100 #Error relativo

#Para el calor, a tres cifras significativas y notando que los contribuyentes de error serán las temperaturas y la masa
# del cilindro

errorDT = errorTf + errorTi
DT = Tf-Ti

errorQ = ((errorm/m)+(errorDT/DT))*100

#Para J, los errores relativos de ambos terminos se suman. Por lo que,

errorJ = errorW + errorQ

#Calculamos el promedio de J y también su error asociado.

J_esperado = np.average(J)

errorJabs = (errorJ/100)*J

errorJ_esperado = np.sqrt(np.sum((errorJabs**2)))

#Porcentaje de error del promedio

AVGporerror = np.abs((J_esperado - J_actual)/J_actual)*100
    
    