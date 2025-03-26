# -*- coding: utf-8 -*-
"""
Universidad de Puerto Rico
Recinto de Mayagüez 

Laboratorio Intermedio II - Ancho de Banda (Gráfica Teórica)

Instructor: Angel D. Reyes
Autor: Jessiel J. Vélez
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"

a=4
b=10
C=1.2

x1 = np.linspace(0,1.32,50)
y1 = a*np.e**(-a*x1) + C-0.0207

x2 = np.linspace(1.32,2.8,50)
y2 = np.ones(shape = np.shape(x2))*C

x3 = np.linspace(2.8,4.16364,50)
coef = (C-b)/10
y3 = coef*(x3+6*C)+b

X = np.concatenate((x1,x2,x3))
Y = np.concatenate((y1,y2,y3))

fig,ax = plt.subplots()

ax.plot(X,Y, color='black')

ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])

ax.set_ylabel('$\sigma$ (S/m)', size=15)
ax.set_xlabel('1000/T(K)', size=15)

ax.text(3.5,1.8,'I', size=20)
ax.text(1.8,2,'II', size=20)
ax.text(0.5,3.4,'III', size=20)

ax.set_title('Conductividad vs Temperatura', size=15)