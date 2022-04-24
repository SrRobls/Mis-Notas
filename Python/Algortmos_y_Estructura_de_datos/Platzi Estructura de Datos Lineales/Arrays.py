# creeemos nuiestra clase Array

class Array(object):

    # creamos su constructor donde recibe por parametro los slots del array y cada slot se rellena por defecto con un None si el usuario no 
    # indica el valor con el que se va a rellenar el array 
    def __init__(self, capacity, fill_value = None):
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)
    # Creacionh de los metodos

    # Para mostrar el len del array
    def __len__(self):
        return len(self.items)

    # Para imprimir la lista
    def __str__(self) :
        return str(self.items)

    # Para obtener el iterador
    def __iter__(self):
        return iter(self.items)

    # Para obtener el valor de un indice dado por parametro
    def __getitem__(self, index):
        return self.items[index]


    # Para remplazar un elemento por otro
    def __setitem__(self, index, new_item):
        self.items[index] = new_item

array1 = Array(5)
print(array1.__len__())
# >>> 5
print(array1)
# >>> [None, None, None, None, None]
print(array1.__iter__())
# >>> <list_iterator object at 0x0000018270FBBA30>

array1.__setitem__(0, 'Holis!')
print(array1)
# >>> ['Holis!', None, None, None, None]
array1.__setitem__(1, 500)
array1.__setitem__(2, 'Johan')
array1.__setitem__(3, 'Robles')
array1.__setitem__(4, 'Crack!')
print(array1.__str__())
# >>> ['Holis!', 500, 'Johan', 'Robles', 'Crack!']
print(array1.__getitem__(4))
# >>> Crack!