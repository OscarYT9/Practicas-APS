# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import scipy

"================================================="
" Senal coseno"
valini = 0 # Valor inicial
lx = 512  # Num muestras
fs = 22100  # Frecuencia de muestre oHz
f = 100   # Frecuencia fundamental
Na = 2 # Numero de armonicos
media = 0  # Media del ruido
sigma = 0.2 # Desviacion tipica
duracion =  44100 #en muestras
n =  np.arange(valini,duracion)/fs
"================================================="
" Creación de coseno "
f = 200 
Na = 20
suma = 0
xcos = np.cos(2 * np.pi * f * n)
"================================================="

for i in range(1,Na+1):
    xcos2 = np.cos(2 * np.pi * i * f * n)
    suma += xcos2
    
xcos = xcos+suma

markerline, stemlines, baseline = plt.stem(n[1:100], xcos[1:100])
plt.show()