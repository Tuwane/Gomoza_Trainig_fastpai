from pydantic import BaseModel

class BooksModel(BaseModel):
    title: str
    author: str
    category : str
    is_available :bool = False
    
    
class BooksModelUpdates(BaseModel):
    title: str
    author: str
    category : str
    is_available :bool = False
    
    