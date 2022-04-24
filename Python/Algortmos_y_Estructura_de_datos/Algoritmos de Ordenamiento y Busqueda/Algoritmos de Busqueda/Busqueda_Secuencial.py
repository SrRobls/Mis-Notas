'''
BUSQUEDA SECUENCIAL Ó BUSQUEDA POR FUERZA BRUTA.

Esta es la busqueda basica, trata basicammente de iterar por los indices de la lista  hasta dar con un indice que tenga como valor al elemento
buscado. este es un altgoritmo lineal y no importa si los elementos este ordenados o no y no importa si estan repetidos, pues como es lienal
el algoritmo dara con el primer indice que tenga el valor a buscar. 
'''

elementos = [4, 67, 1, 2, 5, 1, 5, 6, 6, 1, 2, 4, 7]

def busqueda_secuencial(lista, elemento_buscar):
    posicion = -1
    # for que iterara por cada uno de los indices y para hasta encontra un inidice que tenga el elemento buscado o hasta iterar por todos los
    # indices de la lista
    for i in range(len(lista)):
        if lista[i] == elemento_buscar:
            posicion = i
            break
    # retornamos el resultado -1 si no se encontro o el valor del indice si se encontro.
    return posicion

print(busqueda_secuencial(elementos, 6))
# 7
print(busqueda_secuencial(elementos, 4))
# 0
print(busqueda_secuencial(elementos, 70))
# -1
print(busqueda_secuencial(elementos, 10))
# -1

'''
Este algoritmo es de complejida temporal O(n)
'''