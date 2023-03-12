# -*- coding: utf-8 -*-
#%%
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
Lh=50
"================================================="
" Creación de señales "


nx =  np.arange(valini,lx)/fs
xcos = np.cos(2 * np.pi * f * nx)
"================================================="
suma = 0
for i in range(1,Na+1):
    xcos2 = np.cos(2 * np.pi * i * f * nx)
    suma += xcos2
    
xcos = xcos+suma
"================================================="

"Creamos un vector con ruido y se lo sumamos a la función"
xn = np.random.normal(media, sigma, lx)
plt.subplot(312)
markerline, stemlines, baseline = plt.stem(nx, xn, '-.') # Señal ruido

x = xcos + xn #La función + Ruido


plt.subplot(311)
markerline, stemlines, baseline = plt.stem(nx, xcos, '-.') #Señal original xcos(n)
plt.subplot(313)
markerline, stemlines, baseline = plt.stem(nx, x, '-.') #Señal con ruido x(n)
plt.show()

"============================================"
" Filtrado en tiempo "
h = np.ones(Lh)/Lh
y = np.convolve(x,h)
lh = len(h)
nh = np.arange(0,lh)/fs
ly = len(y)
ny = np.arange(0,ly)/fs

plt.subplot(313)
markerline, stemlines, baseline = plt.stem(nh, h, '-.') #Filtro de media h(n)
plt.show()


plt.subplot(313)
markerline, stemlines, baseline = plt.stem(ny, y, '-.') #Señal original reconstruida

# %%
