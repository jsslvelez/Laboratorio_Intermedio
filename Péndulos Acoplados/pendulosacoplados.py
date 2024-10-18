#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 23:28:12 2024

En este código se realizaran las gráficas y cálculos necesarios para el informe
Péndulos Acoplados.

@author: jessielvelez
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.integrate import trapezoid

import pandas as pd

import scipy as sp

plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman"]

faseizq = np.loadtxt('/Users/jessielvelez/env/Laboratorio Intermedio/Péndulos Acoplados/sensorangizquierdo_1.txt', skiprows=2)
faseder = np.loadtxt('/Users/jessielvelez/env/Laboratorio Intermedio/Péndulos Acoplados/sensorangderecho_1.txt', skiprows=2)

nofaseizq = np.loadtxt('/Users/jessielvelez/env/Laboratorio Intermedio/Péndulos Acoplados/sensorangizquierdo_3.txt', skiprows=2)
nofaseder = np.loadtxt('/Users/jessielvelez/env/Laboratorio Intermedio/Péndulos Acoplados/sensorangderecho_3.txt', skiprows=2)

unosoloizq = np.loadtxt('/Users/jessielvelez/env/Laboratorio Intermedio/Péndulos Acoplados/sensorangizquierdo_7.txt', skiprows=2)
unosoloder = np.loadtxt('/Users/jessielvelez/env/Laboratorio Intermedio/Péndulos Acoplados/sensorangderecho_7.txt', skiprows=2)

'''
FIT LINEAL
'''

def line(x,m,b):
    
    y = m*x + b
    
    return y

'''
GRÁFICAS
'''

fontsize = 18

#Gráfica de posición angular vs tiempo Caso 1

figf, axf = plt.subplots(nrows=2, dpi=100, figsize=(10,5), sharex = True)

figf.subplots_adjust(hspace= 0.1)
figf.subplots_adjust(top=0.85)
figf.suptitle('Caso 1: Oscilaciones en fase \n Posición angular versus tiempo', fontsize = 15, weight = 'bold')
figf.supylabel(r'$\theta$ (rad)', fontsize= fontsize)

#Izquierdo

axf[0].plot(faseizq[:,0],faseizq[:,1],color='black')

# axf[0].set_xlabel('t (s)', fontsize= fontsize)
axf[0].set_ylabel('Izquierdo', fontsize= fontsize)
# axf[0].set_title('(a) Posición angular versus tiempo: péndulo izquierdo', fontsize= fontsize)

axf[0].tick_params(axis='both', which='both', labelsize=12)

axf[0].set_xlim([14,30])

#Derecho

axf[1].plot(faseder[:,0],faseder[:,1],color='black')

axf[1].set_xlabel('t (s)', fontsize= fontsize)
axf[1].set_ylabel('Derecho', fontsize= fontsize)
# axf[1].set_title('(b) Posición angular versus tiempo: péndulo derecho', fontsize= fontsize)

axf[1].tick_params(axis='both', which='both', labelsize=12)

#Lineas verticales

axf[0].axvline(x=16.05, color = 'black', linestyle='dashed')
axf[1].axvline(x=16.05, color = 'black', linestyle='dashed')

axf[0].axvline(x=17.12, color = 'black', linestyle='dashed')
axf[1].axvline(x=17.12, color = 'black', linestyle='dashed')

axf[0].axvline(x=18.27, color = 'black', linestyle='dashed')
axf[1].axvline(x=18.27, color = 'black', linestyle='dashed')

axf[1].set_xlim([14,30])

'''
################################################################################################
'''

#Gráfica de posición angular vs tiempo Caso 2

figf, axf = plt.subplots(nrows=2, dpi=100, figsize=(10,5), sharex = True)

figf.subplots_adjust(hspace= 0.1)
figf.subplots_adjust(top=0.85)
figf.suptitle('Caso 2: Oscilaciones fuera de fase \n Posición angular versus tiempo', fontsize = 15, weight = 'bold')
figf.supylabel(r'$\theta$ (rad)', fontsize= fontsize)

#Izquierdo

axf[0].plot(nofaseizq[:,0],nofaseizq[:,1],color='black')

# axf[0].set_xlabel('t (s)', fontsize= fontsize)
axf[0].set_ylabel('Izquierdo', fontsize= fontsize)
# axf[0].set_title('(a) Posición angular versus tiempo: péndulo izquierdo', fontsize= fontsize)

axf[0].tick_params(axis='both', which='both', labelsize=12)

axf[0].set_xlim([26,40])

#Derecho

axf[1].plot(nofaseder[:,0],nofaseder[:,1],color='black')

axf[1].set_xlabel('t (s)', fontsize= fontsize)
axf[1].set_ylabel('Derecho', fontsize= fontsize)
# axf[1].set_title('(b) Posición angular versus tiempo: péndulo derecho', fontsize= fontsize)

#Lineas verticales

axf[0].axvline(x=31.02, color = 'black', linestyle='dashed')
axf[1].axvline(x=31.02, color = 'black', linestyle='dashed')

axf[0].axvline(x=27.95, color = 'black', linestyle='dashed')
axf[1].axvline(x=27.95, color = 'black', linestyle='dashed')

axf[0].axvline(x=29.18, color = 'black', linestyle='dashed')
axf[1].axvline(x=29.18, color = 'black', linestyle='dashed')

axf[1].tick_params(axis='both', which='both', labelsize=12)

axf[1].set_xlim([26,40])

'''
###########################################################################################################
'''

#Gráfica de posición angular vs tiempo Caso 3

figf, axf = plt.subplots(nrows=2, dpi=100, figsize=(10,5), sharex = True)

figf.subplots_adjust(hspace= 0.1)
figf.subplots_adjust(top=0.85)
figf.suptitle('Caso 3: Desplazamiento incial de un solo péndulo \n Posición angular versus tiempo', fontsize = 15, weight = 'bold')
figf.supylabel(r'$\theta$ (rad)', fontsize= fontsize)

#Izquierdo

axf[0].plot(unosoloizq[:,0],unosoloizq[:,1],color='black')

# axf[0].set_xlabel('t (s)', fontsize= fontsize)
axf[0].set_ylabel('Izquierdo', fontsize= fontsize)
# axf[0].set_title('(a) Posición angular versus tiempo: péndulo izquierdo', fontsize= fontsize)

axf[0].tick_params(axis='both', which='both', labelsize=12)
# axf[0].grid(visible=True, which='both')

axf[0].set_xlim([3,30])

#Derecho

axf[1].plot(unosoloder[:,0],unosoloder[:,1],color='black')

axf[1].set_xlabel('t (s)', fontsize= fontsize)
axf[1].set_ylabel('Derecho', fontsize= fontsize)
# axf[1].set_title('(b) Posición angular versus tiempo: péndulo derecho', fontsize= fontsize)

axf[1].tick_params(axis='both', which='both', labelsize=12)
# axf[1].grid(visible=True, which='both')
# Visualización de la envolvente


axf[1].set_xlim([3,30])

'''
########################################################################################################################
'''

#Para determinar una función senosoidal envolvente a la información obtenida
#es posible extraer el mínimo o máximo local de la data para así hacer una regresión sobre esta.

'''
Calculamos las frecuencias usando las funciones de numpy para DFT
'''

tstep = 0.001

sigizq = unosoloizq[:,1][5:]
sigder = unosoloder[:,1][5:]

nizq = sigizq.size
nder = sigder.size

fourier_izq = np.fft.fft(sigizq)
fourier_der = np.fft.fft(sigder)

fizq_mag = np.abs(fourier_izq)/nizq
fder_mag = np.abs(fourier_der)/nder

#Visualizamos la transformada del izquierdo

fstep = 1000/nizq
frecuenciaizq = np.linspace(0, (nizq-1)*fstep, nizq)

fig, ax = plt.subplots(dpi=100, figsize = (8,6))

ax.plot(frecuenciaizq,fizq_mag, color = 'black')
ax.set_xlabel('f (hz)', fontsize = fontsize)
ax.set_ylabel('Amplitud TFD' , fontsize = fontsize)
ax.set_title('Caso 3: TFD para el péndulo izquierdo', fontsize = fontsize)

ax.set_xlim([0,20])

ax.tick_params(axis='both', which='both', labelsize=12)

#Visualizamos la transformada del derecho

fstep = 1000/nder
frecuenciader = np.linspace(0, (nder-1)*fstep, nder)

fig, ax = plt.subplots(dpi=100, figsize = (8,6))

# ax.plot(1/(unosoloder[:,0][5:]),fder_mag, color = 'black')
ax.plot(frecuenciader,fder_mag, color = 'black')
ax.set_xlabel('f (hz)', fontsize = fontsize)
ax.set_ylabel('Amplitud TFD' , fontsize = fontsize)
ax.set_title('Caso 3: TFD para el péndulo derecho', fontsize = fontsize)

ax.set_xlim([0,20])

ax.tick_params(axis='both', which='both', labelsize=12)

#Cuales son las frecuencias?????

frange1 = np.where((frecuenciaizq > 0.5) & (frecuenciaizq < 1))
frange2 = np.where((frecuenciaizq > 1.5) & (frecuenciaizq < 1.8))

#Péndulo izquierdo

ampfmenor = np.max(fizq_mag[frange1])
ampfmayor = np.max(fizq_mag[frange2])

freqsizq = [frecuenciaizq[np.where(fizq_mag == ampfmenor)],frecuenciaizq[np.where(fizq_mag == ampfmayor)]]

ampfmenorder = np.max(fder_mag[frange1])
ampfmayorder = np.max(fder_mag[frange2])

freqsder = [frecuenciaizq[np.where(fder_mag == ampfmenorder)],frecuenciaizq[np.where(fder_mag == ampfmayorder)]]

#Péndulo derecho

# from scipy.signal import argrelextrema





# freqsAizq = argrelextrema(fizq_mag, np.greater) #Me dan las posiciones de los máximos de la función.
# freqsAder = argrelextrema(fder_mag, np.greater) #Quiero encontrar la posición de los dos números más grandes.

# fsizq = fizq_mag[freqsAizq]
# fsizq = fsizq[fsizq>0.7]

# periodosizq = unosoloizq[:,0][np.where(fizq_mag == fsizq)]

# fsder = fder_mag[freqsAder]

# fsizq = np.sort(fsizq)
# fsder = np.sort(fsder)

# for i in fsizq:
#     print(i)

# print(f'Las frecuencias para el péndulo izquierdo son: {fsizq[0:2]}')
# print('')
# print(f'Las frecuencias para el péndulo derecho son: {f}')

# fourier_izq = sp.fft.fft(sigizq)
# fourier_der = sp.fft.fft(sigder)

# nizq = sigizq.size
# nder = sigder.size

# timestep = 0.001

# freqizq = sp.fft.fftfreq(nizq, d = timestep)
# freqder = sp.fft.fftfreq(nder, d = timestep)