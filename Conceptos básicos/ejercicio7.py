# Ingresar una cadena de texto y que devuelva la cadena sin vocales
# Imprima la cantidad de vocales y consonantes
vocales = []
consonantes = []
cadena = input("Introduzca una frase: ")
contador = 0
for letra in cadena:
    if letra.lower() in 'aeiou':
        vocales.append(letra)
    else: 
        consonantes.append(letra)
for dato in consonantes:
    if dato == ' ':
        contador +=1
print(f'La cantidad de vocales encontradas son: {len(vocales)}\nLa cantidad de consonantes encontradas son: {len(consonantes) - contador}')
print(''.join(consonantes))