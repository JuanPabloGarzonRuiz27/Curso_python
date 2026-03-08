#Calculadora Basica Python
def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    return a/b
salir=False
while not salir:
    entrada=input("Ingresa la operacion que desea calcular"" ")
    if entrada == "salir":
        salir=True
    else:
        if entrada =="suma":
            a=float(input("ingresa el primer digito:"" "))
            b=float(input("ingresa el segundo digito:"" "))
            print(suma(a,b))
        elif entrada =="resta":
            a=float(input("ingresa el primer digito:"" "))
            b=float(input("ingresa el segundo digito:"" "))
            print(resta(a,b))
        elif entrada =="multiplicacion":
            a=float(input("ingresa el primer digito:"" "))
            b=float(input("ingresa el segundo digito:"" "))
            print(multiplicacion(a,b))
        elif entrada == "division":
            a=float(input("ingresa el primer digito:"" "))
            b=float(input("ingresa el segundo digito:"" "))
            print(division(a,b))


