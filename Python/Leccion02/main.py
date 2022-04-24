#                           Operadores Aritmeticos:
print("                     operadores aritmeticos")
variable1 = 5
variable2 = 3
suma = variable1 + variable2
resta = variable1 - variable2
division = variable1 / variable2
residuo = variable1 % variable2
divisionInt = variable1 // variable2 #solo regresa la parte entera
mult = variable1 * variable2
expo = variable1 ** variable2
print('reultado suma: ', suma)
print('reultado resta: ', resta)
print('reultado division: ', division)
print('reultado division(int): ', divisionInt)
print('reultado residuo: ', residuo)
print('reultado multiplicacion: ', mult)
print('reultado exponenciacion: ', expo)
print('---------------------------------------------------------------------------------------------------------------')
#                                      Operadores de Asignacion En Python
print('                                Operadores de Asignacion En Python')
var =  10
print(var)
#si queremos hacerle un "acumulado" seria
var = var + 1 #le sumamos 1 a la variable var
print(var)
#tambien se puede escribir como "var (operador)= (el numero que queremos relacionar)
var += 1
print(var) #es lo mismo que var = var + 1. y asi se hace para con otros operadores
var -= 2
print(var)
var *= 3
print(var)
print('---------------------------------------------------------------------------------------------------------------')
#                            Operadores de Comparacion
print('                      Operadores de Comparacion')
a = 5
b = 4
#para comparar:
resultar = (a == b) #se usa "==" para comparar dos valores (¿es a igual a b?. dependiendo del resultado sera falso o verdadero
print(resultar)
resultar = (a != b) # ¿es a diferente de b?
print(resultar)
#mayor, menor que (<,>). mayor igual, menor igual (<=,>=)
resultar = (a >= b)
print(resultar)
print('---------------------------------------------------------------------------------------------------------------')
#                         Operadores logicos en python
print('                  Operadores logicos en python')
# and -> los operadores tiene que ser todos verdadero para que devuelva verdader
# or -> con ta soo un operador verdader devueve verdadero
# not -> si algunos de los operadores es falso, devuelve verdadero
# actividad, usando los operadores logicos realizar un programa que diga si tu edad se encuentra entre los 20s o 30s
edad = int(input('Dame tu edad: '))
if edad >= 20 and edad < 30:
    print("tu edad se encuentra entre los 20's")
elif edad >= 30 and edad < 40:
    print("tu edad se encuentra entre los 30's")
else: print("tu edad NO se encuentra en niguna de estas dos")


