from fastapi import FastAPI, Request, Response, status, HTTPException
from pydantic import BaseModel
from starlette.middleware.base import BaseHTTPMiddleware
from services import check_db_connection
from database import SessionLocal, Base, engine
from typing import List
import models


app = FastAPI()

class Item(BaseModel): # serializer
    name: str
    description: str
    price: int
    discount: bool

class ItemResponse(BaseModel):
    id: int
    name: str
    description: str
    price: int
    discount: bool

    class Config:
        orm_mode = True

db = SessionLocal()
print("Creating database....")
Base.metadata.create_all(engine)

class CustomHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['Content-Type'] = 'application/json'
        return response

app.add_middleware(CustomHeaderMiddleware)

def health_check(request: Request):
    method = request.method
    if check_db_connection() and method == 'GET':
        return True
    elif check_db_connection() and method != 'GET':
        raise HTTPException(status_code=405, detail="Method Not Allowed")
    else:
        raise HTTPException(status_code=503, detail="Service Unavailable")

@app.get('/healthz')
async def health_check(request: Request):
    body = await request.body()
    method = request.method
    if check_db_connection() and method == 'GET':
        if not body:
            response = Response(status_code=200)
            return response
        else:
            response = Response(status_code=400)
            return response
    elif check_db_connection() and not method =='GET':
        response = Response(status_code=405)
        return response
    else:
        response = Response(status_code=503)
        return response
    
@app.get('/items', response_model=List[ItemResponse], status_code=status.HTTP_200_OK)
def get_all_items():
    items_query = db.query(models.Item)
    return items_query.all()

@app.get('/item/{item_id}', response_model=ItemResponse, status_code=status.HTTP_200_OK)
def get_an_item(item_id: int):
    item_query = db.query(models.Item).filter(models.Item.id==item_id).first()
    return item_query


@app.post('/items', response_model=ItemResponse, 
          status_code=status.HTTP_201_CREATED)
def create_an_item(item: Item):
    db_item = db.query(models.Item).filter(models.Item.name==item.name).first()

    if db_item is not None:
        raise HTTPException(status_code=400,detail=f"Item '{db_item.name}' already exists.")
    
    new_item = models.Item(
        name = item.name,
        price = item.price,
        description = item.price,
        discount = item.discount
    )
    db.add(new_item)
    db.commit()
    return new_item

@app.put('/item/{item_id}', response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def modify_item(item_id: int, item: Item):
    old_item = db.query(models.Item).filter(models.Item.id==item_id).first()
    old_item.name = item.name
    old_item.description = item.description
    old_item.price = item.price
    old_item.discount = item.discount

    db.commit()

    return old_item


@app.delete('/item/{item_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_an_item(item_id: int):
    item_to_delete = db.query(models.Item).filter(models.Item.id==item_id).first()
    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Resource with id '{item_id}' not found.")

    db.delete(item_to_delete)
    db.commit()
    return
