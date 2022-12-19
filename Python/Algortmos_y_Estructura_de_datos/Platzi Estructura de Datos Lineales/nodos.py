# Un nodo sirve para almacenar un valor  y ese nodo tiene un puntero que referenciara o llevara a otro nodo que almacena otro valor,
# podemos ver a los nodos como los elementos de una lista pero la diferencia es que los valores de los nodos no estan ubicados en el mismo
# lugar de memoria (como con los valores de la lista) si no en diferentes lugares de memoria, lo cual el puntero del nodo es el encargado
# para referenciar el lugar de memoria de otro nodo.

# Es muy útil al tener infromación dispersa en memoria y cuando queremos que sean consultas ágiles, es importante entender 
# que los nodos son la base para implementaciones más elaboradas de estructuras de datos, Stacks, Qeues, Deque, Doubly, Singly List, 
# Circular list, Graphs.

# Creemos nuestra clase nodo



class Nodo(object):
    # El atributo valor es donde se almacenara el valor del nodo y el atributo siguente es el puntero del nodo para referenciar a otro nodo.
    def __init__(self, valor, siguente = None) -> None:
        self.valor = valor
        self.siguiente = siguente

nodo0 = None
nodo1 = Nodo('A', None)
# Colocamos como parametro siguiente a None porque este nodo1 no tiene un nodo que le siga, es decir, seria el ultimo nodo de la serie de nodos
print(nodo1)
# <__main__.Nodo object at 0x0000018E1BCAADA0>
print(nodo1.valor)
# A
print(nodo1.siguiente)
# None

# Creemos nodos que se 'enlacen':
nodo2 = Nodo('B', nodo1)
print(nodo2.valor)
# B
print(nodo2.siguiente)
# <__main__.Nodo object at 0x0000025379A97D60>
print(nodo2.siguiente.valor)
# A
# Asi creamos un nodo2 con un valor 'B' y que referencia a su siguiente nodo nodo1.
# Ahora unamos a los tres nodos nodo0, nodo1 y nodo2

# print(nodo0.valor)
# AttributeError: 'NoneType' object has no attribute 'valor
nodo0 = Nodo('C', nodo2)
print(nodo0.valor)
# C
print(nodo0.siguiente.valor)
# B
# Aca accedemos al valor del siguiente del siguiente nodo de nodo0
print(nodo0.siguiente.siguiente.valor)
# A
# Asi Nodo0 con valor 'C' hace referencia a su siguiente nodo el nodo2 con valor 'B' que hace a referencia a nodo1 con valor 'A' que hace referencia a None, es deicr a ninun otro nodo
print('----------------------------------------------------------------------------------------------------------------------------------------')
# Ahora creemos una serie de nodos:

# creamos a head con valor inicial None, head va aser nuestra serie de nodos.
head = None
for i in range(1, 6):
    # Creamos la serie de nodos en la cual el valor va a ser el valor de i y el nodo/nodo siguiente sera el valor o el nodo anteriormente creado
    # En el caso del nodo con valor i su nodo siguiente es None pues es el valor correspondiente de head al inicio 
    # Entonces basicamente el nodo con valor 1 y suigente None es nuestro ultimo nodo de la serie
    head = Nodo(i, head)

# (5, 4) -> (4, 3) -> (3, 2) -> (2, 1) -> (1, None)

print(head.valor)
# 5
print(head.siguiente.valor)
# 4
print(head.siguiente.siguiente.valor)
# 3
print(head.siguiente.siguiente.siguiente.valor)
# 2
print(head.siguiente.siguiente.siguiente.siguiente.valor)
# 1

while head:
    print(head.valor)
    head = head.siguiente
# 5
# 4
# 3
# 2
# 1