'''
ingresar dos numero por teclados, producir un numero aleatorio usando de limites
los numeros anteriores y lugo replazar los limites por los numeros aleatorios
generados producidos
'''
import random

def dameNum():
    print("ingrese el limite inferior (numero natural): ")
    inf=int(input())
    print("ingrese el limite superior (numero natural):")
    sup=int(input())
    dameRandom(inf,sup)
    
def dameRandom(a,b):
    aleatorio1=random.randint(a,b)
    imprimir(a,b,aleatorio1)
    aleatorio2=random.randint(aleatorio1,b)
    imprimir(aleatorio1,b,aleatorio2)
    aleatorio3=random.randint(aleatorio1,aleatorio2)
    imprimir(aleatorio1,aleatorio2,aleatorio3)

def imprimir (inf,sup,ran):
    print("Limite inferior ",str(inf),",limite superior ",str(sup),". Numero generado: ",str(ran))
    
def main():
    dameNum()
    
main()