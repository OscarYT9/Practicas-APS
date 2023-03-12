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
    xcos2 = np.cos(2 * np.pi * i * frec * n)
    sumatorio += xcos2

x = xcos + sumatorio

N = len(x)  # Numero de puntos
# Definir la frecuencia de corte

fcorte = 2 * frec

# Calcular la transformada rápida de Fourier (FFT) de la señal
Xf = fft(x)

# Generar el filtro paso bajo ideal
f = fftfreq(N, 1/fs)
HPB = (f > -fcorte) & (f < fcorte)

# Aplicar el filtro a la señal en el dominio de la frecuencia
Yf = np.multiply(Xf, HPB)

# Calcular la transformada inversa rápida de Fourier (IFFT) para obtener la señal filtrada en el dominio del tiempo
y = ifft(Yf)
ly = len(y)
ny = np.arange(0,ly)/fs
freqs = fftfreq(N, 1/fs)

# Representar el espectro de magnitud de la señal filtrada
plt.plot(freqs[:N//2], 2.0/N * np.abs(Yf[0:N//2]))
plt.grid()
plt.show()

# Representar la señal filtrada en el dominio del tiempo
markerline, stemlines, baseline = plt.stem(ny, y, '-.')
plt.show()

# %%
