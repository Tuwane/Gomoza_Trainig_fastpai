from pydantic import BaseModel


    
class StudentModel(BaseModel):
    name : str
    age : int
    is_registered : bool = False
    