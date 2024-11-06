#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 15:36:32 2024

Código para los cálculos asociados al informe:
    
CIRCUITOS DE CORRIENTE ALTERNA

@author: Jessiel J. Vélez
"""

import numpy as np

def pordif(a,b): # Función de porcentaje de diferencia
    
    posum = np.abs(a-b)
    mean = (a+b)/2
    y = (posum/mean) * 100
    
    return y
    
'''
DATOS DE LA PARTE B1
'''

R1 = 9.89e3 # Resistor de la parte 1
C1 = 0.098e-6 # Capacitor de la parte 1
T1half = 660e-6 # Tiempo en llegar a la mitad del valor máximo de voltaje

tau1T = R1*C1 # Tiempo característico teórico para la parte 1

fMax1 = 1/(10*tau1T) # Frecuencia de oscilación para la parte 1

tau1E = T1half/np.log(2) # Tiempo caracterísitco experimental para l parte 1

diftau1 = pordif(tau1T, tau1E) # Porcentaje de diferencia

#ANÁLISIS DE ERROR ############################################################
###############################################################################

errR1 = 0.005e3
errC1 = 0.0005e-6
errT1half = T1half*(0.01/100)

termtauerr1 = (errR1*C1)**2 + (errC1*R1)**2
errtau1T = np.sqrt(termtauerr1) # La ecucación viene de R1*C1

errfMax1 = errtau1T/(10*(tau1T**2)) # La ecuación es 1/(10*tau1T)

errtau1E = errT1half/np.log(2) # La ecuación es T1half/np.log(2) 

###############################################################################
###############################################################################

'''
DATOS DE LA PARTE B2
'''

L2 = 25.3e-3 # Inductor de la parte 2
R2 = 0.987e3 # Resistor de la parte 2
T2half = 17.20e-6 # Tiempo en llegar a la mitad del valor máximo de voltaje

tau2T = L2/R2 # Tiempo característico teórico para la parte 2

fMax2 = 1/(10*tau2T) # Frecuencia de oscilación para la parte 2

tau2E = T2half/np.log(2) # Tiempo caracterísitco experimental para l parte 2

diftau2 = pordif(tau2T,tau2E) # Porcentaje de diferencia

#ANÁLISIS DE ERROR ############################################################
###############################################################################

errL2 = 0.05e-3 
errR2 = 0.0005e3 
errT2half = T2half*(0.01/100)

termtauerr2 = ((1/R2)*errL2)**2 + ((L2/(R2**2))*errR2)**2
errtau2T = np.sqrt(termtauerr2) # La ecucación viene de L2/R2

errfMax2 = errtau2T/(10*(tau2T**2)) # La ecuación es 1/(10*tau2T)

errtau2E = errT2half/np.log(2) # La ecuación es T1half/np.log(2)

###############################################################################
###############################################################################

'''
DATOS DE LA PARTE B3
'''

#Valores que se miden con un multímetro.

RL3 = 17.0
RR3 = 108.3
R3 = RR3 + RL3 # Resistor de la parte 3
L3 = 5.86e-3 # Inductor de la parte 3
C3 = 107.1e-6 # Capacitor de la parte 3

RFT = (1/(2*np.pi))*np.sqrt(1/(L3*C3)) # Frecuencia de resonancia estimada (Ecuación 13b)
RWT = np.sqrt(1/(L3*C3))

RFE = 217.7 # Frecuencia de resonancia experimental. Esta se obtiene de la gráfica de voltaje en función
# de frecuencia en el osciloscopio. Se utiliza un fit lineal para obtener este resultado.

I3 = 8.46e-3 # Luego de apagar el generador de señales se conecta un amperímetro al circuito.
# Luego, se encienda nuevamente el generador y se baja la frecuencia a un valor inferior al anterior.
# Verifica que sea una frecuencia que permita mediciones correctas.

# Los voltajes entre los elementos del circuito se determinan utilizando
# un voltímetro. Estos son valores RMS (tanto corriente como voltaje).

VRE = 0.932 # Voltaje experimental entre el resistor 
VLE = 0.109 # Voltaje experimental entre el inductor
VCE = 83.0e-3 # Voltaje experimental entre el capacitor
VTE = 1.06 # Voltaje experimental suplido al circuito
 
FT_E = 150
WT_E = FT_E*(2*np.pi)

# Las siguientes cuatro cantidades son calculadas con las ecuaciones 12a y 12b del manual
# escrito por el profesor Félix E. Fernández.

XC = 1/(WT_E*C3) # Reactancia capacitiva: otra forma de calcular esta cantidad
# es utilizando la forma de Ohm. VTE/I = -i X_C
XL = WT_E * L3 # Reactancia inductiva: la frecuencia angular multiplicada por la inductancia.
# Otra forma de calcular esta cantidad es igual que la reactancia capacitiva: VTE/I = i X_L

termz = R3**2 + (XL-XC)**2
Z = np.sqrt(termz) # La impedancia es la divición del voltaje aplicado con la corriente total.

termf = (XL-XC)/R3
Phase = np.arctan(termf)

# Diferencia de potencial teórica entre los elementos del circuito.
# Estos se calculan a partir de las reactancias, resistencia, impendancia,
# y el valor medido de la corriente.

VRT = RR3*I3 # Voltaje calculado entre el resistor 
VLT_RES = RL3*I3
VLT_IND = XL*I3 # Voltaje calculado entre el inductor por su inductancia
VLT = VLT_RES+VLT_IND
VCT = XC*I3 # Voltaje calculado entre el capacitor
VTT = Z*I3 # Voltaje calculado suplido al circuito

#Porcentaje de diferencia entre los valores de voltaje entre los elementos.

difVR = pordif(VRE, VRT)
difVL = pordif(VLE, VLT)
difVC = pordif(VCE, VCT)
difVT = pordif(VTE, VTT)

# El factor de potencia y la potencia disipada por el circuito son cantidades calculadas.

PF = np.cos(Phase) # El factor de potencia es sencillamente el coseno del ángulo.
POWC = I3*VTE*PF # Se determina la potencia disipada por el circuito. Puedo usar el voltaje experimental o el voltaje experim

# Si lo deseamos, podemos determinar el factor de mérito.

Q = (1/R3) * np.sqrt((L3/C3)) # Mientras más alto este valor, más estrecho será el pico de resonancia,
# por lo que, se dice que el circuito es más selectivo.

# ANÁLSIS DE ERROR PARA LA ÚLTIMA PARTE #######################################
###############################################################################

errRR3 = 0.05
errRL3 = 0.05
errR3 = errRR3 + errRL3 # Resistor de la parte 3
errL3 = 0.005e-3 # Inductor de la parte 3
errC3 = 0.05e-6 # Capacitor de la parte 3

errRFT = (RFT/2) * np.sqrt( (errL3/L3)**2 + (errC3/C3)**2 )
errRWT = (RWT/2) * np.sqrt( (errL3/L3)**2 + (errC3/C3)**2 )

errRFE = 0.003 # Esto se obtiene del osciloscopio. No es una incertidumbre calculada.

errI3 = 0.01e-3 #Esto se obtiene de la medida del amperímetro

errVRE = 0.0005 # Error del voltaje experimental entre el resistor 
errVLE = 0.001 # Error del voltaje experimental entre el inductor
errVCE = 0.1e-3 # Error del voltaje experimental entre el capacitor
errVTE = 0.01 # Error del voltaje experimental suplido al circuito

errFT_E = 1
errWT_E = (2*np.pi)*errFT_E

errXC = XC * np.sqrt( (errWT_E/WT_E)**2 + (errC3/C3)**2 ) # La ecuación es 1/(RFT*C3)
errXL = XL * np.sqrt( (errWT_E/WT_E)**2 + (errL3/L3)**2 ) # La ecuación es RFT * L3

subX = XL-XC
errZterm = (R3*errR3)**2 + (subX*errXL)**2 + (subX*errXC)**2
errZ = (1/Z) * np.sqrt(errZterm)

term = (subX/R3)
Der = (1/(1+(term**2)))*(1/R3)
errPhase = Der * np.sqrt( (errXL)**2 + (errXC)**2 + (term*errR3)**2 ) # Error de la fase

errVLT_RES = VLT_RES * np.sqrt( (errRL3/RL3)**2 + (errI3/I3)**2 )

errVLT = (VLT * np.sqrt( (errXL/XL)**2 + (errI3/I3)**2 )) + errVLT_RES # XL*I3 Error del voltaje teórico entre el resistor 
errVRT = VRT * np.sqrt( (errRR3/RR3)**2 + (errI3/I3)**2 ) # R3*I3 Error del voltaje teórico entre el inductor
errVCT = VCT * np.sqrt( (errXC/XC)**2 + (errI3/I3)**2 ) # XC*I3 Error del voltaje teórico entre el capacitor
errVTT = VTT * np.sqrt( (errZ/Z)**2 + (errI3/I3)**2 ) # Z*I3 Error del voltaje teórico suplido al circuito

errPF = np.abs(np.sin(Phase)*errPhase)
errPOWC = POWC * np.sqrt( (errI3/I3)**2 + (errVTE/VTE)**2 + (errPF/PF)**2 ) #Verficamos si usar el valor que calculamos de forma experimental o el teórico.

errQ = Q * np.sqrt( (errR3/R3)**2 + (errL3/(L3*2))**2 + (errC3/(C3*2))**2 )

###############################################################################
###############################################################################