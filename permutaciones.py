per=[]
n=int(input("Introduce el número de la permutacion :"))

def permutaciones(n,per):
    for lista in per:
        if n not in lista:
            lista_importar=lista
    permutacion=lista_importar.append(n)
