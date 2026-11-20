from fastapi import (
    APIRouter,status,HTTPException
    
)
from schemas.books import BooksModel
from storage.storage_books import load_books
import json


router = APIRouter()


@router.get("/",response_model=list[BooksModel])
def read_books()->list[BooksModel]:
    try:
        data_base_books = load_books()
        return data_base_books
    except FileNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="File not found"
        )

    except json.JSONDecodeError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Invalid Json file"
        )
    except OSError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to read file"
        )
        
        
        
@router.get("/{book_id}", response_model=BooksModel)
async def get_one_book(book_id:int)->BooksModel:
    try:
        data_base_books = load_books()
        
    except FileNotFoundError:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="File not found"
            )
    
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Invalid Json file"
        )
    except OSError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to read file"
        )
        
    for book in data_base_books:
        if book["id"] == book_id:
            return book
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )