from sqlalchemy.orm import Session
from models import Book
from schemas import BookCreate

def get_books(db: Session):
    return db.query(Book).all()

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def create_book(db: Session, book: BookCreate):
    db_book = Book(title=book.title, author=book.author, price=book.price)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    book = get_book(db, book_id)
    if book:
        db.delete(book)
        db.commit()
    return book

"""
Database Operations (Create, Read, Update, Delete)
Purpose:

Write functions that interact with the database separate from the API logic.

Contains:

Functions like:

create_book()

get_book()

get_books()

delete_book()

Why needed?

Keeps your code clean and organized:

main.py handles URL routes

crud.py handles database queries
"""