import turtle, time

# creamos esta variable para que el el ciclo del juego vaya mas rapido o mas lento acorede a este juego (si posponer es un numero menor entonces el
# juego ira mas rapido si posponer es un numero mayor entonces mas lento)
posponer = 0.05

ventana = turtle.Screen()
ventana.bgcolor('black')
ventana.title('Prueba_Snake')
# usamos ventana.setup(height = x, width = y) para redimensionar el tamañao de la pantalla
ventana.setup(height = 700, width = 900)
# para que la aninmaciones dentro dela ventana sean visulamente mejor para nosotros
ventana.tracer(1, 1)

# configuracion de la serpiente (objeto que controlara el usuario)
snake = turtle.Turtle()
snake.speed(1)
snake.color('red')
# Usamos shape para cambiar la forma de la serpiente a circulo
snake.shape('circle')
# usamos penup para quitar el reastro que deja el puntor,al moverse
snake.penup()
# usamos goto para inicializar la serpiente en el cenrtro
snake.goto(0, 0)
direccion = 'Stop'

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
    if direccion == 'Up':
        y = snake.ycor()
        snake.sety(y + 10)

    if direccion == 'Down':
        y = snake.ycor()
        snake.sety(y - 10)

    if direccion == 'Left':
        x = snake.xcor()
        snake.setx(x - 10)        

    if direccion == 'Right':
        x = snake.xcor()
        snake.setx(x + 10)

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

    movimientos()
    time.sleep(posponer)















turtle.done()