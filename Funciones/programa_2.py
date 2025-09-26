def saludo():
    print("Hola mundo")

def datos():
    n = int(input("Ingrese un numero: "))
    b = int(input("Ingrese un numero: "))
    return n,b

def operaciones(n,b):
    print("La suma es: ", n+b, "El resultado de la resta es: ", n-b)
    menu()

def menu():
    print("Bienvenido al menu\n 1. Imprimir saludo\n 2. Operaciones")
    op = int(input("Ingrese una opcion: "))
    if op == 1:
        saludo()
        menu()
    elif op == 2:
        n,b = datos()
        operaciones(n,b)
        menu()
    else:
        print("Error, intentalo de nuevo")
        menu()
menu()