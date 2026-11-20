from fastapi import (
    APIRouter,HTTPException,status
)
from schemas.books import BooksModel
from storage.storage_books import load_books,save_books
router = APIRouter()

@router.post("/",status_code=status.HTTP_201_CREATED)
async def add_books(add_book: BooksModel):
    try:
        data_load_books = load_books()
    except FileNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="book files not found"
        )
    new_book = add_book.model_dump()
    
    new_book["id"] = max(
        (book["id"] for book in data_load_books),
        default=0
    ) +1
    
    data_load_books.append(new_book)
    try:
        save_books(data_load_books)
    except Exception:
        raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Book was not saved / added "
    )
    return new_book