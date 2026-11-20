from pydantic import BaseModel

class BooksModel(BaseModel):
    title: str
    category : str
    
    