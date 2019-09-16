
#programa solicite un numero real
#mostrara la descoposicion del numero real en esu pate estrada y su parte decimal

def desco(num):
    ent=int(num) #paso a entro
    dec= num - ent
    print("Numer0 = ", num ,", parte entera = ",ent, ", parte decimal = ", dec)

def dameNum():
    print("Dame numero: ")
    num=float(input())
    desco(num)
    
def main():
    dameNum()

main()