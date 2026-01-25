from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str


class BookCreated(BaseModel):
    id : int
    title: str
    author : str
    price: int
    pages : int
    published_year : int
    in_stock : bool

class BookUpdate(BaseModel):
    title: str
    author : str
    price: int
    pages : int
    in_stock : bool

class BookResponse(BaseModel):
    id: int
    title : str
    author : str
    price: int
    pages : int
    published_year : int
    in_stock : bool