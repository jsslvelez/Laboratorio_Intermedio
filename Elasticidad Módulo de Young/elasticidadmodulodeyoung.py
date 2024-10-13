#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 15:57:01 2024

Análisis de Datos para el experimento: Elasticidad Módulo de Young

 """

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.integrate import trapezoid

import pandas as pd

#Algunas variables importantes

fontsize = 15

Dia = 0.0033
L = 0.035

#Comenzamos cargando la data quperimental que se obtuvo en el experimento

data = pd.read_csv('/Users/jessielvelez/env/Laboratorio Intermedio/Elasticidad Módulo de Young/masdatajic.txt', sep='\t')

P3 = data['Position (m) Run #3']
F3 = data['Force (N) Run #3']

STRSS3 = 10e-6 * ((F3+100)/(np.pi*((Dia/2)**2)))
STRAIN3 = P3/L

P6 = data['Position (m) Run #6']
F6 = data['Force (N) Run #6']

#Calculamos por errores
STRSS6 = 10e-6 * ((F6+100)/(np.pi*((Dia/2)**2)))
STRAIN6 = P6/L

# STRSS6 = data['Stress (MPa) Run #6']
# STRAIN6 = data['Strain Run #6']

#Encargarse de los NaNs

P6 = P6.fillna(0)
F6 = F6.fillna(0)

STRSS6 = STRSS6.fillna(0)
STRAIN6 = STRAIN6.fillna(0)

'''
PARTE LINEAL
'''

LF3 = data[['Position (m) Run #3','Force (N) Run #3']].to_numpy()
LS3 = data[['Strain Run #3','Stress (MPa) Run #3']].to_numpy()

LF6 = data[['Position (m) Run #6','Force (N) Run #6']].to_numpy()
LS6 = data[['Strain Run #6','Stress (MPa) Run #6']].to_numpy()

#Posición de la data que quiero

a = LS3[:,0]
b = LS6[:,0]

loc3 = np.where(a<0.01)
loc6 = np.where(b<0.004)

#Ahora voy a extraer la parte lineal de las gráficas


LinP3 = LF3[:,0][list(loc3)]
LinF3 = LF3[:,1][list(loc3)]


st3 = STRSS3.to_numpy()
str3 = STRAIN3.to_numpy()

LinSTRAIN3 = str3[list(loc3)]
LinSTRESS3 = st3[list(loc3)]

LinP6 = LF6[:,0][list(loc6)]
LinF6 = LF6[:,1][list(loc6)]

st6 = STRSS6.to_numpy()
str6 = STRAIN6.to_numpy()

LinSTRAIN6 = str6[list(loc6)]
LinSTRESS6 = st6[list(loc6)]


'''
FIT LINEAL
'''

def line(x,m,b):
    
    y = m*x + b
    
    return y

#Se calculan los fits, y por lo tanto las pendientes.

params3F, pcov3F = curve_fit(line, LinP3.flatten(), LinF3.flatten())
params3S, pcov3S = curve_fit(line, LinSTRAIN3.flatten(), LinSTRESS3.flatten())

params6F, pcov6F = curve_fit(line, LinP6.flatten(), LinF6.flatten())
params6S, pcov6S = curve_fit(line, LinSTRAIN6.flatten(), LinSTRESS6.flatten())

#Los errores correspondientes son:
    
err3f = np.sqrt(np.diag(pcov3F))
err3s = np.sqrt(np.diag(pcov3S))
err6f = np.sqrt(np.diag(pcov6F))
err6s = np.sqrt(np.diag(pcov6S))

#Área debajo de las curvas

A3f = trapezoid(F3, P3)
A3s = trapezoid(STRSS3, STRAIN3)
A6f = trapezoid(F6, P6)
A6s = trapezoid(STRSS6, STRAIN6)

A3fL = trapezoid(LinF3, LinP3)
A3sL = trapezoid(LinSTRESS3, LinSTRAIN3)
A6fL = trapezoid(LinF6, LinP6)
A6sL = trapezoid(LinSTRESS6, LinSTRAIN6)

#Valores Máximos

maxload3f = np.max(F3)
totext3f = np.max(P3)

maxload6f = np.max(F6)
totext6f = np.max(P6)

tensils3 = np.max(STRSS3)
tensils6 = np.max(STRSS6)

duct3 = np.max(STRAIN3)
duct6 = np.max(STRAIN6)

# #Información Relevante Sobre las Gráficas

# offsetYstress = 

'''
GRAFICAS
'''

'''
ALUMINIO
'''

#Gráfica de Fuerza vs. Desplazamiento ALUMINIO

figFA, axFA = plt.subplots(dpi=100, figsize=(10,5))

axFA.scatter(P6,F6,color='black', s=15)
axFA.set_xlabel('Posición (m)', fontsize= fontsize)
axFA.set_ylabel('Fuerza (N)', fontsize= fontsize)
axFA.set_title('Fuerza versus Posición: Aluminio', fontsize= fontsize)

axFA.tick_params(axis='both', which='both', labelsize=10)


#Gráfica de Stress vs. Strain ALUMINIO

figSA, axSA = plt.subplots(dpi=100, figsize=(10,5))

axSA.scatter(STRAIN6,STRSS6,color='black', s=15)
# axSA.plot(1.02*LinSTRAIN6.flatten(),line(LinSTRAIN6,params6S[0],params6S[1]).flatten(), color='blue')

axSA.set_xlabel('Tensión', fontsize= fontsize)
axSA.set_ylabel('Estrés (MPa)', fontsize= fontsize)
axSA.set_title('Estrés versus Posición: Aluminio', fontsize= fontsize)

axSA.tick_params(axis='both', which='both', labelsize=12)

# axSA.set_xlim([0, 0.01])


'''
POLIETILENO
'''

#Gráfica de Fuerza vs. Desplazamiento Polietileno

figFP, axFP = plt.subplots(dpi=100, figsize=(10,5))

axFP.scatter(P3,F3,color='black', s=15)

axFP.set_xlabel('Posición (m)', fontsize= fontsize)
axFP.set_ylabel('Fuerza (N)', fontsize= fontsize)
axFP.set_title('Fuerza versus Posición: Polietileno', fontsize= fontsize)

axFP.tick_params(axis='both', which='both', labelsize=10)

#Gráfica de Stress vs. Strain Polietileno

figSP, axSP = plt.subplots(dpi=100, figsize=(10,5))

axSP.scatter(STRAIN3,STRSS3,color='black', s=15)
# fitFLP = line(LinSTRAIN3,params3S[0],params3S[1])
# axSP.plot(1.02*LinSTRAIN3.flatten(),fitFLP.flatten(), color='blue')

axSP.set_xlabel('Tensión', fontsize= fontsize)
axSP.set_ylabel('Estrés (MPa)', fontsize= fontsize)
axSP.set_title('Estrés versus Tensión: Polietileno', fontsize= fontsize)

axSP.tick_params(axis='both', which='both', labelsize=12)

# axSP.set_xlim([-0.1, 0.05])

#Gráficas de la parte lineal

'''
POLIETILENO
'''

#Gráfica de Fuerza vs. Desplazamiento Polietileno

figFLP, axFLP = plt.subplots(dpi=100, figsize=(10,5))

#Linefit
fitFLP = line(LinP3,params3F[0],params3F[1])


axFLP.scatter(LinP3,LinF3,color='black', s=15)
axFLP.plot(LinP3.flatten(),fitFLP.flatten(), color='black')

axFLP.set_xlabel('Posición (m)', fontsize= fontsize)
axFLP.set_ylabel('Fuerza (N)', fontsize= fontsize)
axFLP.set_title('Fuerza versus Posición: Polietileno', fontsize= fontsize)

axFLP.tick_params(axis='both', which='both', labelsize=12)

axFLP.text(0.000060,5,f'Fuerza = {params3F[0]}*Posición + {params3F[1]}')

#Gráfica de Stress vs. Strain Polietileno

figSLP, axSLP = plt.subplots(dpi=100, figsize=(10,5))

axSLP.scatter(LinSTRAIN3,LinSTRESS3,color='black', s=15)
axSLP.plot(LinSTRAIN3.flatten(),line(LinSTRAIN3,params3S[0],params3S[1]).flatten(), color='black')

axSLP.set_xlabel('Tensión', fontsize= fontsize)
axSLP.set_ylabel('Estrés (MPa)', fontsize= fontsize)
axSLP.set_title('Estrés versus Tensión: Polietileno', fontsize= fontsize)

axSLP.tick_params(axis='both', which='both', labelsize=12)
axSLP.text(0.002,125,f'Estrés = {params3S[0]}*Tensión + {params3S[1]}')

'''
ALUMINIO
'''

#Gráfica de Fuerza vs. Desplazamiento ALUMINIO

figFLA, axFLA = plt.subplots(dpi=100, figsize=(10,5))

axFLA.scatter(LinP6,LinF6,color='black', s=15)
axFLA.plot(LinP6.flatten(),line(LinP6,params6F[0],params6F[1]).flatten(), color='black')

axFLA.set_xlabel('Posición (m)', fontsize= fontsize)
axFLA.set_ylabel('Fuerza (N)', fontsize= fontsize)
axFLA.set_title('Fuerza versus Posición: Aluminio', fontsize= fontsize)

axFLA.tick_params(axis='both', which='both', labelsize=12)
axFLA.text(0.00005,725,f'Fuerza = {params6F[0]}*Posición + {params6F[1]}')


#Gráfica de Stress vs. Strain ALUMINIO

figSLA, axSLA = plt.subplots(dpi=100, figsize=(10,5))

axSLA.scatter(LinSTRAIN6,LinSTRESS6,color='black', s=15)
axSLA.plot(LinSTRAIN6.flatten(),line(LinSTRAIN6,params6S[0],params6S[1]).flatten(), color='black')

axSLA.set_xlabel('Tensión', fontsize= fontsize)
axSLA.set_ylabel('Estrés (MPa)', fontsize= fontsize)
axSLA.set_title('Estrés versus Tensión: Aluminio', fontsize= fontsize)

axSLA.tick_params(axis='both', which='both', labelsize=12)
axSLA.text(0.0015,1000,f'Estrés = {params6F[0]}*Tensión + {params6F[1]}')





