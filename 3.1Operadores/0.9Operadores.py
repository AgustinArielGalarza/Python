def dameNum1():
    print("Ingrese el primer numero: ")
    num1=int(input())
    return num1

def dameNum2():
    print("Ingrese el segundo numero: ")
    num2=int(input())
    return num2
def dameOperador():
    print("Ingrese el operador: ")
    operador=input()
    return operador
    
def operar(a,b,operador):
    if operador == "+" :
        res = a + b
    elif operador == "-" :
        res = a -b
    elif operador == "*" :
        res = a * b
    elif operador == "/" :
        res = a / b
    elif operador == "//" :
        res = a // b
    elif operador == "**" :
        res = a ** b
    return res

def main():
    num1=dameNum1()
    num2=dameNum2()
    operador=dameOperador()
    resultado = operar(num1, num2, operador) 
    print(str(resultado))
main()