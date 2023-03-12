# -*- coding: utf-8 -*-
#%%
import matplotlib.pyplot as plt
import numpy as np
import scipy

"================================================="
" Convolución de señales "
tipoconv = 2

"Función 1"
x = np.ones(10)  # valor de cada punto en la gráfica (1)
Lx = len(x)
nx = np.arange(0, Lx)  # 0....9    ℎ(𝑘)

"Función 2"
h = np.ones(3)  # valor de cada punto en la gráfica (1)
Lh = len(h)
nh = np.arange(0, Lh)  # 0...2 #    𝑥(𝑘)

if tipoconv == 1:
    y = scipy.convolve(x, h)

elif tipoconv == 2:
    y = []

    # Invertir la señal h
    h_inv = list(reversed(h))

    # Extender la señal x con ceros
    Lxe = Lx + Lh
    xe = [0] * Lxe
    xe[Lh-1:Lh-1+Lx] = x

    # Inicializar la señal resultante y con ceros
    Ly = Lx+Lh-1
    y = np.zeros(Ly)

    # Utilizar dos bucles for anidados para recorrer todos los posibles valores de n y m
    for n in range(Ly):
        for m in range(Lx):
            # Calcular el producto de f[m] y g[n-m]
            if n - m < 0 or n - m >= Lh:
                # Si n-m está fuera de los límites de la señal g,
                # se asume que el valor de g en ese punto es cero
                y[n] += x[m] * 0
            else:
                y[n] += x[m] * h[n - m]
            
# Imprimir la señal resultante
print(y)


Ly = len(y)
ny = np.arange(0, Ly)


plt.subplot(311)
markerline, stemlines, baseline = plt.stem(nx, x, '-.')
plt.subplot(312)
markerline, stemlines, baseline = plt.stem(nh, h, '-.')
plt.subplot(313)
markerline, stemlines, baseline = plt.stem(ny, y, '-.')
plt.show()

# %%
