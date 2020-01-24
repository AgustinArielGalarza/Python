def dameNum():
    num=int(input())
    return num
#def secuencia(a,b,c):
#    while a < b :
#        print(str(a))
#        a = a + c
def secuencia(a,b,c):
    for a in range(a,b,c):
        print(str(a))
        
def main():
    print("ingrese numero inferior: ")
    inf=dameNum()
    print("ingrese numero superior: ")
    sup=dameNum()
    print("ingrese numero salto: ")
    salto=dameNum()
    secuencia(inf,sup,salto)
main()