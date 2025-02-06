# -*- coding: utf-8 -*-
"""
Razón Carga-Masa

Autor: Jessiel J. Vélez
"""

import numpy as np

#Constantes

a = 15e-2
N = 130
mu0 = 4e-7*np.pi

valorteocm = 1.75882e11

#Mediciones

V = 279.40 # Voltaje
I = 1.6040 # Corriente
r = 4.5e-2 # Radio

errV = 0.0005
errI = 0.01
errr = 0.02e-2

#Calculo de e/m

num = 2*((5/4)**3)*(a**2)
den = (N*mu0)**2

const = num/den

razoncm = const*(V/(I*r)**2)

pordif = ((razoncm-valorteocm)/valorteocm)*100

#Análsis de error

term1 = const*(1/((I*r)**2))*errV
term2 = const*(-2*V)/((r**2)*(I**3))*errI
term3 = const*(-2*V)/((I**2)*(r**3))*errr

errrazoncm = np.sqrt(term1**2+term2**2+term3**2)



