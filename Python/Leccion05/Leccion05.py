#                           Listas en python:
#Una lista/array es una variable que tiene x cantidad de elemetos (desde 0<->x-1)
lista = ['Juan', 'Karla', 'Maria', 2, 300, True]  #Asi se escribe una lista
       #[   0       1        2     3  4    5 ]  #Donde puede tener caracteres, numeros, etc.
#Imprimir la lista
print(lista)
#Acceder a los elementos de la lista (recordar que las listas comienzan con indice 0)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
print(lista[5])
#Acceder a los elementos de manera inversa:
print('-------------1')
print(lista[0])
print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-4])
print(lista[-5])
print('-------------2')
#Imprimir un rango:
print(lista[0:4]) #Imprime los elementos de los indices 0,1,2,3 solamente, el 4 no se incluye
#Imprimir una lista pero hasta una lista dada
print(lista[:3]) #se imprime los elementos de los indices 0,1,2 y para en el indice 3
#Imprimir desde el indice indicado:
print(lista[2:]) #Se imprime los elemetos de los indices 2,3,4,5 y 6
#Cambiar el valor de un indice:
print(f'Cambiamos a {lista[2]} por: ')
lista[2] = 'Johan'
print(lista[2])
print(lista)
print('-------------3')
#iterar una lista:
for i in lista:
	print(i)
else:
	print('Fin For')
print('-------------4')
#Preguntar el 'largo' de una lista:
print(len(lista)) #Se usa 'len' para que nos muestre la cantidad de elementos de una lista
#Agregar un elemento:
lista.append('Sebastian') # se usa la funcion 'lista'.append('los elementos a agregrar separados por una ,')
                          # para agragar elementos a una lista
print(lista)
#Insertar un elemento en un indice en especifico:
lista.insert(3, 5000) #Se usa 'lista'.insert('#indice', 'elemento a agregar') para agregar el elemento en el indice proporcionado
#Notemos que ningun elemento se borra, solo se 'corre' como creando otro +1 indice
print(lista)
#Remover el ultimo valor de la lista:
lista.pop()
#Notemos que se elimina el ultmo elemento de la lista
print(lista)
#Para remover un elemento:
lista.remove(300)
lista.remove('Karla') #Usamos 'lista'.remove('elemento') para eliminar a ese elemento del array
print(lista)
#Para eliminar un indice:
del lista[0] #del 'lista'['el indice que queremos eliminar']
print(lista)
#eliminar una lista:
del lista #del 'lista a eliminar'
print(lista) #Nos marcara error ya que se elimino la lista
#Ejercicio: Pedir 5 numeros al usuario e imprimir solo los que son divisibles por 3
numeros = []
num = 0
i = 1
while i <= 5:
	num = int(input(f'Dame el numero a agregar #{i}: '))
	numeros.append(num)
	i += 1
else:
	print('Fin de recoleccion')
	i = 0

for i in numeros:
	if i % 3 == 0:
		print(f'El numero {i} es multiplo de 3')
else:
	print('Final')