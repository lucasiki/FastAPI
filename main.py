from fastapi import FastAPI, Path
from a2wsgi import ASGIMiddleware
from typing import Optional
from pydantic import BaseModel

app = FastAPI()
##uvicorn main:app --reload
wsgi_app = ASGIMiddleware(app)

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

inventory={}


@app.get('/')
def appget():
    return ['lucas']

@app.get('/about')
def about():
    return{"data":"about"}

@app.get("/get-item/{item_id}") 
def get_item(item_id: int = Path(None, description="The ID of the item you'd like to view")):
     return inventory[item_id]  

@app.get("/get-by-name/{item_id}}")
def get_item2(*, item_id: int, name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"data":"Not Found"}       

## RequestBODY

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item already exists"}

    inventory[item_id] = item  
    return inventory[item_id] 
    
    
    
    
    
    



    