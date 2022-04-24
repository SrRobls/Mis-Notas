# Recursividad:

'''
Basicamente la recursividad programacion es una funcion que se llama a si misma hasta que se cumpla una condicion para no caer en un bucle 
infinito. hay dos principios fundamentales en la recursividad; el caso base, es el caso o la condicion que se debe cumplir para retornar
un valor fijo (numerico, booleano, etc) y no volver a llamar la funcion (basicamente parar la recursividad en si). Y el caso recursivo, que
es el caso donde la funciona se llama a si misma y por lo general lo hace con parametros diferentes, este se llama asi mismo hasa llegar al 
caso base. 
'''

# Ejemplo: Calcular el factorial de un numero.
'''
instintinamente, para calcular el factorial de un numero solo basta con multiplicar el nuemro en si con los valores sucecivamente que 
son menores que el.
5! = 5 x 4 x 3 x 2 x 1 = 120
o tambien podemos verla de forma distinta como:
5 x 4! = 5 x 24 = 120
    4 x 3! = 4 x 6 = 24
        3 x 2! = 3 x 2 = 6
            2 x 1! = 2 x 2 =1
                1 x 0! = 1 x 1 = 1
el factorial de 0 es 1 y tambien es nuestro caso base. 
veamos esto con codigo!
'''

def factorial(numero):
    # Caso base:
    if numero == 0:
        return 1
    # Caso recursivo:
    else:
        # interpretemonos como si retornaremos la multiplicacion de los valores retorndos anteriormente.
        return numero * factorial(numero-1)

print(factorial(5))
print(factorial(4))
print(factorial(3))
print(factorial(2))
print(factorial(1))

# 120
# 24
# 6
# 2
# 1

'''
Como vimos anteriormente, podemos ver que con recursividad podemos resolver problemas dividendolos en problemas mas pequeños y por tanto, para 
resolver estos problemas se necesita de la solucion del caso siguiente o anterior (dependiendo de problema. ademas notar que para este caso
se realiza con base al resultado del caso anterior o del numero anterior). estas soluciones quedan 'pendientes' en memoria para resolver cuando
se alcance una condición de fin o caso base, y el algoritmo retroceda resolviendo cada una de estas llamadas que quedó en espera y liberando 
la memoria hasta obtener el resultado final. veamos esta ultima parte como si fuera una pila (stack), cumpliendo asi el principio fundamental
de las plias, LIFO (Last in, Firts Out) que significa que el ultimo que entro (o el caso a ejecutar) es el primero en salir (en retornar la 
solucion).
'''
print('\n')
# Veamos un Ejemplo mas complicado:
'''
Hallar un numero de la serie fubonachi corrspondiente a un umero dado:
serie fubonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 ...
''' 

def fubonashi(numero):
    # Caso Base
    if numero == 0 or numero == 1:
        return numero
    # Caso recursivo
    else:
        # Ojo NO se llaman a la vez, se llama primero uno (el del numero-1) y luego el otro (el del numero-2), y posteriormentes se trabaja
        # con los argumentos que se les cambia
        return fubonashi(numero-1) + fubonashi(numero - 2)

print(fubonashi(0))
print(fubonashi(1))
print(fubonashi(2))
print(fubonashi(3))
print(fubonashi(4))
print(fubonashi(5))
print(fubonashi(6))
print(fubonashi(7))
print(fubonashi(8))
print(fubonashi(9))
print(fubonashi(10))

# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55

'''
Podemos ver el prceso del ejercico de la siguiente manera:
numero = 3
f -> para referirse a la funcion.

caso base cuando numero == 1 o numero == 2:
    retorno numero
caso resesivo:

                                    f(3) -> 2                    +                     f(2) -> 1     = 3
                                     |                                                   |
                    |----------------|----------------|                  |---------------|---------------|                                     
                    |                                 |                  |                               |
                f(2) -> 1            +            f(1) -> 1 = 2        f(1) -> 1         +           f(0) -> 0 = 1
                    |                                                                                 
           |--------|--------|                                                                         
           |                 |
          f(1) -> 1 +      f(0) -> 0 = 1
                      
'''

'''
Por ultimo recalcar que debemos saber cuando es o no conveniente usar recursividad, ya que en muchos problemas (sobre todo problemas con
datos numericos elevados) el uso de la rcursividad puede sobrepasar la pila de memoria para esta actividad. por tanto es necesario hacer un 
analisis previo del problema y ver si el uso de las funciones recursivas es 'natural' o no en esta.
'''