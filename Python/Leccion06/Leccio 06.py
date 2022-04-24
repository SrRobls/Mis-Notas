print('                 Funciones en python')
#Una funcion es un bloque de codigo que podemoa llamar n cantidad de veces
#Primero que todo hay que definir la funcion (no podemos llamar una funcion antes de definirla, marcaria error)
def miFuncion(): #Usamoa def 'nombre de la funcion'(): -> para crea una funcion
	print('Hola desde mi funcion!!!')

#para 'llamar' una funcion debemos colocar el nombre de la funcio y colocar los ()
miFuncion()
miFuncion()
miFuncion()
print('---------------------------')
#Parametros en una funcion:
#parametros: variables que declaramos en la funcion
#argumento: valor que enviamos a la funcion (lo que vale el parametro)
def miFuncion2(nombre, apellido): #lo que esta en ('Parametros') son los parametros
	print(f'Hola soy {nombre} {apellido}. Mucho gusto!')

miFuncion2('Johan', 'Robles') #nombre = 'Johan', apellido = 'Robles'
#Lo que esta en ('Argumentos') son lo argumentos, es decir las variables que se les pasa para trabajar con los pararametros de la funcion
#Nota tiene que haber la misma cantidad de argumentos y parametrso, si no, maracara error
miFuncion2(5, 7)
print('---------------------------')
def sumar(a,b):
	return a + b #Usamos return para regresar la suma de a + b y no usar una variable que guarde la suma
#return se lo utiliza en funciones para devolver un solo valor. return detiene la ejecución de la función y devuelve el resultado indicado. ej. def cuadrado (x): return x*x.
resultado = sumar(5,2)
print(f'La suma es: {resultado}')
#tambien podemos
print(f'La suma es: {sumar(5,6)}')
print('---------------------------')
#Tambien podemos colocara parametros por defecto
def sumar(a = 0, b = 0):
	return a + b 
resultado = sumar() #Se hace la suma con los valor por default
print(f'La suma es: {resultado}')
resultado = sumar(20,33) #Aqui se cambian si le pasamos los argumentos cambianos los valores por default
print(f'La suma es: {resultado}')
print('---------------------------')
#Para poner un parametro de varios valores (como una lista)
def listaNombre(*nombres): #ese *nombres se puede interpretar como una tupla
	for i in nombres:      #Esto se conoce como argumentos variados (su notacion es*args)
		print(i)

listaNombre('Johan', 'Sebastian', 'Laura', 'Valentina') #que son los argumenos que se guardaran como una tupla por el *nombres
print('*')
listaNombre('Pedro', 'Juan', 'Daniela')
#Ejercicio: Crear una función para sumar los valores recibidos de tipo numérico, utilizando argumentos variables *args como parámetro de la función y regresar como resultado la suma de todos los valores pasados como argumentos.
print('-------------------')
def sumarNumeros(*numeros):
	caja = 0
	for i in numeros:
		caja += i #caja = caja + i
	return caja	

resultado = sumarNumeros(2,3,2,5,2,3)
print(f'resultado: {resultado}')

#Ejercicio: Crear una función para multiplicar los valores recibidos de tipo numérico, utilizando argumentos variables *args como parámetro de la función y regresar como resultado la multiplicación de todos los valores pasados como argumentos.

def muliplicarNumeros(*args):
	caja = 1 #Debe iniciar en 1 porque si inicia en 0 se anularian las multiplicaciones
	for i in args:
		caja *= i
	return caja


resultado = muliplicarNumeros(2,5,4)
print(f'resultado: {resultado}')