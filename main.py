from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal, engine
import models
from schemas import BookCreate, Book
import crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency - every request gets a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/books/", response_model=Book)
def create_book_api(book: BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

@app.get("/books/", response_model=list[Book])
def read_books_api(db: Session = Depends(get_db)):
    return crud.get_books(db)

@app.get("/books/{book_id}", response_model=Book)
def read_book_api(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.delete("/books/{book_id}")
def delete_book_api(book_id: int, db: Session = Depends(get_db)):
    book = crud.delete_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted"}
