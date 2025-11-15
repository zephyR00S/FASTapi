from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Book(BaseModel):
    id: int
    title: str
    author: str
    price: float

# Fake database (list)
books = []

@router.get("/books")
def get_books():
    return books

@router.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    return {"error": "Book not found"}

@router.post("/books")
def add_book(book: Book):
    books.append(book)
    return {"message": "Book added", "book": book}

@router.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for i, book in enumerate(books):
        if book.id == book_id:
            books[i] = updated_book
            return {"message": "Book updated", "book": updated_book}
    return {"error": "Book not found"}

@router.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, book in enumerate(books):
        if book.id == book_id:
            deleted = books.pop(i)
            return {"message": "Book deleted", "book": deleted}
    return {"error": "Book not found"}
