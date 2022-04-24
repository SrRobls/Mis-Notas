print('                  Ciclo While en Python ')
#El ciclo while ("mientras" en español) en python es un ciclo que no termina hasta que una
#condicion sea falasa, ejemplo:
limite = int(input('¿Hasta que numero quieres imprimir en pantalla:? '))
numero = 0

while numero <= limite: #Mientras esta condicion sea verdadera se ejecuta ese codigo
    print(numero)
    numero += 1 #numero = numero + 1
else: #Cuando la condicion deja de ser verdadera ejecuta ese codigo y termina el ciclo
    print('Fin')
print(                               'Ciclo For')
#la sintaxis es para python (ya que en otros lenguajes e progranacion funciona diferente):
# for (variable) in (elemento a recorrer -> lista,tupla,arreglo, cadena texto etc)
palabra = None #None se usa para decir que una variable no tiene nada
cadena = 'hola!' #esta cadena de texto se puede interpretar como un arreglo que contiene los caracteres h,o,l,a,!
for palabra in cadena:
    print(palabra)

for letra in 'Colombia/barranquilla':
    if letra == 'b':
        print(f'letra encontrada: {letra}')
        break #Se usa para romper o terminar de una el bucle for
else: #Se interpreta que cuando termina el ciclo se ejecuta este codigo. esto es opcional
    print('Fin cicloFor')
#ejemplo: imprimir los numero pares del 0 al 8 con el ciclo for

for num in range(8): #range(numero) lo podemos interpretra como una lista de 8 numeros (0 al 8) para este caso
    if num % 2 != 0:
        continue #continue a diferencia de break no para o rompe el ciclo, si no que "pasa de una vez a la siguiente interacion dentro del ciclo"
    print(num)