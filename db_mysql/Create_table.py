from db_mysql.Connection_mysql import conecction_mysql


def create_table_users():

    consult = """CREATE TABLE users (
        id INT(11) NOT NULL AUTO_INCREMENT,
        sexo VARCHAR(10) NOT NULL,
        fecha_de_nacimiento DATE NOT NULL,
        nombre VARCHAR(100) NOT NULL,
        apellido VARCHAR(100) NOT NULL,
        email VARCHAR(254) NOT NULL,
        direccion VARCHAR(200) NOT NULL,
        casa_apartamento VARCHAR(50) NOT NULL,
        pais VARCHAR(100) NOT NULL,
        departamento VARCHAR(100) NOT NULL,
        ciudad VARCHAR(100) NOT NULL,
        PRIMARY KEY (id)
    )"""
    conecction = conecction_mysql()
    cursor = conecction.cursor()
    cursor.execute(consult)
    conecction.commit()
    conecction.close()
    print("Table (users) create with success")

