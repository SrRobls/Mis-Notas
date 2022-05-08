# usamos read (r) para leer los archivos
archivo_leer = open('nuevo_archivo.txt','r')
# podemos iterar por las lineas
# for i in archivo_leer:
#     print(i)
'''
Este es otro archivo que esta remplazando al anterior

 jejejjejejje
'''

# print(archivo_leer.readline())
# # Este es otro archivo que esta remplazando al anterior

# print(archivo_leer.readline())
# #  jejejjejejje

# y podemos agregar con append (a) ohjo es diferente que write (w) pues en write estamos sobrescribiendo, aca estamos añadiendo
archivo_agregar = open('nuevo_archivo.txt','a')
archivo_agregar.write('\nestamos agregando otra linea')
archivo_agregar.write('Xd')

'''
Este es otro archivo que esta remplazando al anterior
 jejejjejejje
estamos agregando otra lineaXd
'''

# recordar que es importante cerrar el archivo (aunque python lo cierra por si solo, es buena practiva hacerlo)