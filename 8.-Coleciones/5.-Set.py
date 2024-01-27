#Un set no mantiene un orden (no tiene indices)
#Es inmutable
#No permite elementos duplicados

planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)

#largo de los elmentos
print(len(planetas))

#revisar si un elemento esta presente
print('Marte' in planetas)

#Agregar un elemento
planetas.add('Tierra')
print(planetas)

#No se puede duplicar elementos
planetas.add('Tierra')
print(planetas)

#Eliminar un elemento posiblemente arrojando un error
planetas.remove('Tierra')
print(planetas)

#Elimina elemento sin arrojar error
planetas.discard('Jupiters')
print(planetas)

#Limpiar set
planetas.clear()
print(planetas)

#Eliminar set
del planetas
#print(planetas)
