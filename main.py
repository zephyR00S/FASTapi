from fastapi import FastAPI
from books import router as books_router


app = FastAPI()
app.include_router(books_router)

@app.get("/")
def root():
    return {"message": "API is running"}


