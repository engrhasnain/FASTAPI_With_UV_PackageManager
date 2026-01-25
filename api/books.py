from db.db import books_date
from fastapi import APIRouter, status
from fastapi.exception_handlers import HTTPException


router = APIRouter(prefix="/books", tags=["Book CRUD"])

from models.books import BookCreated, BookResponse, BookUpdate
from typing import List


@router.get("/get", response_model=List[BookResponse])
async def get_books():
    return books_date

@router.post("/create", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
async def create_book(book: BookCreated):
    new_book = book.model_dump()
    new_book["id"] = len(books_date) + 1
    books_date.append(new_book)
    return BookResponse(**new_book)


@router.post("/get_book/{book_id}", response_model= BookResponse, status_code=status.HTTP_302_FOUND)
async def get_book(book_id:int):
    for book in books_date:
        if book["id"] == book_id:
            return book
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
        )

@router.patch("/update_book/{book_id}")
async def update_book(book_id: int, book_update_date: BookUpdate) -> dict:
    for book in books_date:
        if book['id'] == book_id:
            book['title'] = book_update_date.title
            book['author'] = book_update_date.author
            book['pages'] = book_update_date.pages
            book['price'] = book_update_date.price
            book['in_stock'] = book_update_date.in_stock

            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
