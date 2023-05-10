from db_mysql.Connection_mysql import conecction_mysql
from pydantic import BaseModel ,conint,constr
from fastapi import HTTPException


class Validate_id(BaseModel):    
    id: conint()


    
def delete_user(validate:Validate_id):

    id = validate.id

    query = f"SELECT * FROM users WHERE id = {id}"
    cursor = conecction_mysql().cursor()
    cursor.execute(query)
    results = cursor.fetchall()    

    if len(results) == 0:

        raise HTTPException(status_code=401, detail="user not found")

    else:

        query = f"DELETE FROM users WHERE id = {id}"
        connect = conecction_mysql()
        cursor = connect.cursor()
        cursor.execute(query)
        connect.commit()

        
    
    return {"detail": "User delete with success"}