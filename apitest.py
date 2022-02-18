from importlib.resources import path
from operator import gt
from pathlib import Path
from pydoc import describe
from fastapi import FastAPI, Path, Query
from typing import Optional

app = FastAPI()

inventory = {
        1: {  
            "name": "aap",
            "price": 2.56,
            "brand": "test"     

         }
    }

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="kies een id van de lijst")):
    return inventory[item_id]

@app.get("/get-item_name/")
def get_item(name: str = Query(None, title="name", description="name of item")):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"data": "not found"}


