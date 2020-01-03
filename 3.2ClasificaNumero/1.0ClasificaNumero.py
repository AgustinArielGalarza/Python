def dameNum():
    print("Ingrese numero: ")
    num=input()
    if '.' in num:
        num=float(num)
       
    else:
        num=int(num)
        
    return num

def estado(num):
     mensaje = ""
     if num > 0 :
         mensaje= "El numero es positivo "
     elif num < 0 :
         mensaje = "El numero es negativo "
     else:
         mensaje = "El numero es cero "
     return mensaje
    
def enteroNatural_entero_Real(num):
    mensaje = ""
    if isinstance(num, int):
        if num > 0 :
            mensaje = "es entero natural."
        else:
            mensaje = "es entero."
    elif isinstance(num, float):
        mensaje = "es Real"
    return mensaje

def main():
    num= dameNum()
    estad= estado(num)
    EnER= enteroNatural_entero_Real(num)
    print(estad,"y",EnER)
    
main()