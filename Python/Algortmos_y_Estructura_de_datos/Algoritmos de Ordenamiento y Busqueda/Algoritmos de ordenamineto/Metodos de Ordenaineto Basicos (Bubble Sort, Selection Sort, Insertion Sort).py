
'''
METODO BURBUJA:

Basicamente el metodo burbuja trata de ordenar una lista iterando por cada elemento e ir preguntando si el siguiente es menor o mayor, y
dependiendo de como queremos ordenarlo hacemos el respectivo cambio entre esos dos elemntos.

Lo que hara este algoritmo es basicamente:
[2, 4, 1, 3, 5],  Iterancion 1
[2, 1, 3, 4, 5]   Iterancion 2
[1, 2, 3, 4, 5]   Iterancion 3
[1, 2, 3, 4, 5]   Iterancion 4

(Ver imagen)
'''

lista_a_ordenar = [3, 6, 5, 8, 2, 3, 6, 9, 3, 1, 1]

def metodo_burbuja(l_ordenar):
    for iter in range(len(l_ordenar)-1):
        # Le restamos iter al for donde se ordenara la lista porque recordemos que a medida que vayamos iterando por iter, ya se habra
        # colocado de ultimo (o de primero, dependiendo de si queremos orednarlo de mayor a menor. en este caso sera de menor a mayor)
        # el elemnto mas mayor de la lista, por tanto al restar iter, nos ahorramos algunas iteraciones mas cuando busquemos al segundo mas mayor, asi
        # evitaremos comparar el mas mayor con el siguiente mas mayor.
        for i in range(len(l_ordenar)-iter-1):
            # Si queremos ordenarlo de mayor a menor, entonces cambiamos el menor que (<) a mayor que (>)
            if l_ordenar[i+1] < l_ordenar[i]:
                l_ordenar[i], l_ordenar[i+1] = l_ordenar[i+1], l_ordenar[i]
    
    return l_ordenar

print(metodo_burbuja(lista_a_ordenar))
# [1, 1, 2, 3, 3, 3, 5, 6, 6, 8, 9]

'''
Hay un problema con esta forma, y es que cuando por ejemplo la lista esta casi o medio ordenada al memento de ordenar, este proceso se hara
mas rapido que una lista totalmente desordenada, por tano, ya no es tan eficiente seguir iterando para ordenar pues no se hara ningun cambio.

para esto esta el metodo por burbuja mejorado:
'''

lista_a_ordenar = [1, 1, 5, 2, 1, 6, 7, 3]

def burbuja_mejorada(l_a_ordenar):
    iter = 0
    # creamos una variable controladora que nos indicara si debemos seguir ordenando (True) o ya se ordenos la lista (False)
    controlador = True
    # ciclo while que terminara o cuando terminemos de iterar por complemto o cuando el controlador no indique si ya la lista esta ordenada.
    while (iter <= len(lista_a_ordenar)-1) and controlador == True:
        # Inicializamos el controlador en false ya que si no se cumple el condicional seguiente entonces signifivca que ya se termino de ordenar.
        # por tanto, salimos del while.
        controlador = False
        # el mismo for y condicional como el de la burbuja sin mejorar
        for j in range(len(l_a_ordenar)-iter-1):
            if l_a_ordenar[j+1] < l_a_ordenar[j]:
                l_a_ordenar[j+1], l_a_ordenar[j] = l_a_ordenar[j], l_a_ordenar[j+1]
                # si sen entro a este condicional eso significaba que la lista No estaba ordenada, por tanto el controlador se vuele True
                # indicandonos que debemos seguir iterando.
                controlador = True
        
        iter += 1

    return l_a_ordenar

print(burbuja_mejorada(lista_a_ordenar))
# [1, 1, 1, 2, 3, 5, 6, 7]

'''
Este metodo es de complejidad temporal O(n**2)
'''

print('---------------------------------------------------------------------------------------------------------------------------------------')
'''

METODO POR SELECCION

La idea principlar de algoritmo de ordenamiento selection sort es iterar en la lista y encontrar el menor de la lista intercambiarlo
con el el valor del inicio y posteriormente volver interar pero del el inicio+1 (Pues sabemos que el valor del inicio es el menor de todos
y la idea es econtrar el siguienemte  menor) hasta el largo de lista para encontrar el valor menor que les sigue y remplazarlo por el valor del indice inicio+1

arr[] = 64 25 12 22 11

Find the minimum element in arr[0...4]
and place it at beginning
11 25 12 22 64

Find the minimum element in arr[1...4]
and place it at beginning of arr[1...4]
11 12 25 22 64

Find the minimum element in arr[2...4]
and place it at beginning of arr[2...4]
11 12 22 25 64

Find the minimum element in arr[3...4]
and place it at beginning of arr[3...4]
11 12 22 25 64 

(Ver imagen)
'''

lista_a_ordenar = [3, 6, 5, 8, 2, 3, 6, 9, 3, 1, 1]

def ord_seleccion(l_a_ordenar):
    # for que iterara por cada una de las posiciones donde se almacenaran los valores ordenados
    for iter in range(len(lista_a_ordenar)-1):
        # en un principio el menor se el valor del indice iter
        menor = iter
        # for ne la que compararemos los valor hast hallar el menor y posteriormente moverlos a la posicion del incide iter
        for i in range(iter+1, len(l_a_ordenar)):
            if l_a_ordenar[menor] > l_a_ordenar[i]:
                menor = i
        l_a_ordenar[iter], l_a_ordenar[menor] = l_a_ordenar[menor], l_a_ordenar[iter]

    return l_a_ordenar

print(ord_seleccion(lista_a_ordenar))
# [1, 1, 2, 3, 3, 3, 5, 6, 6, 8, 9]


'''
Este metodo es de complejidad temporal O(n**2)
'''

print('---------------------------------------------------------------------------------------------------------------------------------------')
'''
METODO POR INSERCION

Este metodo desde un principio tomara por ordendao el primer elemnto, por tanto, se comieza desde el segundo. entonces desde el segundo hasta
el ultimo se ordenadara, la forma en la que se hara es ir iterando por los elementos de la lista k (desde el segunbdo hasta el ultimo) e ir preguntando
si el valor  anterior es menor o  mayor (dependiendo de como queremos ordenarlo), e ir intercambiandolos hasta que se encuentre un elemnto que al
compraralo no se cumpla la condicion de si es manyor o menor, de tal forma que al terminar se obtenga una lista ordenada.

supongamos tehemos una lista = [11, 3, 81, 7, 45]

y utilizamos dos ciclos, uno for y otro whle, donde en el for se comenzara desde el segundo hasta el ultimo indice + 1. y en el while es donde se
haran llos intercambios (siempre y cuando se cumplan las condiciones del while claro esta). y utilizaremos una veriable k que el indice que se
comparar para intercambir, esta variable siempre se inicia con indice-1

(VER IMANGE DE INSERSION SORT PARA VER COMO FUCNIONA.)

'''

lista_a_ordenar = [11, 3, 81, 7, 45]
def ord_por_insercion(l_a_ordenar):
    for iter in range(2, len(l_a_ordenar)+1):
        k = iter-1
        # Si queremos que se ordene de mayor a menor estonces cambiamos las operacions (<, >) 
        while k > 0 and (l_a_ordenar[k] < l_a_ordenar[k-1]):
            l_a_ordenar[k], l_a_ordenar[k-1] = l_a_ordenar[k-1], l_a_ordenar[k]
            k -= 1
    return l_a_ordenar

print(ord_por_insercion(lista_a_ordenar))
# [3, 7, 11, 45, 81]

'''
Este metodo es de complejidad temporal O(n**2)
'''