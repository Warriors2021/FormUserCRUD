from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, constr, conint
from datetime import date, timedelta
from db_mysql.Connection_mysql import conecction_mysql


class UserUpdate(BaseModel):
    id: conint()
    sexo: constr(max_length=10)
    fecha_de_nacimiento: date
    nombre: constr(max_length=100)
    apellido: constr(max_length=100)
    email: EmailStr
    direccion: constr(max_length=200)
    casa_apartamento: constr(max_length=50)
    pais: constr(max_length=100)
    departamento: constr(max_length=100)
    ciudad: constr(max_length=100)


def adult(birth_date: date) -> bool:    
    today = date.today()   
    limit_date = today - timedelta(days=365*18)
    return birth_date <= limit_date




    
def update_user(validate:UserUpdate):

    id = validate.id
    sexo = validate.sexo
    fecha_de_nacimiento = validate.fecha_de_nacimiento
    nombre= validate.nombre
    apellido= validate.apellido
    email= validate.email
    direccion= validate.direccion
    casa_apartamento=validate.casa_apartamento
    pais=validate.pais
    departamento= validate.departamento
    ciudad= validate.ciudad

    query = f"SELECT * FROM users WHERE id = {id}"
    cursor = conecction_mysql().cursor()
    cursor.execute(query)
    results = cursor.fetchall()    

    if len(results) == 0:

        raise HTTPException(status_code=401, detail="user not found")

    else:
        if adult(birth_date=fecha_de_nacimiento):

            query = f"SELECT COUNT(*) FROM users WHERE ciudad = '{ciudad}'"
            conecction = conecction_mysql()
            cursor = conecction.cursor()
            cursor.execute(query)
            count_city = cursor.fetchone()[0]


            if count_city < 3:

                query = f"""UPDATE users SET sexo = '{sexo}',
                fecha_de_nacimiento = '{fecha_de_nacimiento}',
                nombre = '{nombre}',
                apellido = '{apellido}',
                email = '{email}',
                direccion = '{direccion}',
                casa_apartamento = '{casa_apartamento}',
                pais = '{pais}',            
                departamento = '{departamento}',
                ciudad = '{ciudad}'      
                WHERE id = {id}"""
                connect = conecction_mysql()
                cursor = connect.cursor()
                cursor.execute(query)
                connect.commit()

                return {"detail": "User update with success"}
            else:

                raise HTTPException(status_code=401, detail="already on the limit of allowed cities") 

        else:
            raise HTTPException(status_code=401, detail="the user is not of legal age")
        
    
    