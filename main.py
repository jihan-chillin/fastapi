import logging
from fastapi import FastAPI, Form, Request, Header, Cookie

# 로깅설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# 더미
items = {
    "1": { "name" : "jihan" },
    "2" : { "name" : "marathon" }
}

@app.get("/items")
async def read_items(user_agent: str = Header(None), ads_id:str = Cookie(None)):
    logger.info("Fetching all items")
    return {
        "items" : items, 
        "User-Agent" : user_agent,
        "ads_id" : ads_id
    }

@app.post("/items")
async def create_item(request:Request):
    data = await request.json()
    print(data)
    return data

@app.post("/login")
async def login(username:str = Form(...), password : str = Form(...)):
    return {
        "username" : username,
        "password" : password
    }

@app.post("/items/{item_id}")
async def create_item(item_id:str, name : str = Form(...)):
    items[item_id] = {"name" : name}
    logger.info(f"item created : {item_id} - {name}")
    return items[item_id]

@app.put("/items/{item_id}")
async def update_item(item_id:str, name:str = Form(...)):
    items[item_id] = { "name" : name }
    logger.info(f"Item updated: {item_id} -{name}")
    return items[item_id]

@app.delete("/items/{item_id}")
async def delete_item(item_id:str):
    print(items)
    if item_id in items:
        del items[item_id]
        logger.info(f"Item.deleted: {item_id}")
        return { "message" : "Item.deleted {item_id}"}

@app.patch("/items/{item_id}")
async def patch_item(item_id:str, name:str = Form(...)):
    if item_id in items:
        items[item_id]["name"] = name
        logger.info(f"Item patched: {item_id} - {name}")
        return items[item_id]
    logger.info(f"Item not found: {item_id}")
    return { "message" : "Item not found"}