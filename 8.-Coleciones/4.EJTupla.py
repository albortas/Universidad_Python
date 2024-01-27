#Dada la siguente tupla
#Crear un lista que solo incluya los numeros menores a 5

tupla = (13, 1, 8, 3, 2, 5, 8)
numeros = []

for numero in tupla:
    if numero < 5:
        numeros.append(numero)

print(numeros)