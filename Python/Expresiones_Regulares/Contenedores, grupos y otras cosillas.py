import re

'''
( )     - Grupos
[]      - Encuentra caracteres en corchetes
[^ ]    - Encuentra caracteres que no están dentro de corchetes
|       - Condicional O

\b      - Limite de palabra
\B      - No limite de palabra

\1      - Referencias
'''
# -----USO DE PARENTESIS-----
# Con los () podemos agarra aquellos caracteres que estan dentro de una cadena de caracteres que cumple una condicion, por ejemplo 
# los primeros 3 numeros de una cadena que tiene tres en tres numeros separados por una -
texto_de_prueba = '''Hola Mundo.
Me gusta Python!!!!!
Mi primer numero de la suerte es 987-654-321
Mi segundo numero de la suerte es 876-543-210
Mi tercero numero de la suerte es 765-432-100
Mi cuarto numero de la suerte es 123-456-123-123-456
'''
print(re.findall(r'\d{3}-\d{3}-\d{3}', texto_de_prueba))
# ['987-654-321', '876-543-210', '765-432-100', '123-456-123']

# Aplicando los () seria:
print(re.findall(r'(\d{3})-\d{3}-\d{3}', texto_de_prueba))
# ['987', '876', '765', '123'] notamos que nos muestra todos los numeros de 3 digitos que esten dentro una cadena de numeros separado 
# por un - y que sean los primeros (es decir que este dentro de los parentesis)

print(re.findall(r'\d{3}-(\d{3})-\d{3}', texto_de_prueba))
# ['654', '543', '432', '456']
# -----USO DE LOS CORCHETES-----
# basicamente con los [] podemos seleccionar todas los caracteres que cumplan la condicion o condiciones que estan adentro de los corchetes

# Podemos usar los corchetes para que me retorne todos los caracteres que sea de 0-9
print(re.findall(r'[0-9]', texto_de_prueba))
# ['9', '8', '7', '6', '5', '4', '3', '2', '1', '8', '7', '6', '5', '4', '3', '2', '1', '0', '7', '6', '5', '4', '3', '2', '1', '0', '0', '1', '2', '3', '4', '5', '6', '1', '2', '3', '1', '2', '3', '4', '5', '6']

# Tambien si queremos que umpla mas condiciones como que acepten letras del a-z o A-Z
print(re.findall(r'[0-9a-z]', texto_de_prueba))
# ['o', 'l', 'a', 'u', 'n', 'd', 'o', 'e', 'g', 'u', 's', 't', 'a', 'y', 't', 'h', 'o', 'n', 'i', 'p', 'r', 'i', 'm', 'e', 'r', 'n', 'u', 'm', 'e', 'r', 'o', 'd', 'e', 'l', 'a', 's', 'u', 'e', 'r', 't', 'e', 'e', 's', '9', '8', '7', '6', '5', '4', '3', '2', '1', 'i', 's', 'e', 'g', 'u', 'n', 'd', 'o', 'n', 'u', 'm', 'e', 'r', 
# 'o', 'd', 'e', 'l', 'a', 's', 'u', 'e', 'r', 't', 'e', 'e', 's', '8', '7', '6', '5', '4', '3', '2', '1', '0', 'i', 't', 'e', 'r', 'c', 'e', 'r', 'o', 'n', 'u', 'm', 'e', 'r', 'o', 'd', 'e', 'l', 'a', 's', 'u', 'e', 'r', 't', 'e', 'e', 's', '7', '6', '5', '4', '3', '2', '1', '0', '0', 'i', 'c', 'u', 'a', 'r', 't', 'o', 'n', 'u', 'm', 'e', 'r', 'o', 'd', 'e', 'l', 'a', 's', 'u', 'e', 'r', 't', 'e', 'e', 's', '1', '2', '3', '4', '5', '6', '1', '2', '3', '1', '2', '3', '4', '5', '6']

print(re.findall(r'[0-9a-zA-Z]', texto_de_prueba))
# ['H', 'o', 'l', 'a', 'M', 'u', 'n', 'd', 'o', 'M', 'e', 'g', 'u', 's', 't', 'a', 'P', 'y', 't', 'h', 'o', 'n', 'M', 'i', 'p', 'r', 'i', 'm', 'e', 'r', 'n', 'u', 'm', 'e', 'r', 'o', 'd', 'e', 'l', 'a', 's', 'u', 'e', 'r', 't', 'e', 'e', 's', '9', '8', '7', '6', '5', '4', '3', '2', '1', 'M', 'i', 's', 'e', 'g', 'u', 'n', 'd', 
# 'o', 'n', 'u', 'm', 'e', 'r', 'o', 'd', 'e', 'l', 'a', 's', 'u', 'e', 'r', 't', 'e', 'e', 's', '8', '7', '6', '5', '4', '3', '2', '1', '0', 'M', 'i', 't', 'e', 'r', 'c', 'e', 'r', 'o', 'n', 'u', 'm', 'e', 'r', 'o', 'd', 'e', 'l', 'a', 's', 'u', 'e', 'r', 't', 'e', 'e', 's', '7', '6', '5', '4', '3', '2', '1', '0', '0', 'M', 'i', 'c', 'u', 'a', 'r', 't', 'o', 'n', 'u', 'm', 'e', 'r', 'o', 'd', 'e', 'l', 'a', 's', 'u', 'e', 'r', 't', 'e', 'e', 's', '1', '2', '3', '4', '5', '6', '1', '2', '3', '1', '2', '3', '4', '5', '6']

# Otra forma de ver esto es como los |, pero esto los corchetes no lo necesitan (aunque si los () por si queremos hacer esto con esas herramientas)
print(re.findall(r'[0-9 | a-z]', texto_de_prueba))
# ['o', 'l', 'a', ' ', 'u', 'n', 'd', 'o', 'e', ' ', 'g', 'u', 's', 't', 'a', ' ', 'y', 't', 'h', 'o', 'n', 'i', ' ', 'p', 'r', 'i', 'm', 'e', 'r', ' ', 'n', 'u', 'm', 'e', 'r', 'o', ' ', 'd', 'e', ' ', 'l', 'a', ' ', 's', 'u', 'e', 'r', 't', 'e', ' ', 'e', 's', ' ', '9', '8', '7', '6', '5', '4', '3', '2', '1', 'i', ' ', 's', 
# 'e', 'g', 'u', 'n', 'd', 'o', ' ', 'n', 'u', 'm', 'e', 'r', 'o', ' ', 'd', 'e', ' ', 'l', 'a', ' ', 's', 'u', 'e', 'r', 't', 'e', ' ', 'e', 's', ' ', '8', '7', '6', '5', '4', '3', '2', '1', '0', 'i', ' ', 't', 'e', 'r', 'c', 'e', 'r', 'o', ' ', 'n', 'u', 'm', 'e', 'r', 'o', ' ', 'd', 'e', ' ', 'l', 'a', ' ', 's', 'u', 'e', 'r', 't', 'e', ' ', 'e', 's', ' ', '7', '6', '5', '4', '3', '2', '1', '0', '0', 'i', ' ', 'c', 'u', 'a', 'r', 't', 'o', ' ', 'n', 'u', 'm', 'e', 'r', 'o', ' ', 'd', 'e', ' ', 'l', 'a', ' ', 's', 'u', 'e', 'r', 't', 'e', ' ', 'e', 's', ' ', '1', '2', '3', '4', '5', '6', '1', '2', '3', '1', '2', '3', '4', '5', '6']

# Por ultimo, en este temas de los corchete, pordemos usar algo parecido al not de un condicional if, es decir, que agarramos todas aquellas 
# caracteres que NO cumplan las condiciones de los []
print(re.findall(r'[^0-9a-z]', texto_de_prueba))
# ['H', ' ', 'M', '.', '\n', 'M', ' ', ' ', 'P', '!', '!', '!', '!', '!', '\n', 'M', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '-', '\n', 'M', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '-', '\n', 'M', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '-', '\n', 'M', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '-', '-', '-', '\n']
# Notar que retornamos los caracteres que NO cumplen las condiciones de los []



# Por ultimos tenemos los \b y \B para, el primero es  para printear los espacios que hay ('') entre letras de diferentes fromas y 
# en la segunda para printear los espacios que hay entre caracteres de la misma forma (o eso creo)

# Y tambien teneremos las referencias \1 que lo que hacen es seleccionar al siguiente  grupo de caracteres que 
# cumplen con la condicion dada
texto_de_prueba = '''Hola Mundo.
Me gusta Python!!!!!
Mi primer numero de la suerte es 987-654-321
Mi segundo numero de la suerte es 876-543-210
123-123-123-123-123-123-123
Mi tercero numero de la suerte es 765-432-100
Mi cuarto numero de la suerte es 123-456-123-123-456
'''

print(re.findall(r'(123-)\1', texto_de_prueba))
['123-', '123-', '123-', '123-']