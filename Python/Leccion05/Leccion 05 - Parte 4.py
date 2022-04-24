print('                   Diccionario en python')
#como su nombre es una coleccion de datos que tendra (key:value), es que guarda variables y su valor
#Diccionario:
diccionario = {
	'IDE': 'Integrated Development Enviroment',
	'OOP': 'Object Oriented Programming',
	'DBMS': 'Database Managment System'
}
print(diccionario)
#largo:
print(len(diccionario))
# Acceder a un elemento (key)
print(diccionario['IDE'])
# Otra forma:
print(diccionario.get('OOP'))
diccionario['IDE'] = 'aqui hay un cambio'
print(diccionario)
print('-----------------')
#Recorre los elementos
for termino, valor in diccionario.items(): #Se usa la funcion items para acceder a la llave y el valor de el diccionario
	print(termino, valor)
print('----')
for termino in diccionario.keys(): #Para solo obtener las llaves
	print(termino)
print('----')
for valor in diccionario.values(): #para imprimir solo los valores
	print(valor)
#Comprobar la existencia de algun elemento:
print('IDE' in diccionario) 
print('PEPE' in diccionario)
print('----')
#agregar un elemento
diccionario['PEPE'] = 'El Pepe!'
print(diccionario)
print('----')
#remover un elemento
diccionario.pop('PEPE')
print(diccionario)
print('----')
#Limpiar
diccionario.clear()
print(diccionario)



