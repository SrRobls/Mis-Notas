'''
El concepto del polimorfismo es crear clases de tal manera que los objetos instanciados usen los metodos que comparten pero de difrente forma dada
las cualidades del objeto en si, puede ser objetos de clases sin ninguna relacion o con relacion de herencia. EL usos de los metodos lo podemos
defir en funciones (como veremos) o no.
'''

from Empleado import Empleados
from Gerencia import Gerencia

def mostrar_objeto(objeto):
    # Imprimiremos el tipo de clase del objeto (Empleados o Gerencia), el nombre y el sueldo (estos atributos son heredados de Empleados a Gerencia)
    # imprimeremos tambien al metodo mostrar_detalles que es un metodo del padre Empleados pero como ya sabe que como la clase Gerencia
    # es hijo de esta clase entonces tambine lo puede usar. este metodo lo que hace es llamar el metodo __str__
    print(type(objeto))
    print(objeto.nombre)
    print(objeto.sueldo)
    print(objeto.mostrar_detalles())

    # Existe una funcion en python que pregunat si un objeto es instancia de una clase, este caso preguntaremos si el parametro objeto es 
    # instanciado del Gerencia y si es asi, entonces imprimimos ese valor, hacemos esto dado que empleados no posee este atributo
    if isinstance(objeto, Gerencia):
        print(objeto.gerencia)

# Creacion de los objetos, de la clase Empleado y otro de la clase Gerencia que tiene como padre a Empleado
objeto_empleado = Empleados('Guillermo', 7000000)
objeto_gerencia = Gerencia('Anna', 10000000, 'Sistemas')

mostrar_objeto(objeto_empleado)
# <class 'Empleado.Empleados'>
# Guillermo
# 7000000
# Empleado: [Guillermo 7000000]

mostrar_objeto(objeto_gerencia)
# <class 'Gerencia.Gerencia'>
# Anna
# 10000000
# Empleado: [Anna 10000000] Gerencia: [Sistemas]
# Sistemas