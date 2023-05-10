from db_mysql.Create_table import create_table_users
from fastapi import FastAPI, Depends
from Dependencies.Register import register
from Dependencies.consult import consult_full_users, consult_full_cities, consult_city, consult_user
from Dependencies.delete_user import delete_user
from Dependencies.update_user import update_user
import uvicorn

app = FastAPI()

@app.get("/users")
def users_full(users: dict = Depends(consult_full_users)):
    return users

@app.post("/user")
def user(user: dict = Depends(consult_user)):
    return user

@app.post("/user/delete")
def user_delete(user: dict = Depends(delete_user)):
    return user

@app.post("/user/update")
def user_update(user: dict = Depends(update_user)):
    return user


@app.get("/cities")
def cities_full(cities: dict = Depends(consult_full_cities)):
    return cities

@app.post("/city")
def cities(city: dict = Depends(consult_city)):
    return city


@app.post("/register")
def register(user: dict = Depends(register)):
    return user








if __name__ == "__main__":

    try:
        create_table_users()
    
    except:

        pass
    
    uvicorn.run("main:app",port=8000, reload=True)