# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda



if texto_1 == copia_texto_1 :
    print("texto_1 es igual a copia_texto_1")

if copia_texto_1 > texto_2 :
    print("copia_texto_1 es igual a texto_2")
else:
    print("copia_texto_1 es distinto a texto_2")

palabra_1=texto_1[0:1]
palabra_2=texto_2[0:1]

if palabra_1>palabra_2:
    print("palabra_1 es mayor a palabra_2")
else:
    print("palabra_1 es menor a palabra_2")
