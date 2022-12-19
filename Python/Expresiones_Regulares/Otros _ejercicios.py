import re

from pyparsing import line

"""
Ejercicio 1: escribe un programa simple que pida una operacion de re. 
Debe pedir al usuario que ingrese una expresión
regular y cuente el número de líneas que coincidan con ésta:
"""
# with open('mbox.txt', 'r') as texto:
#     expresion = input('give me a expresion: ')
#     total_lienas_coincidentes = 0
#     for linea in texto:
#         linea = linea.lstrip()
#         if re.search(expresion, linea):
#             total_lienas_coincidentes += 1
    
#     print(f'there is {total_lienas_coincidentes} matching lines in mbox')

# Priuebas
'''
give me a expresion: ^Author
there is 1798 matching lines in mbox

give me a expresion: ^X-
there is 14368 matching lines in mbox

give me a expresion: java$
there is 4175 matching lines in mbox
'''

'''
Ejercicio 2: escribe un programa que busque líneas en la forma: New Revision: 39772
'''

'''
Extrae el número de cada línea usando una expresión regular y el
método findall(). Registra el promedio de esos números e imprímelo.
'''
archive_name = input('Give a archive name: ')
with open(archive_name, 'r') as texto:
    sum_numbers, total_numbers = 0, 0
    for linea in texto:
        numbers_finded = list(map(int, re.findall(r'New Revision: (\d+)', linea)))
        total_numbers += len(numbers_finded)
        sum_numbers += sum(numbers_finded)
    print(sum_numbers/total_numbers)
        
# Resultado: 1790 lienas tiene la paalabra New Revision seguida de numeros
# Give a archive name: mbox-short.txt
# 39756.92592592593

# Give a archive name: mbox.txt
# 38549.79497206704
