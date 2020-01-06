def dameDia():
    dia=int(input("Ingrese dia: "))
    return dia
def dameMes ():
    mes=int(input("Ingrese Mes: "))
    return mes
def dameAño ():
    año=int(input("Ingrese Año: "))
    return año

def validaFecha(dias,mes,año):
    mensaje = False
    if año > 0 :
        if mes > 0 and mes <= 12:
            if dias <= 31 and dias > 0 and mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 :
                    mensaje = True
            elif dias <= 30  and dias > 0 and  mes == 4 or mes == 6 or mes == 9 or mes == 11 :
                    mensaje = True
            elif dias <= 29 and dias > 0 and mes == 2:
                    if año %4 == 0 and año %100 != 0 or año %400 == 0 :
                        mensaje = True
            elif dias <= 28 and dias > 0 and mes == 2:
                    mensaje = True
            else:
                mensaje = False
        else:
            mensaje = False
    else:
        mensaje = False
        
    return mensaje

def imprimir(dia,mes,año,valida):
    mensaje = ""
    if valida :
        mensaje = "es correcto"
    else:
        mensaje = "es incorrecto"
        
    print("\n",dia,"/",mes,"/",año," ",mensaje)
    
def main():
    dia= dameDia()
    mes= dameMes()
    año= dameAño()
    valida = validaFecha(dia,mes,año)
    imprimir(dia,mes,año,valida)    
    
main()