from django.db import models
from django.forms import BooleanField, CharField, DateField, EmailField, IntegerField

# Create your models here.

# En esta pestaña de models van las tablas sql de nuestra app. para crear tablas en django cn sql
# se hace como si crearamos clase (heredadas de models.Model) lo cual hace mas sencillo
# la creacion de estas en django

class Clientes_Tienda(models.Model):
    # Ahora, para crear las colmnas de cada nombre, el nombre de la variable sera el nombre de la
    # columna, y le indicamos el tipo de dato con el metodo (Tipo_Dato)Field(parametros si es necesario)
    Nombre = models.CharField(max_length=30)
    Direccion = models.CharField(max_length=100, verbose_name="La Direccion") # Con verose_name le podemos definir como aparecer el nombre de esta casilla cuando insertamos registros a este modelo desde el administrador de django
    Email = models.EmailField(blank=True, null=True) #Este metod es genial ya que viene con una expresion regular internamnete que obliga ingresar un email en formato correcto
    # Usamo blank y null en true, esto nos permite que no es necesario o obligatorio introducir un email al crear clientes.
    Telefono = models.CharField(max_length=10)

class Articulos_Tienda(models.Model):
    Nombre = models.CharField(max_length=30)
    Seccion = models.CharField(max_length=30)
    Precio = models.IntegerField()

    # Con este metodo podemos ver informacion de las consultas cuando usamos .query.__str__().
    # Pero como estamos modificando estos modelos, debemos consolidarlas, es decir, hacer makemigrations y migrate
    def __str__(self) -> str:
        return f"Nombre: {self.Nombre}, Seccion: {self.Seccion}, Precio: {self.Precio}"

class Pedidos_Tienda(models.Model):
    Numero = models.IntegerField()
    Fecha = models.DateField()
    Entregado = models.BooleanField()

# Cabe aclarar, y es que cuando importamos/migramos estas tablas a la base de datos, django le crea una columna por defecto llamado id
# el cual lo asigna como primary key.

# Ahora, Debemos realizar las migraciones (en la terminal), usamos makemigartions para Consolidar las tablas creadas
# Usamos manage.py makemigrations. nos debe salir algo como
#   GestionPedidos\migrations\0001_initial.py
#     - Create model Articulos
#     - Create model Clientes
#     - Create model Pedidos
# El numero de la direccion es muy importante, ese el numero de control. ahora hagamos el codigo sql para crear esas tablas en la base de datos
# usamos sqlmigrate + app + numero de control de la migracion anterior. usamos python manage.py sqlmigrate GestionPedidos 0001
# Nos genera el codigo sql de postgres para crear las tablas

# BEGIN;
# --
# -- Create model Articulos
# --
# CREATE TABLE "GestionPedidos_articulos" ("id" bigserial NOT NULL PRIMARY KEY);
# --
# -- Create model Clientes
# --
# CREATE TABLE "GestionPedidos_clientes" ("id" bigserial NOT NULL PRIMARY KEY);
# --
# -- Create model Pedidos
# --
# CREATE TABLE "GestionPedidos_pedidos" ("id" bigserial NOT NULL PRIMARY KEY);
# COMMIT;

# Por utimos usamos migrate para crear la tabla en la base de datos postgresql. python manage.py migrate
# Ahora vemos que en la base de datos donde le indicamos donde crear las tablas, estan la tablas con sus reespectivas
# colunas y el id que creo django por defecto.


# Ahora, podemos insertar, eliminar o acttualizar registros en nuestros modelos, pero esto lo hacemos en la terminal
# Primero debemos abrir el shell de python en la app e importar el modelo a modificar.

# python manage.py shell
# from GestionPedidos.models import Articulos

# Para insterta, cremos una variable o un objeto del modelo al que queremos insertar, pasarle los parametros de los registro y
# luego usaar save, o bien, en vez de save, usar object.create...

# art1 = Articulos_Tienda(Nombre="Cama", Seccion="Hogar", Precio = 5000000)
# art1.save()

#  art2 = Articulos_Tienda.objects.create(Nombre = "Mesa", Seccion = "Hogar", Precio = 80000)
# art3 = Articulos_Tienda.objects.create(Nombre = "Televisor", Seccion = "Electrodomestcios", Precio = 1200000)

# Para actualizar un rgistro, es como si fuermamo a cambiar el atributo a aun objeto
# art2.Precio = 100000

# Para eliminar un registro debemos en una variable obtener los registros a eliminar (con object.get(criterio)) y a esa variable, aplicar delete
# In [11]: arteliminar = Articulos_Tienda.objects.get(id=2)
# In [12]: arteliminar.delete()
# Out[12]: (1, {'GestionPedidos.Articulos_Tienda': 1})

# Ahora si vamos a postgesql y colocamos la consulta SELECT * FROM "GestionPedidos_articulos_tienda"
# Vemos como quedo la tabla


# [Agregamos mas campos en articulos_tienda]

# para aplicar where desde django (terminal) debemos usar el metodo filter(filtros) de objects
# Articulos_Tienda.objects.filter(Seccion = "Deporte")
# <QuerySet [<Articulos_Tienda: Nombre: Camiseta Real Madrid, Seccion: Deporte, Precio: 10000>, <Articulos_Tienda: Nombre: Balon, Seccion: Deporte, Precio: 25000>]>

# Articulos_Tienda.objects.filter(Seccion = "Deporte", Precio = 10000)
# <QuerySet [<Articulos_Tienda: Nombre: Camiseta Real Madrid, Seccion: Deporte, Precio: 10000>]>

# si queremos usar los >= o <=, seria __gte y __lte respectivamente, o si es para >, < seri __gt y __lt
# In [6]: Articulos_Tienda.objects.filter( Precio__gte= 2000000)
# Out[6]: <QuerySet [<Articulos_Tienda: Nombre: Cama, Seccion: Hogar, Precio: 5000000>, <Articulos_Tienda: Nombre: Computador, Seccion: Electrodomestcios, Precio: 3000000>]>

# Articulos_Tienda.objects.filter( Precio__lte= 2000000)
# Out[7]: <QuerySet [<Articulos_Tienda: Nombre: Televisor, Seccion: Electrodomestcios, Precio: 1200000>, <Articulos_Tienda: Nombre: Nevera, Seccion: Electrodomestcios, Precio: 1850000>, <Articulos_Tienda: Nombre: Camiseta Real Madrid, Seccion: Deporte, Precio: 10000>, <Articulos_Tienda: Nombre: Balon, Seccion: Deporte, Precio: 25000>, <Articulos_Tienda: Nombre: Mesa, Seccion: Hogar, Precio: 50000>]>

# Para ordenar usamos order_by(parametro) o order_by(__parametro) si lo queremos de manera descendente

# In [10]: Articulos_Tienda.objects.order_by("Precio")
# Out[10]: <QuerySet [<Articulos_Tienda: Nombre: Camiseta Real Madrid, Seccion: Deporte, Precio: 10000>, <Articulos_Tienda: Nombre: Balon, Seccion: Deporte, Precio: 25000>, <Articulos_Tienda: Nombre: Mesa, Seccion: Hogar, Precio: 50000>, <Articulos_Tienda: Nombre: Televisor, Seccion: Electrodomestcios, Precio: 1200000>, <Articulos_Tienda: Nombre: Nevera, Seccion: 
# Electrodomestcios, Precio: 1850000>, <Articulos_Tienda: Nombre: Computador, Seccion: Electrodomestcios, Precio: 3000000>, <Articulos_Tienda: Nombre: Cama, Seccion: Hogar, Precio: 5000000>]>