# Para crear nuestras vistas lo debemos hacer mediante requests (peticiones) y el servidor nos madara un http respondiendo con la informacion
# solicitada, para eso necesitamos importar httpreponse.
from django.http import HttpResponse
import datetime #importamos datime para trabajar con fechas
from django.template import Template,  Context
from django.template import loader
from django.shortcuts import render

# Creamos nuestra primeras vistas. se hacen en funciones y siempre el primero paraetro es el request
def saludo(request):
    return HttpResponse("Hola mundo!. Aprendiendo Django!.")

def hasta_luego(request):
    return HttpResponse("No vemos luego!.")

# Para trabajar con parametros, debemos pasarla por parametros de las vistas y trabajar con ellas, inclusive podemos crear un documento html 
# para esto

# vista para que calcule la edad que tendre en un año futuro dado dos valores, la edad actual y el año futuro

def edadFutura(request, edad, anio_futuro):

    anio_actual = int(str(datetime.date.today()).split('-')[0])
    edad_furura = edad + (anio_futuro - anio_actual)
    documento = f"""
    <html>
        <body>
            <h2>
                Tu edad actual es {edad} y en el año {anio_futuro} tendras {edad_furura}
            </h2>
        </body>
    </html
    """

    return HttpResponse(documento)


# Ahora usaremos las vistas con plantillas. basicamente las plantilas son documentos externos que nos ayudar a cargar o mostrar la interfaz de las
# vistas. por ejemplo un documento html es una plantilla

def ver_plantilla(request):
    
    # Usamos with para abrir el archivo
    with open(r'C:\Users\Johan\Desktop\Universidad\Notas_Programacion\Django\Proyecto1\Plantillas\plantila.html', 'r') as plantilla:

        # Creamos un objeto tipo template que lea el archivo o docemento 
        plt = Template(plantilla.read())
        # Creamos un contexto, un contexto son los datos adicionales para el template o plantilla (variables, funciones), por ejemplo
        # cuanod creamos una vista dinamica como lo hicimos anteriormente. si no lo necesitaos datos adicionales, igualmente hay que crear
        # el contexto
        ctx = Context()

        # Renderizamos el template pasandole como parametro el contexto y guardandolo en una variable para retornarlo con el http
        doumento = plt.render(ctx)

        return HttpResponse(doumento)

# Claramente tambien podemos mandar valores o parametros a las plantillas, ya sea valores de variable comunes (numeros, string, etc) o valores
# de objetos (atributos, metodos, etc). para demostrar esto, creemos una clase Persona y con los atributos trabajamos una plantilla

class Persona():
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido
    


# creesmo nuestra vista para trabajar con este objeto.

def platilla_con_valores(request):
    # Creamos nuestra persona para trabajar con sus atributos
    persona1 = Persona("Johan", "Robles")
    # un objeto que me retornara la fecha de hoy
    fecha_hoy = datetime.datetime.now()

    # Abrims la plantilla con with
    with open(r'C:\Users\Johan\Desktop\Universidad\Notas_Programacion\Django\Proyecto1\Plantillas\plantilla2.html', 'r') as html:
        
        plantilla = Template(html.read())
        # Ahora en el conetcto, le dembemos pasar los valores con el que trabaja la plantilla esto lo hacemos mediante un diccionario de pytho
        # o mas bien en formato JSON. estonces los key seran string y los values seran los valores o ente caso son lo objetos y/o atributos 
        contexto = Context({
        # pasamos los atributos de persona 1 con un key y values cada respectivamnete
        "nombre": persona1.nombre, 
        "apellido": persona1.apellido,
        # pero tambien podemos mandar un objeto y trabajar desde la plantilla con sus atribitos o metodos.
        "fecha": fecha_hoy,
        "temas": ["Vistas", "Urls", "Backend", "Formularios", "Django"]
        # Para accerder a los valores o atributos de cualquier objeto en la plantilla siempre es con el .valor, asi si queremos
        # accder a los indices de una lista lo hacemos mediante .indice
        })
        # Entonces la forma de llamar estos valores en la plantilla es usar {{valor}} y desde hay podemos o simplemento llamar el valor o jugar
        # con sus atributos. (ver plantilla2.html)

        # notar que en la plantilla (ver plantilla) podemos usar acciones o operdores de un lenguaje de programacion, bueno, usamos estos
        # para iterar por cada valores de la lista temas y nos lo muestre como una lista desordenada y en caso de que la lista no tenga nada
        # entonces nos mostrara un parrafo informandonoslo.

        documento = plantilla.render(contexto)

        return HttpResponse(documento)

# Ahora, podemos trabajar con archivos sin necesidad de usar a cada rato open y luego cerrarlo, (esto nos lleva "mucho" codigo), lo que
# haremos es usar un metodo de temple llamada loader, donde desde TEMPLATES del archivo setting.py podemos cargar nuetras plantillas.
# para esto primero debemos ir a TEMPLATES y indicarle la ubicacion de la carpeta de nuestras plantillas. tenemos que importar el modulo loader
def plantilla_con_loader(reques):# Creamos nuestra persona para trabajar con sus atributos
    persona1 = Persona("Johan", "Robles")
    # un objeto que me retornara la fecha de hoy
    fecha_hoy = datetime.datetime.now()

    
    # Para "leer" la plantilla usamos get_template
    plantilla = loader.get_template("plantilla2.html")
    # OJO ahora este template es DIFERENTE al template que estabamos usando anteriormnete. si queremos renderizar este template, no debemos
    # pasar un objeto tipo contexto ya que este no lo recibe asi, solo necesitamos pasar el diccionario con los valores que la plantilla
    # trabajara
    documneto = plantilla.render({"nombre": persona1.nombre, "apellido": persona1.apellido,"fecha": fecha_hoy,"temas": ["Vistas", "Urls", "Backend", "Formularios", "Django"]})

    return HttpResponse(documneto)



# Bien, podemo aun simplificar MAS la crecion del template, renderizado de una vista, esto lo hacemos con el modulo render de shorcut
# ademas, lo veremos concatenando una plantilla con otra (en una aplicacion web esta conformada asi, por varias plantillas) pero esto 
# se hace desde el html de la plantilla al cual queremos concatenar plantilla.

def shorcutRender_subPlantillas(request):

    # Usando el metodo render pdemos simplificar significativamente el codigo para usar una plantilla en una vista. los parametros minimos
    # que necesista este modulo de shorcuts es el request (obviamente) y el archivo, si queremos le pasamo el contexto y demas parametros.
    # Notar que NO necesitamos el http response pues este ya viene internamente en el render. 
    return render(request, "plantilla3.html", {"nombre": "Johan", "apellido": "Robles"})

    # Ademan notar que en la plantilla 3 se le esta concatenando otro archivo (ver plantilla 3 y barra)


# Podemos crear plantillas PADRES de tal manera que sus hijos hereden secciones o caracteristicas de estas, todo este codigo de herencia y demas
# se hace en los archivos y no en codigo, asi que ver los archivos padre.html, hija1.html, hija2.html

def hija1(request):
    return render(request, "hija1.html")

def hija2(request):
    fecha_hoy = datetime.datetime.now()
    return render(request, "hija2.html", {"fecha": fecha_hoy})