# -*- coding: utf-8 -*-
"""
Universidad de Puerto Rico
Recinto de Mayagüez 

Laboratorio Intermedio II - Interferometría

Instructor: Angel D. Reyes
Autor: Jessiel J. Vélez
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"

def perdif(a,b):
    return abs((a-b)/b)*100

#%% EXPERIMENTO 1 - Michelson Moreley

di = 5.250e-4
df = 1e-4*np.array([5.320,5.335,5.335,5.337,5.340,5.333,5.325,5.320,5.330,5.325])
N1 = np.array([22,27,27,27,26,25,25,22,26,25])

dm1 = df-di

wavelens1 = (2*(dm1))/N1 #ESTO VA EN EL INFORME
wavelen1 = np.average(wavelens1) #ESTO VA EN EL INFORME

#Análisis de Error

errordidf = 0.002e-4 #ESTO VA EN EL INFORME
errwavelens1 = (2/N1)*errordidf #ESTO VA EN EL INFORME
errwavelen1 = np.sqrt(np.sum(errwavelens1**2)) #ESTO VA EN EL INFORME

perdif1 = perdif(wavelen1,632.8e-9)
#%% EXPERIMENTO 1 - Fabry Perot

dffb = 1e-4*np.array([5.310,5.310,5.320,5.310,5.318,5.320,5.320,5.315,5.310,5.310])
N1fb = np.array([28,19,28,20,20,22,20,20,20,20])

dm1fb = dffb-di

wavelens1fb = (2*(dffb-di))/N1fb
wavelen1fb = np.average(wavelens1fb)

#Análisis de Error

errwavelen1fb = (2/N1fb)*errordidf
errwavelenfb = np.sqrt(np.sum(errwavelen1fb**2))

perdif1fb = perdif(wavelen1fb, 632.8e-9)
#%% EXPERIMENTO 2 

wavelen2=632.8e-9
d = 3e-2
P = 76-30
errP = 0.5

N2 = np.array([13,11,11,12,12,12,13,12,12,12])

pendientes = (N2*wavelen2)/(2*d*P) #ESTO VA EN EL INFORME
pendiente = np.average(pendientes) #ESTO VA EN EL INFORME

#Análsis de Error

errpendientes = pendientes*(errP/P) #ESTO VA EN EL INFORME
errpendiente = np.sqrt(np.sum(errpendientes**2)) #ESTO VA EN EL INFORME

#GRAFICANDO

pres = np.linspace(1,100,2)
ns = pres*pendiente + 1

presatm = 76
natm = presatm*pendiente +1 
errnatm = 76*errpendiente

perdif2 = perdif(natm,1.0002926)

fig, ax = plt.subplots()

ax.plot(pres,ns, color='black')
plt.fill_between(pres, ns-pres*errpendiente,  ns+pres*errpendiente, color='gray')
ax.hlines(natm,0,presatm, color='black', linestyle='dashed')
ax.vlines(presatm, 1, natm, color='black', linestyle='dashed')
ax.text(50,1.00022,'$n_{atm} = 1.000209$')

xticks = np.array([0,20,40,60,76,100])
yticks = np.array([0,0.00005,0.00010,0.00015,0.000209,0.00025])+1

ax.set_xticks(xticks)
ax.set_yticks(yticks)

ax.set_xlabel('P (cm Hg)', size=12)
ax.set_ylabel('n', size=12)
ax.set_title('Índice de Refracción vs Presión', size=12)
#%% EXPERIMENTO 3 
 
t = 0.6e-2
errt = 0.05e-2

ang = 10.0*(np.pi/180)
errang = 0.5*(np.pi/180)

N3 = np.array([103,101,101,99,100,103,102,103,101,101]) #ESTO VA EN EL INFORME

den = 2*t*(1-np.cos(ang)) - N3*wavelen2
num = N3*wavelen2*np.cos(ang)

ng = 1 + num/den #ESTO VA EN EL INFORME
NG = np.average(ng) #ESTO VA EN EL INFORME

#Análsis de Error

dert = (N3*wavelen2*np.cos(ang)*2*(1-np.cos(ang)))/den**2
derang = ((N3*wavelen2)/den)*((t*np.sin(2*ang))/2 - np.sin(ang))

term1 = (dert*errt)**2
term2 = (derang*errang)**2

errng = np.sqrt(term1+term2) #ESTO VA EN EL INFORME
errNG = np.sqrt(np.sum(errng**2)) #ESTO VA EN EL INFORME

perdif3 = perdif(NG, 1.5)