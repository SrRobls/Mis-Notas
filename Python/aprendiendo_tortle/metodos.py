# creamos el ambiente turtle
import time, turtle
aprendiendo = turtle

# mmandamos a llamar la pantalla
aprendiendo.Screen()

# cambiar el color de fondo de la bantalla (por defecto viene en blanco), se lo cambiaremos a rojo
aprendiendo.bgcolor('red')

# Le poenmos un titulo
aprendiendo.title('Aprendiendo')

# puntor sera nuestro objeto que se movera, (basicamente nuestra tortuga)
puntor = turtle.Turtle()
# usamos speed(x) para dale una velocidad al puntor. cuando mas lejor de 1 es mas rapido y cuando mas cera mas lento
puntor.speed(1)
# podemos hacer que el puntor inicie/mueva en una posicion dada
puntor.setposition(30, 60)
# para cambiar el color del puntor
puntor.color('white')

# Hagamos que se mueva:


# usamos forward(x pixeles) para que se mueva x pixeles en su direccion (en un principio la direccion por defecto es hacia la dera o 0 grados.
# mas adelante veremos como cambiar la direccion)
puntor.forward(100)
# notar que el puntor deje un rastro cuando se mueve

# usamos right(x) para que el puntor tome rote x grados HACIAS LA DERECHA respecto a su posicion, tambien existe left() para rotar hacia la izuiqerda.  
puntor.right(90)
puntor.forward(100)

puntor.right(90)
puntor.forward(100)


puntor.right(90)
puntor.forward(100)

puntor.right(45)
puntor.forward(75)

puntor.right(93)
puntor.forward(75)
# creamos una casita !!!

# el puntor hace un circulo de radio x cuando usamos circle(x)
puntor.circle(100)
puntor.color('blue')
# usamos backward para hacer que el puntor se mueva hacia atras x pixeles
puntor.backward(100)

# usamos home para que el puntor se mueva a su punto de origen
puntor.home()


# Usamos done para no darel mas ordenes al puntor, despue de esta linea de codigo ya no se ejecturara ninguna linea de codigo de turtle
# tambien con done mantenemos la pantalla abierta hasta que el usuario la cierre
turtle.done()
# este codigo NO se ejecuta
puntor.forward(100)
aprendiendo.bgcolor('white')