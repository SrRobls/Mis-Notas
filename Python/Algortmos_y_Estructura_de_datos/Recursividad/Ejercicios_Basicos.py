


'''
Implementar una función que permita obtener la serie de numeros de la sucesión de Fibonacci para un 
número dado.
'''


def fibonacci(numero):
    if numero == 0 or numero == 1:
        return numero
    else:
        return fibonacci(numero-1) + fibonacci(numero - 2)

def sucecion(num, string=''):
    # caso base:
    if num == 0:
        string += str(' 0')
        print(string)
    else:
        string += ' ' + str(fibonacci(num))
        return sucecion(num-1, string)
    
sucecion(5)
# 5 3 2 1 1 0
sucecion(10)
# 55 34 21 13 8 5 3 2 1 1 0
sucecion(15)
# 610 377 233 144 89 55 34 21 13 8 5 3 2 1 1 0

'''
Implementar una función que calcule la suma de todos los números enteros comprendidos 
entre cero y un número entero positivo dado.

el metodo usado es como con el factorial.}

numero = 5
f(5) = 15
5 + f(4) = 15
    4 + f(3) = 10
        3 + f(2) = 6
            2 + f(1) = 3
                1
'''              



def suma_recursiva(numero):
    # Caso Base
    if numero == 1:
        return numero
    # Caso recursivo
    else:
        return numero + suma_recursiva(numero-1)

print(suma_recursiva(5))
# 15
print(suma_recursiva(10))
# 55
print(suma_recursiva(100))
# 5050

'''
mplementar una función para calcular la potencia dado dos números enteros, el primero representa la base y segundo el exponente.
'''

def potencia_recursiva(base, potencia):
    # Caso base
    if potencia == 1:
        return base
    # Caso recursivo 
    else:
        return base * potencia_recursiva(base, potencia-1)
    
print(potencia_recursiva(2, 3))
# 8
print(potencia_recursiva(4, 3))
# 64
print(potencia_recursiva(8, 9))
# 134217728
print(potencia_recursiva(14, 6))
# 7529536

'''
Desarrollar una función que permita convertir un número romano en un número decimal

def valor_correspondiente(romano, ind):
    romano_numero = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if ind > 0 and romano_numero[romano[ind]] > romano_numero[romano[ind - 1]]:
        return romano_numero[romano[ind]] - 2 * romano_numero[romano[ind -1 ]]
    else:
        return romano_numero[romano[ind]]

def pasar_romano_a_numero(romano, num = 0, ind=0):
    if ind == len(romano)-1:
        num += valor_correspondiente(romano, ind)
        return num
    else:
        num += valor_correspondiente(romano, ind)
        return pasar_romano_a_numero(romano, num, ind+1)
'''
def romoano_a_numero(romano, ind = 0, numero = 0):
    romano_numero = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if ind == len(romano):
        return numero
    else:
        if ind > 0 and romano_numero[romano[ind]] > romano_numero[romano[ind - 1]]:
            numero += romano_numero[romano[ind]] - 2 * romano_numero[romano[ind -1 ]]
            return romoano_a_numero(romano, ind+1, numero)
        else:
            numero += romano_numero[romano[ind]]
            return romoano_a_numero(romano, ind+1, numero)


print(romoano_a_numero('XIV'))
# 14
print(romoano_a_numero('XXXXVI'))
# 46
print(romoano_a_numero('DCCVIII'))
# 708
print(romoano_a_numero('CCCLXVI'))
# 366
print(romoano_a_numero('MMCML'))
# 2950

'''
Dada una secuencia de caracteres, obtener dicha secuencia invertida
'''

def invertir(palabra, palabraInvertidad = '', i = 1):
    if i == len(palabra):
        letra = palabra[-i]
        palabraInvertidad += letra
        return palabraInvertidad
    else:
        letra = palabra[-i]
        palabraInvertidad += letra
        return invertir(palabra, palabraInvertidad, i+1)

print(invertir('holis'))
# siloh
print(invertir('estuvo melo'))
# olem ovutse
print(invertir('Dada una secuencia de caracteres, obtener dicha secuencia invertida'))
# aditrevni aicneuces ahcid renetbo ,seretcarac ed aicneuces anu adaD
print(invertir('otorrinoralingologo'))
# ogolognilaronirroto
print(invertir('Johan Sebastian Robles Rincon'))
# nocniR selboR naitsabeS nahoJ

'''
Desarrollar un algoritmo que permita calcular la siguiente serie: (ver imagen)
'''

def h(numero, i=1):
    if i == numero:
        return 1/i
    else:
        return 1/i + h(numero, i+1)

print(h(7))
# 2.5928571428571425
print(h(45))
# 4.394948115551323
print(h(77))
# 4.927500538276902
print(h(190))
# 5.826869007613195
print(h(2))
# 1.5

'''
Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a sistema binario.
'''

class Entero_binario(object):
    def __init__(self, entero) -> None:
        self.entero = entero
    
    # Metodos:
    def convertir(self):
        entero = self.entero
        positivo = True
        binario = ''
        if entero < 0:
            positivo = False
            entero = abs(entero)
        elif entero == 0:
            binario = '0'
        def pasar_a_binario(entero, binario, positivo):
            if entero == 0:
                if positivo:
                    return binario[::-1]
                binario += '-'
                return binario[::-1]
            else:
                binario += str(entero % 2)
                return pasar_a_binario(entero//2, binario, positivo)
        
        return pasar_a_binario(entero, binario, positivo)

pasar15 = Entero_binario(15)
print(pasar15.convertir())
# 1111
pasar15346 = Entero_binario(15346)
print(pasar15346.convertir())
# 11101111110010
pasar9989 = Entero_binario(9989)
print(pasar9989.convertir())
# 10011100000101
pasar15negativo = Entero_binario(-15)
print(pasar15negativo.convertir())
# -1111
pasar0 = Entero_binario(0)
print(pasar0.convertir())
# 0

'''
Desarrollar un algoritmo que invierta un número entero sin convertirlo a cadena.
'''

def invertirEntero(num):
    if num == 0:
        return ''
    else:
        digito = round(((num/10) - (num//10)) * 10)
        return str(digito) + invertirEntero(num//10)

print(invertirEntero(255))
# 552
print(invertirEntero(12546123546))
# 64532164521
print(invertirEntero(919391))
# 193919
print(invertirEntero(2))
# 2
print(invertirEntero(123456789))
# 987654321

'''
Desarrollar el algoritmo de Euclides para calcular el máximo común divisor (MCD) de dos 
números entero
'''

def poder_seguir(num1, num2):
    primos = [2, 3, 5, 7, 9, 11, 13, 17, 23, 27]
    for primo in primos:
        if  num1 % primo == 0 and num2 % primo == 0:
            num1, num2 = num1 // primo, num2 // primo
            return num1, num2, primo
    if num1 == num2  and num1 > 27:
        num1, num2, primo = 1, 1, num1
    else:        
        num1, num2, primo = 1, 1, 1       
    return  num1, num2, primo

def euclidesMCD(num1, num2):
    num1, num2, primo = poder_seguir(num1, num2)
    if num1 == 1 or num2 == 1:
        return primo
    else:
        return primo * euclidesMCD(num1, num2)


print(euclidesMCD(24, 56))
# 8
print(euclidesMCD(16, 16))
# 16
print(euclidesMCD(12, 26))
# 2
print(euclidesMCD(5, 8))
# 1
print(euclidesMCD(31, 31))
# 31
print(euclidesMCD(59, 14))
# 1
print(euclidesMCD(30, 60))
# 30

'''
Desarrollar el algoritmo de Euclides para calcular también el mínimo común múltiplo (MCM) 
de dos número entero.
'''

def poder_seguir(num1, num2):
    primos = [2, 3, 5, 7, 9, 11, 13, 17, 23, 27]
    for primo in primos:
        if num1 % primo == 0 or num2 % primo == 0:
            if num1 % primo == 0:
                num1 = num1 // primo
            if num2 % primo == 0:
                num2 = num2 // primo    

            return num1, num2, primo
    if num1 != 1 or num2 != 1:
        if num1 > 27:
            primo = num1
            num1 = 1
        if num2 > 27:
            primo = num2
            num2 = 1
        return num1, num2, primo


def euclidesMCM(num1, num2):
    num1, num2, primo = poder_seguir(num1, num2)
    if num1 == 1 and num2 == 1:
        return primo
    else:
        return primo * euclidesMCM(num1, num2)


print(euclidesMCM(12, 28))
# 84
print(euclidesMCM(30, 24))
# 120
print(euclidesMCM(12, 7))
# 84
print(euclidesMCM(1343, 23422))
# 398174
print(euclidesMCM(123, 28))
# 3444
print(euclidesMCM(8, 90))
# 360

'''
Desarrollar un algoritmo que permita realizar la suma de los dígitos de un número entero, no 
se puede convertir el número a cadena.
'''
def sumaDigitos(num):
    if num == 0:
        return 0
    else:
        return (num % 10) + sumaDigitos(num // 10)

print(sumaDigitos(456))
# 15
print(sumaDigitos(12345))
# 15
print(sumaDigitos(88888))
# 40
print(sumaDigitos(2354625472))
# 40
print(sumaDigitos(123456789))
# 45

'''
Escribir una función recursiva que permita mostrar los valores de un vector de atrás hacia adelante.
'''

def mostrar_lista_alevez(lista, i=1):
    if i == len(lista):
        return str(lista[-i]) 
    else:
        return str(lista[-i]) + ' ' + mostrar_lista_alevez(lista, i+1)

print(mostrar_lista_alevez([1, 2, 3, 4, 5]))
# 5 4 3 2 1
print(mostrar_lista_alevez([3, 5, 1, 2, 5, 2, 9, 9]))
# 9 9 2 5 2 1 5 3
print(mostrar_lista_alevez([5, 8, 2, 1, 9, 9, 9]))
# 9 9 9 1 2 8 5
print(mostrar_lista_alevez([1, 4, 6, 6, 6, 999]))
# 999 6 6 6 4 1

'''
Implementar una función recursiva que permita recorrer una matriz y mostrar sus valores.
'''

def recorrer_lista(lista, i = 0):
    if  i == len(lista)-1:
        print(lista[i])
        return str(lista[i])
    else:
        print(lista[i])
        return str(lista[i]) + ' ' + recorrer_lista(lista, i+1)

print(recorrer_lista([1, 2, 3, 4, 5]))
# 1
# 2
# 3
# 4
# 5
# 1 2 3 4 5

'''
Dada la siguiente definición de sucesión recursiva, realizar una función recursiva que permita 
calcular el valor de un determinado número en dicha sucesión (ver foto)
'''

def funcion(n):
    if n == 1:
        return 2
    else:
        return n + 1/(funcion(n-1))

print(funcion(8))
# 8.139635118379879
print(funcion(2))
# 2.5
print(funcion(25))
# 25.04159146809772
print(funcion(100))
# 100.0100999691912
print(funcion(1))
# 2


'''
Desarrollar un algoritmo que permita implementar la búsqueda secuencial con centinela de 
manera recursiva, y permita determinar si un valor dado está o no en dicha lista.
'''

def recursive_find_secuencial(lista, valor, i = 0):
    # Este ejercicio tiene dos caso bases
    if i == len(lista):
        return False
    elif lista[i] == valor:
        return True
    else:
        return recursive_find_secuencial(lista, valor, i+1)
numeros = [2, 5, 2, 7, 12, 545, 68, 123,  3, 64, 23,  100]

print(recursive_find_secuencial(numeros, 123))
# True
print(recursive_find_secuencial(numeros, 3))
# True
print(recursive_find_secuencial(numeros, 2))
# True
print(recursive_find_secuencial(numeros, 100))
# True
print(recursive_find_secuencial(numeros, 12323))
# False
print(recursive_find_secuencial(numeros, 13))
# False
print('_________________')
'''
Dada una lista de valores ordenadas, desarrollar un algoritmo que modifique el método de 
búsqueda binaria para que funcione de forma recursiva, y permita determinar si un valor dado 
está o no en dicha lista.
'''
numeros_ordenados = [2, 4, 7, 12, 13, 32, 45, 79, 102, 150]

def recursive_binary_search(lista, valor):
    if not lista:
        return False     
    punto_medio = (len(lista)) // 2
    if lista[punto_medio] == valor:
        return True

    elif lista[punto_medio] > valor:
        return recursive_binary_search(lista[:punto_medio], valor)
    elif lista[punto_medio] < valor:
        return recursive_binary_search(lista[punto_medio+1:], valor)

print(recursive_binary_search(numeros_ordenados, 7))
# True
print(recursive_binary_search(numeros_ordenados, 2))
# True
print(recursive_binary_search(numeros_ordenados, 150))
# True
print(recursive_binary_search(numeros_ordenados, 13))
# True
print(recursive_binary_search(numeros_ordenados, 79))
# True
print(recursive_binary_search(numeros_ordenados, 78))
# False
print(recursive_binary_search(numeros_ordenados, 1))
# False
print(recursive_binary_search(numeros_ordenados, 9999))
# False
print(recursive_binary_search(numeros_ordenados, 33))
# False

'''
El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u 
otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos 
objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con 
ayuda de la fuerza” realizar las siguientes actividades:

a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no 
queden más objetos en la mochila;

b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;

c. Utilizar un vector para representar la mochila.

'''



def usar_la_fuerza(mochila, objetos_sacados = []):
    if not mochila:
        return 'No se encontro el Sable de Luz. Todos los objetos fueron sacados: [' + ' '.join(objetos_sacados) + ']'
    elif mochila[0] == 'Sable de Luz':
        return 'Se encontro el Sable de Luz, se tuvo que sacar un total de ' + str(len(objetos_sacados)) + ' objetos: [' + ' '.join(objetos_sacados) + ']'    
    
    else:
        print(f'Objeto sacado: {mochila[0]}')
        objetos_sacados.append(mochila[0])
        return usar_la_fuerza(mochila[1:], objetos_sacados)

mochila = ['Capa', 'LLave', 'Zapatos', 'Calculadora', 'Almuerzo', 'Sable de Luz', 'Celular', 'Teclado']
print(usar_la_fuerza(mochila))
# Objeto sacado: Capa
# Objeto sacado: LLave
# Objeto sacado: Zapatos
# Objeto sacado: Calculadora
# Objeto sacado: Almuerzo
# Se encontro el Sable de Luz, se tuvo que sacar un total de 5 objetos: [Capa LLave Zapatos Calculadora Almuerzo]

mochila = ['Capa', 'LLave', 'Zapatos', 'Calculadora', 'Almuerzo', 'Celular', 'Teclado']
print(usar_la_fuerza(mochila))
# Objeto sacado: Capa
# Objeto sacado: LLave
# Objeto sacado: Zapatos
# Objeto sacado: Calculadora
# Objeto sacado: Almuerzo
# Objeto sacado: Celular
# Objeto sacado: Teclado
# No se encontro el Sable de Luz. Todos los objetos fueron sacados: [Capa LLave Zapatos Calculadora Almuerzo Capa LLave Zapatos Calculadora Almuerzo Celular Teclado]

'''
Dada la siguiente definición de sucesión recursiva, realizar una función recursiva que permita 
calcular el valor de un determinado número en dicha sucesión (ver foto).
'''

def f(n):
    if n == 1:
        return 3
    else:
        return f(n-1) + 2*n

print(f(5))
# 31
print(f(1))
# 3
print(f(50))
# 2551
print(f(100))
# 10101
print(f(12))
# 157



'''
En el momento de la creación del mundo, los sacerdotes del templo de Brahma recibieron una 
plataforma de bronce sobre la cual había tres agujas de diamante. En la primera aguja estaban 
apilados setenta y cuatro discos de oro, cada una ligeramente menor que la que estaba debajo. 
A los sacerdotes se les encomendó la tarea de pasarlos todos desde la primera aguja a la tercera, 
con dos condiciones, solo puede moverse un disco a la vez, y ningún disco podrá ponerse encima de otro más pequeño. 
Se dijo a los sacerdotes que, cuando hubieran terminado de mover los discos, llegaría el fin del mundo. Resolver este 
problema de la Torre de Hanói.
'''
# # meh
# def resolverHanoiTower(n, origen,  aux, destino, movimientos = []):
#     if n == 1:
#         print('Mover disco de ' + origen + ' a ' +  destino)
#     else:
#         resolverHanoiTower(n-1, origen, destino, aux, movimientos+1)
#         print('Mover disco de ' + origen + ' a ' +  destino)
#         resolverHanoiTower(n-1, aux, origen, destino, movimientos+1)

# resolverHanoiTower(int(input('Dame el total de discos: ')), 'A', 'B', 'C')


'''
Un palíndromo es una aristra de caracteres que se lee igual de izquierda a derecha que de derecha a izquierda ―por ejemplo anilina. 
Esto significa que el primer carácter es igual al último, el segundo al penúltimo, el tercero al antepenúltimo, etc. Desarrolle un 
método al que se le pasa por parámetro una aristra devuelva verdadero o falso, según sea palíndromo, o no.


def determonar_arista(arista, arista_alrevez = '',  i = 1):
    if len(arista_alrevez) == len(arista):
        return (arista == arista_alrevez)
    else:
        arista_alrevez += arista[-i]
        return determonar_arista(arista, arista_alrevez, i+1)

print(determonar_arista('anilina'))
# True
print(determonar_arista('pan'))
# False
print(determonar_arista('otooto'))
# True
print(determonar_arista('werew'))
# True
print(determonar_arista('gaseosa'))
# False
'''


'''
Un palíndromo es una aristra de caracteres que se lee igual de izquierda a derecha que de derecha a izquierda ―por ejemplo anilina. 
Esto significa que el primer carácter es igual al último, el segundo al penúltimo, el tercero al antepenúltimo, etc. Desarrolle un 
método al que se le pasa por parámetro una aristra devuelva verdadero o falso, según sea palíndromo, o no.
'''
# funcion que recibe como parametro la letra
def verificar_palindromo(palabra):
    # otra funcion, esta sera nuestra funcion recursiva
    def verificacion(palbra, i = 0, k = len(palabra)-1):
        # caso base: i i es igual o mayor a k entonces significa que todas la letras de atras hacia adelante y todas las letras de adelante hacia atras sn iguales
        # retornamos True
        if i >= k:
            return True
        # condicionales para verificas si i o k son espacios (los espacios no cuentan), entonces llamamos otra vezx la funcion con el valor que le sigue a estas
        elif palbra[i] == ' ':
            return verificacion(palbra, i+1, k)
        elif palbra[k] == ' ':
            return verificacion(palbra, i, k-1)
        # nuestro condicional imprtante, si la letra i y la letra k son iguales, llamamos otra vez la fucion con los el valor siguiente de i y k
        elif palbra[i] == palbra[k]:
            return verificacion(palbra, i+1, k-1)
       # este es como nuetro otro caso base, si le valor correspondinte de i y k no son iguales, entonces la palabra oo frase no es palindorma
    #    retornamos False.
        else:
            return False 
    return verificacion(palabra) 

print(verificar_palindromo('se verlas al reves'))
# True
print(verificar_palindromo('anita'))
# False
print(verificar_palindromo('atale demoniaco cain o me delata')) 
# True
print(verificar_palindromo('a mi me mima')) 
# True
print(verificar_palindromo('perro')) 
# False
print(verificar_palindromo('anilina'))
# True

