
def analizar_max(lista1,lista2):
    max_1=max(lista1)
    max_2=max(lista2)

    if max_1==max_2:   # a==b   a>b   b>a    
        return True
    elif max_1>max_2:
        rep1=lista1.count(max_1)
        if rep1>1:
            return True
        else:
            return False
    else:
        rep2=lista2.count(max_2)
        if rep2>1:
            return True 
        else:
            return False
        

lista1=[99, 10 ,16 ,15 ]
lista_2=[10 ,16 ,15 ,15]
if analizar_max(lista1,lista_2):
    print("yes")
else:
    print("No")


   4 [a, b, c, d]   = 5-4=1   => [0]   [0,1,2,3]
   3  [a,b,c] [b,c,d]   5-3=2  => [0,1]   [0,1,2]
   2 [a,b]  [b,c]  [c,d]  5-2=3 => [0,1,2]  [0,1]
   1 [a] [b]  [c]  [d] 5-1=4    => [0,1,2,3]   [0]


suma.py   s1=-1 +3 -2 +5 +3 -5 +2 +2
   s2= -1 +3 -2 +5 +3 -5 +2
   s2 +3 -2 +5 +3 -5 +2 +2
    -1 +3 -2 +5 +3 -5
    +3 -2 +5 +3 -5 +2
    -2 +5 +3 -5 +2 +2
    -1 +3 -2 +5 +3