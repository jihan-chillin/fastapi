from typing import List
from pydantic import BaseModel, validator

class Item(BaseModel):
    name : str
    description : str = None
    price : float
    tax : float = 0.0

# 18살 미만의 유저 유효성 검사
class User(BaseModel):
    name :str
    age : int

    @validator("age")
    def check_age(cls, v):
        if v < 18:
            raise ValueError("Age must be at least 18")
        return v

class Order(BaseModel):
    id : int
    items : List[Item]

order = Order(
    id=123, 
    items=[
        {"name" : "apple", "price" : 5},
        {"name" : "banana", "price" : 3.0}
    ]
)


# ORM모드
class ORMModel:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class UserModel(BaseModel):
    name: str
    age: int

    class Config:
        orm_mode = True

orm_user = ORMModel(name="Alice", age=30)
user = UserModel.from_orm(orm_user)

item = Item(name="Apple", description="Red fruit", price = 5.5)

# 직렬화
item_json = item.json()
print(item_json)

#역직렬화
item = Item.parse_raw(item_json)
print(item)