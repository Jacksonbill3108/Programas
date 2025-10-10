dato = []
class Word:
    def __init__(self, word, meaning, translation, pronunciation):
        self.word = word
        self.meaning = meaning
        self.translation = translation
        self.pronunciation = pronunciation

    def mostrar_info(self):
        print(f" {self.word} = {self.meaning}\n Traduccion: {self.translation} ({self.pronunciation})")

    def translate(self):
        pass

    def define(self):
        pass

def register(): 
    print("Bienvenido al registro de palabras")
    word = input("Palabra: ")
    meaning = input("Definicion: ")
    translation = input("traduccion: ")
    pronunciation = input("Pronunciacion: ")
    objeto = Word(word,meaning,translation, pronunciation)
    dato.append(objeto)
    print("Palabra guardada correctamente!")
    objeto.mostrar_info()
def translator(): pass
def search(): 
    word = input("Ingrese la palabra a buscar: ")
    for objeto in dato:
        if objeto.word == word:
            objeto.mostrar_info()

while True:
    print("Bienvenido al menu\n 1. Registrar palabra\n 2. Traducir\n 3. Buscar definicion\n 4. Salir")
    try:
        op = int(input("Seleccione una opcion: "))
        if op == 1: register()
        elif op ==2: translator()
        elif op == 3: search()
        elif op ==4: break
        else: print("Ingrese un valor valido")
    except ValueError:
        print("Write only numbers")