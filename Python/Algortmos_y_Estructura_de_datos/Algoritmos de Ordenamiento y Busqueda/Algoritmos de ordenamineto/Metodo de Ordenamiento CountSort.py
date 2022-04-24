'''
COUNT SORT

Este algoritmo a diferencia de los anteriores no ordena por comparación, sino que utiliza un vector de conteo para determinar la 
posición de cada elemento en la nueva lista de los elementos ordenados.

ver video explicativo:
https://www.youtube.com/watch?v=mNp-_lRPjuk

tener en cuenta que este algoritmo solo fucnion para numero entero positivo y que es aconsejable usarla cuando la diferencia del valor minimo
y valor maximo no sea tan alta. pues si por ejemplo el valor minimo = 0 y valor maximo = 100 y la lista a ordenar es de 10 elemntos, entonces
tendriamos que crear una lista auxiliar de 100 elemntos para ordenar solo 10.

(Ver Imagen)
'''
lista_a_ordenar = [9, 3, 1, 5, 9, 2, 0, 1]

# funcion que recibe a la lista a ordena y el valor minimo y maximo
def count_sort(lista, minimoValor, maximoValor):
    # la lista de conteo es nuestra lista auxiliar donde se almacenaran la cantidad de veces que se repite un elemnto, se guardan en el
    # indice respectivo del elemento de la lista
    lista_conteo = [0] * (maximoValor + 1)
    # la listaque se retornara, pues es la lista ordenada
    lista_ordenada = [None] * len(lista)

    # Proceso para ordenar y mostrar la lista ordanda (ver video o debbugin)
    for i in lista:
        lista_conteo[i] += 1

    total = 0
    for i in range(len(lista_conteo)):
        lista_conteo[i], total = total, total + lista_conteo[i]

    for indice in lista:
        lista_ordenada[lista_conteo[indice]] = indice
        lista_conteo[indice] += 1

    return lista_ordenada

print(count_sort(lista_a_ordenar, 0, 9))
# [0, 1, 1, 2, 3, 5, 9, 9]

'''
Este algoritmo es de complejidad temporal O(n+k)
donde n es el total de elemntos a ordenar y k el lomite maximo de la lista
'''