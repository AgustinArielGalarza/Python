def dameNum ():
    num=int(input())
    return num

def calculaMayor (a,b,c):
    mayor= 0
    if a > b and c:
        mayor = a
    elif b > a and c:
        mayor = b
    elif c > a and b:
        mayor = c
    return mayor

def calculaMenor (a,b,c):
    menor = 0
    if a < b and c:
        menor = a
    elif b < a and b:
        menor = b
    elif c < a and b:
        menor = c
    return menor

def calculaMedio(a,b,c):
    medio = 0
    if a > b and a < c or a < b and a > c:
        medio = a
    elif b > a and b < c or b < a and b > c:
        medio = b
    elif c > a and c < b or c < a and c > b:
        medio = c
    return c

def calculaDistancia(menor, mayor, medio):
    valor = False
    distancia = medio - menor
    resultado = distancia + medio
    if resultado == mayor:
        valor = True
    else:
        valor = False
    return valor

def imprimir (a,b,c,valor):
    if valor :
        print(a,"-",b,"-",c,"- Estan igualmente distanciados!")
    else:
        print(a,"-",b,"-",c,"- No igualmente distanciados!")
    
def main():
    print("Ingrese primer numero: ")
    num1=dameNum()
    print("Ingrese segundo numero: ")
    num2=dameNum()
    print("Ingrese tercer numero: ")
    num3=dameNum()
    menor=calculaMenor(num1,num2,num3)
    medio=calculaMedio(num1,num2,num3)
    mayor=calculaMayor(num1,num2,num3)
    valor=calculaDistancia(menor,medio,mayor)
    imprimir(num1,num2,num3,valor)
    
main()