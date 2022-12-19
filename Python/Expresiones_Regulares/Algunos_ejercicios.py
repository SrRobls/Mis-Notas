import re

'''
Encontrar los diferentes signos de puntuacion de un string.
'''
texto =  '''
Los molinos de viento en los que Don Quijote sólo veía «desaforados gigantes» corresponden, sin duda, a la postal más reconocible de La Mancha.
 Más que un icono que representa a la madre de todas las quijotadas, la silueta de los molinos con sus aspas cercenando la llanura manchega es 
 también un objetivo de muchos viajeros que se dirigen en busca de los tópicos clásicos de una región que llevan imaginando toda la vida. 
 Y en ningún modo se marchan decepcionados. Al contrario, asomarse a los distintos balcones de La Mancha que cuentan con su colección de 
 molinos de viento es una manera muy loable de comenzar un flirteo con aquello que nos mostró Miguel de Cervantes en la novela más universal 
 escrita en castellano.
'''
print(re.findall(r'[^\w\s]', texto))
# ['«', '»', ',', ',', '.', ',', '.', '.', ',', '.']
# \s es para los espacios en blanco (espacio, tab, nueva linea) y \w para los caracteres alphanumericos 

'''
Validar fechas en formato dia-mes-año
22-12-2002 -> True
02-02-2122 -> True
2021-04-1 -> False/None
'''

print(re.search(r'[0-9]{2}-[0-9]{2}-[0-9]{4}', '22-12-2002'))
# <re.Match object; span=(0, 10), match='22-12-2002'>
print(re.search(r'[0-9]{2}-[0-9]{2}-[0-9]{4}', '02-02-2122'))
# <re.Match object; span=(0, 10), match='02-02-2122'>
print(re.search(r'[0-9]{2}-[0-9]{2}-[0-9]{4}', '2021-04-1'))
# None

