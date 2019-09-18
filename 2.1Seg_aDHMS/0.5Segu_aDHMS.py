'''
Ingrese un numero entero que sera la cantidad de segundos
Invocar la funcion convertir y devuelva dicho numero en dias
horas minutos y segundos
'''

def dameSeg():
    print("Ingrese la cantidad de segundos")
    seg= int(input())
    return seg

def convertir(seg):
    dias= 0
    horas= 0
    minutos= 0
    while seg >= 60:
        seg = seg - 60
        minutos += 1
        if minutos == 60:
            minutos= 0
            horas +=1
            if horas == 24:
                horas = 0
                dias += 1
    print(dias," dias(s),",horas," hora(s),",minutos," minuto(s),",seg,"segundo(s)")
    
def main():
    seg = dameSeg()
    convertir(seg)
    
main()