datos = []
neg = 0
contador = 0
pos = 0

def control():
    for i in range(4):
        dato = int(input("Ingrese un número: "))
        datos.append(dato)

def proceso(neg, contador, pos):
    for dato in datos:
        if dato<0:
            neg = neg + dato
        else:
            contador += 1
            pos = pos + dato
    return neg, pos, contador    

control()
print(datos)
a,b,c = proceso(neg,contador, pos)
print(f'La suma de los negativos es: {a}\nEl promedio de los positivos es: {b/c}')