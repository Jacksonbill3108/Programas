dic = {}
def register():
    print("Registre su nueva palabra: ")
    x = input("")
    y = input("Escriba su traduccion: ")
    dic[x] = y
    print(dic)
def search():
    x = input("Ingrese la palabra: ")
    print(dic[x])

def eliminar():
    x = input("Ingrese la palabra: ")
    dic.pop(x)
    print(dic)


while True:
    print("Bienvenido al menu\n 1. Registrar palabra\n 2. Buscar palabra\n 3. Eliminar\n 4. Salir")
    try:
        op = int(input("Ingrese una opcion valida: "))
        if op ==1:
            register()
        elif op ==2: 
            search()
        elif op == 3:
            eliminar()    
        elif op ==4:
            break
        else: 
            print("ERROR intentelo de nuevo")
    except ValueError:
        print("Error, solo numeros son validos")