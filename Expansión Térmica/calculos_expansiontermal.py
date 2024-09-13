#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 19:01:20 2024

Cálculos para Expansión Termal

@author: Jessiel J. Vélez
"""

import numpy as np

L, errL = np.array([416.5,417.0,417.0]), 0.5 # Valores de Largo

Deltatheta, errDtheta = np.array([0.1414,0.1618,0.1916]), 0.0008 # Desplazamiento Angular

T_in, errT_in = np.array([22, 22, 21]), 1 # Temperatura Inicial

T_fi, errT_fi = np.array([61,63,72]), 1 # Temperatura Final

r_sensor = 1.327 # Radio de la punta del sensor

# Determinar el cambio en L

DeltaL = Deltatheta*r_sensor
errDeltaL = (errDtheta/Deltatheta) #Falta Multiplicar por 100%

# Determinar el cambio en temperatura

DeltaT = T_fi - T_in
errDeltaT = errT_fi+errT_in #Este es un error absoluto
errDeltaTfrac = errDeltaT/DeltaT

# Determinar el coeficiente de expansión

coef = DeltaL/(L*DeltaT)
errcoef = (errDeltaTfrac+(errL/L)+errDeltaL)*100

#Determinar el porcentaje de error para cada coeficiente

valoresaceptados = np.array([17e-6,19e-6,23e-6])

PorDif = ((np.abs(coef-valoresaceptados))/((coef + valoresaceptados)/2)) * 100

#Detalles Adicionales

errDeltaL = errDeltaL*100


