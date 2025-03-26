# -*- coding: utf-8 -*-
"""
Universidad de Puerto Rico
Recinto de Mayagüez 

Laboratorio Intermedio II - Efecto Hall

Instructor: Angel D. Reyes
Autor: Jessiel J. Vélez
"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"

def linefit(x,m,b):
    return m*x + b

def pordif(a,b):
    return (a-b)/((a+b)/2)

#%% RESULTADOS EXPERIMENTALES

v1i = np.array([1.60,1.78,1.95,1.96,1.92])
v1f = np.array([1.67,1.82,2.00,2.13,2.13])
v1 = np.average(v1f-v1i)
B1I = 108e-3*11.83

v2i = np.array([1.70,1.73,1.79,1.74,1.87])
v2f = np.array([1.96,2.00,2.03,2.01,2.03])
v2 = np.average(v2f-v2i)
B2I = 206e-3*11.93

v3i = np.array([2.14,2.20,2.20,2.15,2.22])
v3f = np.array([2.00,2.00,2.14,2.03,2.09])
v3 = np.average(v3f-v3i)
B3I = -108e-3*11.75

v4i = np.array([2.49,2.48,2.49,2.62,2.61])
v4f = np.array([2.20,2.11,2.24,2.36,2.39])
v4 = np.average(v4f-v4i)
B4I = -206e-3*11.86

v5i = np.array([0.03,0.00,-0.12,-0.14,1.06])
v5f = np.array([0.33,0.30,0.26,0.06,1.42])
v5 = np.average(v5f-v5i)
B5I = 303e-3*11.65

v6i = np.array([1.01,1.00,0.98,0.91,0.96])
v6f = np.array([0.70,0.65,0.56,0.60,0.52])
v6 = np.average(v6f-v6i)
B6I = -303e-3*11.57

v7i = np.array([1.48,1.60,1.57,1.60,1.67])*-1
v7f = np.array([1.05,1.06,1.10,1.10,1.18])*-1
v7 = np.average(v7f-v7i)
B7I = 404e-3*11.70

v8i = np.array([1.82,1.93,1.84,1.94,1.93])*-1
v8f = np.array([2.37,2.36,2.32,2.42,2.40])*-1
v8 = np.average(v8f-v8i)
B8I = -404e-3*11.70

v9i = np.array([1.60,1.65,1.73,1.77,1.78])*-1
v9f = np.array([1.04,1.05,1.09,1.14,1.17])*-1
v9 = np.average(v9f-v9i)
B9I = 516e-3*11.47

v10i = np.array([1.90,2.00,2.02,2.03,2.04])*-1
v10f = np.array([2.63,2.63,2.70,2.61,2.71])*-1
v10 = np.average(v10f-v10i)
B10I = -516e-3*11.88

Bs = np.array([B1I,B2I,B3I,B4I,B5I,B6I,B7I,B8I,B9I,B10I])
Vs = np.array([v1,v2,v3,v4,v5,v6,v7,v8,v9,v10])*1e-5

#%% FIT LINEAL DE LA DATA

params, cov = curve_fit(linefit,Bs,Vs)

mfit = params[0]
bfit = params[1]

#%% Análsis de error

#El error de las medidas de voltaje era de 0.05 V. Por lo que,
#para cada proedio el error será la raíz de la suma del cuadrado
#de 0.1.

errorV = np.sqrt(0.05)*1e-5

#%% PLOTTING

Vsfit = linefit(Bs,mfit,bfit)

fig, ax = plt.subplots(dpi=100)

# ax.errorbar(Bs,Vs,xerr=errorV,yerr=0, color='black')
# ax.plot(Bs, Vsfit, color='black', linestyle='dashed')

ax.scatter(Bs,Vs)
ax.plot(np.sort(Bs),np.sort(Vsfit), color='black', linestyle='--')
ax.errorbar(x=Bs,y=Vs, xerr=1,yerr=errorV, fmt='o', color='black')

ax.set_ylabel(r'$U_H$ (V)', size=15)
ax.set_xlabel(r'$B \cdot I$ (mT $\cdot$ A)', size=15)
ax.set_title('Voltaje de Hall vs Campo Magnético por Corriente', size=15)

plt.tick_params(axis='both', which='minor', labelsize=15)
plt.tick_params(axis='both', which='major', labelsize=15)

#%% EL RESULTADO DEL COEFICIENTE R_H

coeficiente = mfit*25e-6
errcoef = np.sqrt(np.diag(cov))[0]
print('El coeficiente de Hall: ',coeficiente)

print('El error del coeficiente de Hall: ',errcoef*1e-5)

porcentajedif = abs(pordif(coeficiente,4.31e-11)*100)
print('El porcentaje de diferenica: ',porcentajedif)
