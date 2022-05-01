from producto import Producto
'''
Para el diseño de clases (cuando las clases se relacionan y tal), es importante reconocer cual es la clase indenpendiente (que no necesiat
alobjeto instanciado de otra clase para funcionar). en este caso la clase Producto es la independiente (en este clase se crearan producto 
con los atributos como la id, nombre y precio) y la clase Canasta es la dependiente (en esta clase dada una lista de los productos creara 
una objeto canasta con atributos como el identificado de la canasta, el total de la lista y el costo total de la lista segun los precios de 
los productos.) 

En este ejercicio no es necesario usar los conceptos de herencia
'''
class Canasta():
    id = 0
    # definimos un metodo de clase para amentar el valor de esad id cuando se cree un nuevo objeto
    @classmethod
    def _aumentar_id(cls):
        cls.id += 1
        return cls.id

    def __init__(self, productos) -> None:
        self._iden = Canasta._aumentar_id()
        self._productos = list(productos)
    
    @property
    def iden(self):
        return self._iden
    
    @property
    def productos(self):
        return self._productos
    
    def añadir_producto(self, producto):
        self._productos.append(producto)

    def total_precio(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        
        return total
    
    def __str__(self) -> str:
        string = f'Canasta {self._iden}: \n'
        for producto in self._productos:
            string += '\t Identificador: ' + str(producto.ident) + ', Nombre: ' + producto.nombre + ', Precio: ' + str(producto.precio) + '\n'
        string += '\n\t Precio Total: ' + str(self.total_precio()) + ' Pesos'
        return string

if __name__ == '__main__':
    producto1 = Producto('Pan', 300)
    producto2 = Producto('Pasta', 1700)
    producto3 = Producto('Queso', 4000)

    canasta1 = Canasta([producto1, producto2, producto3])

    print(canasta1)
    '''
    Canasta 1: 
         Identificador: 1, Nombre: Pan, Precio: 300
         Identificador: 2, Nombre: Pasta, Precio: 1700
         Identificador: 3, Nombre: Queso, Precio: 4000

         Precio Total: 6000 Pesos
    '''
    producto4 = Producto('Jamon', 5000)
    producto5 = Producto('Dulce', 500)
    producto6 = Producto('Aceite', 2000)

    canasta1.añadir_producto(producto5)
    print(canasta1)
    '''
    Canasta 1:
         Identificador: 1, Nombre: Pan, Precio: 300
         Identificador: 2, Nombre: Pasta, Precio: 1700
         Identificador: 3, Nombre: Queso, Precio: 4000
         Identificador: 5, Nombre: Dulce, Precio: 500

         Precio Total: 6500 Pesos
    '''

    canasta2 = Canasta([producto3, producto5, producto1, producto4, producto2, producto6])
    print(canasta2)
    '''
    Canasta 2:
         Identificador: 3, Nombre: Queso, Precio: 4000
         Identificador: 5, Nombre: Dulce, Precio: 500
         Identificador: 1, Nombre: Pan, Precio: 300
         Identificador: 4, Nombre: Jamon, Precio: 5000
         Identificador: 2, Nombre: Pasta, Precio: 1700
         Identificador: 6, Nombre: Aceite, Precio: 2000

         Precio Total: 13500 Pesos
    '''