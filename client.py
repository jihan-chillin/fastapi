import requests

BASE_URL = "http://127.0.0.1:8000/users"

def get_users():
    response = requests.get(f"{BASE_URL}")
    return response.json()

def create_user(name, age):
    response = requests.post(f"{BASE_URL}", json={"name" : name, "age": age})
    return response.json()

def get_user(user_id):
    response = requests.get(f"{BASE_URL}/{user_id}")
    return response.json()

def update_user(user_id, name, age):
    response = requests.put(f"{BASE_URL}/{user_id}", json={"name" : name, "age": age})
    return response.json()

def delete_user(user_id):
    response = requests.delete(f"{BASE_URL}/{user_id}")
    return response.json()

print("Get users", get_users())
print("Create user", create_user("chillin", 28))
print("Get user", get_user(4))
print("Update user", update_user(4, "chillin", 28))
print("Delete user", delete_user(4))

# base_url = "http://127.0.0.1:8000/

# def create_item(name, description, price):
#     response = requests.post(
#         f"{base_url}/items", 
#         json={
#             "name" : name,
#             "description" : description, 
#             "price" : price
#         }
#     )

#     return response.json()

# def get_item(item_id):
#     response = request.get(
#         f"{base_url}/items/{item_id}"
#     )
#     return response.json()

# # 예시 사용
# print(create_item("생플 아이템", "설명", 1000))
# print(get_item(1))