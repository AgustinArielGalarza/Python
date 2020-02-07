def dameNum():
    num = int(input())
    return num

def damePrimo(num):
    i= 1
    acumula=""
    for i in range(1,num):
        j=1
        contador = 0
        while j <= i:
            if i % j == 0:
                contador += 1
                j += 1
            else:
                j+=1
        if contador == 2:
            acumula += '{:^5}'.format(i)
            
    print (acumula,"\n")        

def cant(num):
    i= 1
    contador = 1
    contadorForamt = 0
    acumula=""
    while contador < num:
        if i < 9999: 
            if i % 1 == 0 and i % i == 0 and i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
                acumula += '{:^5}'.format(i)
                contadorForamt += 1
                if contadorForamt == 10:
                    print("\t")
                contador += 1
                i += 1
            elif  i == 2 or i == 3 or i ==5:
                acumula +='{:^5}'.format(i)
                contador += 1
                i+= 1
            else:
                i += 1
           
    print (acumula,"\n")
            
def main():
    print ("Ingrese un numero: ")
    num = dameNum()
    print("Primos entre 1 y",num,": \n")
    damePrimo(num)
    print("Primeros",num,"primos: \t")
    cant(num)

    
main()