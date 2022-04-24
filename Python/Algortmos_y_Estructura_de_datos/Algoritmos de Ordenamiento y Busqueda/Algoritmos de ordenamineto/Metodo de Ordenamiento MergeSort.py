'''
MERGE SORT

Este metodo de ordenamiento es similar al de Quick Sort, pues se basa en la tecnica Divide y Venceras!. Trata de ir dividendo la lista en sublistas
(se dividen por la mitad) y a esas sublistas hacerles lo mismo (para esto usamos recursividad) hasta que se den con sublistas que tenga un unico
elemento por lo cual, logicamente ya esta ordenada, a esa sublistas las mezclaremos con las otra de tal forma que sea ordenada (para esto 
usamos una funcion auxliar merge) y asi sucecivamente hasta obtener la lista ordenada.

El algoritmo va mas o menos como en el siguiente video:
https://www.youtube.com/watch?v=nga05GPMsRs

(Ver Imagen)
'''

lista_a_ordenar = [8, 5, 3, 9, 1, 4, 7]
# Para hacernos una idea del codigo, iria asi:
# [8, 5, 3, 9]                   |           [1, 4, 7]
# [8, 5]    |    [3, 9]                      [1, 4] | [7]
# [8]|[5]        [3]|[9]                     [1]|[4]   [7]
# ----------------se ordenan y concatenan--------------------
# [5][8] | [3][9]                            [1]|[4] | [7]
# [5, 8] |[3, 9]                             [1, 4] | [7]
# [3, 5, 8, 9]                 |              [1, 4, 7]
# ya teniendo las dos partes de la lista ordenada, porcedemos a unirla ordenadamente:
# [1, 3, 4, 5, 7, 8, 9]

# Funcion recursiva MergeSort
def mergeSort(lista):
    if len(lista) < 2:
        return lista
    else:
        # Halar el indice mitad de la lista
        medio = len(lista) // 2

        # sublistas izquierda y derachas con los elementos de la lista repsoectivamente
        izquierda = [lista[i] for i in range(0, medio)]
        derecha = [lista[i] for i in range(medio, len(lista))]

        # Llamamos recursivamente esta funcion pero le mandamos como parametros las sublistas egeneradas, y seguimos con las sublistas de estas
        # sublistas hasta terminar el caso base, a esas llamadas que nos retornaran una sublista ordenada (con un elemento) la almacenamos en
        # variables             
        izquierda = mergeSort(izquierda)
        derecha = mergeSort(derecha)

        # aca comprobamos si el ultimo valor de la lista izquierda es menor que el de la derecha, si es asi, los concatenamos y retornamos la lista
        # izquireda pues significa que no hace falta llamar la funcion para mezclar la lista pues significa que todos los elementos de la sublista 
        # derecha son mayores o iguales que los de la sublista izquierda
        if izquierda[medio-1] <= derecha[0]:
            izquierda += derecha
            return izquierda
        #  si no es asi entonces procedemos a usar la funcion auxiliar para mezclarlas y obtener una lista ordenada
        resultado_mezcla = merge(izquierda, derecha)
        return resultado_mezcla


# Funcion aux para mezclar las listas
def merge(izquierda, derecha):
    # lista donde estarana lso eleemntos de las sublistas ordenadas
    lista_mezclada = []
    # ciclo donde se compara y se ecogera el menor de los elementos para alamecenarlos en la lsiat mezclada y asi ordenarlas de menor a mayor
    while (len(izquierda) > 0) and (len(derecha) > 0):
        if izquierda[0] < derecha[0]:
            lista_mezclada.append(izquierda.pop(0))
        else:
            lista_mezclada.append(derecha.pop(0))
    
    # En caso de que quede un valor restante en algunas de las listas (si sigues el proceso a detalle notaras que casi siempre pasara)
    # entonces lo concantenamos en la lista ya que ese valor sera el mayor de la lista mezclada
    if len(izquierda) > 0:
        lista_mezclada += izquierda
    else:
        lista_mezclada += derecha    

    # retornamos la lista mezclada
    return lista_mezclada

print(mergeSort(lista_a_ordenar))
# [1, 3, 4, 5, 7, 8, 9]

'''
Este algoritmo es de complejidad temporal O(n log n).
'''