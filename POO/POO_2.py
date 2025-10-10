dato = []
class Word:
    def __init__(self, palabra, traduccion, pronunciacion):
        self.palabra = palabra
        self.traduccion = traduccion
        self.pronunciacion = pronunciacion

    def buscar(self):
        pass

    def mostrar(self):
        print(f"{self.palabra} = {self.traduccion} ({self.pronunciacion})")

def register():
    print("Bienvenido al registro")
    palabra = input("Ingrese la palabra: ")
    traduccion = input("Ingrese su traduccion: ")
    pronunciacion = input("Ingrese la pronunciacion: ")
    obj = Word(palabra, traduccion, pronunciacion)
    dato.append(obj)
    print(dato)
def search():
    a = input("Ingrese la palabra que necesita: ")
    for obj in dato:
        if obj.palabra == a:
            obj.mostrar()


def eliminar(): pass

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