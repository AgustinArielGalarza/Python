'''

'''
def dameLado():
    print("Ingrese un lado: ")
    lado= int(input())
    return lado

def areaCirc(rad):
    rad= rad/2
    pi= 3.14
    areaCirculo= pi*(rad * rad)
    return areaCirculo

def areaCuad (lado):
    areaCuadrado = lado*lado
    return areaCuadrado

def areaNeg(areanegra, cir1, cir2, cir3):
    areanegraRestante= float(areanegra - cir1 -cir2 -cir3)
    return areanegraRestante

def porcentajeTotal(areanegra,arearestante):
    porcentaje= (arearestante/areanegra)*100
    return porcentaje
    
def impresor():
    return ""

def main():
    circulo1=areaCirc(8)
    circulo2=areaCirc(4)
    circulo3=areaCirc(4)
    AreaNegra=areaCuad(dameLado())
    AreaNegraRestante = areaNeg(AreaNegra,circulo1,circulo2,circulo3)
    porcentajeTotalDelAreaDelCuadrado= porcentajeTotal(AreaNegra, AreaNegraRestante)
    print("El area negra es: ",AreaNegraRestante," y es de un ",porcentajeTotalDelAreaDelCuadrado,"% del area total de un cuadrado.")
main()