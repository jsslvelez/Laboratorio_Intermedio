#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 06:27:55 2024

Código para cálculos en el laboratorio de Equivalente Mecánico del Calor

@author: Jessiel J. Vélez
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#Fit de la tabla de temperatura vs resistencia para el termistor del aparato.

data = np.loadtxt('temperaturavsresistencia.txt', skiprows=1)

res = data[:,0]
temp = data[:,1]

def poly2(x,a,b,c):
    
    y = a/((x)**b)+c
    
    return y

def invpoly(x,a,b,c):
    
    y = x
    
    return y

parametros, cov = curve_fit(poly2, res, temp)

afit = parametros[0]
bfit = parametros[1]
cfit = parametros[2]

errparams = np.sqrt(np.diag(cov))

'''
La ecuación sería:
    
    y = [(734.1839101840109)/x^(0.12962695048894465)] + -140.13482018300394
'''

#Error del Fit

def errorT(R,errR):

    term4 = afit*bfit*(R**(bfit-1))*errR
    
    errT = np.abs(term4)
    
    return errT

def invpoly2(y):
    
    x = (afit/(y - cfit))**(1/bfit)
    
    return x

#Crear la data fitted

fitdat = poly2(res, afit, bfit, cfit)
invfit = invpoly2(temp)

fig, ax = plt.subplots(figsize  = (10,8), dpi=100)

ax.scatter(res,temp, color='black', label='Data original')
ax.plot(res,fitdat, color='red', label='Fit')
# ax.plot(invfit,temp, color = 'black')

ax.set_xlabel('Resistencia ($\Omega$)')
ax.set_ylabel('Temperatura ($\degree$C)')
ax.set_title('Temperatura vs Resistencia Del Termistor')

ax.legend()
