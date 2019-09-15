'''
Ingrese 2 numero y mostrar por consola la resta, suma, multiplicacion y divicion de ambos numero
'''

def dameNume():
    print ("Ingrese primer numero: ")
    num1= int(input())
    print ("Ingrese segundo numero: ")
    num2= int(input())
    calculatodo(num1, num2)
    
def calculatodo(a , b):
    print("suma: ", suma(a, b))
    print("resta: ",resta(a, b))
    print("multiplicaciòn: ",multiplicacion(a, b))
    print("diviciòn: ",divicion(a, b))
def suma(a, b):
    r = a + b
    return r
def resta(a, b):
    r = a - b
    return r
def multiplicacion(a, b):
    r = a * b
    return r
def divicion (a, b):
    r= int(a / b)
    return r
def main():
    dameNume()
    
main()