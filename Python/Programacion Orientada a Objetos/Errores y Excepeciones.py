# https://docs.python.org/es/3/tutorial/errors.html

# Podeos gestionar errores de excepcion de la siguiente manera:
print('Si quiers terminar coloca -1')
x = 0
while True:
    try:
        #Aca va el codio que quiero interntar
        x = int(input())
    except ValueError: #Si se come este erroe de excepcion en concreto, printeamos lo siguiente y continuamos la iteracion (Notar que no se termina el codigo por este error)
        print('Uy, introdiciste un valor invalido. vueleve a intentarlo!')
    if x == -1:
        break

# Basicamente con try y excep la idea es ejecutar un codigo y si por alguna razon se comete un arreor de excepcion por parte del ususario
# en vez de mostrar la excepcion y terminar el codigo, podemos decirle que haga otra cosa y/o no termine el codio si no que ejecute lo que falta.
# esto lo podemos ver en ejemplo anterior

# tambien podemos 'prevernir' mas de una excepcion:
x = 0
while True:
    try:
        x = int(input())
        z = int(input())
        print(x/z)
    except (ValueError, ZeroDivisionError, TypeError):
        print('Cagaste pa')
        break

# Tambien podemos guarda el identificador de la excepcion

while True:
    try:
        x = int(input())
    except ValueError as error:
        print(f'Nonas comiste un error de tipo {error}')
        break

# Podemos forzas de que ocurrar una excepcion con raise:
# raise NameError('Holis')
# >>> File "c:\Users\Johan\Desktop\Universidad\Notas Programacion\Python\Errores y Excepeciones.py", line 3, in <module>
# >>> raise NameError('Holis')
# >>> NameError: Holis

# Tambien podemos que en try al final de que se ejecute el codigo dado haga lo que le digamos en finally:

try:
    x = int(input())
except ValueError as error:
    print(f'Ojo, cometiste el error {error}')
finally:
    print('Hemos salido del codigo') 

# Tambien, si usamos return, el return se queda con el utimo valor dado, es decir el del finally:
def bool_return():
    try:
        return True
    finally:
        return False
print(bool_return())
# >>> False

# Ejemlo:
def divide(x, y):
    try:
      result = x / y
    except ZeroDivisionError:
         print("division by zero!")
    else:
         print("result is", result)
    finally:
         print("executing finally clause")

# divide(2, 1)
# >>> result is 2.0
# >>> executing finally clause
# divide(2, 0)
# >>> division by zero!
# >>> executing finally clause
# divide("2", "1")
# >>> executing finally clause
# >>> Traceback (most recent call last):
# >>>   File "<stdin>", line 1, in <module>
# >>>   File "<stdin>", line 3, in divide
# >>> TypeError: unsupported operand type(s) for /: 'str' and 'str