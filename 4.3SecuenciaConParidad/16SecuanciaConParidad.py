def dameNum():
    num=int(input())
    return num
def secuencia(a,b,c,d):
    if d == 0:
        for a in range (a,b,c):
            if a %2 == 0:
                print(int(a))
    elif d == 1:
        for a in range (a,b,c):
            if a % 2 != 0:
                print(int(a))
    elif d == 2:
        for a in range (a,b,c):
            print(int(a))
    

def imprimir(a,b,c,d):
    if d == 0:
        d ="es par"
    elif d == 1:
        d == "es impar"
    elif d == 2:
        d == "es ambos"
        
    print ("Secuencia entre ",str(a),"y",str(b),",de",str(c),"en",str(c),"",d)
    
def main():
    print("Ingrese numero inferior: ")
    numInf= dameNum()
    print("Ingrese numero superior: ")
    numSup= dameNum()
    print("Ingrese salto: ")
    numSalto= dameNum()
    print("Ingrese paridad: 0(par), 1(impar), 2(ambos)")
    numParidad= dameNum()
    imprimir(numInf,numSup,numSalto,numParidad)
    resSecuencia = secuencia(numInf,numSup,numSalto,numParidad)
    
main()