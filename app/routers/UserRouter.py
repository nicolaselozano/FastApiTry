from fastapi import APIRouter, HTTPException
from app.config.db import conn
from app.models.user import users
from app.schemas.User import User

from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
userR = APIRouter()

@userR.get("/users")
def get_users():
    try:
        result = conn.execute(users.select()).all()
        users_list = [dict(row) for row in result]
        return users_list
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@userR.post("/users")
def post_users(user:User):
    try:
        new_user = {"name" : user.name,"email" : user.email}
        new_user["password"] = f.encrypt(user.password.encode("utf-8"))
        result = conn.execute(users.insert().values(new_user))
        print(result)
        conn.commit()
        conn.close()
        return {"message": "User created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
