# Se realiza la conexion e interaccion con la base de datos MySQL. 
import mysql.connector
from mysql.connector import Error

try: 
    conexion = mysql.connector.connect(

        host='localhost',
        port=3306,
        user='root',
        password='',
        db='turismobd'
    )

    if conexion.is_connected():
      print("Conexion exitosa.")
      infoServer= conexion.get_server_info()
      print("Informacion del servidor:",infoServer)


except Error as ex: 
    print("Error durante la conexion:", ex)
finally:
    if conexion.is_connected():
        conexion.close() # Se cierra  la conexion a la BD
        print("La conexion ha finalizado")
