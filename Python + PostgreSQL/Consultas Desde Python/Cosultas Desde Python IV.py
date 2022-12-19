import psycopg2

conectar_bd = psycopg2.connect(
    user = 'postgres',
    password = 'PDUxst52',
    host = '127.0.0.1',
    port = '5432',
    database = 'Conectando Con Python'
)

try:
    with conectar_bd:
        with conectar_bd.cursor() as cursor:
            senetencia = "DELETE FROM personas WHERE id = %s"
            ids_eliminar = (
                ('5'),
                ('2'),
                ('9')
            )
            cursor.executemany(senetencia, ids_eliminar)
            print(f"Registros Eliminados: {cursor.rowcount}")
except Exception as e:
    print(e)
finally:
    conectar_bd.close()
# Registros Eliminados: 2
# SE HAN ELIMINADO LOS REGISTROS