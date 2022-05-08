# podems usar open en para abrir una archivo txt (o crearla) y poder escribir dentro de ella (write, w) o solo leer (read, r)
# por lo general al hacer esto se hace dentro de un try

try:
    archivo = open('nuevo_archivo.txt', 'w', encoding='utf8')
    # usamos open para abrir un archivo y leerlo o escribir en el. le pasamos como parametros el nombre del archivo (aunque si no existe en tonces 
    # este se crea), el parametro de la accio que en este caso es w de write y cpn encodigng definimos que tipos de caracteres usamos

    # si queremos escribir usamos
    archivo.write('Esto es una nueva informaion\n')
    archivo.write('Adios')
    '''
    Esto es una nueva informaion
    Adios
    '''
    # OjO SI CREAMO OTRO OPEN CON WRITE ENTONCES LO QUE ESCRIBIMOS DESDE AHI REMPLAZARIA LO QUE ESTA
    archivo2 = open('nuevo_archivo.txt', 'w', encoding='utf8')
    archivo2.write('Este es otro archivo que esta remplazando al anterior\n jejejjejejje')
    '''
    Este es otro archivo que esta remplazando al anterior
     jejejjejejje
    '''
except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
    archivo.close()
    print('Archivo cerrado')
# Notar que  se creo un nuevo archivo y tiene escrito lo del write. el archivo est afuera de esta carpeta
'''
    Este es otro archivo que esta remplazando al anterior
     jejejjejejje
'''