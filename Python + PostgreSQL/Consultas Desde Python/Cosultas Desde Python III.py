import psycopg2

conexion = psycopg2.connect(
    user = 'postgres',
    password = 'PDUxst52',
    host = '127.0.0.1',
    port = '5432',
    database = 'Conectando Con Python'
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "UPDATE personas SET nombre = %s, edad = %s WHERE id=%s"
            cursor.execute(sentencia, ('Sebastian', '17', '8'))
            print("Registros actualizados: ", cursor.rowcount)
except Exception as e:
    print(e)
finally: conexion.close()
# Notar que se actualizado el registro

conexion = psycopg2.connect(
    user = 'postgres',
    password = 'PDUxst52',
    host = '127.0.0.1',
    port = '5432',
    database = 'Conectando Con Python'
)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "UPDATE personas SET nombre = %s, edad = %s WHERE id = %s"
            valores = (
                ("Emily", "30", "6"),
                ("Pablo", "11", "7")
            )
            cursor.executemany(sentencia, valores)
            print("Registros actualizados: ", cursor.rowcount)
except Exception as e:
    print(e)
finally: conexion.close()
# Registros actualizados:  2
# Notar que se hicieron todos los cambios
