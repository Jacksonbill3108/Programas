def dato(op):
    if op == 1:
        figura = 'radio del circulo'
    elif op == 2:
        figura = 'lado del cuadrado'        
    print("Ingrese el dato del ", figura)    
    data = int(input())
    return data

def circulo(a):
    print("La figura seleccionada es: Circulo\n Con radio = ", a, "\n El area es: ", 3.1416 * a**2, "\n El perimetro es: ", 2*3.1416*a)
    menu()

def cuadrado():
    pass



def menu():
    print("Bienvenido al menu \n Seleccione la figura a trabajar \n 1. Circulo \n 2. Cuadrado \n 3. Salir")
    op = int(input("Ingrese su preferencia: "))
    if op == 1:
        a = dato(op)
        circulo(a)
    elif op == 2:
        dato(op)
        cuadrado(a)
    elif op == 3:
        exit()
    else:
        print("Error vuelvalo a intentar")
        menu()


menu()        