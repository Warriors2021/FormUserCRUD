from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, constr
from datetime import date, timedelta
from db_mysql.Connection_mysql import conecction_mysql


class UserRegister(BaseModel):
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



def register(user_register: UserRegister):

    
    sexo = user_register.sexo
    fecha_de_nacimiento = user_register.fecha_de_nacimiento
    nombre= user_register.nombre
    apellido= user_register.apellido
    email= user_register.email
    direccion= user_register.direccion
    casa_apartamento=user_register.casa_apartamento
    pais=user_register.pais
    departamento= user_register.departamento
    ciudad= user_register.ciudad

    


    if adult(birth_date=fecha_de_nacimiento):

        
        query = f"SELECT COUNT(*) FROM users WHERE ciudad = '{ciudad}'"
        conecction = conecction_mysql()
        cursor = conecction.cursor()
        cursor.execute(query)
        count_city = cursor.fetchone()[0]

        if count_city < 3:

            query = f"""INSERT INTO users
            (sexo, fecha_de_nacimiento,
             nombre, apellido, email,
             direccion, casa_apartamento,
             pais, departamento,ciudad)
             VALUES ('{sexo}', '{fecha_de_nacimiento}',
            '{nombre}', '{apellido}', '{email}',
            '{direccion}', '{casa_apartamento}',
            '{pais}', '{departamento}', '{ciudad}')"""
                
            cursor.execute(query)
            conecction.commit()
            user_id = cursor.lastrowid

            return {"detail": f"User register with success ",
                    "id": user_id}
            
        else:

            raise HTTPException(status_code=401, detail="already on the limit of allowed cities")

    else:
        raise HTTPException(status_code=401, detail="the user is not of legal age")









