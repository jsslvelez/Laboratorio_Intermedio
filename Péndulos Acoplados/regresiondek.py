#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 18:29:08 2024

Regresión Lineal para determinar la constante del resorte

@author: jessielvelez

"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman"]

F = np.array([6.103e-2, 12.21e-2, 18.31e-2, 24.41e-2])
x = np.array([0.0845, 0.1000, 0.1150, 0.1310])

def linefit(x,m,b):
    
    y = (m*x)+b
    
    return y

params, pcov = curve_fit(linefit,x,F)

fontsize = 18

fig, ax = plt.subplots(dpi=100, figsize=(8,6))

mfit = params[0]
bfit = params[1]

ax.errorbar(x,F, xerr = 0.0005, yerr = 0.03, fmt='o', color = 'black', )
ax.plot(x, linefit(x,mfit,bfit), color = 'black', linestyle = 'dashed')
ax.text(0.11,0.100,f'F = {mfit:.3f}x + {bfit:.3f}', fontsize = fontsize)

ax.set_xlabel('x (m)', fontsize= fontsize)
ax.set_ylabel('F (N)', fontsize= fontsize)
ax.set_title('Fuerza versus estiramiento del resorte', fontsize= fontsize)

ax.tick_params(axis='both', which='both', labelsize=12)

#Calculamos el error asociado a la búsqueda de m...

error = np.sqrt(np.diag(pcov))

for i in error:
    print(i)