# Sintaxis de range (inicio <opcional>, fin <requerido>, incremento <opcional>)

#Ejercicio 1. Iterar un rango de 0 a 10 e imprimir numeros divisibles en 3
print('-'*55)
print(f'Numeros divisibles entre 3 en un rango de (0 a 10) son:')
for rango1 in range(0, 10 + 1, 3):
    if rango1 == 0:
        continue
    print(f'{rango1}',end='\t')

#Ejecicio 2. Crear un rango de numeros de 2 a 6, e imprimirlos
print(f'\nRango de numeros de 2 a 6:')
for rango2 in range(2, 6 + 1):
    print(rango2,end='\t')

#Ejercicio 3. Crear un rango de 3 a 10, pero con incremento de 2 en 2
print(f'\nRango de (3 a 10), pero con incremento de 2')
for rango3 in range(3, 10 + 1, 2):
    print(rango3,end='\t')
else:
    print()

print('-' * 55)

