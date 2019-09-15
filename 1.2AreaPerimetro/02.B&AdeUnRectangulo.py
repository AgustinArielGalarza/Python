'''
Ingrese dos lados de un rectangulo y calcular perimetro y area del mismo

'''

def dameLado():
    print("Ingrese lado 1: ")
    lado1= int(input())
    print("Ingrese lado 2: ")
    lado2= int(input())
    print ("El perimetro del rectangulo es: ", calculaPerimetro(lado1, lado2))
    print ("El area de un rectangulo es: ", calculaArea(lado1, lado2))
    
    
def calculaPerimetro(l1, l2):
    p= l1 + l2
    p= p*2
    return p

def calculaArea(b, a):
    a= b * a
    return a

def main():
    dameLado()
    
    
main()