#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 20:48:30 2024

Cálculos de Temperatura para el Experimento #3
de Radiación Térmica.

Estaré utilizando los dos métodos descritos por el manual y estaré comparandolos.
De esta forma, puedo encontrar cuál es el mejor método.

@author: jessielvelez
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


data = np.loadtxt('Data_Exp3.txt', skiprows=1)

VoltFed = data[:,0]
Amps = data[:,1]
Rad = data[:,2]
VoltMed = data[:,3]

def ResCalc(V,I):
    
    return V/I

ResFed = ResCalc(VoltFed,Amps)
ResMed = ResCalc(VoltMed,Amps)

'''
ERROR DE RESISTENCIA
'''

errrelI = (0.001/Amps) * 100
errrelV = (0.1/Rad) * 100

errrel = errrelI +errrelV

print("Error en Resistencia")
for i in errrel:
    print(i)

#Método para cambios pequeños en temperatura
def TempSmol(Res):
    
    TempRoom = 294
    ResRoom = 0.5
    alpha = 4.5e-3
    
    Temp1 = ((Res - ResRoom)/(alpha*ResRoom))+TempRoom
    
    return Temp1

# FIT DE TABLA DE TEMPERATURA VS RESISTIVIDAD PARA TUNGSTENO

datafit = np.loadtxt('RelResVsTemp.txt', skiprows=1)

relres = datafit[:,0]
temp = datafit[:,1]

fig1, ax1 = plt.subplots()

ax1.scatter(relres,temp, color='black')

def polyfunc(x,a,b):
    
    temperature = a*x**(b)
    return temperature

params, cov = curve_fit(polyfunc, xdata=relres, ydata=temp)

fita = params[0]
fitb = params[1]

tempfit = polyfunc(relres, fita, fitb)
perr = np.sqrt(np.diag(cov))

#PLOT FIT

ax1.plot(relres,tempfit, color='black')
ax1.set_xlabel('Resistencia ($\Omega$)')
ax1.set_ylabel('Temperatura (K)')
ax1.set_title('Fit de Valores de Resistencia vs Temperatura para Tungsteno')

#Método para cambios grandes en temperatura
def TempBig(Res):
    
    ResRoom = 0.5 # Solo dió a una cifra
    
    RelRes = Res/ResRoom
    Temp2 = polyfunc(RelRes, fita, fitb)
    
    return Temp2

'''
ERROR PARA EL METODO USADO PARA CALCULAR T
'''

errR = (errrel/100)*ResMed

term1 = fita*fitb*(ResMed*(fitb-1))
term2 = errR

errorT = np.sqrt((term1**2)*(term2**2))

print('Error de T')
for i in errorT:
    print(i)




plt.savefig('fit', dpi=100)

#Comparación de Data

fig, ax = plt.subplots(dpi=100)

tempcal1 = TempSmol(ResMed)
tempcal2 = TempBig(ResMed)

'''
ERROR EN T4
'''

errorT4rel = (errorT/tempcal2)*400


print('Error en la temperatura a la cuarta potencia')
for i in errorT4rel:
    print(i)





ax.scatter(ResMed, tempcal1,label = 'Método 1 (intervalos pequeños)')
ax.scatter(ResMed, tempcal2,label = 'Método 2 (intervalos grandes)')

ax.set_xlabel('Resistencia ($\Omega$)')
ax.set_ylabel('Temperatura (K)')
ax.set_title('Resistencia del Filamento vs Temperatura')
ax.legend()

# Ahora grafico RadVsTemp y RadVsTemp^4

fig2, ax2 = plt.subplots(ncols=2,figsize = (9,4), dpi=100)

#Fit de Rad vs Temp^4

fourthpow1 = tempcal1**4
fourthpow2 = tempcal2**4

def linefit(x,m,b):
    y = m*(x*1e10)+b
    return y

#Para tempcal 1

params1, covline1 = curve_fit(f = linefit, xdata = Rad, ydata = fourthpow1)

fitm1 = params1[0]
fitb1 = params1[1]
perr1 = np.sqrt(np.diag(covline1))

#Para tempcal 2

params2, covline2 = curve_fit(f = linefit, xdata = Rad, ydata = fourthpow2)

fitm2 = params2[0]
fitb2 = params2[1]
perr2 = np.sqrt(np.diag(covline2))

#Calcualte the fits

fit1 = linefit(Rad, fitm1, fitb1)
fit2 = linefit(Rad, fitm2, fitb2)

#Plotting

ax2[0].scatter(Rad, tempcal1)
ax2[0].scatter(Rad, tempcal2)
ax2[1].scatter(Rad, fourthpow1)
ax2[1].scatter(Rad, fourthpow2)

#Plot fits

ax2[1].plot(Rad, fit1)
ax2[1].plot(Rad,fit2)

ax2[0].set_xlabel('Radiación (mV)')
ax2[0].set_ylabel('Temperatura (K)')
ax2[0].set_title('Rad Vs T')

ax2[1].set_xlabel('Radiación (mV)')
ax2[1].set_ylabel(r'$\mathrm{T}^4 \ (\mathrm{K}^4)$')
ax2[1].set_title(r'Rad vs $\mathrm{T}^4$')

#LA DATA QUE SE VA A USAR

TempData = tempcal2
TempData4 = TempData**4

params3, cov3 = curve_fit(linefit, Rad, TempData4)

finalmfit = params3[0]
finalbfit = params3[1]

finalfit = linefit(Rad, finalmfit, finalbfit)

#Final Plotting


finalfig, finalax = plt.subplots(ncols=1, dpi=100)

finalax.set_xlabel('Rad (mv)')
finalax.set_ylabel('Temperatura (K)')
finalax.set_title('Radiación vs Temperatura')

finalax.scatter(Rad,TempData, color = 'black')

plt.savefig('RadvT',dpi=100)

finalfig, finalax = plt.subplots(ncols=1, dpi=100)

finalax.scatter(Rad, TempData4, color = 'black')
finalax.plot(Rad,finalfit, color = 'black')

finalax.set_xlabel('Rad (mv)')
finalax.set_ylabel(r'$\mathrm{T}^4 (\mathrm{k}^4)$')
finalax.set_title(r'Radiación vs $\mathrm{T}^4$')

plt.savefig("RadvTemp4",dpi=100)