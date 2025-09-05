lista=[]
for i in range(5):
    dato=input("Ingrese dato:")
    lista.append(dato)
print(lista[0]+" "+lista[1])
b=bool(int(lista[2]))
print(b)
print(f"El estado logico es:{b}")
c=int(lista[3])
d=int(lista[4])
print(c-d)