from fastapi import FastAPI
from data_processing import libary_data

library = libary_data("library.json")
books = library.books

app = FastAPI()

@app.get("/books")
async def read_books():
    return books