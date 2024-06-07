from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select, insert, update, delete, func
from db import engine

class User(BaseModel):
    name: str
    age: int

class UserResponse(BaseModel):
    id: int
    name: str
    age: int = None

class UserUpdate(BaseModel):
    name : str = None
    age: int = None

# 평균 연령 응답을 위한 pydantic 모델
class AverageAgeResponse(BaseModel):
    name:str
    average_age:float

app = FastAPI()

@app.post("/users", response_model=UserResponse)
async def create_user(user:User):
    with engine.connect() as conn:
        result = conn.execute(insert(users).values(name=user.name, age=user.age))
        conn.commit()
        new_user_id = result.lastrowid
        return UserResponse(
            id=new_user_id,
            **user.dict()
        )

@app.get("/users", response_model=List[UserResponse])
async def read_users():
    with engine.connect() as conn:
        result = conn.execute(select(users))
        user_list = result.fetchall()
        return [UserResponse(id=row[0], name=row[1], age=row[2]) for row in user_list]

@app.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id:int, user:UserUpdate):
    with engine.connect() as conn:
        update_stmt = update(users).where(users.c.id == user_id)
        if user.name:
            update_stmt = update_stmt.values(name=user.name)
        if user.age:
            update_stmt = update_stmt.values(age=user.age)

        conn.execute(update_stmt)
        conn.commit()
    return await read_user(user_id)

@app.get("/users/{user_id}", response_model=UserResponse)
async def read_user(user_id: int):
    with engine.connect() as conn:
        result = conn.execute(select(users).where(users.c.id == user_id))
        user = result.fetchone()
        if user:
            return UserResponse(
                id=user.id,
                name=user.name, 
                age=user.age
            )
        else:
            raise HTTPException(status=404, detail="User not found")

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    with engine.connect() as conn:
        result = conn.execute(delete(users).where(users.c.id == user_id))
        conn.commit()
    return { "message" : "User deleted" }