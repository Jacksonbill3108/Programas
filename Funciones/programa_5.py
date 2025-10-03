lista = []
def datos():
    print("Bienvenido al registro de notas")
    curso = input("Ingrese la materia: ")
    cantidad = int(input("Ingrese la cantidad de alumnos: "))
    for i in range(cantidad):
        nota = int(input("Ingrese la nota: "))
        lista.append(nota)
    menu(curso, cantidad)

def note_print(curso):
    print("Informe del curso", curso, "\n Las notas obtenidas son: ", lista)
    menu(curso, len(lista))
def prom(cantidad, curso):
    x=0
    for i in range(cantidad):
        if (51>lista[i]):
            x=x+1
    promedio = sum(lista)/cantidad
    print("El curso ", curso, "tiene un promedio de nota de: ", promedio, "\n Una cantidad de reprobados de: ", x)
    menu(curso, cantidad)
        
def menu(a=None, cantidad=None):
    print("Bienvenido al menu docente de la UAGRM\n  \n 1. Ingresar notas \n 2. Imprimir  notas \n 3. Calcular el promedio y reprobados")
    op = int(input("Ingrese su preferencia: "))
    if op == 1:
        datos()
    elif op == 2:
        note_print(a)
    elif op == 3:
        prom(cantidad, a)
    else:
        print("Error vuelvalo a intentar")
        menu()


menu()        