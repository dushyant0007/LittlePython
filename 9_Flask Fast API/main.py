from urllib import response
from fastapi import FastAPI,Path
from flask import request
from pydantic import BaseModel
from typing import Optional
import time
import requests

app = FastAPI()

items = {
  1 : {
    "name":"Milk",
    "price": 3.99,
    "brand":"Mother Deary"
  },
  2 : {
    "name":"Tomato",
    "price": 6.50,
    "brand":"Fresh Farm"
  }
}

@app.get('/')
def home():
  return {"Data":"Test"} 

@app.get('/about')
def about():
  return {"Data":"About"} 

@app.get('/get-items')
def getitems():
  return items

@app.get('/get-item/{item_id}')
def getitem(item_id:int=Path(None,description="None is the default value")):
  return items[item_id]

# localhost/get-by-name?name=Milk
@app.get('/get-by-name')
def get_item(*,name:Optional[str] = None,test:int):#None is Default value
  for item_id in items:
    if items[item_id]["name"] == name:
        return items[item_id]
    else:    
      return {"Data":"Not Found"}


class Item(BaseModel):
  
  name:str = None
  price:float = None
  brand:Optional[str] = None

@app.post("/create-item/{item_id}")      
def create_item(item_id:int,item:Item):
  if item_id in items:
    return {"Error":"Item ID already exist"}
  else:
    items[item_id] = {"name":item.name,"price":item.price,"brand":item.brand} 
    print(items)
    return {"Success"}

@app.put("/update-item/{item_id}")      
def create_item(item_id:int,item:Item):
  if item_id not in items:
    return {"Error":"Item ID already exist"}
  else:
    if item.name != None:
     items[item_id] = item.name
    if item.price != None:
     items[item_id].price = item.price
    if item.brand != None:
     items[item_id].brand = item.brand
    print(items) 
    return {"Success"}

  
@app.delete("/delete-item")
def delete_item(item_id:int):
  if item_id in items:
    del items[item_id]
    return {"Success"}
  else:
    return {"No Item Exist With This Id"}  



# Parsed Format





# To run the file 

# Install uvicorn
# command uvicorn fileNameWithout.py:app --reload