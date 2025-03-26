# -*- coding: utf-8 -*-
"""
Universidad de Puerto Rico
Recinto de Mayagüez 

Laboratorio Intermedio II - Ancho de Banda del Germanio

Instructor: Angel D. Reyes
Autor: Jessiel J. Vélez
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

plt.rcParams["font.family"] = "Times New Roman"

def f(x,b,c):
    return x*b + c

def porerror(a,b):
    return abs((a-b)/b)*100

c = 40e-6 # (V/K)
l = 20e-3
A = 10e-6
k = 8.617333262145179e-05 # (eV)
Tamb = 24+273.15

# LA LITERATURA PROPORCIONA UN VALOR GENERALMENTE ACEPTADO

AnchoTeo = 0.67 # (eV)

###############################################################################
# Mediciones Experimentales

VTermometro = np.array([
    3.186,
    2.718,
    2.290,
    1.937,
    1.632,
    1.386,
    1.179,
    1.013,
    0.867,
    0.746
    ])*1e-3 - 0.046e-3
VSample = np.array([
    0.9829,
    1.2771,
    1.6107,
    1.9411,
    2.2580,
    2.5444,
    2.7905,
    2.9929,
    3.1650,
    3.3107
    ])
ISample = np.array([
    12.27,
    11.39,
    10.39,
    9.39,
    8.44,
    7.58,
    6.84,
    6.23,
    5.71,
    5.27
    ])*1e-3

###############################################################################
# TEMPERATURA DE LA MUESTRA

Temp = VTermometro/c + Tamb
invTemp = 1000/Temp

#CONDUCTIVIDAD DE LA MUESTRA

Cond = (l/A)*(ISample/VSample)
logdecond = np.log(Cond)

###############################################################################
# LINEFIT

params, cov = curve_fit(f, invTemp, logdecond)

mfit = params[0]
bfit = params[1]

errmfit = np.sqrt(np.diag(cov))[0]

# CALCULAMOS EL ANCHO DE BANDA

AnchoExp = -(mfit*2000*k)
errAnchoExp = errmfit*2000*k
Err = porerror(AnchoExp, AnchoTeo)

print(f'El ancho de banda experimental es de: {AnchoExp}')
print(f'El error asociado es de {Err}.')

###############################################################################
# ANÁLISIS DE ERROR

errVTerm = 0.001e-3
errVSamp = 0.0001
errISamp = 0.005e-3

errTemp = errVTerm/c
errinvTemp = ((1000*errTemp)/Temp**2)

term1 = (errISamp/ISample)**2
term2 = (errVSamp/VSample)**2
errcond = Cond*np.sqrt(term1+term2)
errlogcond = np.sqrt(term1+term2)

###############################################################################
# GRAFICAMOS

fig, ax = plt.subplots()

ax.errorbar(invTemp, logdecond, yerr= errlogcond, xerr=errinvTemp, fmt='o', color='black')
ax.plot(invTemp, f(1000/Temp,mfit,bfit), color='black', linestyle='--')

ax.set_xlabel(r'$1000/T \ K^{-1}$' , fontsize=12)
ax.set_ylabel(r'$\log(\sigma)$', fontsize=12)
ax.set_title('Coductividad vs Temperatura', fontsize=15)

ax.tick_params(labelsize=12)



