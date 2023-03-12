# -*- coding: utf-8 -*-
#%%
import matplotlib.pyplot as plt
import numpy as np
import scipy

"================================================="
" Convolución de señales "
tipoconv = 4

"Función 1"
x = np.ones(10) #valor de cada punto en la gráfica (1)
Lx = len(x)
nx = np.arange(0,Lx) #0....9    ℎ(𝑘)

"Función 2"
h = np.ones(3) #valor de cada punto en la gráfica (1)
Lh = len(h)
nh = np.arange(0,Lh) #0....2    𝑥(𝑘)

if tipoconv == 1:
    y = scipy.convolve(x,h)
    
elif tipoconv == 2:

    "Inizializamos el vector donde meterémos los puntos y los valores que toman en el intervalo"
    y = []

    "Invertir la señal h"
    h = list(reversed(h))

    "Utilizar dos bucles for anidados para recorrer todos los posibles valores de n y m"
    for n in range(0, len(x) + len(h) - 1):    # n coge los valores desde 0 hasta "len(x) + len(h) - 1" que es la longitud de y
        s = 0                                  #Inizializamos el sumatorio para ir sumando los diferentes valores de la convuloción en los diferentes puntos de y
        for m in range(0, len(x)):             # m coge los valores de 0 hasta len(x) que es la longitud de x
            # Calcular el producto de x[m] y h[n-m]
            if n - m < 0 or n - m >= len(h):

                # Si n-m está fuera de los límites de la señal h, 
                # se asume que el valor de h en ese punto es cero

                s += x[m] * 0

            else:

                #Sino simplemente multiplicamos las aplitudes de las señales y al final siempre añadimos el resultado a y

                s += x[m] * h[n - m]

        # Agregar el valor de s a la lista y al final de la convolución de cada punto, creando así la función y
        #Añadimos el punto tanto cuando es 0, como cuando el valor es distinto de 0
        print("con n= ",n,"y m=",m)
        print("La multiplicación de los valores que toman x e y         en n m es: ",s)
        y.append(s)

elif tipoconv == 3:
    
    # Calcular la longitud de las señales de entrada
    N = len(x)
    M = len(h)

    # Calcular la longitud de la señal resultante
    L = N + M - 1

    # Inicializar la señal resultante y con ceros
    y = [0] * L

    # Utilizar dos bucles for anidados para recorrer todos los posibles valores de n y m
    for n in range(L):
        for m in range(N):
            # Calcular el producto de x[m] y g[n-m]
            if n - m < 0 or n - m >= M:
                # Si n-m está fuera de los límites de la señal h, 
                # se asume que el valor de h en ese punto es cero
                y[n] += x[m] * 0
            else:
                y[n] += x[m] * h[n - m]

elif tipoconv == 4:
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
            # Calcular el producto de x[m] y h[n-m]
            if n - m < 0 or n - m >= Lh:
                # Si n-m está fuera de los límites de la señal h,
                # se asume que el valor de h en ese punto es cero
                y[n] += x[m] * 0
            else:
                y[n] += x[m] * h[n - m]
            

"Imprimir la señal resultante"
print(y)


Ly = len(y)             #Definimos la longitud de y una vez métidos los valores
ny = np.arange(0,Ly)    #Creamos un vector de 0 hasta la longitud de y


plt.subplot(311)
markerline, stemlines, baseline = plt.stem(nx, x, '-.')
plt.subplot(312)
markerline, stemlines, baseline = plt.stem(nh, h, '-.')
plt.subplot(313)
markerline, stemlines, baseline = plt.stem(ny, y, '-.')
plt.show()

# %%
