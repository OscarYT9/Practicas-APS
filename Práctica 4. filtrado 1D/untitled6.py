# -*- coding: utf-8 -*-
#%%
import matplotlib.pyplot as plt
import numpy as np


valini = 0 # Valor inicial
lx = 512  # Num muestras
fs = 22100  # Frecuencia de muestre oHz
f = 100   # Frecuencia fundamental

Na = 2 # Numero de armonicos
media = 0  # Media del ruido
sigma = 1 # Desviacion tipica
Lh = 10

xn = np.random.normal(media, sigma, lx)
n =  np.arange(valini,lx)/fs



sumatorio = 0
xcos = np.cos(2 * np.pi * f * n)
for i in range(1,Na+1):
    xcos2 = np.cos(2 * np.pi * i * f * n)
    sumatorio += xcos2

funcion= xcos + sumatorio
funcion = funcion + xn #DFT de la suma de un coseno más otro con armonicos

" Filtrado en tiempo "
h = np.ones(Lh)/Lh
y = np.convolve(funcion,h)
lh = len(h)
nh = np.arange(0,lh)/fs
ly = len(y)
ny = np.arange(0,ly)/fs
plt.subplot(313)
markerline, stemlines, baseline = plt.stem(ny, y, '-.')
plt.subplot(312)
markerline, stemlines, baseline = plt.stem(xn, funcion, '-.')
plt.show()

# %%
