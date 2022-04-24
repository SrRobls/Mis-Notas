#                       Sentencia If/else
print('                 Sentencia If/Else')
num1 = int(input('Dame un numero: '))
num2 = int(input('Dame otro numero: '))

if num1 > num2:
    print(f'{num1} es mayor a {num2}') #Es importante la indentacion (los espacios antes de escribir codigo)
elif num1 == num2:
    print(f'{num1} es igual a {num2}') #elif es SiNo Si (es decir, otra condicion)
else:
    print(f'{num2} es mayor a {num1}') #SiNo si no se cumple la/s condicion/es anteriores se ejecuta este codigo
#Otra forma du usar la sentencia if/else es:
#("hacer algo") if condicion else ("hacer lo otro")
print(f'el numero {num1} es mayor a 5') if num1 > 5 else print(f'El numero {num1} No es mayor a 5')