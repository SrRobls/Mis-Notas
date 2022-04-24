#Definir una tupla
frutas = ('Naranja', 'Plátano', 'Guayaba')
print(frutas)
#saber el largo
print(len(frutas))
#acceder a un elemento
print(frutas[0])
# navegación inversa
print(frutas[-1])
# acceder a un rango
print(frutas[0:1])# sin incluir el último índice
#recorrer elementos
for fruta in frutas:
    print(fruta, end=' ') #Se usa end='(el caracter que queramos)' para que en vez de que haga un salto de linea imprima lo que pusimos como caracter
#cambiar valor tupla. recordemos que no se puede hacer como una lista, asi que debemos usar este metodo
# frutas[0] = 'Pera'
frutasLista = list(frutas)
frutasLista[0] = 'Pera'
frutas = tuple(frutasLista)
print('\n',frutas)
#eliminar la tupla
#del frutas
print(frutas)
#Ejercicio dada la siguiente tupla: crear una lista que solo incluya los numero menores que 5 utilizando:
# tupla = (13,1,8,3,2,5)
nums = (13,1,8,3,2,5)
listaNums = list(nums)
j = 0
for i in listaNums:
	while listaNums[j] >= 5:
		listaNums[j] = int(input(f'Dame un valor menor a 5 para el indice #{j+1}: '))
	else:
		j += 1
else:
	nums = tuple(listaNums)
	print(f'La tupla ahora tiene los siguientes valores: {nums}')


	
