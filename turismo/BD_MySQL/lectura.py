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
      cursor=conexion.cursor()
      cursor.execute("SELECT database();")
      registro=cursor.fetchone()
      print("Conectado a la base de datos:",registro)
      cursor.execute("SELECT * FROM persona")
      resultados=cursor.fetchall()
      for fila in resultados:
        print(fila[0],fila[1],fila[2])
      print("Total de registros:",cursor.rowc)

except Error as ex: 
    print("Error durante la conexion:", ex)
finally:
    if conexion.is_connected():
        conexion.close() # Se cierra  la conexion a la BD
        print("La conexion ha finalizado")
