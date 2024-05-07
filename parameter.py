import requests
import json

# 요청본문 테스트
url = "http://localhost:8000/items"
data = {"key" : "value"} #전송할 JSON 데이터

response = requests.post(url, json=data)
print(f"Status Code : {response.status_code}")
print(f"JSON Reponse : {response.json()}")