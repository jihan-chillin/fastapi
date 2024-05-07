from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message" : "하이하이"
    }

app.get("/test")
async def test():
    return {
        "message" : "테스트예제"
    }