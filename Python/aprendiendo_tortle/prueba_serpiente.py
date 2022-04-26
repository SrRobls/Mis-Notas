import turtle, time, random

from numpy import Infinity

# creamos esta variable para que el el ciclo del juego vaya mas rapido o mas lento acorede a este juego (si posponer es un numero menor entonces el
# juego ira mas rapido si posponer es un numero mayor entonces mas lento)
posponer = 0.05

ventana = turtle.Screen()
ventana.bgcolor('black')
ventana.title('Prueba_Snake')
# usamos ventana.setup(height = x, width = y) para redimensionar el tamañao de la pantalla
ventana.setup(height = 420, width = 420)
# para que la aninmaciones dentro dela ventana sean visulamente mejor para nosotros
# ventana.tracer(1, 1)

# CABEZA DE LA SERPIENTE:
# configuracion de la serpiente (objeto que controlara el usuario)
snake = turtle.Turtle()
velocidad = 1
snake.speed(velocidad)
snake.color('red')
# Usamos shape para cambiar la forma de la serpiente a circulo
snake.shape('circle')
# usamos penup para quitar el reastro que deja el puntor,al moverse
snake.penup()
snake.shapesize(outline=12)
# usamos goto para inicializar la serpiente en el cenrtro
snake.goto(0, 0)
direccion = 'Stop'

# MANZANA/COMIDA DE LA SERPIENTE:
comida = turtle.Turtle()
comida.color('#ff44cb')
comida.shape('circle')
comida.speed(0.1)
comida.penup()
x = random.randint(-200, 200)
y = random.randint(-200, 200)
comida.goto(x, y)

# PUNTAJE:
puntos = 0
puntaje = turtle.Turtle()
puntaje.color('white')
puntaje.penup()
puntaje.speed(0)
puntaje.goto(0, 190)
puntaje.ht()
puntaje.write(f'Puntos: {puntos}              Puntaje Maximo: 10', align="center", font=(25))

# CUERPO DE LA SERPIENTE:
# la metodologia que vamos a usar es crear nuevos punteros que se sigan a si mismas, por ejemplo. si tenemos 3 segmentos de cuepo entonces el
# segmeneto 3 seguira al 2, el 2 al 1 y el 1 a la cabeza de la serpiente (es decir, el obkjeto snake)
cuerpo = []

# funciones para que la direccion cambie respecto al boton del teclado que se presione
def arriba():
    global direccion
    direccion = 'Up'

def abajo():
    global direccion
    direccion = 'Down'

def izquierda():
    global direccion
    direccion = 'Left'
    
def derecha():
    global direccion
    direccion = 'Right'

# Movimiento de la serpiente. esta funcion ira dentro del ciclo del juego, pues dependiendo de la direccion del snake, este se movera hacia 
# esa direccion
def movimientos():
    global direccion
    if direccion == 'Up':
        y = snake.ycor()
        snake.sety(y + 20)

    if direccion == 'Down':
        y = snake.ycor()
        snake.sety(y - 20)

    if direccion == 'Left':
        x = snake.xcor()
        snake.setx(x - 20)        

    if direccion == 'Right':
        x = snake.xcor()
        snake.setx(x + 20)

# esto es importante. con listen le estamos diciendo a la pantalla cuando se abre que este pendiente cuando se presiona un botton del 
# teclado para ejecutar un codigo y con onkeypress(funcion, botton) que sirve para cuando se oprima un teclado (arriba, abajo, izquierda o derecha)
# se ejecute la funcion para cambiar la direccion del snake.
ventana.listen()
ventana.onkeypress(arriba, 'Up')
ventana.onkeypress(abajo, 'Down')
ventana.onkeypress(izquierda, 'Left')
ventana.onkeypress(derecha, 'Right')

# creamos un clclo donde basicamente ocurrirra todos los eventos del juego, tener en cuenta que todos los juegos tiene un ciclo principal donde este corre
# que termina hasta cumplir cierta condiccion y terminar el juego
while True:

    ventana.update()


    # Si el snake choca con las paredes, entonces se reinicia el juego.
    if snake.xcor() == -200 or snake.xcor() == 200 or snake.ycor() == -200 or snake.ycor() == 200:
        velocidad = 1
        snake.speed(0)
        time.sleep(1)
        for i in range(largo_cuerpo):
            cuerpo[i].ht()
            cuerpo[i].clear()
        cuerpo = []
        puntos = 0
        puntaje.clear()
        puntaje.write(f'Puntos: {puntos}              Puntaje Maximo: 10', align="center", font=(25))
        snake.goto(0,0)
        snake.speed(velocidad)
        direccion = 'Stop'
    
    #   Si el snake colisiona con su propio cuerpo
    if any(snake.distance(segmento) < 10 for segmento in cuerpo):
        velocidad = 1
        snake.speed(0)
        time.sleep(1)
        for i in range(largo_cuerpo):
            cuerpo[i].ht()
            cuerpo[i].clear()
        cuerpo = []
        puntos = 0
        puntaje.clear()
        puntaje.write(f'Puntos: {puntos}              Puntaje Maximo: 10', align="center", font=(25))
        snake.goto(0,0)
        snake.speed(velocidad)
        direccion = 'Stop'

    # Si el snake come, entonces crece
    if snake.distance(comida) < 20:
        puntos += 1
        # Cuando Ganemos!:
        if puntos == 10:
            puntaje.clear()
            puntaje.goto(0,0)
            puntaje.write('Ganaste!!', align="center", font=("Courier", 30, "normal"))
            break

        # generamos otra manzana aleatoriamente dentro de la pantalla
        x = random.randint(-190, 190)
        y = random.randint(-190, 190)
        comida.goto(x, y)
        # cada vez que la serpiente come, entonces va mas rapido. esto lo hacemos para que los frames sea mejor visualmente
        snake.speed(velocidad)
        velocidad += 0.5
        puntaje.clear()
        puntaje.write(f'Puntos: {puntos}              Puntaje Maximo: 10', align="center", font=(25))

        # Creacion del cuerpo de la serpiente:
        # creamos un nevo puntero, con color en un inicio negro (ya que el fondo es negro y por tanto en un principio no se notara en pantalla)
        # esto lo hacemos ya que cada puntero siempre inicia en la posicion 0,0 y si el colo fuera diferente del color de fonfo, entonces se mostraria
        # el puntero en pantalla moviendose hasta la cola del snake.
        # le damos las demas atributos.
        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.color('black')
        nuevo_cuerpo.shape('circle')
        nuevo_cuerpo.speed(0)
        nuevo_cuerpo.penup()
        nuevo_cuerpo.shapesize(outline=7)

        # agregamos cada puntero en nuestra lista cuerpo.
        cuerpo.append(nuevo_cuerpo)

        
     
    largo_cuerpo = len(cuerpo)
    # La idea para que el cuerpo de la serpiente aumente, es hacer que cada uno de los segmentos del cuerpo (los nuevos punteros creados) se sigan
    # uno detras del otro, es decir, un puntero sigue al puntero anteriormete creado
    for i in range(largo_cuerpo-1,  0, -1):
        x = cuerpo[i-1].xcor()
        y = cuerpo[i-1].ycor()
        cuerpo[i].goto(x, y)
        # una vez ya este en la cola, le cambiamos el color
        cuerpo[i].color('#ff706b')
    
    # el codigo anterior solo funciona para los punteros diferentes al primer puntero o segmento_de_cuerpo, pues este primero puntero no tiene
    # a otro puntero de la lista cuerpo al cual seguir, entonces hacemos que siga a la cabeza del snake. es decir, al puntero snake
    if largo_cuerpo > 0:
        x = snake.xcor()
        y = snake.ycor()
        cuerpo[0].goto(x, y)
        cuerpo[0].color('#ff706b')

    
    movimientos()
    # time.sleep(posponer)














turtle.done()