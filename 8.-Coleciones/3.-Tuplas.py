#Definir una tupla
frutas = ('Naranja', 'Platano', 'Guayaba')
print(frutas)

#Saber el largo
print(len(frutas))

#Acceder a un elemento
print(frutas[0])

#Navegacion inversa
print(frutas[-1])

#Acceder a un rango
print(frutas[0:1]) #sin incluir el ultimo elemento

#Recorrer elementos
for fruta in frutas:
    print(fruta, end='\t')
else:
    print()

#cambiar el valor 
#Tupla es inmutable
#frutas[0] = 'Pera'
    
#Convertir de un tupla a lista
frutas_lista = list(frutas)
frutas_lista[0] = 'Pera'
frutas = tuple(frutas_lista)
print(frutas)

#Eliminar la tupla
del frutas