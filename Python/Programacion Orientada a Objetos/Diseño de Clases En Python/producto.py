'''
Para el diseño de clases (cuando las clases se relacionan y tal), es importante reconocer cual es la clase indenpendiente (que no necesiat
alobjeto instanciado de otra clase para funcionar). en este caso la clase Producto es la independiente (en este clase se crearan producto 
con los atributos como la id, nombre y precio) y la clase Canasta es la dependiente (en esta clase dada una lista de los productos creara 
una objeto canasta con atributos como el identificado de la canasta, el total de la lista y el costo total de la lista segun los precios de 
los productos.) 

En este ejercicio no es necesario usar los conceptos de herencia
'''


class Producto():
    # Nuestro contador/id, que crecera a medida que haya mas objetos producto y estos tendran como atributo el valor de esta id cuando se genero el
    # objeto
    id = 0

    # definimos un metodo de clase para amentar el valor de esad id cuando se cree un nuevo objeto
    @classmethod
    def _aumentar_id(cls):
        cls.id += 1
        return cls.id
    
    def __init__(self, nombre, precio) -> None:
        # definimos los atributos y llamamos al metodo que hace crecer al id cada vez que se creen un objeto.
        self._ident = Producto._aumentar_id()
        self._nombre = nombre
        self._precio = precio
    
    # decoradores GET para los atributos encapsulados, solo harenos este ya que solo se podra obtener el valor del atributo pero no modificarlo
    @property
    def ident(self):
        return self._ident
    

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def precio(self):
        return self._precio
    
    def __str__(self) -> str:
        return f'Identificador: {self._ident}, Nombre: {self._nombre}, Precio: {self._precio} Pesos'

# Pruebas:
if __name__ == '__main__':
    producto1 = Producto('Pan', 300)
    producto2 = Producto('Pasta', 1700)
    producto3 = Producto('Queso', 4000)

    print(producto1)
    # Identificador: 1, Nombre: Pan, Precio: 300 Pesos
    print(producto2)
    # Identificador: 2, Nombre: Pasta, Precio: 1700 Pesos
    print(producto3)
    # Identificador: 3, Nombre: Queso, Precio: 4000 Pesos

    print(producto1.ident)
    # 1
    print(producto1.nombre)
    # Pan
    print(producto1.precio)
    # 300