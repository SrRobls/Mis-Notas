import re

s = 'Una nota de csev@umich.edu a cwen@iupui.edu sobre una reunión @ 2PM'
print(re.findall(r'\S+@\S+', s))
# Recordemos que \S hace referencia a los caracteres que sean diferente a espacioas " "
# Traduciendo la expresión regular al castellano, estamos buscando subcadenas que
# tengan al menos un carácter que no sea un espacio, seguido de una @, seguido de al
# menos un carácter que no sea un espacio. La expresión \S+ coincidirá con cuantos
# caracteres distintos de un espacio sea posible.

# La expresión regular retornaría dos coincidencias (csev@umich.edu y cwen@iupui.edu),
# pero no coincidiría con la cadena “@2PM” porque no hay caracteres que no sean
# espacios en blanco antes del signo @.

string = """From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
Return-Path: <postmaster@collab.sakaiproject.org>
for <source@collab.sakaiproject.org>;
Received: (from apache@localhost)
Author: stephen.marquard@uct.ac.za"""

print(re.findall(r'[a-zA-Z0-9]\S+@\S+[a-zA-Z0-9]', string))
# ['stephen.marquard@uct.ac.za', 'postmaster@collab.sakaiproject.org', 'source@collab.sakaiproject.org', 'apache@localhost', 'stephen.marquard@uct.ac.za']
# Lo que estamos pidiendo es que si o si el primer caracter de la subcadena sea de tipo [a-zA-Z0-9] asi restrintgimos los caracteres especiales como '>', '<', etc.
# luego le pedimos que agarre todos los caracteres diferente de  ' ' hasta a un @, luego lo mismo, que agarre todos los caracter diferentes a un ' '
# pero siempre y cuando el esos caracteres sean de tipo [a-zA-Z0-9] asi, de igual manera, nos aseguramos que no termine en un caracter especial

# Lo que hacemos con los corchetes [] es que agarre uno o mascaracteres que cumplan eso

s = """Hola estoes una tecto rando para probar esta joas
8-DSPAM-Confidence: 0.8475 adhikbfd
habia una vez un pollitp que respiraba por el ano 123-DSPAM-Confidence: 9.235
que se sento y sem murio"""

print(re.findall(r'\d+-.+: [0-9.]+', s))
# ['8-DSPAM-Confidence: 0.8475', '123-DSPAM-Confidence: 9.235']
# Lo que haces es encontra todas las subcaddena que empiecen en numero/s (\d+) y un guion (-), segudo de de carcateres hasta los :, luego un espacio
# y todos los caracteres que sea o numeros o puntos

# Ahoara si queremos exctrer infromacion implicita de una subcadena de expresion regular, usamos los ()
print(re.findall(r'\d+-.+: ([0-9.]+)', s))
# ['0.8475', '9.235']
#  con esto no retornara unicamente la parte final de numeros y puntos de la expresion qweu estamos buscando

s = """From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"""

print(re.findall(r'^From .+ \d{2}:\d{2}:\d{2}', string))
# ['From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16']
print(re.findall(r'^From .+ (\d{2}):(\d{2}):(\d{2})', string))
# [('09', '14', '16')]