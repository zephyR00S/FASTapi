from sqlalchemy import Column, Integer, String, Float
from database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    price = Column(Float)

"""
SQLAlchemy ORM Models
Purpose:

Defines the database tables.

Contains:

Book class → represents a row in the database

Each class attribute = database column

Why needed?

ORM (Object Relational Mapping) lets you write Python objects instead of SQL queries.
SQLAlchemy uses this file to create tables inside the database.
"""