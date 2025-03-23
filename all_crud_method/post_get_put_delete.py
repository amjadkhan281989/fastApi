from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

app = FastAPI()
data = []

conn = psycopg2.connect(
    
)

class Book(BaseModel):
    title: str
    author: str
    publisher: str

@app.post('/book')
def createbook(book: Book):
    data.append(book.dict())
    return data

@app.get('/{id}')
def readbook(id: int):
    return data[id]

@app.put('/book/{id}')
def updatebook(id: int, book: Book):
    data[id] = book
    return book

@app.delete('/book/{id}')
def deletebook(id: int):
    data.pop(id)
    return data