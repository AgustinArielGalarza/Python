def dameNum():
    num=int(input())
    return num

def secuencia(a,b,c,d):
    if d == 0:
        while a < b:
            if a %2 == 0:
                print(str(a))
                a = int(a)
                a += c
    elif d == 1:
            if a %2 != 0:
                print(str(a))
                a= int(a)
                a += c
    elif d == 2:
        while a < b:
            print(str(a))
            a = int(a)
            a += c
            
def validar (x):
    res = True
    if x > 100 or x < 0:
        res = False
    return res
        
def validarParidad(x):
    res = True
    if x > 2 or x < 0:
        print ("Error, ingrese un numero entre [0-2]: ")
        res = False
    return res
        
def repetirNum(res):
    while res == False:
        repNum = dameNum()
        res = validar(repNum)
    return repNum
        
def imprimir(a,b,c,d):
    if d == 0:
        mnj ="es par"
    elif d == 1:
        mnj == "es impar"
    elif d == 2:
        mnj == "es ambos"
        
    print ("Secuencia entre ",str(a),"y",str(b),",de",str(c),"en",str(c),"",mnj)
    a=int(a)
    b=int(b)
    c=int(c)
    d=int(d)
    secuencia(a,b,c,d)
    
def main():
    
    print("Ingrese numero inferior: ")
    numInf= dameNum()
    if validar(numInf) == False:
        print ("Error, ingrese un numero entre [1-99]: ")
        num=repetirNum(validar(numInf))
    
    print("Ingrese numero superior: ")
    numSup= dameNum()
    if validar(numSup) == False:
        print ("Error, ingrese un numero entre [1-99]: ")
        numSup=repetirNum(validar(numSup))
        
    print("Ingrese salto: ")
    numSalto= dameNum()
    
    print("Ingrese paridad: 0(par), 1(impar), 2(ambos)")
    numParidad= dameNum()
    if validar(numParidad) == False:
        print ("Error, ingrese un numero entre [1-99]: ")
        numParidad=repetirNum(validar(numParidad))
        
    imprimir(numInf,numSup,numSalto,numParidad)
    
    
main()