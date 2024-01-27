# El area y perimetro de rectangulo

alto = int(input('Proporciona el alto de un rectangulo: '))
ancho = int(input('Proporciona el ancho de un rectangulo: '))

# Calculo del area
area = alto * ancho
perimetro = (alto + ancho) * 2

print(f'El area: {area}')
print(f'El perimetro: {perimetro}')
