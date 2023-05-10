import MySQLdb
import os
from dotenv import load_dotenv

load_dotenv()

# Datos de conexión a la base de datos
host = os.getenv("DATABASE_HOST")
usuario = os.getenv("DATABASE_USER")
password = os.getenv("DATABASE_PASSWORD")
bd = os.getenv("DATABASE_NAME")


def conecction_mysql():
# Establecer conexión
    conecction = MySQLdb.connect(host=host, user=usuario, password=password, db=bd)

    return conecction


coneccion = conecction_mysql()