'''
BUSQUEDA BINARIA

Este algoritmo de busquedad se basa en la tecnica Divide y Venceras!, pus trata basicamente de tomar el punto medio de la lista y verificar
si este punto medio es el elemento a buscar, si no es asi aplicara el mismo proceso con la parte izquierda o derecha de la lista y asi
sucecivamente hasta o dar con el elemento o ya no se puede dividir mas los valores de los indices. Importante saber que este algoritmo solo
funciona a lista que esten ordenadas, pues de lo contrario muy probablemente no de con el elemento a buscar si esta en la lista.
'''


elementos_ordenados = [3, 6, 7, 9, 11, 11, 14, 67, 89, 140, 200]

def binary_search(lista, elemento_buscar):
    # definimos las variables que nos serviran para halla el punto medio de la lista o el punto medio de la 'sublista' derecha o izquierda
    inicio = 0
    final = len(lista)-1
    # incializamos el valor posicion en -1, pues si no se encuentra el elemnto entonces a finalizar el cilo principal nos retornara -1 indicandonos
    # que el elemento no esta
    posicion = -1

    # ciclo principal que para cuando ya no se pueda particionar los limites en un punto medio (cuando inicio > final) o cuando se encuentre la
    # posicion del elemnto a buscar.
    while inicio <= final and posicion == -1:
        medio = (inicio + final) // 2
        if lista[medio] == elemento_buscar:
            posicion = medio
        # si no se encontro el elemento en el punto medio de la lista o sublista, entonces veremos en que sublista (izquierda o derecha) es mas
        # probable encontrar el elemento.
        # para izquierda
        elif lista[medio] > elemento_buscar:
            final = medio - 1
        # para derecha
        elif lista[medio] < elemento_buscar:
            inicio = medio + 1

    return posicion

print(binary_search(elementos_ordenados, 11))
# 4
print(binary_search(elementos_ordenados, 6))
# 1
print(binary_search(elementos_ordenados, 140))
# 8
print(binary_search(elementos_ordenados, 141))
# -1
print(binary_search(elementos_ordenados, 1))
# -1