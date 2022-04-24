# print se usa para mostra algo en pantalla (texto, una variable, un resultado etc)
print("Hola Mundooooooooooo!!!!!")
# Tarea: Saludar en Python:
print("Hola Soy Johan Sebastian Robles Rincon y voy a ser el mejor!!!!!!")
print("----------------------------------------------------------------------------------")
#                                    Variables En Python:
print("                              Variables En Python:")
# Una variable puede contener numeros, letras ("letra"),cadenas de texto etc.
miVariable = "holis"
print(miVariable)
print(miVariable + " a todos!")
num1 = 5
num2 = 7
num3 = num1 + num2
print(num3)
num3 = num3 * 3
print(num3)
# El codigo "id" se usa para coneocer la dereccion de memoria donde se guardo un literal (un valor numerico,
# caracter, etc).
print(id(num1))  # usamos print para que se nos meustre en pantalla
print(id(num2))
print(id(num3))
print("----------------------------------------------------------------")
#                       Tipos De Variables En Python:
print("                 Tipos De Variables En Python:")
# se usa "type" para saber de que tipo es una variable:
print((type(num1)))
# vemos que nos da <class int> eso significa que es de tipo entero
x = "hola"
print(type(x))
# nos da <class str> es decir que es un sring, un texto.
y = 15.7
print(type(y))
# nos da <class float> es flotante, es decir un numero con decimales
z = True  # o False (importante para las variables booleanas se debe empezar con la primera letra en mayuscula
print(type(z))
print("----------------------------------------------------------------------------------")
#                        Manejo De cadenas En Python
print("                  Manejo De cadenas En Python")
# Cadena:
Myfavoritegroup = "El Cuarteto De Nos"
comentario = "Musica Chimbita"
print("mi grupo favorito es " + Myfavoritegroup + ", " + comentario)  # esto se llama concatenacion
print("mi grupo favorito es ", Myfavoritegroup, comentario)  # Tambien se puede concatenar usando la coma (ademas
# este ya tiene el espacio por defecto)
# Ahora si quiero convertir un texto a numero debemos hacer por ejemplo:
x = "5"
y = "7"
print("Concatenacion", x + y)
# El proceso seria:
print("Suma", int(x) + int(y))  # Metemos la variable que tiene el texto dentro del condigo "int"
print("----------------------------------------------------------------------------------")
#                 Procesar entrada del usuario (funcion input)
print("           Procesar entrada del usuario (funcion input)")
# Se usa input para pedirle un valor al usuario
variable1 = int(input( "escribe un numero!: "))
variable2 = int(input("escribe otro numero!: "))
# dentro de los () podemos mostrar en pantalla lo que pedimos. guardamos el valor en una variable
#ademas usamos el int para que el valor del usuario lo convirtamos a un numero
#aqui se muestra algunos operadores aeitmeticos para python
print("suma = ", variable1 + variable2)
print("resta = ", variable1 - variable2)
print("multiplicacion = ", variable1 * variable2)
print("division = ", variable1 / variable2)
print("residuo: ", variable1 % variable2)
print("exponeciacion: ", variable1 ** variable2)
print("Muchas gracias!")
