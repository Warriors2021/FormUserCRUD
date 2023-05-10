from db_mysql.Connection_mysql import conecction_mysql
from pydantic import BaseModel ,conint,constr
from fastapi import HTTPException

class Validate_city(BaseModel):
    
    ciudad: constr(max_length=100)

class Validate_id(BaseModel):    
    id: conint()
    

def consult_city(validate:Validate_city):

    ciudad = validate.ciudad

    query = f"SELECT ciudad, COUNT(*) as total FROM users GROUP BY ciudad HAVING ciudad = '{ciudad}'"

    cursor = conecction_mysql().cursor()
    cursor.execute(query)
    results = cursor.fetchall()

    if len(results) == 0:

        raise HTTPException(status_code=401, detail="city not found")

    else:

        document = {
            "ciudad": results[0][0],
            "cantidad": results[0][1]
         }
    
    return document

   
def consult_full_cities():

    query = f"SELECT ciudad, COUNT(*) as total FROM users GROUP BY ciudad"

    cursor = conecction_mysql().cursor()
    cursor.execute(query)
    results = cursor.fetchall()

    documents = []

    for row in results:

        document = {
                "ciudad": row[0],
                "cantidad": row[1]
            }
        
        documents.append(document)
    
    return documents
    

def consult_user(validate:Validate_id):

    id = validate.id
    query = f"SELECT * FROM users WHERE id = '{id}'"
    cursor = conecction_mysql().cursor()
    cursor.execute(query)
    results = cursor.fetchall()

    if len(results) == 0:

        raise HTTPException(status_code=401, detail="user not found")

    else:

         document = {
            "id": results[0][0],
            "sexo": results[0][1],
            "fecha_de_nacimiento": results[0][2].strftime("%d-%m-%Y"),
            "nombre": results[0][3],
            "apellido": results[0][4],
            "email": results[0][5],
            "direccion": results[0][6],
            "pais": results[0][7],
            "casa_apartamento": results[0][8],
            "departamento": results[0][9],
            "ciudad": results[0][10]
        }
    
    return document


def consult_full_users():

    query = "SELECT * FROM users"


    cursor = conecction_mysql().cursor()
    cursor.execute(query)
    results = cursor.fetchall()


    documents = []

    for row in results:

        document = {
            "id": row[0],
            "sexo": row[1],
            "fecha_de_nacimiento": row[2].strftime("%d-%m-%Y"),
            "nombre": row[3],
            "apellido": row[4],
            "email": row[5],
            "direccion": row[6],
            "pais": row[7],
            "casa_apartamento": row[8],
            "departamento": row[9],
            "ciudad": row[10]
        }

        documents.append(document)
    
    return documents


