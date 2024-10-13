#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 14:28:32 2024

Regresión de Resistencis Vs Temperatura para el Cubo de Leslie.

@author: jessielvelez
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = np.loadtxt('ResVTempforCube.txt', skiprows=1)

Res = data[:,0]
Temp = data[:,1]

def inversefunction(x,a,b,c):
    
    y_fit = a*((x+c)**b)
    
    return y_fit

params, cov = curve_fit(f = inversefunction, xdata = Res, ydata = Temp)

fita = params[0]
fitb = params[1]
fitc = params[2]

fitTemp = inversefunction(Res, fita, fitb, fitc)
perr = np.sqrt(np.diag(cov))


'''



PLOTTING




'''

fig, ax = plt.subplots(figsize=(10,8))

ax.set_xlabel('Therm. Res. ($\Omega$)', fontsize = 15)
ax.set_ylabel('Temp. ($\degree C$)', fontsize = 15)
ax.set_title('Resistencia vs. Temperatura para el Cubo de Radiación Térmica', fontsize = 15)

plt.scatter(Res, Temp, color = 'black', label = "Datos del manual")
plt.plot(Res,fitTemp, linestyle = 'dashed', color = 'red', label = 'Fit')

fig.text(0.5, 0.4, r'$y= a \ \frac{1}{(x+c)^b}+d$', size=(25))

textstr = '\n'.join((
    r'$a =%.2f$' % (fita, ),
    r'$b=%.2f$' % (fitb, )))
    # r'$c =%.2f$' % (fitc, ),
    # r'$d =%.2f$' % (fitd, )))

props = dict(boxstyle='square', facecolor='white', alpha=0.5)

ax.text(0.78, 0.85, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)

plt.legend(prop={'size':12})

plt.show()

#CALCULA LOS VALORES CORRESPONDIENTES A TUS DATOS

datosexp = np.array([40.50e3,29.50e3,20.50e3,15.86e3])
resultados = inversefunction(datosexp, fita, fitb, fitc)


'''



PARTE 4 & ERROR




'''

R = np.array([64.7,39.6,24.86,15.52])
errorR = np.array([0.1,0.1,0.01,0.01])


term1 = fita*fitb*((R-fitc)**(fitb-1))
term2 = errorR

errorT = np.sqrt((term1**2)*(term2**2))

print('ERROR EN T')
for i in errorT:
    print(i)





