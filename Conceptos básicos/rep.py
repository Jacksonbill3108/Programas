def sum():
    a=float(input('digite el primer numero: '))
    b=float(input('digite el segundo numero: '))
    c= a + b
    print(c)
def rest():
    e=float(input("digite el primer numero: "))
    f=float(input("digite el segundo numero: "))
    g= e - f
    print(g)
def menu():
    print("digite una opcion 1.Suma , 2.Resta")
    op=int(input("ingrese una opcion: "))
    if op==1:
        sum()
        menu()
    elif op==2:
        rest()
        menu()
menu()