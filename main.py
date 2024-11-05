import random

# Obtiene la cantidad de numeros que son impares en la lista
def CantidadNumerosImpares(Numeros):
    Cantidad = 0
    for i in Numeros:
        if i%2 != 0:
            Cantidad += 1
    print("El total de numeros impares es:",Cantidad)
    return

# Saca el promedio de los numeros pares sin contar los 0
def PromedioNumerosPares(Numeros):
    Total = 0
    Cantidad = 0
    for i in Numeros:
        if i%2 == 0 and i != 0:
            Cantidad += 1
            Total += i
    print("El promedio de los numeros pares es:",Total/Cantidad)
    return

# Saca la cantidad de numeros que se encuentran dentro de la segunda docena (13-24)
def CantidadNumerosSegundaDocena(Numeros):
    Cantidad = 0
    for i in Numeros:
        if 12<i and i<=24:
            Cantidad += 1
    print("La cantidad de numeros de la segunda docena (13-24) es de:",Cantidad)
    return

# Saca el numero mas grande de la lista
def NumeroMasGrande(Numeros):
    while True:
        cambios = 0
        for i in range(len(Numeros)-1):
            if Numeros[i] > Numeros[i+1]:
                Numeros[i], Numeros[i+1] = Numeros[i+1], Numeros[i]
                cambios += 1
        if cambios == 0:
            break
    print("El numero mas grande es:",Numeros[len(Numeros)-1])
    return
    
# Se guardan los numeros
Numeros = []

# Se generan los numeros
while True:
    Numero = round(random.random() * (36 - 1 + 1) + 1)
    Numeros.append(Numero)
    if Numero == 36:
        break

# Se muestran los numeros que se generaron
print("Estos son los numeros aleatorios:")
for i in Numeros:
    print("   ",i)

# Se utilizan las funciones
CantidadNumerosImpares(Numeros)
PromedioNumerosPares(Numeros)
CantidadNumerosSegundaDocena(Numeros)
NumeroMasGrande(Numeros)