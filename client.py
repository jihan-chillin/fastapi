import requests
import json

# 서버 URL
base_url = "http://127.0.0.1:8000"

# 아이템 목록을 조회하는 함수
def get_items():
    response = requests.get(f"{base_url}/items")
    return response.json()

# 아이템 목록 출력
def print_items(title, items):
    print(f"\n{title}:\n", items)

# GET 요청 테스트
def test_get_item():
    items_before = get_items()
    print_items("Before GET Request", items_before)

    response = requests.get(f"{base_url}/items")
    print("GET Response :", response.status_code, response.json())

    items_after = get_items()
    print_items("After GET Request", items_after)

# POST 요청 테스트
def test_create_item():
    items_before = get_items()
    print_items("Before POST Request", items_before)

    response = requests.post(f"{base_url}/items/3", data={ "name" : "Notebook" })
    print("POST Response :", response.status_code, response.json())

    items_after = get_items()
    print_items("After POST Request", items_after)

# PUT 요청 테스트
def test_update_item():
    items_before = get_items()
    print_items("Before PUT Request", items_before)

    response = requests.put(f"{base_url}/items/1", data={ "name" : "Updated Pen" })
    print("PUT Response :", response.status_code, response.json())

    items_after = get_items()
    print_items("After PUT Request", items_after)

# DELETE 요청 테스트
def test_delete_item():
    items_before = get_items()
    print_items("Before DELETE Request", items_before)

    response = requests.delete(f"{base_url}/items/2")
    print("DELETE Response :", response.status_code, response.json())

    items_after = get_items()
    print_items("After DELETE Request", items_after)

# PATCH 요청 테스트
def test_patch_item():
    items_before = get_items()
    print_items("Before PATCH Request", items_before)

    response = requests.patch(f"{base_url}/items/1", data={ "name" : "Patched Pen" })
    print("PATCH Response :", response.status_code, response.json())

    items_after = get_items()
    print_items("After PATCH Request", items_after)

#테스트 실행
test_get_item()
test_create_item()
test_update_item()
test_delete_item()
test_patch_item()