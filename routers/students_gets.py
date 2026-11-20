from fastapi import (
    APIRouter,HTTPException,
    status 
    
    )
from storage.storage_students import (
    load_students, 
    save_students
    
)
from schemas.students import StudentModel
import json

router = APIRouter()

@router.get("/", response_model=list[StudentModel])
async def read_student()-> list[StudentModel]:
    try:
        data_load_student = load_students()
        return data_load_student
    except FileNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Student File not found"
        )
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Student Data base not found "
        )
    except OSError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Sorry About Error try again"
        )
        
    #return data_load_student
    
        
        

@router.get("/{student_id}", response_model=StudentModel)
async def sigle_student(student_id : int)->StudentModel:
    try:
        data_load_student = load_students()
        
    except FileNotFoundError:    
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    except json.JSONDecodeError:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Invalid json"
        )
    except OSError:
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to read student data"
        )
    for student in data_load_student:
                if student["id"] == student_id:
                    return student
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Stundent not found"
    )