# Elaborar un programa que pida dos numeros y me imprima la suma.
lista = [2,5]
a = int(input('Ingrese un numero: '))
b = int(input('Ingrese otro numero: '))
lista.append(a)
lista.append(b)
print(lista)
c = int(input('Ingrese el valor a sumar: '))
print("La suma es: ", b + lista[c])