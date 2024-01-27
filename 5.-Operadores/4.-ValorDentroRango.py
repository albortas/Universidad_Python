# Valor dentro de rango

numero = int(input('Proporcione un numero entre (0 y 200): '))

#if numero >= 0 and numero <= 200:
if 0 <= numero <= 200:
    print(f'Valor dentro de rango')
else:
    print(f'Valor fuera de rango')