def dameSueldo():
    sueldo = int(input("Ingrese sueldo: "))
    return sueldo

def tieneHijo():
    res = False
    hijos=input("¿Tiene hijos (s/n)?: ")
    if hijos == "s":
        res = True
    elif hijos == "n":
        res = False
    return res

def dameCategoria():
    cat=int(input("Ingrese categoria (1-9): "))
    return cat

def bono(sueldo):
    if sueldo > 2000:
        res = (sueldo * 15) / 100
    else:
        res=(sueldo * 20) / 100
    return res

def plus(sueldo,plush,plusc):
    pluss= sueldo + plush +plusc 
    return pluss

def plusH(sueldo,hijos):
    if hijos:
        plus = (sueldo*5)/100
    else:
        plus = 0
    return plus

def plusC(sueldo, categoria):
    if categoria == 1 or 2 or 3:
        res = (sueldo * 10)/100
    elif categoria == 4 or 5 or 6:
        res = (sueldo * 12)/100
    else:
        res = (sueldo * 20)/100
    return res

def main():
    sueldo=dameSueldo()
    hijos=tieneHijo()
    categoria=dameCategoria()
    bonoSueldo=bono(sueldo)
    plusCategoria=plusC(sueldo, categoria)
    plusHijos=plusH(sueldo, hijos)
    total = plus(sueldo,plusCategoria,plusHijos)
    total = total + bonoSueldo
    print("El sueldo total sera de: $",str(total))
main()