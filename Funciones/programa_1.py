
def suma():
    a = int(input("Escriba un numero: "))
    print(a+a)
    menu()

def sumpro():
    negativo = []
    positivo = []
    for i in range(6):
        num = int(input("Ingrese un numero: "))
        if num < 0:
            negativo.append(num)
        elif num >0:
            positivo.append(num)
    prom = sum(positivo) / len(positivo)   
    sumatoria = sum(negativo)
    return prom, sumatoria
        

def menu():
    print("-------------Bienvenido al menu-----------\n 1. Saludo\n 2. Suma\n 3. Ejercicio 7\n 4. Salir")
    op = int(input("Ingrese una opcion: "))
    if op ==1:
        print('Hola mundo')
        menu()
    elif op==2:
        suma()
    elif op==3:
        a,b=sumpro()    
        print("La sumatoria de valores negativos es: ", b, "\nEl promedio calculado es: ", a)
    elif op == 4:
        exit()
    else:
        print("Valor incorrecto, vuelvalo a intentar")
        menu()

menu()