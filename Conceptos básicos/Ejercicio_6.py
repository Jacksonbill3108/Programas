# Programa que permita ingresar 4 números positivos y negativos, 
# que como resultado muestre la suma de los negativos y el promedio de los positivos.

# indexado o index --> [a,b,c,d,e,f] --> 0,1,2,3,4,5 --> -6,-5,-4,-3,-2,-1
datos = []
neg = 0
contador = 0
pos = 0
for i in range(4):
    dato = int(input("Ingrese un número: "))
    datos.append(dato)
print(datos)    

for dato in datos:
    if dato<0:
        neg = neg + dato
    else:
        contador += 1
        pos = pos + dato

print(f'La suma de los negativos es: {neg}\nEl promedio de los positivos es: {pos/contador}')

