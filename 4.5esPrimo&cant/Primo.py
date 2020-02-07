'''
esPrimo

Recibe un numero entero por paramtro,
retorna True si es primo, False si no lo es
1,2,3,5,7,11,13,17,19

1233333333332

'''

def  damePrimo(num):
    res=False
    contador = 0
    for i in range(num):
        i = i + 1
        if num%i == 0:
            contador += 1
            
    if contador == 2:
        res = True
    
    print(res)



damePrimo(7)
damePrimo(12)