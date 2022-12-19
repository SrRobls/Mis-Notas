resultados = []
casos = int(input())
for caso in range(casos):
    print(f'Caso {caso + 1}')
    matriz = []

    for fila in range(4):
        filas = input().split()
        numers = [int(x) for x in filas]
        matriz.append(numers)

    sumas = []
    sumaDiagonalDerecha = 0
    sumaDiagonalIzquierda = 0

    for i in range(1, 5):
        sumas.append(sum(matriz[i - 1]))
        sumaDiagonalIzquierda += matriz[i - 1][i - 1]
        sumaDiagonalDerecha += matriz[i - 1][-i]

    sumas.append(sumaDiagonalDerecha)
    sumas.append(sumaDiagonalIzquierda)

    if sum(matriz[0]) * 6 == sum(sumas):
        resultados.append('Cuadrado magico')
        continue
    resultados.append('Cuadrado muggle')

for resultado in resultados:
    print(resultado)