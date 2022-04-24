
from nodos import Nodo

print('____________________________________________')

# Basicamente una circular linked list es una linked list pero de cierta forma ciclica es decir que el ultimo elmeneto de la serie de nodos 
# apunta al primero

# El 1er nodo -> 2do nodo, 2do nodo -> 3er nodo, 3cer nodo -> 1er nodo ...


# Para comenzar definamos un nodo que se referencie a si mismo
circularLinkedList = Nodo(1, None)
circularLinkedList.siguiente = circularLinkedList

# Agregemosles un valor
agregar = 5

# iteramos hastaque que enoconremos el nodo que tenga como referencia al primer nodo
pread = circularLinkedList
while pread.siguiente != circularLinkedList:
    pread = pread.siguiente

# una vez hecho lo anterior, hacemos que el nodo que tenia como siguiente al primero ahora tenga como siguiente a un nuevo nodo que apuntara al
# primer nodo.
pread.siguiente = Nodo(agregar, circularLinkedList)
pread = pread.siguiente

# creeemos mas nodos:
for i in range(3):
    pread.siguiente = Nodo(i, circularLinkedList)
    pread = pread.siguiente

pread = pread.siguiente


# como veremos ya se tiene una circular linked list, notar que por mas que iteremos por los valores de la serie de nodos nunca va a terminar
# pues es ciclica
print(pread.valor)
print(pread.siguiente.valor)
print(pread.siguiente.siguiente.valor)
print(pread.siguiente.siguiente.siguiente.valor)
print(pread.siguiente.siguiente.siguiente.siguiente.valor)
print(pread.siguiente.siguiente.siguiente.siguiente.siguiente.valor)
print(pread.siguiente.siguiente.siguiente.siguiente.siguiente.siguiente.valor)
print(pread.siguiente.siguiente.siguiente.siguiente.siguiente.siguiente.siguiente.valor)
print(pread.siguiente.siguiente.siguiente.siguiente.siguiente.siguiente.siguiente.siguiente.valor)
# 1
# 5
# 0
# 1
# 2
# 1
# 5
# 0
# 1
...