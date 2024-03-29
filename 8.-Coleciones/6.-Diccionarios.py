#Diccionarios (key, value)
diccionario ={
    'IDE':'Integrated Development Environment',
    'OOP':'Object Oriented Programming',
    'DBMS':'Database Management System'
}
print(diccionario)

# Largo
print(len(diccionario))

# Acceder a un elmento (key)
print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('OOP'))

# Modificar elementos
diccionario['IDE'] = 'integrated development environment'
print(diccionario)

#Recorrer los elementos 
for termino, valor in diccionario.items():
    print(termino, valor)

for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

#Comprobar existencia de algun elemento
print('IDE' in diccionario)

#Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

#Remover un elemento
diccionario.pop('DBMS')
print(diccionario)

#Limpiar
diccionario.clear()
print(diccionario)

#Eliminar diccionario
del diccionario