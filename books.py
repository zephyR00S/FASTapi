from fastapi import APIRouter
from pydantic import BaseModel,Field
import json
import os


def save_books():
    with open(FILE_PATH, "w") as f:
        json.dump(books, f, indent=4)

def load_books():
    global books, next_id
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            books = json.load(f)
            if books:
                next_id = max(b["id"] for b in books) + 1

FILE_PATH = "books_data.json"

router = APIRouter()
load_books()

class Book(BaseModel):
    title: str = Field(..., min_length=3)
    author: str = Field(..., min_length=2)
    price: float = Field(..., gt=0)

# Fake database (list)
books = []
next_id = 1





@router.get("/books")
def get_books():
    return books

@router.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    return {"error": "Book not found"}


@router.get("/books/search")
def search_books(title: str = None, author: str = None, min_price: float = None, max_price: float = None):
    results = books

    if title:
        results = [b for b in results if title.lower() in b["title"].lower()]

    if author:
        results = [b for b in results if author.lower() in b["author"].lower()]

    if min_price:
        results = [b for b in results if b["price"] >= min_price]

    if max_price:
        results = [b for b in results if b["price"] <= max_price]

    return results

@router.get("/books/sort")
def sort_books(by: str = "price", order: str = "asc"):
    if by not in ["price", "title", "author"]:
        return {"error": "Invalid sort field"}

    reverse = True if order == "desc" else False

    return sorted(books, key=lambda x: x[by], reverse=reverse)


@router.get("/books/page")
def paginate_books(page: int = 1, limit: int = 5):
    start = (page - 1) * limit
    end = start + limit
    return {
        "page": page,
        "limit": limit,
        "total": len(books),
        "data": books[start:end]
    }


@router.post("/books")
def add_book(book: Book):
    global next_id
    book_dict = book.model_dump()
    book_dict["id"] = next_id
    next_id += 1
    books.append(book_dict)
    save_books()
    return {"message": "Book added", "book": book_dict}

@router.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for i, book in enumerate(books):
        if book.id == book_id:
            books[i] = updated_book
            save_books()
            return {"message": "Book updated", "book": updated_book}
    return {"error": "Book not found"}

@router.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, book in enumerate(books):
        if book.id == book_id:
            deleted = books.pop(i)
            save_books()
            return {"message": "Book deleted", "book": deleted}
    return {"error": "Book not found"}
