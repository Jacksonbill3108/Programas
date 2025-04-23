
def Suma():
    a = int(input("Ingrese un número: "))
    b = int(input("Ingrese otro número: "))
    print("La suma es: ", a+b)

def resta():
    a=int(input("Ingrese un número: "))
    b = int(input("Ingrese otro número: "))
    print("el resultado es: ", a-b)

def multiplicacion():
    a=int(input("Ingrese un número: "))
    b= int(input("Ingrese otro número: "))
    print("El resultado es: ", a*b)

def division():
    a = int(input("Ingrese un número: "))
    b = int(input("Ingrese otro número: "))
    print("El resultado es: ", a/b)

while True:
    print("Bienvenido al menú\n 1. Sumar\n 2. Despedir")
    option = int(input("Ingrese una opción: "))
    if option == 1:
        Suma()
    elif option == 2:
        resta()
    elif option == 3:
        multiplicacion()
    elif option == 4:
        division()
    else:
        print("Seleccione una opción válida")