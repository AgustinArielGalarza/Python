def dameNum():
    num = int(input("Ingrese un numero: "))
    return num
def tabla(num):
    i = 1
    print("La tabla es: ")
    while i < 10:
        res= i * num
        i+=1
        print(num,"X",i,"=",res)

def tabla2(num):
    print("La tabla es: ")
    for i in range(1,11):
        res = i * num
        print(num,"X",i,"=",res)


def opcion():
    num = int(input("Ingrese 1 para usar While o 2 para usar For: "))
    if num == 1:
        tabla(dameNum())
    else:
        tabla2(dameNum())

def main():
    opcion()    

main()

