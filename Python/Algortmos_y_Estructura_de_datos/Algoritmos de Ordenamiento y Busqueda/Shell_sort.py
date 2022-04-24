'''
Shell Sort

Basicamente merge sort trabaja casi igual que insertion short, la unica diferencia es que shell sort va comparando intervalo por intervalo (cada vez el intervalo va siendo mas pequeño), 
realizando asi menos iteraciones que selection sort.
importante ver el video para entender un poco mejor, pues este algoritmo es un poco confuso
https://www.youtube.com/watch?v=cQlEIdW2DU0&t=908s
'''


numeros = [23, 63, 12, 62, 21, 12, 35, 132, 98, 121, 32]

def shell_sort(lista):
    # dos variables importantes donde se guaradara el largo del la lista y el intervalo (que en un principio es la mitad del largo de la lista)
    tamaño = len(lista)
    intervalo = tamaño // 2
    # ciclo que parara cuando el intervalo sea 0 (ya no paodamos comparara mas elemetos y la lista esta odenada), este es el ciclo principal 
    # donde se hara las comparaciones y los intercambios
    while intervalo != 0:
        # for que incia en el valor del intervalo hasta el final de la lista
        for i in range(intervalo, tamaño):
            # variables para guardar el valor (value) que nos sirve para cuando ya hemos iterado o ya se hayan hecho las comparaciones colocar este
            # valor en el indice comparado, con indice almacenamos el valor del iterador, esto no sirve para comparar el valor de value con un
            # valor anterior que tenndra como indice indice - intervalo
            valor = lista[i]
            indice = i
            # ciclo que se efectua si indice aun puede retroceder en la lista para hacer comparaciones y el valor de indice - intervalo es mayor
            # que el valor que queremos cambiar
            while indice >= intervalo and valor < lista[indice - intervalo]:
                # si se cumple, le asignamos el valor del indice en el que estamos por el valor con el que comparamos
                lista[indice] = lista[indice - intervalo]
                # cambiamos el indice, ahora sera el valor -intevalo
                indice -= intervalo

            # una vez ya comparados los elemento que se puedana cambiar, asignamos el valor de value al indice en el que quedo luego de realizar
            # en anterior bucle
            lista[indice] =  valor
        # importante actualizar el intervalo pues ees la forma principal en como funciona el algoritmo
        intervalo //= 2

    return lista


print(shell_sort(numeros))
# [12, 12, 21, 23, 32, 35, 62, 63, 98, 121, 132]