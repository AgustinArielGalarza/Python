def dameNum():
    num = int(input())
    return num
    
def producto(a,b):
  
    
    productoTercerDigito= b * tercerDigito(a)
    productoSegundoDigito = b * segundoDigito(a)
    supp = productoSegundoDigito * 10
    productoPrimerDigito = b * primerDigito(a)
    supp2 = productoPrimerDigito * 100
    
    suma= productoTercerDigito + supp + supp2
    
    print('{:>12}'.format(a))
    print('{}{:>11d}'.format("x",b))
    print("-------------")
    print ('{:> 12}'.format(productoTercerDigito))
    print ('{} {:>9d}{}'.format("+", productoSegundoDigito, "-"))
    print ('{:> 10d}{}{}'.format(productoPrimerDigito,"-","-"))
    print("-------------")
    print('{:>12}'.format(suma))
    
def tercerDigito(x):
    res = x % 10
    return res

def segundoDigito(x):
    res = int((x % 100)/10)
    return res

def primerDigito(x):
    res = int((x % 1000)/100)
    return res

def main():
    print("Ingrese un numero de 3 sifras: ")
    num1=dameNum()
    print("Ingrese nuevamente un numero de 3 sifras: ")
    num2=dameNum()
    producto(num1, num2)
    
main()