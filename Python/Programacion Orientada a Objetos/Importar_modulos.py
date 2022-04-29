# Podemos imporata modulos a parte de los que ya viene por defector en python. podemos
# importar la clase Persona que creanmos en el archivo Encapsulamiento_en_Python
from Encapsulamiento_En_Python import Persona

# y podemos crear objetoc con base a la clase que importamos
natalia = Persona('Natalia', 'Gomez', 25)
'''
natalia.mostrar_detalles()
Nombre: Johan, Apellido: Robles, Edad: 19.
Nombre: Sebas, Apellido: Robles, Edad: 19.
Nombre: Sebas, Apellido: Robles, Edad: 19.
Llamando a Get
Sebas
Llamando a Set
Llamando a Get
Johan
Llamando a Set
Llamando a Set
Llamando a Get
Laura
Rincon
13
Nombre: Laura, Apellido: Robles, Edad: 13.
Nombre: Natalia, Apellido: Gomez, Edad: 25.
'''
# Notar que tambien se imprime las pruebas que teniamos en nuestro modulo Encapsulamiento_En_Python. para corregir esto usamos el atributyo de python
# __name__, este atributo nos retornara '__main__' si ejecutamos alguna clase o fucnion que ejecutemos en el mismo archivo, o retornara
# el nombre del archivo si ejecuramos codigo proveniente pues de otro archivo (modulo, en nuestro caso Encapsulamiento_En_Python)

# Entonces debemos crear un condiciona enn uestro archivo Encapsulamiento_En_Python para que cuando __name__ == __main__ se ejecute le codigo, que
# se llamen dentro del modulo Encapsulamiento_En_Python, y si no es asi no se ejecute, por tanto, solo se ejecutara el que codigo que este en este archivo
# ver el archivo Encapsulamiento_En_Python:

# if __name__ == '__main__':
#    ...
# Una vez puesto eso en nuestro archimo del modulo que importado, ahora solo mostrara el codigo que creao aca
if __name__ == '__main__':
    print('Creacion de Objetos'.center(50, '-'))
    natalia = Persona('Natalia', 'Gomez', 25)
    natalia.mostrar_detalles()
    # Nombre: Natalia, Apellido: Gomez, Edad: 25.
    print('Eliminacion de Objetos')
    del natalia
    # El Objeto fue Eliminado: Natalia Gomez