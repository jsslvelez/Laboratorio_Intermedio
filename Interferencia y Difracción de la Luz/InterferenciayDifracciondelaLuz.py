# -*- coding: utf-8 -*-
"""
Universidad de Puerto Rico
Recinto de Mayagüez 

Laboratorio Intermedio II - Interferencia y Difracción de la Luz

Instructor: Angel D. Reyes
Autor: Jessiel J. Vélez
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Times New Roman'

#%% PARTE 1 - Difracción por un borde recto

#Observar y describir el patrón de interferencia formado por un borde recto.

#DEBE HABER UNA FOTO EN EL INFORME

#%% PARTE 2 - Difracción por una rendija

'''
Se realizaron unas medidas de intensidad en función del movimiento de un
RMS en Data-Studio.

Se deben hacer predicciones teóricas de lo que se observaría para este
experimento y se deberían comparar con los observado en el laboratorio.
'''

#GRAFICAS DE RESULTADOS

difsim1 = np.loadtxt("C:/Users/USER/Desktop/Data Interferencia/Run #5.txt", skiprows=2)
difsim2 = np.loadtxt("C:/Users/USER/Desktop/Data Interferencia/Run #6.txt", skiprows=2)
difsim3 = np.loadtxt("C:/Users/USER/Desktop/Data Interferencia/Run #11.txt", skiprows=2)
difsim4 = np.loadtxt("C:/Users/USER/Desktop/Data Interferencia/Run #12.txt", skiprows=2)

#CENTRALIZA LOS PICOS

max1 = np.max(difsim1[:,1])
max2 = np.max(difsim2[:,1])
max3 = np.max(difsim3[:,1])
max4 = np.max(difsim4[:,1])

xmax1s = difsim1[np.where(difsim1[:,1]==max1),0]
xmax2s = difsim2[np.where(difsim2[:,1]==max2),0]
xmax3s = difsim3[np.where(difsim3[:,1]==max3),0]
xmax4s = difsim4[np.where(difsim4[:,1]==max4),0]

xmax1 = np.floor(np.average(xmax1s))
xmax2 = np.floor(np.average(xmax2s))
xmax3 = np.floor(np.average(xmax3s))
xmax4 = np.floor(np.average(xmax4s))

#CONVERSION A GRADOS DEL SENSOR

def convertm(arr):
    return arr*(6.35e-3/2)*(np.pi/180)

def converttheta(arr):
    m = convertm(arr)
    L = 600e-3
    return m/L


degsim1 = converttheta(difsim1[:,0]-xmax1)
degsim2 = converttheta(difsim2[:,0]-xmax2)
degsim3 = converttheta(difsim3[:,0]-xmax3)
degsim4 = converttheta(difsim4[:,0]-xmax4)

plt.rcParams['scatter.marker'] = 'o'

fig, ax = plt.subplots(nrows=2,ncols=2)

ax[0,0].scatter(degsim1, difsim1[:,1], color='black')
ax[0,0].text(0.005,13,r'$b=0.16$ mm', size = 8)

ax[0,1].scatter(degsim2, difsim2[:,1], color='black')
ax[0,1].text(0.005,4,r'$b=0.08$ mm', size = 8)

ax[1,0].scatter(degsim3, difsim3[:,1], color='black')
ax[1,0].text(0.02,0.75,r'$b=0.04$ mm', size = 8)

ax[1,1].scatter(degsim4, difsim4[:,1], color='black')
ax[1,1].text(0.01,0.3,r'$b=0.02$ mm', size = 8)

fig.suptitle(r'Difracción por una rendija: I vs $\theta$')
fig.supxlabel(r'$\theta$ (rad)')
fig.supylabel(r'I (Unidades arbitrarias)')

#PREDICCIONES

theta = np.linspace(-0.15,0.15, num=1000)
lam = 650e-9
anchos = [0.16e-3,0.08e-3,0.04e-3,0.02e-3]

Ies = []
betas = []
for b in anchos:
    beta = ((np.pi*b)/lam)*np.sin(theta)
    I = (np.sin(beta)/beta)**2
    betas.append(beta)
    Ies.append(I)
    
    
figp, axp = plt.subplots(nrows=2,ncols=2, dpi=200)

axp[0,0].plot(theta, Ies[0], color='black')
axp[0,0].text(0.005,0.60,r'$b=0.16$ mm', size = 8)
axp[0,0].set_xlim(-0.03,0.03)

axp[0,1].plot(theta, Ies[1], color='black')
axp[0,1].text(0.005,0.60,r'$b=0.08$ mm', size = 8)
axp[0,1].set_xlim(-0.03,0.03)

axp[1,0].plot(theta, Ies[2], color='black')
axp[1,0].text(0.02,0.60,r'$b=0.04$ mm', size = 8)
axp[1,0].set_xlim(-0.09,0.09)

axp[1,1].plot(theta, Ies[3], color='black')
axp[1,1].text(0.02,0.60,r'$b=0.02$ mm', size = 8)
axp[1,1].set_xlim(-0.09,0.09)

figp.suptitle(r'Difracción por una rendija: Predicciones de I vs $\theta$')
figp.supxlabel(r'$\theta$ (rad)')
figp.supylabel(r'I (Unidades arbitrarias)')

#%% PARTE 3 - Interferencia por rendija doble

'''
#Se realizó una gráfica de intensidad vs RMS para una de las rendijas dobles
#en data studio. Se deben comparar los resultados experimentales con la
#predicción. Verifica si se cumple la predicción tal que 
#\Delta y = \frac{L\lambda}{a}.
'''

dsdata = np.loadtxt("C:/Users/USER/Desktop/Data Interferencia/Run #14.txt", skiprows=2)

maxds = np.max(dsdata[:,1])
xmaxdss = dsdata[np.where(dsdata[:,1]==maxds),0]
xmaxds = np.floor(np.average(xmaxdss))

dsm = convertm(dsdata[:,0]-xmaxds)

pltds, axds = plt.subplots()

axds.plot(dsm, dsdata[:,1], color='black')
axds.set_xlim(-0.004,0.004)

axds.set_xlabel(r'$\Delta y$ (m)')
axds.set_ylabel(r'I (Unidades Arbitrarias)')
axds.set_title(r'Difracción por rendija doble: I vs $\Delta y$')

#La separación entre los máximos debería ser de \delta y = L*\lambda /a

L = 600e-3
a= 0.25e-3

# Graficamos unas lineas bien lindas para ver donde quedan los maximo

xds = (L*lam)/a
for i in range(12):
    cnt = (i - 5)
    xloc = xds*cnt
    axds.vlines(x=xloc,ymin=0.0,ymax=2.9, color='black', linestyle='dashed')

#%% PARTE 4 - Interferencia por rendija múltiple

#Analiza de forma gráfica y corrobora que en el patrón de interferencia
#formado por rendijas multiples el número de máximos secundarios es de N-2.

mdata1 = np.loadtxt("C:/Users/USER/Desktop/Data Interferencia/Run #15.txt", skiprows=2)
mdata2 = np.loadtxt("C:/Users/USER/Desktop/Data Interferencia/Run #16.txt", skiprows=2)
mdata3 = np.loadtxt("C:/Users/USER/Desktop/Data Interferencia/Run #17.txt", skiprows=2)
mdata4 = np.loadtxt("C:/Users/USER/Desktop/Data Interferencia/Run #18.txt", skiprows=2)

mmax1 = np.max(mdata1[:,1])
mmax2 = np.max(mdata2[:,1])
mmax3 = np.max(mdata3[:,1])
mmax4 = np.max(mdata4[:,1])

mxmax1s = mdata1[np.where(mdata1[:,1]==mmax1),0]
mxmax2s = mdata2[np.where(mdata2[:,1]==mmax2),0]
mxmax3s = mdata3[np.where(mdata3[:,1]==mmax3),0]
mxmax4s = mdata4[np.where(mdata4[:,1]==mmax4),0]

mxmax1 = np.floor(np.average(mxmax1s))
mxmax2 = np.floor(np.average(mxmax2s))
mxmax3 = np.floor(np.average(mxmax3s))
mxmax4 = np.floor(np.average(mxmax4s))

mdatathet1 = converttheta(mdata1[:,0]-mxmax1)
mdatathet2 = converttheta(mdata2[:,0]-mxmax2)
mdatathet3 = converttheta(mdata3[:,0]-mxmax3)
mdatathet4 = converttheta(mdata4[:,0]-mxmax4)

figm, axm = plt.subplots(nrows=2,ncols=2, dpi=200)

axm[0,0].plot(mdatathet1, mdata1[:,1], color='black')
axm[0,0].text(0.002,4,r'$n=2$', size = 8)
axm[0,0].set_xlim(-0.005,0.005)

axm[0,1].plot(mdatathet2, mdata2[:,1], color='black')
axm[0,1].text(0.002,7,r'$n=3$', size = 8)
axm[0,1].set_xlim(-0.005,0.005)

axm[1,0].plot(mdatathet3, mdata3[:,1], color='black')
axm[1,0].text(0.002,15,r'$n=4$', size = 8)
axm[1,0].set_xlim(-0.005,0.005)

axm[1,1].plot(mdatathet4, mdata4[:,1], color='black')
axm[1,1].text(0.003,8,r'$n=5$', size = 8)
axm[1,1].set_xlim(-0.004,0.006)

figm.suptitle(r'Difracción por rendijas multiples: I vs $\theta$')
figm.supxlabel(r'$\theta$ (rad)')
figm.supylabel(r'I (Unidades arbitrarias)')


#%% PARTE 5 - Difracción por un pelo

'''
#Utiliza la explicación del principio de Babinet. Intenta
#usar la ecuación (que es la misma que la ecuación 1) para determinar
#el grosor del cabello.
'''

#%% PARTE 6 - Largo de onda medido con una regla

'''
#Esta es la parte donde se utiliza la regla metálica. Podemos encontrar
#el largo de onda utilizado con la ecuación (4) ó (6).
''' 
l = 218e-2
ym = (np.array([4.37,5.61,6.89,7.93,9.02,10.10,11.06,12.09,13.08,13.98,14.89])+20.4)*1e-2
d = 0.1e-2
lamsss = []
for i in range(0,10):
    lamda = ((d)/(2*L**2))*(ym[i+1]**2 - ym[i]**2)
    lamsss.append(lamda)

lambdaprom = np.average(np.array(lamsss))




#%% PARTE  7 - Difracción por apertura circular

'''
#Verifica si el primer mínimo de intensidad para esta parte cumple con la
#predicción que indica que: d\sin{\teta_1} \approx 1.22 \lambda.
'''

#%% PARTE 8 - Difracción por otras aperturas

#Solamente observación.

#%% PARTE 9 - Interferencia por película delgada

#En esta parte su usaron los dos pedazos de vidrio. También es solo observación.

#%% PARTE 10 - Espejo de Lloyd

#Tampoco hay que calcular. Solo observación.
