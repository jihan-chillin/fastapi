from fastapi import FastAPI, Request, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware
from pydantic import BaseModel
import time
import httpx
import asyncio

# metadata
tags_metadata = [
    {
        "name" : "middleware-test",
        "description" : "미들웨어 테스트를 위한 예시경로입니다."
    }
]

app = FastAPI(
    title="Fastapi Practice",
    description="Skim Through Basic Fastapi",
    openapi_tags=tags_metadata
)

class UserInput(BaseModel):
    name : str
    age : int

class UserResponse(BaseModel):
    name : str
    age : int
    is_adult: bool

# 에러모델과 성공모델을 다르게 response
class SuccessModel(BaseModel):
    message: str

class NotFoundModel(BaseModel):
    error: str

class ValidationErrorModel(BaseModel):
    errors : list


# 커스텀 미들웨어 클래스 
class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        print("Hello, It's Jihan")
        response  = await call_next(request)
        return response

# 미들웨어 추가
app.add_middleware(CustomMiddleware)

# 미들웨어 정의
@app.middleware("http")
async def log_requests(request:Request, call_next):
    start_time = time.time()
    #요청 처리
    response = await call_next(request)
    #처리시간 계산
    process_time = time.time() - start_time
    print(f"Request : {request.method} {request.url} - Completed in {process_time} secs")
    return response

# 미들웨어 에시경로
@app.get("/", tags=["middleware-test"])
async def read_root():
    return {"hello" : "Hello"}

@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return { "item_id" : item_id }


async def get_remote_data(url):
    async with httpx.AsyncClient() as client:
        print(url, "url")
        response = await client.get(url)
        return response.json()

@app.get("/data")
async def read_data():
    external_data = await get_remote_data("https://some-external-api.com/data")

@app.get("/item/{item_id}", response_model=SuccessModel)
async def get_item(item_id: int):
    if item_id == 0:
        # 데이터 베이스 조회 등의 로직
        raise HTTPException(status_code=404, detail="Item not found")
    return SuccessModel(message="Item found")

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc: HTTPException):
    if exc.status_code == 404:
        return NotFoundModel(error=exc.detail)
    elif exc.status_code == 422:
        return ValidationErrorModel(errors=exc.detail)
    # 기타 상태 코드에 대한 정리

@app.post("/user", response_model=UserResponse)
def create_user(user : UserInput):
    # 입력받은 데이터를 처리
    is_adult = user.age >= 18
    # 응답 모델을 사용하여 응답데이터를 구성
    response_data = UserResponse(
        name=user.name,
        age=user.age,
        is_adult=is_adult,
    )

    return response_data