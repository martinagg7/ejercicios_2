per=[]
def permutaciones(per):
    max_glob=[]
    for lista in per:
        max_l=max(lista)
        max_glob.append(max_l)
    num_per=max(max_l)
    for lista in per:
        if num_per not in lista:
            cadena=lista
    permutacion=cadena.append(num_per)
    return permutacion
        


        