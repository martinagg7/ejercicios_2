"""
Dada una cadena de longitud ≤ 8 que formada por caracteres ‘I’ y ‘D’, donde ‘I’
denota la secuencia creciente y ‘D’ denota la secuencia decreciente, descifra la
secuencia para construir el número mínimo sin cifras repetidas usando la estructura
de la pila.
cadena salida
IIDDIDID ——> 125437698
IDIDII ——> 1325467
DDDD ——> 54321
IIII ——> 12345

IIDDIDID ——> 125437698
             129837465
I=12 # el siguiente es superior sin repetir [3456789]
II=(12)I=123 #siguiente es superior sin repetir[356789]
IID=(124)D=1243 #le sumas 1 al anterior (123+1)-(mas pequeño libre)
IIDD=(1243)+D = 1243 - 12543
IIDDI = (12543)+I = 125436
IIDDID = (125436)+D = (125436+1=125437)+(6)=1254376
IIDDIDI = 1254376+I = 1254376+8 = 12543768
IIDDIDID = 12543768+D = 12543768+1=12543769 - 8  ()
"""

from pilas_colas.pilas import *

cadena1 = 'DIDDIDID'
cadena2 = 'IDIDII'
cadena3 = 'DDDD'
cadena4 = 'IIII'



def descrifrar(cadena):

    pila_solucion=Pila()
    pila_aux=Pila()
    pila_disponible=Pila()
    des = 0
    for i in  range (9,0,-1):
        pila_disponible.apilar(i)
    # IIDDDD      1276   543       7897

    pila_solucion.apilar(pila_disponible.desapilar())   
    for letra in cadena:
        
        if letra=="I":
            pila_solucion.apilar(pila_disponible.desapilar())
            des = 0     
        else: #CASO DE "D"
            des +=1 
            for i  in range(des):
                pila_aux.apilar(pila_solucion.desapilar())
            pila_solucion.apilar(pila_disponible.desapilar())
            for i in range(des):
                pila_solucion.apilar(pila_aux.desapilar())
    resultado = ""
    while not pila_solucion.pila_vacia():
        resultado = str(pila_solucion.desapilar())+resultado
    return resultado
                


cadena1 = 'DIDDIDID'
cadena2 = 'IDIDII'
cadena3 = 'DDDD'
cadena4 = 'IIII'
print(cadena1)
print(descrifrar(cadena1))
print(cadena2)
print(descrifrar(cadena2))
print(cadena3)
print(descrifrar(cadena3))



