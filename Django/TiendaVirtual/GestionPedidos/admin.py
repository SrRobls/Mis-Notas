from django.contrib import admin
# Debemos importar los modelos para que luego podamos interactuar con ellas en el adminstrador
from GestionPedidos.models import Clientes_Tienda, Pedidos_Tienda, Articulos_Tienda

# En esta pestaña es la adminitrador que nos ofrecer django, para acceder a ella se debe correr el servidor e ir a localhost/admin/
# Ya esta la vista por defecto en los urls. PERO para acceder al administrador debemos teber un superusuario, para eso lo creamos
# en la terminal

# python manage.py createsuperuser

# Una vez creado el super usuario, podemos ingresar a la administrdro, donde podemos gestionar usuarios, modelos, ect.

# Register your models here.

# Creamos una clase que herede de admin.ModelAdmin para que nosotros en el administrador tengamos mas informacio o intercatuamos mas
# con los registros de un modelo
class ClientesAdmin(admin.ModelAdmin):
    # Usamos list_display, para que cuando nos muestre informacion de los registros, nos muestre por Nombre y Telefono (por defecto, no es asi, si no, diferente)
    list_display = ("Nombre", "Telefono")
    # Usamos search_files para agregar un buscador que nos ayudara a encontrar registros del modelo, segun el parametro que le indiquemos
    # es importante, que en caso de que solo queramos que tome un criterio/columna, entonces se lo pasamos en una lista, si son mas una tupla de los valores 
    search_fields = ["Nombre"]

class ArticulosAdmin(admin.ModelAdmin):
    list_display = ("Nombre", "Seccion", "Precio")
    # Le podemos agregra un filtrador al trabajar con modelos desde el administrador, para esto usamos list_filter y le pasamos el criterio
    # o columna por el cual filtrar. Notar que nos permite filtrar por cada uno de los valores diferentes del criterio.
    list_filter = ("Seccion",)

class PedidiosAdmin(admin.ModelAdmin):
    list_display = ("Numero", "Fecha", "Entregado")
    date_hierarchy = "Fecha" #Con este metodo podemos filtra de una forma diferente, ver administrador

# Ahora para registras los modelos y poderlos modificar o intercatuar hacemos
admin.site.register(Clientes_Tienda, ClientesAdmin) # Adicional le pasamos el admin class ClientesAdmin para intercatuar mas con este modelo en el administrador
admin.site.register(Pedidos_Tienda, PedidiosAdmin)
admin.site.register(Articulos_Tienda, ArticulosAdmin)
# Ahora si vamos al admnistrador, podemos intercatuar con ellaas como agregando eliminando registros de cada una. y cada registr que creemos,
# eliminemos, etc. se veran reflejados en la base de datos.





# Por utimos como superusuarios, podemos crear otro usuarios, (ya sean super, staff o no) en el cual le podemos dar permisos
# como acceder a los modelos y demas entre otras funcionalidades.
# https://www.youtube.com/watch?v=7yZCxwwfTk4&list=PLU8oAlHdN5BmfvwxFO7HdPciOCmmYneAB&index=20