#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 10:53:13 2024
CALCULOS DE ERROR PARA EXP 3
@author: jessielvelez
"""

import numpy as np

data = np.loadtxt('Data_Exp3.txt', skiprows=1)

R = np.array([
    0.938394,
    1.54029,
    1.9652,
    2.30764,
    2.59053,
    2.84342,
    3.07337,
    3.2832,
    3.47721,
    3.65854,
    3.82832,
    3.99309
])

#Para calcular el error en R

V = data[:,3]
I = data[:,1]

errV = 0.001
errI = 0.001

zeroterm1 = (1/I)*errV
zeroterm2 = V*((-I)**(-2))*errI

errR = np.sqrt(zeroterm1**2+zeroterm2**2)

#Método 1

R_ref = 0.5
T_ref = 294
alpha = 4.5e-3

errR_ref = 0.1
errT_ref = 1

Aterm1 = 1/(alpha*R_ref)*(errR)
Aterm2 = (R/alpha)*(R_ref**(-2))*errR_ref
Aterm3 = 1*errT_ref

errT1 = np.sqrt(Aterm1**2+Aterm2**2+Aterm3**2)

#Método 2

a = 290.90357393156745
b = 0.8358993314047718

erra = 0.788123
errb = 0.00103221

Bterm1 = (R**b)*erra
Bterm2 = a*b*(R**(b-1))*errR
Bterm3 = a*(R**b)*(np.log(R))*errb

errT2 = np.sqrt(Bterm1**2+Bterm2**2+Bterm3**2)

#Verificamos que el error de R sea consistente con el que tengo en la libreta

errporR = errR/R*100

# Error de T^4

T = np.array([
    492.376,
    745.069,
    913.352,
    1044.61,
    1150.62,
    1243.79,
    1327.32,
    1402.66,
    1471.62,
    1535.49,
    1594.84,
    1652.01
])

errT4 = 4*(T**3)*errT2





