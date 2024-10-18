#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 19:19:14 2024

Algunos cálculos rápidos

@author: jessielvelez
"""

from scipy.constants import g
import numpy as np

l = 0.3703
k = 3.95
m = 0.07574

wplus = np.sqrt(g/l)

print(wplus)

#Su error

errleff = 0.001
erwplus = 1/2*((g/l)**(-1/2))*(errleff/g)

print(erwplus)

def perdif(x,y):
    
    prom = ((x-y)/((x+y)/2))*100
    
    return prom

print((1/0.625)*2*np.pi)

#Error de w teórico para fase

errorw_M = (1/2) * np.sqrt((g/(l**3)))*0.001

#Error de w teórico para fuera de fase

errorl = 0.001
errorm = 0.07e-3
errork = 0.03

const = 1/2*(((g/l)+(2*k)/m)**(-1/2))

term1 = ((const*g*(1/(l**2)))*errorl)**2

term2 = ((const*(2/m))*errork)**2

term3 = ((const*((2*k)/(m**2)))*errorm)**2

errorw_m = np.sqrt(term1+term2+term3)

#Calculando la envolvente y su error

w_M = np.sqrt(g/l)
w_m = np.sqrt(g/l + (2*k)/m)

T_env = (4*np.pi)/(w_m - w_M)

errT_env = ((4*np.pi)/((w_m - w_M)**2))*np.sqrt((errorw_m**2)+(errorw_M**2))