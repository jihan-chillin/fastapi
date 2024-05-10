import request

base_url = "http://127.0.0.1:8000/

def create_item(name, description, price):
    response = requests.post(
        f"{base_url}/items", 
        json={
            "name" : name,
            "description" : description, 
            "price" : price
        }
    )

    return response.json()

def get_item(item_id):
    response = request.get(
        f"{base_url}/items/{item_id}"
    )
    return response.json()

# 예시 사용
print(create_item("생플 아이템", "설명", 1000))
print(get_item(1))