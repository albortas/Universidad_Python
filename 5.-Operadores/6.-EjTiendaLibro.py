print('Proporcione los siguientes datos del libro')
nombre = input('Proporcione el nombre del libro: ')
id = int(input('Proporcione el ID del libro: '))
precio = float(input('Proporcione el valor del libro: '))
envioGratuito = input('Indica si es envio gratuito (True/False): ')

if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito = False
else:
    print('Valor incorrecto proporcione (True o False)')

print(f'''
    Nombre: {nombre}
    Id: {id}
    Precio: {precio}
    Envio Gratuito: {envioGratuito}
''')