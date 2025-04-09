lista = []
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))
c = int(input("Ingrese un numero: "))
lista.extend([a,b,c])
if lista[0]%2==0:
    print("El primer digito es par")
if lista[0]%2!=0:
    print("Es impar")
if lista[-2]%2==0:
    print("El segundo digito es par")
if lista[-2]%2!=0:
    print("El segundo valor es impar")     
if lista[2]%2==0:
    print("El tercer valor es par")
if lista[2]%2!=0:
    print("El tercer valor es impar")
