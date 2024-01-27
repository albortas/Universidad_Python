""" for letra in 'Holanda':
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        break
else:
    print('Fin ciclo for') """

""" for i in range(6):
    if i % 2 == 0: 
        print(f'Valor: {i}') """

for i in range(10):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')