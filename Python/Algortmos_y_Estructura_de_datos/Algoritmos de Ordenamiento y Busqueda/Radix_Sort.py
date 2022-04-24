'''
Radix Sort:

Radix sort es un algoritmo que trabaja similar a bucket sort (en el tema de que usa una lista de listas auxiliar), la metodologia de este 
algoritmo es ir alamcenando los numeros segun sus digitos (desde el ultimo hasta el primer digito, uno por uno) y una vez hecho esto, remplazar
los elementos de los casillero en nuestra lista a ordenar, todo esto hasta que el primer casillero sea igual al tamaño de la lista, por tanto, ya esta en orden y se procede a
remplazar los elemntos de los casillero en la lista por ultima vez y retornar

https://www.youtube.com/watch?v=VtihNrE_vYk

Este algoritmo tiene un problema y es que NO es aconsejable usarlo cuando los numeros a ordenar tinene demasiados digito (son grandes), pues
se trendria que hacer mas iteracion y remplazos generando asi, que sea ineficaz. por tanto, es mejor para ordenar numeors con pocos digitos. 

este algoritmo es en promedio de complejidad temporal lineal es decir O(n)
'''
lista_ordenar = [-2, 7, 15, -14, 0, 15, 0, 7, -7, -4, -13, 5, 8, -14, 12]

def radixSort(lista):
    # necesitamos el largo de la lista a ordenar y crear una lista de listas (que reprentan como los casilleros), para que cuando el largo del 
    # primer casillero correspondiente al digito 0 sea igual al largo del la lista a ordenar, se termine el ciclo while, donde se ejecuta el 
    # proceso de ordenamiento
    largo_de_lalista = len(lista)
    casilleros_de_digitos = [[] for _ in range(10)]
    # dos variables mas donde ira el valor del digito (pues con base a este, se le asignara al numero en en si su casillero) segun la variable posicion
    # la variable posicion es, si vemos a los numeros como indices, el indice de atras hacia adelante del numero de la lista, se inicializa siempre en 1,
    # quremos en un principio el ultimo digito del numero. tambien inicializamos, el valor del digito en -1, pues en un principio no se le asignara 
    # nada hasta entrar al bucle
    valor_numero, posicion = -1, 1
    # es el que le diraal while cuando parar
    poder_seguir = False
    
    # ciclo donde se hara el proceso de ordenamiento, la idea es que pare cuando el primero casillero sea igual en largo al largo de la lista
    while not poder_seguir:
        for num in lista:
            # hacemos division al numero de la lista entre la posicion del digito que queremos y posteriormente 
            # le sacamos su modulo dividiendolo en 10, asi obtenemos el valor del digito segun el indice
            valor_numero = (num / posicion)
            # asigamos el numero segun el valor del digito en el casillero correspondiente. necesitamos que valor_numero sea entero cuando le
            # saquemos el modulo, pues de lo contrario no podremos obtener el digito , e importante tambien colocralo en un abs en caso de trabaja con
            # numero negativos
            casilleros_de_digitos[abs(int(valor_numero)) % 10].append(num)

            # cuando el largo del casillero 0 es igual al largo de la lista y no aseguramos que el mayor numero (ultimo de la lista 
            # ordenada) su primer digito (o el ultimo que evaluamos con el indice) sea mayor a 0 (esto es logico porque nunca el numero mayor
            # comenzara en cero a expecion que se evalie una lista en la que sus elementos sea 0)
            if len(casilleros_de_digitos[0]) == largo_de_lalista and valor_numero > 0:
                poder_seguir = True
                break
        # proceso donde ordenamos segun el orden de los numeros de cada casillero. para esto, necesitamos a un indice que se inicie en 0 y vaya
        # aumentando cada vez que se remplaza un elemento en ese indice, esto, hasta que no haya mas elementos en nigun casillero
        indice_en_la_lista = 0
        for casillero in casilleros_de_digitos:
            while casillero != []:
                lista[indice_en_la_lista] = casillero.pop(0)
                indice_en_la_lista += 1
        
        # aumentamos x10 el valor de posicion, basicamene para tomar el digito anterior al digito de la posicion anterior.
        posicion *= 10
    

    return lista



print(radixSort(lista_ordenar))