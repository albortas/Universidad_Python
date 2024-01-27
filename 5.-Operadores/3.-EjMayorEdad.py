# Determina si una persona es mayor de edad

MAYOR_EDAD = 18

edad = int(input('Proporcione la edad: '))

if edad < MAYOR_EDAD:
    print(f'La persono con edad {edad} es menor de edad')
else:
    print(f'La persona con edad {edad} es mayor de edad')