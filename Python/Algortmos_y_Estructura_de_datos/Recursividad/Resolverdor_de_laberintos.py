'''
Salida del laberinto. Encontrar un camino que permita salir de un laberinto definido en una 
matriz de [n x n], solo se puede mover de a una casilla a la vez –no se puede mover en diagonal– 
y que la misma sea adyacente y no esté marcada como pared. Se comenzará en la casilla (0, 0) 
y se termina en la (n-1, n-1). Se mueve a la siguiente casilla si es posible, cuando no se pueda 
avanzar hay que retroceder sobre los pasos dados en busca de un camino alternativo.
'''

laberinto = [[' ', 'X', 'X', 'X', 'X'], 
             [' ', 'X', ' ', ' ', ' '],
             [' ', 'X', ' ', 'X', ' '], 
             [' ', ' ', ' ', 'X', ' '], 
             ['X', 'X', 'X', 'X', ' ']]

laberinto2 = [[' ', 'X', 'X', 'X', 'X', 'X'], 
              [' ', 'X', ' ', ' ', ' ', ' '],
              [' ', 'X', ' ', 'X', 'X', ' '], 
              [' ', ' ', ' ', ' ', 'X', ' '], 
              [' ', ' ', ' ', ' ', 'X', ' '],
              ['X', 'X', 'X', 'X', 'X', ' ']]

laberinto3 = [[' ', 'X', 'X', 'X', 'X', 'X'], 
              [' ', 'X', ' ', ' ', ' ', ' '],
              [' ', 'X', ' ', 'X', 'X', ' '], 
              [' ', ' ', 'x', ' ', ' ', ' '], 
              [' ', ' ', ' ', ' ', 'X', ' '],
              ['X', 'X', 'X', 'X', 'X', ' ']]

laberinto4 = [[' ', 'X', 'X', 'X', 'X', 'X'], 
              [' ', ' ', ' ', 'x', ' ', ' '],
              ['x', 'X', ' ', 'X', 'X', ' '], 
              [' ', ' ', ' ', ' ', 'X', ' '], 
              [' ', ' ', ' ', ' ', ' ', ' '],
              ['X', 'X', 'X', 'X', 'X', ' ']]

laberinto5 = [[' ', 'X', 'X', ' ', ' ', ' '], 
              [' ', 'X', ' ', ' ', 'X', ' '],
              [' ', 'X', ' ', 'X', ' ', ' '], 
              [' ', ' ', ' ', 'X', ' ', 'X'], 
              [' ', 'X', ' ', 'X', ' ', ' '],
              ['X', 'X', 'X', 'X', 'X', ' ']]

laberinto6 = [[' ', 'X', ' ', ' '],
              [' ', 'X', ' ', ' '], 
              [' ', ' ', ' ', ' '], 
              [' ', 'X', ' ', ' ']]

# el puntor preguntara si pueder dar el siguiente paso hacia la derecha, abajo, izquierda o arriba. en ese ordem, dependiendo del caso el hara dara el paso,
# el puntor dara el paso si, el paso siguiente NO es una pared (x), ya ha pasado por ahi o es un lugar donde se habia quedado estancado antes.
# se tiene las siguientes condiciones. 1. si puede dar el siguiente paso, lo da, siempre y cuando el no haya pasado por ahi antes.
                                      #2. si se queda estancado marcamos es estancamiento como si fuera un paso y entonces se devuelve un paso 
'''
def encontrarCamino(laberinto, x = 0, y = 0):
    if x == len(laberinto)-1 and y == len(laberinto)-1:
        laberinto[x][y] = '*'
        string = ''
        for x in laberinto:
            string += ' '.join(x) + '\n'
        return string
    else:
        laberinto[x][y] = '*'
        # si puede dar el paso hacia la derecha:
        if puedeEstardentro(laberinto, x, y+1) and laberinto[x][y+1] == ' ':
            return encontrarCamino(laberinto, x, y+1)
        # si puede dar el paso hacia abajo
        elif puedeEstardentro(laberinto, x+1, y) and laberinto[x+1][y] == ' ':
            return encontrarCamino(laberinto, x+1, y)
        # si puede dar el paso hacia la izquierda
        elif puedeEstardentro(laberinto, x, y-1) and laberinto[x][y-1] == ' ':
            return encontrarCamino(laberinto, x, y-1)
        # si puede dar el paso hacia la arriba
        elif puedeEstardentro(laberinto, x-1, y) and laberinto[x-1][y] == ' ':
            return encontrarCamino(laberinto, x-1, y)
        # si puede dar el paso hacia la derecha:
        else: 
            laberinto[x][y] = '.'
            if puedeEstardentro(laberinto, x-1, y) and laberinto[x][y+1] == '*':
                return encontrarCamino(laberinto, x, y+1)
            # si puede dar el paso hacia abajo
            elif puedeEstardentro(laberinto, x, y-1) and laberinto[x+1][y] == '*':
                return encontrarCamino(laberinto, x+1, y)
            # si puede dar el paso hacia la izquierda
            elif puedeEstardentro(laberinto, x+1, y) and laberinto[x][y-1] == '*':
                return encontrarCamino(laberinto, x, y-1)
            # si puede dar el paso hacia la arriba
            elif puedeEstardentro(laberinto, x, y+1) and laberinto[x-1][y] == '*':
                return encontrarCamino(laberinto, x-1, y)
        
        

def puedeEstardentro(laberinto, x, y):
    return ((x >= 0 and x < len(laberinto)) and (y >= 0 and y < len(laberinto)))
'''

def encontrarCamino(laberinto, x = 0, y = 0, string = ''):
    if x == len(laberinto)-1 and y == len(laberinto)-1:
        laberinto[x][y] = '*'
        return laberinto  

    elif estadentro(laberinto, x, y):
        laberinto[x][y] = '*'

        if encontrarCamino(laberinto, x, y+1):
            return laberinto
        if encontrarCamino(laberinto, x+1, y):
            return laberinto
        if encontrarCamino(laberinto, x, y-1):
            return laberinto
        if encontrarCamino(laberinto, x-1, y):
            return laberinto
        else:
            laberinto[x][y] = ' '
    else:
        return False
        
def estadentro(laberinto, x, y):
    return ((x >= 0 and x < len(laberinto)) and (y >= 0 and y < len(laberinto))) and (laberinto[x][y] == ' ')


def mostrar_laberinto_hecho(laberinto_hecho):
    string = ''
    for linea in laberinto_hecho:
        string += ' '.join(linea) + '\n'
    return string

print(mostrar_laberinto_hecho(encontrarCamino(laberinto)))
print(mostrar_laberinto_hecho(encontrarCamino(laberinto2)))
print(mostrar_laberinto_hecho(encontrarCamino(laberinto3)))
print(mostrar_laberinto_hecho(encontrarCamino(laberinto4)))
print(mostrar_laberinto_hecho(encontrarCamino(laberinto5)))
print(mostrar_laberinto_hecho(encontrarCamino(laberinto6)))