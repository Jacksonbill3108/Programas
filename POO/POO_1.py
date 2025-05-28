Procesadores = []
Motherboards = []
Computadoras = []

class procesador:
    def __init__(self, marca, generacion, modelo):
        self.marca_proc = marca
        self.generacion = generacion
        self.modelo_proc = modelo

    def __str__(self):
        return f' Procesador {self.marca_proc} {self.modelo_proc}'

class motherboard:
    def __init__(self, marca, modelo):
        self.marca_moth = marca
        self.modelo_moth = modelo

    def __str__(self):
        return f' Motherboard {self.marca_moth} {self.modelo_moth}'

class computadoras(procesador,motherboard):
    def __init__(self, procesador, motherboard, ram, memoria, capacidad):
        self.procesador = procesador
        self.motherboard = motherboard
        self.ram = ram
        self.memoria = memoria
        self.capacidad = capacidad

    def __str__(self):
        return f'---------------\n Computadora \n ------------------ {self.procesador}\n {self.motherboard}\n Ram: {self.ram} GB\n Memoria: {self.memoria} {self.capacidad} GB'
        

def Ingresar_computadora():
    print("------------------------\n Armado de computadora\n ------------------------\n Estas son sus opciones: ")
    print("------------------------\nProcesadores: ")
    for i in Procesadores:
        print(f'\n{Procesadores.index(i)}. {i}')
    procesador_index = int(input("Ingrese el procesador de preferencia: "))
    print("------------------------\nMotherboards: ")
    for o in Motherboards:
        print(f'\n{Motherboards.index(o)}. {o}')
    motherboard_index = int(input("Ingrese la motherboard de preferencia: "))
    procesador = Procesadores[procesador_index]
    motherboard = Motherboards[motherboard_index]
    ram = int(input("Ram: "))
    memoria = input("SSD o HDD o M.2\n")
    capacidad = int(input("Ingrese la memoria: "))
    ensamblaje = computadoras(procesador,motherboard,ram,memoria,capacidad)
    Computadoras.append(ensamblaje)
    print(ensamblaje)


def Ingresar_procesador():
    print("------------------------\n Ingreso de procesador\n ------------------------")
    marca = input("Marca: ")
    if marca.lower() == 'intel':
        generacion = input("Generación: ")
        modelo = input("Modelo: ")
    elif marca.lower() == 'amd':
        generacion = None
        modelo = input("Modelo: ")
    else: 
        print("Ingrese una marca conocida")
        menu()
    objeto = procesador(marca, generacion, modelo)
    Procesadores.append(objeto)
    print(f'{objeto} añadido exitosamente')

    

def Ingresar_motherboard():
    print("------------------------\n Ingreso de motherboard\n ------------------------")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    objeto = motherboard(marca, modelo)
    Motherboards.append(objeto)
    print(f'{objeto} añadido exitosamente')
    
def Buscar_computadora():
    pass

def Buscar_procesador():
    pass

def Buscar_motherboard():
    pass


def menu():
    print("**** Bienvenido al menú ****\n1. Ingresar equipo\n2. Buscar equipo\n3. Mostrar todo\n4. Salir")
    op = int(input("Ingrese una opción: "))
    if op == 1:
        op2 = input("a) Computadora\nb) Componente\n")
        if op2 == 'a':
            Ingresar_computadora()
        elif op2 == 'b':
            op3 = input("a) Procesador\nb) Motherboard\n")
            if op3 == 'a':
                Ingresar_procesador()
            elif op3 == 'b':
                Ingresar_motherboard()
            else: 
                print("Ingrese una opción valida")
            menu()
        else: 
            print("Ingrese una opción valida")
        menu()            
    elif op == 2:
        op2 == input("a) Computadora\nb) Procesador\nc) Motherboard")
        if op == 'a':
            Buscar_computadora()
        elif op == 'b':
            Buscar_procesador()
        elif op == 'c':
            Buscar_motherboard()
        else:
            print("Inserte una opción valida")
        menu()    
    elif op == 3:
        pass
    else:
        exit()

menu()