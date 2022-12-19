'''
Quick Sort

Este metodo de ordenamiento es uno de los mas eficaces (de compeljidad O(n log n)), la metodologia de este es mediante el proceso 
de Divide y Veceras!. Basicamente tratade tomar cualquiere elemento de la lista (por lo genral puede ser el primero, el del medio  
el ultimo) al cual llamaremos pivote, con base a estocompararemos los elementos con el pivote de tal forma que se creen dos sublistas, 
los menores que el pivote y los mayores que el pivote.

5, 2, 7, 3, 9, 1, 6
pivote => 5

haciendo las comparacion y generando las sublistas, quedaria de la siguiente forma:

menores        mayores
[2, 3, 1] |5| [7, 9, 6] 

la idea es utilizar un proceso recursivo para que a cada sublista se le aplique el mismo metodo de divide y venceras hasta que se obtenga sublistas
de 0 o 1 elemnto ([] ó [elemeto]) y posteriormente concatenarla con el resto de las sublistas.

si seguimos quedaria asi:

para menores:
pivote 2

[1] |2| [3]
lo cual ya no seguiriamos ya que se llego al caso base de que retornemos las sublitas con elemntos menores que 2

para mayores:
pivote = 7

[6] |7| [9]

lo cual ya no seguiriamos ya que se llego al caso base de que retornemos las sublitas con elemntos menores que 2


al concatenar quedaria la lista ordenada
[1] + |2| + [3] + |5| + [6] + |7| + [9] = [1, 2, 3, 5, 6, 7, 9]

Veamos tres formas de hacer este metodo de ordenamiento:
1. Version simple con listas auxiliares (este nos ayudara a entender un poco mejor el metodo, pero su compeljidad es un poco enifieciente, es
de O(n)) 

2. Version con particionado de Hoare (Hoare es el creador de este metodo, este es el metodo original. en este metodo no se usan sublistas, pero
si se usa divide y venceras)

3. Version con particionado de Lomuto (este metodo es mas sencillo de implementa y enetendible que el de Hoare pero un poquito menos eficiente)

NOTA: Este metodo es inestable ya que generaria una complejidad O(n**2) si la lista esta o esta medio ordenada, pero existe algunas optimizaciones
que permiten escoger el mejor pivote para el proceso de divide y venceras.

(Ver imagen Quick Sort.PNG)
ver video explicativo: https://www.youtube.com/watch?v=I318gmPeDHc
'''

# Version simple con listas auxiliares

ordenar = [5, 2, 7, 3, 9, 1, 6]
# Creamos una funcion auxiliar que nos retornara las sublistas menores y mayores y de por medio el pivote.
def aux_divide_y_venceras(lista):
    pivote = lista[0]
    menores, mayores = [], []

    for elemento in range(1, len(lista)):
        if lista[elemento] >= pivote:
            mayores.append(lista[elemento])
        else:
            menores.append(lista[elemento])
    
    return menores, pivote, mayores

# Fundcion recuriva Quick Sort (en mi concepto de recursividad, esta es una funcion recursiva por concatenacion).
def Quick_Sort(lista):
    # Caso base , si la sublista tiene 0 elemntos o 1 ([], [elemnto]) retornar esta sublista
    if len(lista) < 2:
        return lista
    else:
        # el caso recursivo es ir concantenando los pivotes y las sublistas de 0 o 1 elemento (pues estas ya estan ordenadas), hacemos esto 
        # llamando recursivamente la funcion pero con el parametro de los menores o mayores. y asi sucecivamente hasta que se cumplan los
        # casos base. 
        menores, pivote, mayores =  aux_divide_y_venceras(lista)
        # al pivote lo debemos convertir a lista ya que recordemos que es un numero y no se puede concatenar numero con listas.
        return Quick_Sort(menores) + [pivote] + Quick_Sort(mayores)

print(Quick_Sort(ordenar))
# [1, 2, 3, 5, 6, 7, 9]

# 2. Version con particionado de Hoare

# funcion 
'''
def QuickSort(lista, menor, mayor):
    # iniciamos las varibles 
    pivote = lista[menor]
    izquierda = menor + 1
    derecha = mayor
    # bucle principal, donde tanto el indice de la derecha como de la izquierda se moveran hasta que encuentren los valores que van a intercambiar
    while izquierda < derecha:

        while lista[izquierda] < pivote and izquierda <= derecha:
            izquierda += 1 

        while lista[derecha] > pivote and derecha >= izquierda:
            derecha -= 1

        # intercambiamos los valores de la izquierda y derecha, siempre y cuando izquierda sea menor que derecha
        if izquierda < derecha:
            lista[derecha], lista[izquierda] = lista[izquierda], lista[derecha]
    
    if pivote > lista[derecha]:
        # pivote
        lista[menor], lista[derecha] = lista[derecha], lista[menor]
    # casos base, pues si no cumple ninguna de estas dos significa que ya no hay elementos en las sublista por comparar:
    if menor < derecha:
        QuickSort(lista, menor, derecha-1)
    if mayor > derecha:
        QuickSort(lista, derecha+1, mayor)
'''
l_ordenar = [3, 6, 5, 8, 2, 3, 6, 9, 3, 1, 1]
# ejemplo:
#menor      izq          der   mayor
# [7, 5, 3, 12, 9, 2, 10, 4, 15, 8]
# intercambiar
# [7, 5, 3, 4, 9, 2, 10, 12, 15, 8]
#menor        izq der           mayor
# [7, 5, 3, 4, 9, 2, 10, 12, 15, 8]
# intercambiar
# [7, 5, 3, 4, 2, 9, 10, 12, 15, 8]
                #izq 
#menor          #der            mayor
# [7, 5, 3, 4, 2, 9, 10, 12, 15, 8]
                #izq 
#menor        #der              mayor
# [7, 5, 3, 4, 2, 9, 10, 12, 15, 8]
# Salimos de while principal que el indice de la izquierda es mayor que el de la derecha
# intercambiamos el valor del indice derecha con el valor del indice menor
# [2, 5, 3, 4, 7, 9, 10, 12, 15, 8]
# notar que se genraron las sublistas y el pivote en el medio [2, 5, 3, 4] |7| [ 9, 10, 12, 15, 8]
# porsteriomente seguimos con recursividad con esas dos sublitas y luego con las sublistas de estas sublistas y asi
# sucecivamente hasta ordenarlas completamente.

l_ordenar = [4, 8, 4, 23, 6, 567, 343, 45, 747, 6578, 456, 3, 3, 46, 57, 54, 3]
def auxliar_particionado(lista, menor, mayor):
     # iniciamos las varibles 
    pivote = lista[menor]
    izquierda = menor + 1
    derecha = mayor
    # bucle principal, donde tanto el indice de la derecha como de la izquierda se moveran hasta que encuentren los valores que van a intercambiar
    while True:


        while izquierda <= derecha and lista[izquierda] <= pivote:
            izquierda += 1 

        while derecha >= izquierda and lista[derecha] >= pivote:
            derecha -= 1

        # intercambiamos los valores de la izquierda y derecha, siempre y cuando izquierda sea menor que derecha
        if derecha < izquierda:
            break
        else:
            lista[derecha], lista[izquierda] = lista[izquierda], lista[derecha]

    #  siempre cuando izquierda sobrepase a derecha, el valor del indice derecha sera menor al valor del pivote (es decir, el indice de menor, es decir
    # derecha es el mas pequeño de la lista o sublista)   
    lista[menor], lista[derecha] = lista[derecha], lista[menor]
    # retornamos derecha, pues derecha es el indice donde se particiona en dos la lista o sublista
    return derecha

# funcion principal
def QuickSort(lista, menor, mayor):
    # con esta condicion si menor es igual o mayor que mayor, entonces significa que la sublista no puede ser dividad en mas partes (solo tiene un elemento)
    # por tanto, ya estaria ordenada y se tiene que concatenar con las otras sublistas. es por eso que no entraria en este condicional para proceder
    #  a ser partido en dos o particionado.
    if menor < mayor:
        # el pivote en un pricipio sera el primer elemento del toda la lista en si, pero cuando comencemosa particionar la lista, entonces el pivote
        # sera el punto en donde se partio la lista
        pivote = auxliar_particionado(lista, menor, mayor)
        # volvemos a llamr la funcion pero para evaluar la parte izquierda y derecha de la lista o sublistas
        QuickSort(lista, menor, pivote-1)
        QuickSort(lista, pivote+1, mayor)


QuickSort(l_ordenar, 0, len(l_ordenar)-1)
print(l_ordenar)
# [3, 3, 3, 4, 4, 6, 8, 23, 45, 46, 54, 57, 343, 456, 567, 747, 6578]
