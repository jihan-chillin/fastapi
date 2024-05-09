from fastapi import FastAPI
from items import router as item_router
from users import router as user_router

# metadata
tags_metadata = [
    {
        "name" : "items",
        "description" : "간단한 API 생성을 위해 기본적인 아이템 CRUD태그"
    }
]

app = FastAPI(
    title="Fastapi Practice",
    description="Skim Through Basic Fastapi",
    openapi_tags=tags_metadata
)

app.include_router(item_router)
app.include_router(user_router)