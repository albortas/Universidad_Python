nombres = ['Juan', 'Karla', 'Ricardo', 'Maria']
#Imprimir la lista de nombres
print(nombres)

# Acceder a los elementos de una lista
print(nombres[0])
print(nombres[1])

#Aceder de forma inversa
print(nombres[-1])
print(nombres[-2])

#Imprimir un rango
print(nombres[0:2]) # sin incluir el indice 2

#Ir del inicio de la lista al indice (sin incluirlo)
print(nombres[:3])

#Desde el indice indicado hasta el final
print(nombres[1:])

#Cambiar un valor
nombres[3] = 'Ivonne'
print(nombres)

# Iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print('No existen mas nombres en la lista')

#Preguntar el largo de una lista
print(len(nombres))

# Agregar un elemento
nombres.append('Lorenzo')
print(nombres)

# Insertar un elemento en un indice especifico
nombres.insert(1, 'Octavio')
print(nombres)

# Remover un elmento
nombres.remove('Octavio')
print(nombres)

#Remover el ultimo valor agragado
nombres.pop()
print(nombres)

#eliminar un indice
del nombres[0]
print(nombres)

# Limpiar la lista
nombres.clear()
print(nombres)

# Borrar la lista por completo
del nombres
#print(nombres)