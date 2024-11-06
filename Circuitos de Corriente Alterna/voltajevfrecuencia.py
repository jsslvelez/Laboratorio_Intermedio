#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 08:31:19 2024

Gráfica Voltaje vs Frecuencia

@author: jessielvelez
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

plt.rcParams["font.family"] = "Times New Roman"

def pordif(a,b): # Función de porcentaje de diferencia
    
    posum = np.abs(a-b)
    mean = (a+b)/2
    y = (posum/mean) * 100
    
    return y

data = np.loadtxt('/Users/jessielvelez/env/Laboratorio Intermedio/Circuitos de Corriente Alterna/voltajevfrecuencia copy 2.txt', skiprows=1)

freq = data[:,0]
V = data[:,2]

freqerr = data[:,1]
Verr = data[:,3]

#Fit Polynomial

def polyfit(x,a,b,c,d,e,f):
    
    y = a*(x**5) + b*(x**4) + c*(x**3) + d*(x**2) + e*x + f

    return y

params, pcov = curve_fit(polyfit,xdata=freq,ydata=V)

a = params[0]
b = params[1]
c = params[2]
d = params[3]
e = params[4]
f = params[5]

Vfit = polyfit(freq,a,b,c,d,e,f)

fig, ax = plt.subplots(dpi=150)

# ax.scatter(freq, V, s=8)
ax.errorbar(x = freq, y = V, xerr = freqerr, yerr = Verr, fmt='o', markersize = 4, color = 'black', label ='Data experimental' )
# ax.plot(freq, Vfit, linestyle='dotted', color='black', label = 'Regresión polinomial')

ax.set_title('Voltaje RMS vs Freuencia', fontsize = 15)
ax.set_xlabel('Frecuencia (Hz)', fontsize = 12)
ax.set_ylabel('Voltaje (V)', fontsize = 12)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# ¿Cual es la frecuencia de resonancia?

freqf = np.arange(start = 100, stop = 1000, step = 0.001)
vf = polyfit(freqf,a,b,c,d,e,f)

maxvloc = np.where(vf == np.max(vf))
v_0 = freqf[maxvloc]

# ticks = list(plt.xticks()[0])
# ticks[1] = 235
# plt.xticks(ticks)

perr = np.sqrt(np.diag(pcov))

#Otro estimadpo

maximos = data[6:17,0]
v_02 = np.average(maximos)
errmaximos = data[6:17,1]
errv_0 = np.sqrt(np.sum((errmaximos**2)))

DIF = pordif(v_02,200.8984510110529)

ax.vlines(v_02, 1.39, 1.465, color='black', linestyle='dashed', label = 'Máximo promedio')

ax.legend()

print(
      f'La frecuencia de resonancia para el circuito es: {v_02}'
      )

print(f'''
El porcentaje de diferencia entre la frecuencia de resonancia experimental 
y teórica es de {DIF}%.
      '''
      )