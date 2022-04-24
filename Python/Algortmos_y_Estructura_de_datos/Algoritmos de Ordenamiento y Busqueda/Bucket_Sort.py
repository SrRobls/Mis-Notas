'''
Bucket Sort o Ordenamiento por casilleros:

El proceso de este algoritmo es basicamente guaradar los elementos en casilleros dependiendo del vallor de elemento, a cada casillero ordenarlo
y posteriormente concatenamos cada casillero y al final obtenemos una lista ordenada.

ejemplo, el proceso es mas o menos asi:
47, 32, 33, 52, 37, 42, 51

casillero #1 (valores entre 30 - 40)
32, 37
ordenarlo = 32, 37
casillero #2 (valores entre 40 - 50)
47, 42
ordenarlo = 42, 47
casillero #3 (valores entre 50 - 60)
52, 51
ordenarlo = 51, 52

ahora si concatenamos los casilleros:
(32, 37) + (42, 47) + (51, 52) = 32, 37, 42, 47, 51, 52
obtenemos la lista ordenada.

'''

array = [42, 32, 33, 52, 37, 47, 51]

def bucket_sort(input_list):
    # Find maximum value in the list and use length of the list to determine which value in the list goes into which bucket 
    max_value = max(input_list)
    size = max_value/len(input_list)

    # Create n empty buckets where n is equal to the length of the input list
    buckets_list= []
    for x in range(len(input_list)):
        buckets_list.append([]) 

    # Put list elements into different buckets based on the size. el coidgo principal y es donde se alamacenaran lo elementos segun el casillero
    for i in range(len(input_list)):
        j = int(input_list[i] / size)
        if j != len(input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])
    
    # Sort elements within the buckets using Insertion Sort and concatenamos la lista en final_output
    final_output = []
    for z in range(len(input_list)):
        # podemos usar cualquier tipo de algoritmo de ordenamiento para ordenar los casilleros (para este caso decidi usar insertio_sort)
        final_output += insertion_sort(buckets_list[z])
    
    return final_output

def insertion_sort(l_a_ordenar):
    for iter in range(1, len(l_a_ordenar)+1):
        k = iter-1
        while k > 0 and (l_a_ordenar[k] < l_a_ordenar[k-1]):
            l_a_ordenar[k], l_a_ordenar[k-1] = l_a_ordenar[k-1], l_a_ordenar[k]
            k -= 1
    return l_a_ordenar

print(bucket_sort(array))

'''
Este algoritmo es por lo general de complejidad temporal O(n)
'''