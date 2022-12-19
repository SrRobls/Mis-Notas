import email
from django.http import HttpResponse
from django.shortcuts import render
from GestionPedidos.models import Articulos_Tienda
# from django.core.mail import BadHeaderError, send_mail
# from django.views.decorators.csrf import csrf_protect
from GestionPedidos.formuarios import FormularioContacto

# Create your views here.

# Creamos una vistta donde el template pide un articulo y lo mandamos a servidor para que tranaje con ella
def busqueda_formulario(request):

    return render(request, "Busqueda_Productos.html")

# Ahora bien, el request es basicamente la peticion (o informacion de la peticion) que les estamos mandando al servidor, por tanto, una vez recibida
# por el servido, el servidor debe mandar una respuesta (ya sea una vista o etc)

# Entonces el parametro request de buscar es la informacion de la peticion que le manda la vista busqueda_formulario, y por tanto, ahora
# el servidor (o la vista) le manda otra vista (en este caso) y/o peticion trabajando con la peticion enviada
def buscar(request):

    if request.GET['Articulo']: #Comprobamos si se recibe una peticion con el metodo GET y si es algo, entonces obtenemos el valor, y con eso 
        # hacemos la consulta desde django a la base de datos y obtenemos el resultado/s
        articulo_a_buscar = request.GET['Articulo']
        articulos = Articulos_Tienda.objects.filter(Nombre__icontains = articulo_a_buscar)
        return render(request, "respuesta_busqueda.html", {"articulos":articulos, "consulta":articulo_a_buscar})
    # En casode que el usario no envio valor, entonces hacemos...
    else:
        return HttpResponse("No se envio ningun articulo a buscar")
    # Obtenemos la informacion que nos manda la vistar anterior mediante el GET. prueba
    # mesaje_verificacion = f"Articulo que se busca: {request.GET['Articulo']}"
    # return HttpResponse(mesaje)


# Creemos una vista de contacto (formulario)
# @csrf_protect
# def contacto(request):
    
#     if request.method == "POST":
#     #     subject = request.POST.get('Asunto')
#     #     message = request.POST.get('mensaje')
#     #     email = request.POST.get('correo')
#     #     send_mail(subject, message, email, ['johanrobles600@gmail.com'])
#     # Lo anterior era para enviar mensaje a los correro, pero no se pudo ya que los emails no permiten accesoa aplicaciones desconocidas

#         return HttpResponse("Mensaje enviado, Muchas Gracias!")

#     return render(request, "contacto.html")

# Pero otra forma usando librearia para hacer formularios de python seria

def contacto2(request):
    # La idea es que cuando se entre a esta vista, verifiquemos si se ha mandado informacion con el metodo post, si no es asi, entonces
    # significa que se entro a la vista para llenar informacion e enviar, en caso de que si, significa que ya se lleno la informacion
    # y al darle enviar llamamos esta misma vista y entra en el condicional que verifica si mandamos con el metodo post
    # posteriormnete, trabajamos con la informacion suministrada.

    if request.method == "POST":
        # return HttpResponse("mensaje obtenido")
        formulario = FormularioContacto(request.POST) #  creamos (otra vez) el objeto pasandole la informacion del post (esto, intuyo ue mediante
        # el formato json, ya que es bastante parecido a un diccionario de python)
        # print(request.POST)
        if formulario.is_valid(): #verficiamos si el formulario es valido, es decir, los inputs estan bien formateados
            informacion = formulario.cleaned_data #para obtener en formato diccionario lo valores de los inputs, accedemos con ellos con los values como keys
            return render(request, "resultado_formulario.html", {"asunto": informacion["asunto"], "email":informacion["email"], 
            "mensaje": informacion["mensaje"]})

    formulario = FormularioContacto()
    return render(request, "contacto2.html", {"formulario": formulario})



