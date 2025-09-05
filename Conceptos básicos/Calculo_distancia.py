
lista = []
print("[x1,y1,x2,y2]")
for i in range(4):
    dato = int(input("Ingrese un punto: "))
    lista.append(dato)
distancia = ((lista[2]-lista[0])**2+(lista[3]-lista[1])**2)**1/2
print("La distancia entre punto 1 y punto 2 es: ", distancia)
