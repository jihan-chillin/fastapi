from fastapi import APIRouter

router = APIRouter()

@router.get("/item/{item_id}")
async def read_items(item_id:int):
    return { "item_id" : item_id }