from pydantic import BaseModel, ValidationError

class User(BaseModel):
    name :str
    age : int

def process_user(user:User):
    #데이터 처리
    return f"Name : {user.name}, Age : {user.age}"

# 유효한 데이터
user_data = { "name" : "Alice", "age" : 30 }
user = User(**user_data)
print(process_user(user))

# 유효하지 않은 데이터
invalid_user_data = { "name" : "Alice", "age" : "thirsty" }
try:
    invalid_user = User(**invalid_user_data)
    print(process_user(user))
except ValidationError as e:
    print(f"ValidationError : {e}")