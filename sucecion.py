# Escribir una programa que calcule los siguientes 3 número de la sucesión 1, 1, 2, -1, 1, -2, -1, ?, ?, ?
# 1, + 1, - 2, + -1, - 1, + -2, - -1, + -1?, - -2?, + 1?

numero = 1
numeroanterior = 1
lista = []

lista.append(numero)
for i in range(9):
    lista.append(numero)
    if i%2 == 0:
        numero, numeroanterior = numeroanterior + numero, numero
    else:
        numero, numeroanterior = numeroanterior - numero, numero

print(lista)