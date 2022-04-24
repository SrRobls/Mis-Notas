#Desarrolaremos un codigo para hacer un sudoku en python, usando recursividad y back traking:
# https://www.youtube.com/watch?v=KWP90gAsOa8

# Reaglas del sudoku:
#Regla 1: hay que completar las casillas vacías con un solo número del 1 al 9.
#Regla 2: en una misma fila no puede haber números repetidos.
#Regla 3: en una misma columna no puede haber números repetidos.
#Regla 4: en una misma región (3x3) no puede haber números repetidos.
#Regla 5: la solución de un sudoku es única.


# las partes vacias lo estamos representando con ceros
         # 0, 1, 2, 3, 4, 5, 6, 7, 8    (x)         0        1         2       (x)
sudoku = [[5, 3, 0, 0, 7, 0, 0, 0, 0],  #0      5, 3, 0, |0, 7, 0, |0, 0, 0
          [6, 0, 0, 1, 9, 5, 0, 0, 0],  #1      6, 0, 0, |1, 9, 5, |0, 0, 0     0
          [0, 9, 8, 0, 0, 0, 0, 6, 0],  #2      0, 9, 8, |0, 0, 0, |0, 6, 0
          [8, 0, 0, 0, 6, 0, 0, 0, 3],  #3      ---------------------------
          [4, 0, 0, 8, 0, 3, 0, 0, 1],  #4      8, 0, 0, |0, 6, 0, |0, 0, 3
          [7, 0, 0, 0, 2, 0, 0, 0, 6],  #5      4, 0, 0, |8, 0, 3, |0, 0, 1     1
          [0, 6, 0, 0, 0, 0, 2, 8, 0],  #6      7, 0, 0, |0, 2, 0, |0, 0, 6
          [0, 0, 0, 4, 1, 9, 0, 0, 5],  #7      ---------------------------
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]  #8      0, 6, 0, |0, 0, 0, |2, 8, 0
                                        #(y)    0, 0, 0, |4, 1, 9, |0, 0, 5     2
                                        #       0, 0, 0, |0, 8, 0, |0, 7, 9
                                                                                #(y)

def imprimir_sudoku(sudoku):
    for fila in sudoku:
        print(fila)
    return

def hallar_valor(dimension_x_o_y):
    #Usmoos estos codigos para jjuagra con las filas y columnas del sudoku y asi ver en cual region se introducera el nuevo valor
    if dimension_x_o_y <= 2:
        return 0 #Estamos en 0 en x o 0 en y
    elif dimension_x_o_y <= 5:
        return 1 #Estamos en 1 en x o 1 en y
    else:
        return 2 #Estamos en 2 en x o 2 en y

def generar_lista_region(x, y, sudoku):
    region_list = []
    #Primero debemos saber cual region estara nestro valor, para eso usamos otra funcion para encontrarlo
    coordenada_x_region = hallar_valor(x)
    coordenada_y_region = hallar_valor(y)
    for columna in sudoku[coordenada_y_region*3:coordenada_y_region*3+3]:
        for celda in columna[coordenada_x_region*3:coordenada_x_region*3+3]:
            region_list.append(celda)
    return region_list




def sera_el_valor_valido(x, y, valor, sudoku):
    #Para la fila:
    if valor in sudoku[y]:
        return False
    
    #Para la columna:
    #Primero generamos una lista con los valores de la columna donde se insertara el valor:
    columna = [] #Donde almacenera los valores de la columna
    for fila in sudoku:
        columna.append(fila[x])
    
    if valor in columna:
        return False

    #Para La region:
    #Aqui llamamos una funcion para crear ina lista  con loselemetos de la region y saber si el valor NO esta en la region:
    region = generar_lista_region(x, y, sudoku)
    if valor in region:
        return False
    
    #Si No esta ne las filas, columnas y la region, entonces si es posible colocar el valor en la celda
    return True



def resolver_sudoku(sudoku):
    # y recorrera por las filas del sudoku:
    for y in range(9):
        #x recorrera por los elementos de y (es decir, de la fila correspondiente a y)
        for x in range(9):
            #sudoku[y/fila][x/elemento de la fila de los indices 0 a 8]
            #En el caso de que x sea cero, eso significa que debemos hallar un valor 
            #que cumpla las reglas del sudoku y posterioremente, remplazarlo
            if sudoku[y][x] == 0:
                #Definimos el valor que remplazara al cero, este valor debe ir de 1 a 9 (es decir usamos un range que vaya del 1 al 10)
                for valor in range(1, 10):
                    #Necesitamos verificar si ese valor NO esta en la fila, columna y region donde se pondra
                    #(Esto para evitar que se repita el valor en algunas de estas y cumplir la reglas del sudoku)

                    #Llamamos la funcion para verificar, pasandole como parametro y, x y el valor:
                    if sera_el_valor_valido(x, y, valor, sudoku):
                        #si el valor es valido, entonces lo remplazamos
                        sudoku[y][x] = valor
                        #Aqui aplicamos un concepto de recursividad, volvemos a llamar la funcion (recordemos que la funcoon ya modifico un valor de la celda)
                        #Para que halle el sigiente valor correspondiente
                        resolver_sudoku(sudoku)
                        #En caso de que al iterar por los valores ya no enecuentre algun numero del 1 al 9 que cumpla con los requisistos, entonces usamos el concepto de back traking
                        #Basicamente cuando ya el valor no cumple, entonces devolvemos al valor anterior (es decir al cero)
                        sudoku[y][x] = 0
                return
    imprimir_sudoku(sudoku)
    return

resolver_sudoku(sudoku)
