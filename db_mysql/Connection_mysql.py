import MySQLdb
import os
from dotenv import load_dotenv

load_dotenv()

# Datos de conexión a la base de datos
host = os.getenv("HOST_DB")
usuario = os.getenv("USUARIO_DB")
password = os.getenv("PASSWORD_DB")
bd = os.getenv("DB")


def conecction_mysql():
# Establecer conexión
    conecction = MySQLdb.connect(host=host, user=usuario, password=password, db=bd)

    return conecction


coneccion = conecction_mysql()