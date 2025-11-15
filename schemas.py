from pydantic import BaseModel

#This holds fields common to all Book-related operations:
#avoid repeating code in both BookCreate and Book.
class BookBase(BaseModel):
    title: str
    author: str
    price: float



#This schema is used when creating a book
#Users PROVIDE this data in JSON
#id is NOT included here → database generates it automatically.
class BookCreate(BookBase):
    pass

#Why do we write pass in:Because we need the class to exist, but we don’t want to add any new fields.

#This schema is used when RETURNING book data to users
#The API returns extra fields (like id), so response schema != request schema.
class Book(BookBase):
    id: int



#Because SQLAlchemy models are not dictionaries, they’re special Python objects.
#When FastAPI tries to convert this to JSON, it fails unless you tell it:

#“This data comes from an ORM model. Convert it properly.”

#Without orm_mode = True
#FastAPI crashes
#Serialization fails
    class Config:
        orm_mode = True
"""
Purpose:

Defines how data enters and leaves your API.

Two types:

✔ Input models → what data users send
✔ Output models → what API returns
Why needed?

Pydantic:

Validates incoming data

Converts ORM models → JSON

Prevents sensitive data from leaking
Schemas protect your API, ensure correct data, and shape output.
"""