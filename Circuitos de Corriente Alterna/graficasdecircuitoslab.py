#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 10:56:43 2024

Gráficas para Laboratorio de Circuitos de Corriente Alterna

@author: Jessiel J. Vélez
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Font

plt.rcParams["font.family"] = "Times New Roman"

'''
#################################################################
Gráfica de Señales para el caso 1
#################################################################
'''

data1 = pd.read_csv('/Users/jessielvelez/env/Laboratorio Intermedio/Circuitos de Corriente Alterna/DATALABCIRC/CASO1/COPE_01.CSV', skiprows=1)
data1 = data1.to_numpy()

tiempo = data1[:,0]
Vsuplido = data1[:,1]
Vcapacitor = data1[:,2]

fig1, ax1 = plt.subplots(nrows=3, dpi=150)

# fig1.set_tight_layout(True)

fig1.subplots_adjust(hspace= 0.1)
fig1.subplots_adjust(top=0.93)
fig1.subplots_adjust(bottom=0.15)

fig1.suptitle('Caso 1: Circuito RC', fontsize=15)
fig1.supylabel('$\Delta$V (V)', x = -0.02, fontsize=15)
fig1.supxlabel('t (s)', fontsize=15)

ax1[0].plot(tiempo, Vsuplido, label ='$\Delta$V Suplido')
ax1[0].plot(tiempo, Vcapacitor, label ='$\Delta$V Capacitor')
ax1[0].legend(loc='upper right', fancybox=False, framealpha=0.8)

ax1[0].set_ylabel('(a)', rotation = 0, fontsize=15, labelpad=8)
ax1[1].set_ylabel('(b)', rotation = 0, fontsize=15, labelpad=8)
ax1[2].set_ylabel('(c)', rotation = 0, fontsize=15, labelpad=8)

################ Gráfica para la diferencia entre las gráficas

DIF = Vsuplido-Vcapacitor

ax1[1].plot(tiempo, DIF)

################ Gráfica bajo voltaje senosoide

dataseno = pd.read_csv('/Users/jessielvelez/env/Laboratorio Intermedio/Circuitos de Corriente Alterna/DATALABCIRC/CASO1/SCOPE_13.CSV', skiprows=1)
dataseno = dataseno.to_numpy()

tseno = dataseno[:,0]
vsupseno = dataseno[:,1]
vcapseno = dataseno[:,2]

ax1[2].plot(tseno, vsupseno)
ax1[2].plot(tseno, vcapseno)


'''
#################################################################
Gráfica de Señales para el caso 2
#################################################################
'''

data2 = pd.read_csv('/Users/jessielvelez/env/Laboratorio Intermedio/Circuitos de Corriente Alterna/DATALABCIRC/CASO2/SCOPE_02.CSV', skiprows=1)
data2 = data2.to_numpy()

tiempo = data2[:,0]
Vsuplido = data2[:,1]
Vresistor = data2[:,2]

fig2, ax2 = plt.subplots(nrows=3, dpi=150)

fig2.subplots_adjust(hspace= 0.1)
fig2.subplots_adjust(top=0.93)
fig2.subplots_adjust(bottom=0.15)

ax2[0].plot(tiempo, Vsuplido, label ='$\Delta$V Suplido')
ax2[0].plot(tiempo, Vresistor, label ='$\Delta$V Resistor')
ax2[0].legend(loc='upper right', fancybox=False, framealpha=0.8)

fig2.suptitle('Caso 2: Circuito LC', fontsize=15)
fig2.supylabel('$\Delta$V (V)', x = -0.02, fontsize=15)
fig2.supxlabel('t (s)', fontsize=15)

ax2[0].set_ylabel('(a)', rotation = 0, fontsize=15, labelpad=8)
ax2[1].set_ylabel('(b)', rotation = 0, fontsize=15, labelpad=8)
ax2[2].set_ylabel('(c)', rotation = 0, fontsize=15, labelpad=8)

#Diferencia entre las gráficas

DIF2 = Vsuplido-Vresistor

ax2[1].plot(tiempo, DIF2)

#Forma senosoide

dataseno2 = pd.read_csv('/Users/jessielvelez/env/Laboratorio Intermedio/Circuitos de Corriente Alterna/DATALABCIRC/CASO2/SCOPE_23.CSV', skiprows=1)
dataseno2 = dataseno2.to_numpy()

tseno = dataseno2[:,0]
vsupseno = dataseno2[:,1]
vcapseno = dataseno2[:,2]

ax2[2].plot(tseno, vsupseno)
ax2[2].plot(tseno, vcapseno)

'''
Graficas PARTE 3
'''

datareso = pd.read_csv('/Users/jessielvelez/env/Laboratorio Intermedio/Circuitos de Corriente Alterna/DATALABCIRC/CASO3/SCOPE_03.CSV', skiprows=1)
datareso = datareso.to_numpy()

tiemporeso = datareso[:,0]
Vsuplidoreso = datareso[:,1]
Vresistorreso = datareso[:,2]

datanoreso = pd.read_csv('/Users/jessielvelez/env/Laboratorio Intermedio/Circuitos de Corriente Alterna/DATALABCIRC/CASO3/SCOPE_31.CSV', skiprows=1)
datanoreso = datanoreso.to_numpy()

tiemponoreso = datanoreso[:,0]
Vsuplidonoreso = datanoreso[:,1]
Vresistornoreso = datanoreso[:,2]

###############################################################################

fig3, ax3 = plt.subplots(nrows=2, dpi=150)

fig3.subplots_adjust(hspace= 0.2)
fig3.subplots_adjust(top=0.93)
fig3.subplots_adjust(bottom=0.15)

ax3[0].plot(tiemponoreso, Vsuplidonoreso, label ='$\Delta$V Suplido')
ax3[0].plot(tiemponoreso, Vresistornoreso, label ='$\Delta$V Resistor')
ax3[0].legend(loc='upper right', fancybox=False, framealpha=0.8)

fig3.suptitle('Caso 3: Circuito RLC', fontsize=15)
fig3.supylabel('$\Delta$V (V)', x = -0.02, fontsize=15)
fig3.supxlabel('t (s)', fontsize=15)

ax3[0].set_ylabel('(a)', rotation = 0, fontsize=15, labelpad=8)
ax3[1].set_ylabel('(b)', rotation = 0, fontsize=15, labelpad=8)

#RESONANCIA

ax3[1].plot(tiemporeso, Vsuplidoreso, label ='$\Delta$V Suplido')
ax3[1].plot(tiemporeso, Vresistorreso/1000, label ='$\Delta$V Resistor')