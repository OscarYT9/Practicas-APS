# -*- coding: utf-8 -*-
#%%
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq, ifft

valini = 0 # Valor inicial
lx = 512  # Num muestras
fs = 22100  # Frecuencia de muestreo en Hz
frec = 1000   # Frecuencia fundamental
Na = 2 # Numero de armónicos
Lh = 10

n = np.arange(valini, lx) / fs

sumatorio = 0
xcos = np.cos(2 * np.pi * frec * n)
for i in range(1, Na + 1):
    xcos2 = np.cos(2 * np.pi * (i+1) * frec * n)
    sumatorio += xcos2

x = xcos + sumatorio

N = lx  # Numero de puntos
T = 1.0 / fs  # Separacion entre puntos
Xf = fft(x) 
frec = fftfreq(N, T) 


fcorte = 1000
HPB = (frec > -fcorte) & (frec < fcorte)

Yf = np.multiply(Xf, HPB)

y = ifft(Yf)
ly = len(y)
ny = np.arange(0,ly)/fs


Yf = plt.plot(frec[:N//2], 2.0/N * np.abs(Yf[0:N//2]))
plt.grid()
plt.show()

plt.subplot(313)
markerline, stemlines, baseline = plt.stem(ny, y, '-.')
plt.show()



# %%
