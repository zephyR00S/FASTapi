from fastapi import FastAPI
from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str
    price: float

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"id": item_id}


@app.get("/search")
def search(q: str = None, limit: int = 10):
    return {"query": q, "limit": limit}


@app.post("/books")
def add_book(book: Book):
    return {"message": "Book added", "data": book}
