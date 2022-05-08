# podemos usar with para abrir un archivo y cerrarlo automaticamente
with open('nuevo_archivo.txt', 'r', encoding='utf8') as archivo: #es importane dare un identificador
    print(archivo.read())
    '''
    Este es otro archivo que esta remplazando al anterior
    jejejjejejje
    estamos agregando otra lineaXd
    '''
    # con with se aplica automaticamente el cierre del archivo (no usamos archivo.close())
    # Vasicamente con with estamos aplicando los metodos __enter__ (este es para entra en el archivo) y __exit__ (este es para salir del archivo)

print('Salimos del with')
# Salimos del with