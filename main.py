from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI() #create a new app

@app.get("/") #using a app decorator define the path for the GET method
def root():
    return {"message": "Hello,World"} #root function is called and the message is returned

class Item(BaseModel):
    text: str #since there is no default value, this field is required thus enforcing validation
    is_done: bool = False

items = []
@app.post("/items") #post method to create a new item
def create_item(item: Item):
    items.append(item) #append the item to the items list
    return items 

@app.get("/items",response_model=list[Item]) #response model ensures the response is a list of Item objects
def list_items(limit: int = 10):
    return items[0:limit] #return the list of items according to the limit specified

@app.get("/items/{item_id}",response_model=Item) #path to get an item by its ID
def read_item(item_id: int) ->Item:
    if item_id>=0 and item_id< len(items):
        item = items[item_id] #retrieve the item from the items list using the item_id
        return item
    else:
        raise HTTPException(status_code=404, detail=f"Item with id {item_id} not found") #raise an exception if the item is not found








