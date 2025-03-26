# -*- coding: utf-8 -*-
"""
Universidad de Puerto Rico
Recinto de Mayagüez

Cálculos para Laboratorio de Difracción de Rayos X

Instructor: Angel D. Reyes
Autor: Jessiel J. Vélez Cancel
"""

import numpy as np
from scipy.constants import c,h

#%% FUNCIONES

def energias(arr, d, n):
    
    c = 2.9979e8
    h = 6.6256e-34
    
    
    E = (n*h*c)/(2*d*np.sin(arr))
    return E

def pordif(a,b):
    
    promedio = (a+b)/2
    diferencia = a-b
    
    porcentajedif = (diferencia/promedio)*100
    
    return np.abs(porcentajedif)

def errorenergia(n,theta,d):
    
    const = (h*c*n)/(2*d*np.sin(theta))
    term1 = (errd/d)**2
    term2 = (errtheta/np.tan(theta))**2
    
    ERR = const*np.sqrt(term1+term2)
    
    return ERR

#%% CONSTANTES

d_KBr = 3.290e-10
d_LiF = 2.014e-10

eV = 1.6021e-19

#%% MEDICIONES Y CALCULOS

errd = 0
errtheta = 0.1*(np.pi/180)


n_KBr = np.array([1,1,2,2,3,3])
n_LiF = np.array([1,1,2,2])

thetaKBr = np.array([12.3,13.6,25.1,27.9,39.3,44.5])
thetaLiF = np.array([20.4,22.6,43.8,50.0])

angKBr = thetaKBr*(np.pi/180)
angLiF = thetaLiF*(np.pi/180)

energias_KBr = energias(angKBr, d_KBr, n_KBr)
energias_LiF = energias(angLiF, d_LiF, n_LiF)

#Cambio a electron voltios

eV_KBr = energias_KBr/eV
eV_LiF = energias_LiF/eV

#Valores Teóricos

#Nota que estos arrays estan ordenados de menor ángulo
#a mayor ángulo.

ang_compKBr = np.array([12.3,13.6,25.1,28.0,39.4,44.7])
ang_compLiF = np.array([20.4,22.7,44.0,50.3])

eV_compKBr = np.array([8.831,8.018,8.870,8.015,8.902,8.041])*1e3
eV_compLiF = np.array([8.830,7.974,8.857,8.005])*1e3

#Porcentaje de diferencia

difKBr = pordif(eV_KBr, eV_compKBr)
difLiF = pordif(eV_LiF,eV_compLiF)

difcristales = pordif(eV_KBr[:4], eV_LiF)

difangKBr = pordif(thetaKBr, ang_compKBr)
difangLiF = pordif(thetaLiF, ang_compLiF)

#Error asociado a los cálculos de energía

errorKBr = errorenergia(n_KBr,angKBr,d_KBr)/eV #En electronvoltios
errorLiF = errorenergia(n_LiF,angLiF,d_LiF)/eV
