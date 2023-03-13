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
Xf = fft(x) # Calcular la transformada rápida de Fourier (FFT) de la señal
frec = fftfreq(N, T) 

# Generar el filtro paso alto ideal
fcorte = 3 * 1000 #Número de armonicos * frec fundamental (cada armónico tiene 1000Hz) = 1000 Hz # Frecuencia de corte del último armónico
HPB = (frec > -fcorte) & (frec < fcorte) # Filtro de paso bajo
HPA = 1 - HPB # Complemento de frecuencia

# Aplicar el filtro a la señal en el dominio de la frecuencia
Yf = np.multiply(Xf, HPA)

# Calcular la transformada inversa rápida de Fourier (IFFT) para obtener la señal filtrada en el dominio del tiempo
y = ifft(Yf)
ly = len(y)
ny = np.arange(0,ly)/fs

# Representar el espectro de magnitud de la señal filtrada
Yf = plt.plot(frec[:N//2], 2.0/N * np.abs(Yf[0:N//2]))
plt.grid()
plt.show()

# Representar la señal filtrada en el dominio del tiempo
plt.subplot(313)
markerline, stemlines, baseline = plt.stem(ny, y, '-.')
plt.show()
# %%
