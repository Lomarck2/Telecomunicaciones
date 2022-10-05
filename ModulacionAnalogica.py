import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

#Modulacion por Doble Banda Lateral
#Declaracion de variables
f0 = 2  #hz
A0 = 10 #Watts
#Se crea un vector de tiempo de 0 a 1000, con 1000 elementos
t = np.linspace(0,1000,1000)

#La señal portadora
portadora = A0* np.cos(2*np.pi*f0*t)

#La señal a transmitir
f1 = 5
x1 = 2 * np.cos(2*np.pi*f1*t)

#Se grafica señal portadora y señal a transmitir

fig = plt.figure()
plt.plot(t,portadora)
plt.plot(t,x1)

#%% Modulacion
Modulada = x1 * portadora
#Se grafica la señal modulada
fig = plt.figure()
plt.plot(t,Modulada)
#%% Demodulacion

#Se calcula la transformada de fourier de la señal modulada
import scipy.fft as fft
transformada=fft.fft(Modulada)

#Para graficar se emplea un vector de frecuencias de -500 a 500 hz
xt=fft.fftfreq(1000,1)

#Se grafica la transformada de furier donde se identifica
#la señalportadora en f0 (y en -f0) y 
#la señal transmitida en f0+f1 (y en -(f0+f1) )
fig = plt.figure()
plt.plot(t,np.abs(transformada))
#%% Funcion que realiza filtro pas Altas, pasa Bajas y Pasa Bandas
def filtroFrecuencias(tipo,fc,signal,xt):
    tam = len(signal)
    resultado = np.zeros(tam,np.complex128)    
    for i in range(tam):
        if(tipo == 'PasaBajas'):
            if(xt[i] <= fc):
                resultado[i]=signal[i]
        if(tipo == 'PasaAltas'):
            if(xt[i] >= fc):
                resultado[i]=signal[i]
        if(tipo == 'PasaBandas'):
            if(xt[i] >= fc[0] and xt[i] <= fc[1]):
                resultado[i]=signal[i]
    return resultado
#%%
#Recuperacion de la señal trasmitida filtrandola de 
#la señal modulada
delta=f1-f0
fL = (2 * f0) - delta
fH = (2 * f0) + delta
filtrada=filtroFrecuencias('PasaBandas',[fL,fH],transformada,t)

#Se debe dividir entre 2, ya que el proceso de
#transformada inversa produce una multiplicación entre 2
inversa=fft.ifft(filtrada)/2 
#Se grafica la señal ya modulada
fig = plt.figure()
plt.plot(t,inversa)
