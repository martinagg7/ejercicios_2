from pilas import *
pila_solucion=Pila()
pila_numeros=Pila()
for numero in range(1, 10):
    pila_numeros.apilar(numero)


lista_indicaciones=[]
indicaciones=input("Introduzca I o D :")
while indicaciones!="" and len(lista_indicaciones)<=8:
    lista_indicaciones.append(indicaciones.upper())
    indicaciones=input("Introduzca I o D :")

print("Las indicaciones son "+str(lista_indicaciones))

#CASO 1 iiiii...

if (lista_indicaciones.count("I"))==len(lista_indicaciones):
    numeroI=lista_indicaciones.count("I")
    for i in range(9-numeroI-1):
        pila_numeros.desapilar()
    s=pila_numeros.lista_pila()
    s.reverse()
    print(s)

#CASO 2 dddd..
if (lista_indicaciones.count("D"))==len(lista_indicaciones):
    numeroD=lista_indicaciones.count("D")
    for i in range(9-numeroD-1):
        pila_numeros.desapilar()
    s=pila_numeros.lista_pila()
    print(s)

#CASO 3 MEZCLA