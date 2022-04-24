print('                           set en python')
#un set es una lista pero no mantiene un orden ni permite almacenar elementos repitidos y modificarlo pero si es posible agregar o eliminar elementos
# set:
planetas = {'Marte', 'Tierra', 'jupiter'}
print(planetas) #Notemos que no se ejecuta en un orden
# largo
print(len(planetas))
# Revisar si un elemento esta presente:
print('Marte' in planetas) #para saber si elemento esta presente en un set solo debemo decir (elemento que queremos saber si esta) in (la variable tipo set). nos regresara true si esta o false si no
#agregar elemento
planetas.add('venus')
print(planetas) #Usamos la funcion add para agregar elementos en un set
#No se puede duplicar elementos:
planetas.add('venus')
print(planetas) #Notemos que no nos sale dos 'venus' si no, solo uno
#eliminar elementos
planetas.remove('venus') #aca si no esta el elemento en el set marcara error
print(planetas)
#otra forma
planetas.discard('Jupiter') #aca independientemente de que este o no el elemento a eliminar este no marcara error
#limpiar un set:
planetas.clear()
print(planetas)
