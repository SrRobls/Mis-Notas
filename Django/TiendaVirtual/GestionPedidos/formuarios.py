from django import forms

# en este documento crearemos los documnetos de nuestros formularios
class FormularioContacto(forms.Form):
    asunto = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField()


# Una vez creada la calse de un formulario, vamos hacerle prueba en la terminal
# desde el shell
# In [1]: from GestionPedidos.formuarios import FormularioContacto

# In [2]: formulario = FormularioContacto()

# In [3]: print(formulario)
# <tr>
#     <th><label for="id_asunto">Asunto:</label></th>
#     <td>

#       <input type="text" name="asunto" required id="id_asunto">


#     </td>
#   </tr>

#   <tr>
#     <th><label for="id_email">Email:</label></th>
#     <td>

#       <input type="email" name="email" required id="id_email">


#     </td>
#   </tr>

#   <tr>
#     <th><label for="id_mensaje">Mensaje:</label></th>
#     <td>

#       <input type="text" name="mensaje" required id="id_mensaje">


#     </td>
#   </tr>

# Notar que nos devuel los valores (inputs, etc) del form pero dentro de tablas, pero si le decimos formulario.as_<etiqueta html> los pasa 
# a entorno de esa etiqueta suministrada.

# si le pasamos los parametros del formulario, le podemos preguntar si eso parametros osn correctos segun el campo que se pide
# formulario = FormularioContacto({'asunto': 'Una prueba', 'email':'johanrobles66@yahoo.com', 'mensaje':'holas!'})
# In [5]: formulario.is_valid()
# Out[5]: True, en caso de que por ejemplo el formato del email era incorrecto, entonces fuese sido false

# Por ultimo, con cleaned_data podemos obtenemos los parametros del formulario
# Out[7]: formulario.cleaned_data
{'asunto': 'Una prueba',
 'email': 'johanrobles66@yahoo.com',
 'mensaje': 'holas!'}