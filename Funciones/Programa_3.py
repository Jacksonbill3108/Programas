# Verificador de CI
# Nos proporcione un CI y verificar que este sea valido, teniendo 7 digitos.


def registrar():
    pass


## usser = 962147J
## len(usser) = 7
## i = 9 ; i = 6 ... ; i = J --> lower() --> i = j

def verificar():
    usser = input("Ingrese su CI: ")
    if len(usser)==7:
        for i in usser:
            if i.lower() in "qwertyuioplkjhgfdsazxcvbnm":
                print("Su CI es invalido, verifique los digitos ingresados")    
                menu()    
        print("CI Valido")
        menu()
    else:
        print("Su CI es invalido, verifique la cantidad de digitos ingresados")    
        menu()

def menu():
    print("Bienvenido al menu \n 1. Registrarse \n 2. Verificar \n 3. Salir")
    op = int(input("Ingrese su preferencia: "))
    if op == 1:
        registrar()
    elif op == 2:
        verificar()
    elif op == 3:
        exit()
    else:
        print("Error vuelvalo a intentar")
        menu()



menu()