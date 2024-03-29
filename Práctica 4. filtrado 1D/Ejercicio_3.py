import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq

valini = 0 # Valor inicial
lx = 512  # Num muestras
fs = 22100  # Frecuencia de muestre oHz
f = 1000   # Frecuencia fundamental
Na = 2 # Numero de armonicos
Lh = 10

n =  np.arange(valini,lx)/fs

sumatorio = 0
xcos = np.cos(2 * np.pi * f * n)
for i in range(1,Na+1):
    xcos2 = np.cos(2 * np.pi * i * f * n)
    sumatorio += xcos2

x= xcos + sumatorio


N = lx  # Numero de puntos
T = 1.0 / fs  # Separacion entre puntos
Xf = fft(x)
frec = fftfreq(N, T) 

plt.plot(frec[:N//2], 2.0/N * np.abs(Xf[0:N//2]))
plt.grid()
plt.show()
