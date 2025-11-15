from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./books.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

"""
database.py — Database Connection + Session
Purpose:

This file creates the SQLite database connection and provides the session that all database operations use.

Contains:

DATABASE_URL → where your database lives

engine → connects FastAPI to SQLite

SessionLocal → creates sessions for each request

Base → SQLAlchemy base class for models

Why needed?

FastAPI needs to talk to a real database.
SQLAlchemy needs an engine + session to run queries.
Without this file, NO DATABASE connection exists.

"""