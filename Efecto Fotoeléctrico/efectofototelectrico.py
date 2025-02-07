# -*- coding: utf-8 -*-
"""
Universidad de Puerto Rico
Recinto de Mayagüez 

Laboratorio Intermedio II - Efecto Fotoeléctrico

Instructor: Angel D. Reyes
Autor: Jessiel J. Vélez
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.constants import e, h 

plt.rcParams["font.family"] = "Times New Roman"

###############################################################################
# FUNCION
###############################################################################

def linefit(x,m,b):
    return (m*x)+b

def porerr(a,b):
    return np.abs((a-b)/b)*100

def promedio(a,b):
    return (a+b)/2

###############################################################################
# MEDICIONES
###############################################################################

frecuencia = np.array([5.18672, 5.48996, 6.87858, 7.4085, 8.20264])

primerorden = np.array([0.604e0, 0.695e0, 1.231e0, 1.425e0, 1.681e0])
segundoorden = np.array([0.492e0, 0.524e0, 1.155e0, 1.320e0, 1.613e0])

###############################################################################
# FIT
###############################################################################

params1, cov1 = curve_fit(linefit, frecuencia, primerorden)
params2, cov2 = curve_fit(linefit, frecuencia, segundoorden)

errcov1 = np.sqrt(np.diag(cov1))
errcov2 = np.sqrt(np.diag(cov2))

errm1, errb1 = errcov1[0], errcov1[1]
errm2, errb2 =errcov2[0], errcov2[1]

m1, b1 = params1[0], params1[1]
m2, b2 = params2[0], params2[1]

myb1 = np.array([m1,errm1,b1,errb1])
myb2 = np.array([m2,errm2,b2,errb2])

hywo1 = myb1*e
hywo2 = myb2*e

###############################################################################
# PLOTTING
###############################################################################

desviacion = np.ones(shape = (1,5), dtype=float)*0.001

fig, ax = plt.subplots(2,1, dpi=200)

ax[0].scatter(frecuencia*1e-14, primerorden, color = 'black')
ax[1].scatter(frecuencia*1e-14, segundoorden, color = 'black')

ax[0].set_title('Primer Orden')
ax[1].set_title('Segundo Orden')

plt.subplots_adjust(hspace=0.35)

#PLOT LOS FITS

ax[0].plot(frecuencia*1e-14, linefit(frecuencia*1e-14, m1*1e14, b1), color = 'black', linestyle = 'dashed')
ax[1].plot(frecuencia*1e-14, linefit(frecuencia*1e-14, m2*1e14, b2), color = 'black', linestyle = 'dashed')

fig.supxlabel('Frecuencia (Hz)', size = 15, y = -0.01)
fig.supylabel('Potencial Eléctrico (Voltios)', size = 15)
fig.suptitle('Potencial de freno vs Frecuencia', size = 18, y = 1)

###############################################################################
# PORCENTAJE DE ERROR
###############################################################################

error1 = porerr(hywo1[0]*1e-14, h)
error2 = porerr(hywo2[0]*1e-14, h)

prom = promedio(hywo1[0]*1e-14, hywo2[0]*1e-14)
errprom = hywo1[1] + hywo2[1]
difprom = porerr(prom,h)