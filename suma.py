
def suma_max(lista): #[a, b, c, d]
    elementos=len(lista)
    maximo = SUMADETODOSLOSVALORESDE LAISTA
    for n in range(elementos, 0, -1):
        for m in range(len(lista)+1-n):
            suma = 0
            for o in range(n):
                suma+=lista[m+o]
            if suma>maximo:
                maximo= suma 
    return maximo

   4 [a, b, c, d]   = 5-4=1   => [0] +  [0,1,2,3] = [0,1,2,3]
   3  [a,b,c] [b,c,d] =5-3=2 INICIAR[0,1] + [0,1,2] = [0,1,2] ,[1,2,3]
   2 [a,b]  [b,c]  [c,d]  5-2=3 => [0,1,2] + [0,1] = [0,1] [1,2] [2,3] 
1 [a] [b]  [c]  [d] 5-1=4    => [0,1,2,3] +  [0] = [0] [1] [2] [3]

[a,b,c,d]   posicion relativa en la propia lista 1  
posicion de los elementos que quiero sumar con respecto al primer elemento que estoy sumando
b=1, [0,1,2]    b=1+0  c=1+1   d=1+2
for x in range(10): #0,1,23,,,,9    
    for y in range(5):
