#Definicion de funciones
def pesoBin(Binario):
    contador = 0
    for j in range(8):
        if Binario[j] == '1':
            contador += 1
    return contador
def diferencia(Binario1,Binario2):
    dif = Binario1^Binario2 #^ XOR
    return dif
#Programa
cadena='select * from alumno'
tam=len(cadena)

listaBin=[]

for i in range(tam):
    ascii_=ord(cadena[i])
    binario=format(ascii_,'08b')
    listaBin.append([ascii_,binario,pesoBin(binario),cadena[i]]) 

cabecera = 255
listaDif = []
for k in range(tam):
    d=diferencia(cabecera,listaBin[k][0])
    listaDif.append(d)
#%% Generacion de errores
listaErrores = [8,13,3,2]
from random import randrange
# val=0
# for i in range(4):
#     val=randrange(0,tam)
#     listaErrores.append(val)
#%%Introducir error
def reemplazar(carac,cad,indice):
    listaCad=list(cad)
    listaCad[indice]=carac
    s="".join(listaCad)
    return s
mensaje=[]
for k in range(tam):
    mensaje.append(listaBin[k])
    
for i in range(4):    
    indiceBin=listaErrores[i]
    binario = mensaje[indiceBin][1]
    nBits = randrange(1,3)
    for j in range(nBits):
        indexB = randrange(0,7)
        if binario[indexB] == '1':
            binario=reemplazar('0',binario,indexB)
        else:
            binario=reemplazar('1',binario,indexB)
    mensaje[indiceBin][0]=int(binario,2)
    mensaje[indiceBin][1]=binario
    mensaje[indiceBin][3]=chr(int(binario,2))
#%%

for k in range(tam):
    d=diferencia(cabecera,mensaje[k][0])
    if(listaDif[k] != d):
        print('Error en Byte: ' + str(k) + ', peso actual: ' + str(d) 
              +' Peso anterior: ' + str(listaDif[k]) )






