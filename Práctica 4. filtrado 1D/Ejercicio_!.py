# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import scipy

"================================================="
" Convolución de señales "
tipoconv = 2

"Función 1"
x = np.ones(10) #valor de cada punto en la gráfica (1)
Lx = len(x)
nx = np.arange(0,Lx) #0....9    ℎ(𝑘)

"Función 2"
h = np.ones(3) #valor de cada punto en la gráfica (1)
Lh = len(h)
nh = np.arange(0,Lh) #0...2 #    𝑥(𝑘)

if tipoconv == 1:
    y = scipy.convolve(x,h)
    
elif tipoconv == 2:
    y = []

    # Invertir la señal g
    x = x[::-1]

    # Utilizar dos bucles for anidados para recorrer todos los posibles valores de n y m
    for n in range(len(x) + len(h) - 1):
        s = 0
        for m in range(len(x)):
            # Calcular el producto de f[m] y g[n-m]
            if n - m < 0 or n - m >= len(h):
                # Si n-m está fuera de los límites de la señal g, 
                # se asume que el valor de g en ese punto es cero
                s += x[m] * 0
            else:
                s += x[m] * h[n - m]
        # Agregar el valor de s a la lista y
        y.append(s)

# Imprimir la señal resultante
print(y)
    
   #nx= -nx #ℎ(−𝑘)
   
   #n=43
   #nx= n -nx #ℎ(n−𝑘)



Ly = len(y)
ny = np.arange(0,Ly)


plt.subplot(311)
markerline, stemlines, baseline = plt.stem(nx, x, '-.')
plt.subplot(312)
markerline, stemlines, baseline = plt.stem(nh, h, '-.')
plt.subplot(313)
markerline, stemlines, baseline = plt.stem(ny, y, '-.')
plt.show()
