# Listas
# Son conjuntos de datos ordenados y mutables
# puden almacenar distintos tipos de datos
# se puede acceder a cada elemento de la lista por su índice, comenzando en 0

print("Tipos de datos LISTA")
lista = ["Aquiles Baeza", True, 45]
print(lista)
print(type(lista))
print(lista[0])

lista[1] = False
print(lista)

# Diccionarios
# Son conjuntos de pares de datos ordenados y mutable
# se puede acceder a cada elemento de la lista por su nombre

print("Tipos de datos DICCIONARIO")
diccionario = {
    'nombre' : 'Alan Brito Delgado',
    'estudiante' : False,
    'edad' : 21
}
print(diccionario)
print(type(diccionario))
print(diccionario['edad'])

diccionario['edad'] = 22
print(diccionario['edad'])

# Conjuntos
# Son conjuntos de elementos desordenados
# podemos agregar o eliminar nuevos elementos

print("Tipos de datos CONJUNTO")
conjunto = {2,'Erick Bailey',True}
print(conjunto)
print(type(conjunto))

conjunto.add('Jaime Rios')
print(conjunto)
conjunto.pop()
print(conjunto)

# Tuplas
# Colecciones de datos inmutables

print("Tipos de datos TUPLA")
tupla = ('Armandos Casas',False,45)
print(tupla)
print(type(tupla))

# Los cambios en tuplas nop están permitidos
# tupla[0]='Jose Feliciano'
# print(tupla)