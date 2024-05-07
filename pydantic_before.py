def process_user(data):
    if not isinstance(data, dict):
        raise ValueError("Invalid data format")

    name = data.get("name")
    age = data.get("age")


    if not isinstance(name, str):
        raise ValueError("Name must be string")

    if not isinstance(age, int) or age < 0:
        raise ValueError("Age must be positive integer")

    #데이터 처리
    return f"Name : {name}, Age : {age}"


# 유효한 데이터
data = {"name" : "Alice", "age" : 30}
print(process_user(data))

# 유효하지 않은 데이터
invalid_data = {"name" : "Alice", "age" : "thirsty"}
print(process_user(invalid_data))