__version__ = '0.1.0'

from typing import Optional, Dict
from collections import defaultdict

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

items: Dict[int, Item] = defaultdict(lambda: None, {})


@app.get("/")
async def read_root() -> Dict:
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int) -> Dict:
    return {"item_id": item_id, "item": items[item_id] }


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item) -> Dict:
    items[item_id] = item
    return {"item_name": item.name, "item_id": item_id}


@app.delete("/items/{item_id}")
async def update_item(item_id: int) -> Dict:
    items[item_id] = None
    return {"item_id": item_id}