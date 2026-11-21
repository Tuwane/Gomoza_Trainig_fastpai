from fastapi import (
    APIRouter,HTTPException,status
)
from schemas.books import BooksModelUpdates
from storage.storage_books import load_books,save_books
import json

router = APIRouter()

@router.put("/{book_id}",status_code=status.HTTP_200_OK)
async def update_book(book_id:int, updated_book:BooksModelUpdates):
    try:
        data_load_books = load_books()
    except FileExistsError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Books data not found",
        )
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Invalid json file ",
        )
    except OSError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to read file",
        )

    for index, book in enumerate(data_load_books):
        if book["id"] == book_id:
            new_book_replaced = {
                "id": book_id,
                **updated_book.model_dump(exclude={"id"}),
            }
            
            new_book_replaced.setdefault("is_registered",False)
            
            data_load_books[index] = new_book_replaced
            
            try:
                save_books(data_load_books)
            except Exception:
                raise HTTPException(
                    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="Book was not found"
                )
            return new_book_replaced
        
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail=f"Book with id {book_id} not found"
    )
    
    