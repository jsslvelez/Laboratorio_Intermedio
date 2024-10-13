#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:45:03 2024

ERROR PROPAGATION

La idea de este código es dejar colocado funciones para calcular el error absoluto o relativo
de cantidades obtenidas en el laboratorio intermedio. De esta forma, podemos acelerar los cálculos
en el futuro y ahorrarnos mucho tiempo.

@author: jessielvelez
"""

# ERROR RELATIVO

"""
Como esta es una expresión porcentual del valor original, una de las entradas de la función debe ser el 
valor de la medida. Adicional, debe tomar el error absoluto de la medida y de alguna forma especificar 
la operación que se desea realizar.
"""

import numpy as np

def errrel(valores, error):
    
    medida = np.array(valores)
    error = np.array(errorasociado)
    
    errporcentual = error/medida
    
    err = errporcentual*100*2
    
    return err

valoresmedidos = [2.5,
                  3.0,
                  3.5,
                  4.0,
                  4.5,
                  5.0,
                  6.0,
                  7.0,
                  8.0,
                  9.0,
                  10.0,
                  12.0,
                  14.0,
                  16.0,
                  18.0,
                  20.0,
                  25.0,
                  30.0,
                  35.0,
                  40.0,
                  45.0,
                  50.0,
                  60.0,
                  70.0,
                  80.0,
                  90.0,
                  100.0]

number = 0.1
elements = len(valoresmedidos)

errorasociado = [number]*elements

resultado = errrel(valoresmedidos,errorasociado)


