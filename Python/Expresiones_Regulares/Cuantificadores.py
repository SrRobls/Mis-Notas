import re

'''
Cuantificadores:
*       - 0 o más (codicioso - greedy)
+       - 1 o más (codicioso - greedy)
?       - 0 or 1 (perezoso - lazy)
{3}     - Numero exacto
{n,}    - Numero n+
{3,4}   - Rango de números (Minimo, Maximo)
'''

# estos lo podemos usar para agrupar mo agarrar mas caracteres de un carater dado, pedri un numero exacto de esos caracteres o un rango dado
texto_de_prueba = '''Hola Mundo.
Me gusta Python!!!!!
Mi primer numero de la suerte es 987-654-321
Mi segundo numero de la suerte es 876-543-210
Mi tercero numero de la suerte es 765-432-100
Mi cuarto numero de la suerte es 123-456-123-123-456
''' 
# Podemos usar + o * para que agarre todos los caracteres siguientes que sean el mismo que el anterior del + o *
print(re.search(r'Python!+', texto_de_prueba))
# <re.Match object; span=(21, 32), match='Python!!!!!'>
print(re.search(r'Python!*', texto_de_prueba))
# <re.Match object; span=(21, 32), match='Python!!!!!'>

# Podemos decir que solo agarre tambien mas de 0 o 1 un caracter, si hay, del caracter inmediatamente  anterior del ?
print(re.search(r'Python!?', texto_de_prueba))
# <re.Match object; span=(21, 28), match='Python!'>

# Como tambien podemos definir que agarre una cantidad exacta de carecteres o un rango en si
print(re.search(r'Python!{2}', texto_de_prueba))
# <re.Match object; span=(21, 30), match='Python!!'>
print(re.search(r'Python!{5}', texto_de_prueba))
# <re.Match object; span=(21, 32), match='Python!!!!!'>
# Notar que se tomas los ! igual a la cantidade de {numnero}. pero si colocamos un numero de tal fomra que no cumpla la condicion entonces nos retorna none
print(re.search(r'Python!{5900}', texto_de_prueba))
# None

# Si lo trabajamos con los rangos
print(re.search(r'Python!{2,}', texto_de_prueba))
# <re.Match object; span=(21, 32), match='Python!!!!!'> Aca decimos que agarre 2 o mas
print(re.search(r'Python!{,3}', texto_de_prueba))
# <re.Match object; span=(21, 30), match='Python!!!'> Aca decimos que agarre 3 o menos 

print(re.search(r'Python!{1,4}', texto_de_prueba))
# <re.Match object; span=(21, 31), match='Python!!!!'> y aca decimos que agarre del 1 a 4