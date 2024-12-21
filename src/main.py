"""FastAPI application"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    """Item model"""

    name: str
    price: float
    is_offer: bool | None = None


@app.get("/")
def read_root():
    """Root endpoint"""
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    """Read item endpoint"""
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """Update item endpoint"""
    return {"item_name": item.name, "item_id": item_id}
