"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Desde este docuemnto llamaeremos nuestras urls o mejor dicho nuestras vistas


from django.contrib import admin
from django.urls import path
from Proyecto1.views import hija1, saludo, hasta_luego, edadFutura, ver_plantilla, platilla_con_valores, plantilla_con_loader, shorcutRender_subPlantillas, hija1, hija2

urlpatterns = [
    path('admin/', admin.site.urls),
    # su estructura seria path('nombrevista/', la funcion vista, debeos importarla)
    path('saludo/', saludo),
    # Ahora si nos dirigimos a http://localhost:8000/saludo/ nos caragar un archivo html con lo que escribimos en la vista.
    # notar que al ir al localhost:8000 nos manda error
    path('hasta_luego', hasta_luego),
    # Para pasar parametros por los urls debe ser <tipo_de_dato:parametro tal cual esta en la vista>/...
    path('edad_futura/<int:edad>/<int:anio_futuro>/', edadFutura),
    # entonces en el buscado pondriamos http://localhost:8000/edad_futura/19/2080/
    path('plantilla/', ver_plantilla),
    path('plantilla_con_valores/', platilla_con_valores),
    path('plantilla_con_loader/', plantilla_con_loader),
    path('plantilla_con_subplantilla_y_usandoShorcut/', shorcutRender_subPlantillas),
    path('hija_uno/', hija1),
    path('hija_dos/', hija2)
]
