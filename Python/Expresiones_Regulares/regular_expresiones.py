'''
Basicamente las expresiones regulares se usan para sacar informacion de un string con base los caracteres que esta en esta.
pagina que nmos ayudara a hacer nustras expresiones regulares
https://regex101.com/
'''
# Necesitamos importar el modulo re para trabajr con expresiones regulares
import re

texto_de_prueba = '''Hola Mundo.
Me gusta Python!!!!!
Mi primer numero de la suerte es 987-654-321
Mi segundo numero de la suerte es 876-543-210
Mi tercero numero de la suerte es 765-432-100
Mi cuarto numero de la suerte es 123-456-123-123-456
'''

'''
Tenemos varias tipos de caracteres con los que podemos trabajar algunos son:
\d      - Digitos (0-9)
\D      - No digitos (0-9)
\w      - Caracter de palabra (a-z, A-Z, 0-9, _)
\W      - No caracter de palabra
\s      - Espacio en blanco (espacio, tab, nueva linea)
\S      - No espacio en blanco (espacio, tab, nueva linea)
.       - Cualquier caracter excepto nueva linea (codicioso - greedy)
\       - Cancela caracteres especiales

        Notar que cada unos de estos tipo de caracter tiene su contraparte que se identifica con la misma letra pero en mayusculas

De Comprobacion: Con esto lo que hacemos es comprobar si el string o cadena de caracteres empieza o termina con un caracxter o cadenas de caracteres dada
^       - Inicio de una cadena de caracteres (string)
$       - Fin de una cadena de caracteres
Estos e puede combinar por ejemplo con flags=re.M para tomoar en cuewnta solo linea por linea (es decir \n por \n) y no todo el string en general
'''

texto_de_prueba = '''Hola Mundo.
Me gusta Python!!!!!
Mi primer numero de la suerte es 987-654-321
Mi segundo numero de la suerte es 876-543-210
Mi tercero numero de la suerte es 765-432-100
Mi cuarto numero de la suerte es 123-456-123-123-456
'''

# si queremos encontrar el primer caracter que especifiquemos usamos re.search(r'tipo_de_caracter', string)
print(re.search(r'\d', texto_de_prueba))
# <re.Match object; span=(66, 67), match='9'>
# donde span es la posicion del caracter y match es el caracter (primer caracter que buscamos) encontrado

# o bien si queremos encontrar todos los caracteres de un tipo usamos re.findall(r'tipo_de_caracter', string)
print(re.findall(r'\d', texto_de_prueba))
# ['9', '8', '7', '6', '5', '4', '3', '2', '1', '8', '7', '6', '5', '4', '3', '2', '1', '0', '7', '6', '5', '4', '3', '2', '1', '0', '0', '1', '2', '3', '4', '5', '6', '1', '2', '3', '1', '2', '3', '4', '5', '6']
# Notar que nos imprimio todos los numeros que esta en el string

# Ejemplos:
# para todos los caracter que no sea caracteres numericos: \D
print(re.findall(r'\D', texto_de_prueba))
# ['H', 'o', 'l', 'a', ' ', 'M', 'u', 'n', 'd', 'o', '.', '\n', 'M', 'e', ' ', 'g', 'u', 's', 't', 'a', ' ', 'P', 'y', 't', 'h', 'o', 'n', '!', '!', '!', '!', '!', '\n', 'M', 'i', ' ', 'p', 'r', 'i', 'm', 'e', 'r', ' ', 'n', 'u', 'm', 'e', 'r', 'o', ' ', 'd', 'e', ' ', 'l', 'a', ' ', 's', 'u', 'e', 'r', 't', 'e', ' ', 'e', 's', ' ', '-', '-', '\n', 'M', 'i', ' ', 's', 'e', 'g', 'u', 'n', 'd', 'o', ' ', 'n', 'u', 'm', 'e', 'r', 'o', ' ', 'd', 'e', ' ', 'l', 'a', ' ', 's', 'u', 'e', 'r', 
# 't', 'e', ' ', 'e', 's', ' ', '-', '-', '\n', 'M', 'i', ' ', 't', 'e', 'r', 'c', 'e', 'r', 'o', ' ', 'n', 'u', 'm', 'e', 'r', 'o', ' ', 'd', 'e', ' ', 'l', 'a', ' 
# ', 's', 'u', 'e', 'r', 't', 'e', ' ', 'e', 's', ' ', '-', '-', '\n', 'M', 'i', ' ', 'c', 'u', 'a', 'r', 't', 'o', ' ', 'n', 'u', 'm', 'e', 'r', 'o', ' ', 'd', 'e', ' ', 'l', 'a', ' ', 's', 'u', 'e', 'r', 't', 'e', ' ', 'e', 's', ' ', '-', '-', '-', '-', '\n']

# para caracteres de palabra \w (este incluye a-z, A-Z, 0-9, _)
print(re.findall(r'\w', texto_de_prueba))
# ['H', 'o', 'l', 'a', 'M', 'u', 'n', 'd', 'o', 'M', 'e', 'g', 'u', 's', 't', 'a', 'P', 'y', 't', 'h', 'o', 'n', 'M', 'i', 'p', 'r', 'i', 'm', 'e', 'r', 'n', 'u', 'm', 'e', 'r', 'o', 'd', 'e', 'l', 'a', 's', 'u', 'e', 'r', 't', 'e', 'e', 's', '9', '8', '7', '6', '5', '4', '3', '2', '1', 'M', 'i', 's', 'e', 'g', 'u', 'n', 'd', 
# 'o', 'n', 'u', 'm', 'e', 'r', 'o', 'd', 'e', 'l', 'a', 's', 'u', 'e', 'r', 't', 'e', 'e', 's', '8', '7', '6', '5', '4', '3', '2', '1', '0', 'M', 'i', 't', 'e', 'r', 'c', 'e', 'r', 'o', 'n', 'u', 'm', 'e', 'r', 'o', 'd', 'e', 'l', 'a', 's', 'u', 'e', 'r', 't', 'e', 'e', 's', '7', '6', '5', '4', '3', '2', '1', '0', '0', 'M', 'i', 'c', 'u', 'a', 'r', 't', 'o', 'n', 'u', 'm', 'e', 'r', 'o', 'd', 'e', 'l', 'a', 's', 'u', 'e', 'r', 't', 'e', 'e', 's', '1', '2', '3', '4', '5', '6', '1', '2', '3', '1', '2', '3', '4', '5', '6']
# Notar que con este juego de caracteres no admite signos despeciales como %, !, ¿,?, etc.
# Ahora con \W
print(re.findall(r'\W', texto_de_prueba))
# [' ', '.', '\n', ' ', ' ', '!', '!', '!', '!', '!', '\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '-', '\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '-', '\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '-', '\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '-', '-', '-', '\n']



# Usando los metodos de comprobacion: Con esto lo que hacemos es comprobar si el string o cadena de caracteres empieza o termina 
# con un caracxter o cadenas de caracteres dada
# Comprobar si el string empieza con un caracter o cadena dada:
print(re.search(r'^Hola', texto_de_prueba))
# <re.Match object; span=(0, 4), match='Hola'>
print(re.search(r'^holaaa', texto_de_prueba))
# None



# Tambien podemos comprobar si la cadena termina en una cadena de cadena de careccteres dada
print(re.search(r'456$', texto_de_prueba))
# <re.Match object; span=(219, 222), match='456'>
print(re.search(r'Mundo.$', texto_de_prueba))
# None

# Ahora notemos que podemos decirle a python que queremos trabajar linea por linea y no todo el string en genral, y asi podemos comprobar si alguna
# linea comienza o termina con una cadena de caracteres dada, esto lo hacemos pasando el siguiente parametro flags=re.M
# Para el comienzo:
print(re.search(r'^Mi tercero', texto_de_prueba, flags=re.M))
# <re.Match object; span=(124, 134), match='Mi tercero'> Notar que ahora verifica si alguna de las lineas comienza con la cadena dada
print(re.search(r'^Mi pruebaxD', texto_de_prueba, flags=re.M))
# None

# Para el final
print(re.search(r'210$', texto_de_prueba, flags=re.M))
# <re.Match object; span=(120, 123), match='210'>

print(re.search(r'numero random$', texto_de_prueba, flags=re.M))
# None

# Por ultimo si queremos saber si una linea de codigo empieza con una letra 'c' y termina en otra 'o', hacemos los siguiente
# (redcordemos que con . hacemos referencia a culaquier caracter siempre y cuando no sea un espacio)
texto_de_prueba = '''Hola Mundo.
Me gusta Python!!!!!
Mi primer numero de la suerte es 987-654-321
Mi segundo numero de la suerte es 876-543-210
Mi tercero numero de la suerte es 765-432-100
Mi cuarto numero de la suerte es 123-456-123-123-456
carballo jeeejjejej este es una prueba.
'''
print(re.search(r'^c.+o', texto_de_prueba, flags=re.M))
# <re.Match object; span=(223, 231), match='carballo'>
# con + lo que estamos haciendo es diciendo a python que agarre todas las letras hasta la una condicion dada condicion
# A esto se le conoce como metodos codiciosas y perezosas, basicamente un metodo codicioso es aquel que quiere agarra todos los caracteres que
# se les pide (por ejemplo el + o el *) y uno perezoso es aquel que solo agarra ninguno o uno si llega a aver el caracter que se le pide (por ejemplo el ?)
# Estos metodos lo profundizaremos en otro modulo.

# Expresion regular para validar emails result = re.search(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+[.][a-zA-Z]{1,3}$', s)

'''
Hacer una validacion de cartas de creditos, que tienen las siguientes condiciones:
► It must start with a 4, 5 or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits.
'''

import re
# N es el conrador de liena, crads donde se alamcenaran las lineas y reult la lista que almacenara los resultados
n = int(input())
cards = [input() for _ in range(n)]
for card in cards:
    aux_card = card.replace('-','')
    # Verificamos si el auxiliar de cards que sera los mismos valores de cards pero sin los - NO tiene numeros que se repiten
    if not re.search(r'(.)\1{3}', aux_card) and len(aux_card) == 16:
        # Si es asi entonces pasamos a verificar ya en card las otras condiciones:
        if re.search(r'^[456]\d{3}(-?\d{4})+$', card):
            print('Valid')
        else:
            print('Invalid')    
    else:
        print('Invalid')
# Con (.)\1 verificamos si hay dos caracteres que se repiten consecutivamente y con (.)\1{n} o (.).*\1{n} verificamos si hay n caractes que se repiten consecutivamente }

# Para validar un numero romano usamos la expresion regular ^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$, en donde basicamente
# estamos pidendo que el numero romano empiece en  M (mil) si hay o no, siempre y cuando no sea mas de 3 Ms, despues viene todas los posible numeros
# romanos que vienen despues de M (MMCM -> 2900, MCD -> 1400, etc.), notar que el | hacer referencia como al OR en un lenguan de programacion.
# Luego de esto, aplica lo mismo para validar todas los posibles nuemros que pueden a ver despues de lo validado anteriormente (MCMXX -> 1920).
# y por ultimo e igualmente como lo anterior, validamos todas las posibles soluciones que vienen depsue y asegurandonos que terminen en estas (MMMCCX111 -> 3213).
# https://stackoverflow.com/questions/267399/how-do-you-match-only-valid-roman-numerals-with-a-regular-expression

import re
from tokenize import group
print(re.findall(r'(?=aa)', 'aaadaa'))