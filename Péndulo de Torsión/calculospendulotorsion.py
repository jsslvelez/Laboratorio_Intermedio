#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 11:21:01 2024

LABORATORIO PÉNDULO DE TORSIÓN

Cálculos para cantidades importantes y errorer posibles.

@author: Jessiel J. Vélez
"""

import numpy as np

'''Parte A'''

    #Cantidades Medidas
    
m = np.array([
    0.324,
    1.53,
    4.63])

errm = np.array([
    3.0e-4,
    8.8e-4,
    0.0058])

l = 0.0250
errl = 0.0005

    #Cálculos de Constante de Torsión
    
k = m*l

errk = ((errm/m)+(errl/l))*100

'''Parte B'''

    #Cantidades Medidas
    
TB = np.array([
    0.8626,
    0.4417,
    0.2450])

errTB = 0.01

m_dis = 0.1207
errm_dis = 0.00005

r_dis = 0.0480
errr_dis = 0.0005

    #Cálculos de Momento de Inercia

IB1 = ((TB/(2*np.pi))**2)*k
errIB1 = (2*(errTB/TB)+(errk/100))*100

IB2 = (1/2)*m_dis*((r_dis)**2)
errIB2 = (2*(errr_dis/r_dis)+(errm_dis/m_dis))*100

'''Parte C'''

    #Cantidades Medidas

m_cil = 0.46590
errm_cil = 0.00005

r1_cil = 0.0270
errr1_cil = 0.0005

r2_cil = 0.0380
errr2_cil = 0.0005

TC = np.array([
    1.825,
    0.955,
    0.5034])
    
errTC = 0.01

    #Cálculos de Momento de Inercia
    
IC1 = ((TC/(2*np.pi))**2)*k
errIC1 = (2*(errTC/TC)+(errk/100))*100

IC2 = IB2 + (1/2)*m_cil*(r1_cil**2+r2_cil**2)

    #Error de IC2

errcuant1 = (errIB2/100)*IB2

errfracm = (errm_cil/m_cil)

term2 = (1/2)*m_cil*(r1_cil**2+r2_cil**2)

fact = (r1_cil**2+r2_cil**2)

errcuantr1 = 2*(errr1_cil/r1_cil)*(r1_cil**2)
errcuantr2 = 2*(errr2_cil/r2_cil)*(r2_cil**2)

errcuantfact = (errcuantr1+errcuantr2)
errfracfact = errcuantfact/fact

errcuant2 = (errfracm+errfracfact)*term2

errcuantIC2 = errcuant1 + errcuant2
errporIC2 = (errcuantIC2/IC2) * 100

'''
Porcentajes de Diferencia
'''

    #Parte B
    
PercentDifB = ((np.abs(IB1-IB2))/((IB1+IB2)/2)) * 100
    
    #Parte C
    
PercentDifC = ((np.abs(IC1-IC2))/((IC1+IC2)/2)) * 100