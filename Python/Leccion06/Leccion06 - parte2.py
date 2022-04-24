def listarTerminos(**terminos): #recibe como parametros un diccionario (por lo general se usa **kwargs)
    for llave, valor in terminos.items():
    	print(f'{llave}: {valor}')

listarTerminos(IDE='Integrated enviroment development', POO='Programacion Orientada a Objetos')
listarTerminos(DBMS='Database Managment System')
print('-----------------------------')
def desplegarNombres(nombres):
	for nombre in nombres:
		print(nombre)
nombres = ['Juan', 'Karla', 'Guillermo']
desplegarNombres(nombres)
desplegarNombres('Carol')#itera cada una de los caracteres, recordemos que una variable que tenga un texto se puede interpretar como una lista de caracteres
desplegarNombres((10, 11)) #asi lo interpreta como una tupla
desplegarNombres([12,14])#asi lo interpreta como una lista
print('-----------------------------')
#Funciones recursivas: es una funcion que se llama a si misma para completar un tarea
def factorial(numero):
	if numero == 1:
		return 1 #la funcion acaba para cuando numero sea igua a 1
	else: 
		return numero * factorial(numero - 1) #esto es una funcio recursiva ya que notamos que se vuelve a llamar hasta que numero sea igual a 1
resultado = factorial(5)
print(f'el factoria de 5 es {resultado}')	
print('-----------------------------')	

