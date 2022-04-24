# La busqueda binaria es un algorino O(log n) y funciona para encontrar en cual indice se encuentra un elemento dado, cabe recalcar que la
# lista debe estar ordenana, ya sea de forma decreciente o creciente.

# se siqguen estos pasos para la creacion de un algoritmo de busqueda binaria:

# 1. Inventa una condición para determinar si la respuesta se encuentra antes, después o en una posición dada
# 2. Recuperar el punto medio y el elemento medio de la lista.
# 3. Si es la respuesta, devuelva la posición media como la respuesta.
# 4. Si la respuesta está antes, repita la búsqueda con la primera mitad de la lista
# 5. Si la respuesta se encuentra después, repita la búsqueda con la segunda mitad de la lista.
# 6. Aquí está el algoritmo genérico para la búsqueda binaria, implementado en Python:


# Busquedad binaria para elementos de una lista que NO se repiten

carts = [13, 11, 10, 7, 4, 3, 1, 0]
# Notar que para este caso la lista esta ordenanda de forma decr    eciente.

# Creamos una funcion que reciba como parametros la lista (carts) y el valor a encontrar (query)
def binary_search(carts, query):

    # guardamos en variables primer y ultimo indice (inicial) de la lista
    last_index = len(carts)-1
    first_index = 0

    # bucle donde se ejecutara el codigo para hallar el indice del valor.
    # en este algoritmo si se cumple de que si el primer elemento es mayor al ultimo entonces no se encontro el elemento en la lista 
    while first_index <= last_index:

        # Guardamos en una variable el indice medio entre el primer indice y el ultimo
        middle_index = ((first_index + last_index)//2)

        # si el indice middle_index es igual al valor que estamos busacondo, entonces ya hallamos el elemento en la lista
        if carts[middle_index] ==  query:
            return middle_index
        
        # En el caso de que no sea asi y el elemento del indice middle_index sea mayor al valor de consulta entonces el NUEVO indice inicial
        # sera el punto medio+1 y asi de cierta forma creariamos una sublista con lo indices que iria desde first_index = middle_inde+1 hasta last_index (siblista derecha)
        elif carts[middle_index] > query:
            first_index = middle_index+1
            continue
        # y si valor de middle_index es menor entonces last_index = midle_index-1 y se crearia una sublista desde first_index hasta last_index = middle_index-1 (siblista izquierda)
        last_index = middle_index-1

    #  retornamos -1 si el query no esta ena lista
    return -1

print('Bynary search normal')
print(binary_search(carts, 4))
print(binary_search(carts, 5))
print(binary_search(carts, 13))
print(binary_search(carts, 10))
print(binary_search(carts, 0))
print(binary_search(carts, 17))
print(binary_search(carts, 1))
print(binary_search(carts, 21))

# Busquedad binaria pero con recursividad:
carts = [13, 11, 10, 7, 4, 3, 1, 0]
def binary_search_recursive(cards, query, first_index, last_index):
    middle_index = (first_index + last_index)//2

    # Casos bases, cuando la fucnion deja de llamarse asi misma
    if first_index > last_index:
        return -1
    elif cards[middle_index] == query:
        return middle_index


    # Casos recursivos, cuando la funcion se llama asi misma hasta que cumpla alguna de los casos bases

    # aplicamos la misma condiciones del la busqueda binaria normal y la mandamos como parametros de la nueva llamada 
    if cards[middle_index] > query:
        return binary_search_recursive(cards, query, middle_index+1, last_index)
    else:
        return binary_search_recursive(cards, query, first_index, middle_index-1)

print('Busquedad binaria usando recursividad')
print(binary_search_recursive(carts, 0, 0, len(carts)-1))
print(binary_search_recursive(carts, 20, 0, len(carts)-1))
print(binary_search_recursive(carts, 10, 0, len(carts)-1))
print(binary_search_recursive(carts, 32, 0, len(carts)-1))
print(binary_search_recursive(carts, 1, 0, len(carts)-1))
print(binary_search_recursive(carts, 13, 0, len(carts)-1))


print('_______________________________________________________________________________________________________________________________________')


# ahora veremos como aplicamos la busquedad binaria pero con listas con elemetos que se repiten (la idea es encontrar el primer valor del indices
# donde se enecuentre el valor de consulta), aunque este caso funciona igual para lista con elementos No repetidos

carts = [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]
# Notar que esta lista es de forma decreciente y tiene valores que se repiten





# funcion ´para comprobar si el valor del indice medio es igual al vlor de consulta, si hay indeces que son iguales a la consulta antes del punto medio
# y si no es y por tanto verificar en que parte de la lista esta (sublista derecha, sublista izquierda)
def comprobrar_middle_index(carts, query, middle_index):

    # si es valor de middel_index es igual al valor de consulta
    if carts[middle_index] == query:


        # verificamos si hay mas indices con valores iguales al valor de consulta antes que el middle_index (pues recordemos que necesitamos
        # el indice inicial donde se encuente ese query), estonces necesitamos una sublista izquierda
        if middle_index-1 >= 0 and carts[middle_index-1] == query:
            return 'izquierda'


        # si no entonces significa que dimos con el unico o inical indice igual al query 
        else:
            return 'encontrado'


    # si midde_inde no corresponde a un valor igual al query entonces como anteriormente vimos verificamos si el valor es mayor o menor y con base
    # a esto 'creamos' las sublista izuierda o derecha
    elif carts[middle_index] > query:
        return 'derecha'
    return 'izquierda'

# definimos una funcion casi identica a la funcion de la busquedad binaria normal, la unica diferencia es que aplicammos las condiciones con base a los resultados de la
# funcion 'comprobrar_middle_index'
def binary_search(carts, query):
    last_index, first_index = len(carts)-1, 0
    while first_index <= last_index:
        middle_index = (first_index + last_index) // 2
        comprobacion = comprobrar_middle_index(carts, query, middle_index)
        if comprobacion == 'encontrado':
            return middle_index
        elif comprobacion == 'izquierda':
            last_index = middle_index-1
        elif comprobacion == 'derecha':
            first_index = middle_index+1
    return -1

# ejemplo:
# supongamos queremos encontrar el valor 6:

# primera iteracion: middle_index = 7, carts[middle_index] = 6, corresponde al valor pero no el indice inicial que contiene ese valor, entonces creamos una sublista izquierda
# [8, 8, 6, 6, 6, 6, 6], 6, 3, 2, 2, 2, 0, 0, 0

# segunda iteracion: middle_index = 3, carts[middle_index] = 6, corresponde al valor pero no el indice inicial que contiene ese valor, entonces creamos una sublista izquierda
# [8, 8, 6], 6, 6, 6, 6

# tercera iteracion: middle_index = 1, carts[middle_index] = 8, no corresponde al valor de consulta procedemos a verificar si es mayor o menor y creamos uan sublista derecha
# 8, 8, [6]

# cuarta iteracion: valor encontrado!, resultado: 3
print('Busquedad binaria para listas con valores repetidos y lista con valores no repetidos')
print(binary_search(carts, 8))
print(binary_search(carts, 5))
print(binary_search(carts, 6))
print(binary_search(carts, 2))
print(binary_search(carts, 0))
print(binary_search(carts, 7))
print(binary_search(carts, 1))
print(binary_search(carts, 3))

# Aplicandolo con recursividad:

# Funcion exactamente igual a la anterior
def comprobrar_middle_index(carts, query, middle_index):
    if carts[middle_index] == query:
        if middle_index-1 >= 0 and carts[middle_index-1] == query:
            return 'izquierda'
        else:
            return 'encontrado'

    elif carts[middle_index] > query:
        return 'derecha'
    return 'izquierda'

# la misma fucnio pero llamando la funciion sucecivamente con las condiones anteriormente vistas
def binary_search_recursive(carts, query, first_index,  last_index):
    middle_index = (first_index+last_index)//2
    comprobacion = comprobrar_middle_index(carts, query, middle_index)
    # Base case
    if not carts:
        return -1
    elif comprobacion == 'encontrado':
        return middle_index
    # recursive cases
    if comprobacion == 'izquierda':
        return binary_search_recursive(carts, query, first_index, middle_index-1)
    elif comprobacion == 'derecha':
        return binary_search_recursive(carts, query, middle_index+1, last_index)

print('Busquedad binaria para listas con valores repetidos y lista con valores no repetidos. usando recursividad')
print(binary_search(carts, 8))
print(binary_search(carts, 5))
print(binary_search(carts, 6))
print(binary_search(carts, 2))
print(binary_search(carts, 0))
print(binary_search(carts, 7))
print(binary_search(carts, 1))
print(binary_search(carts, 3))






print('_______________________________________________________________________________________________________________________________________')
# Opcional
# Aplicando busquedad binaria con clases y recursividad
class Solution(object):
    def search(self, nums, target, first_index, last_index):
        self.nums = nums
        self.target = target
        self.first_index = first_index
        self.last_index = last_index
        while first_index <= last_index:
            middle_index = (self.first_index + self.last_index) // 2
            if self.nums[middle_index] == self.target:
                return middle_index
            elif self.nums[middle_index] > self.target:
                return Solution.search(self, self.nums, self.target, self.first_index, middle_index-1)
            return Solution.search(self ,self.nums, self.target, middle_index+1, self.last_index)
        return -1
    
prueba = Solution()
nums = [2, 3, 4, 10, 40]
print(prueba.search(nums, 40, 0, len(nums)-1))