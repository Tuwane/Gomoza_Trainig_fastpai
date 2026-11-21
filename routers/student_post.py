from fastapi import (
    APIRouter,status,
    HTTPException
    
)
from schemas.students import StudentModel
from storage.storage_students import (
    load_students,
    save_students
)
router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_student(new_student_add : StudentModel):
    try:
        data_load_student = load_students()
        
    except FileNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="student file not found"
        )
        
    new_student = new_student_add.model_dump()
    
    next_id = max(
        (student["id"] for student in data_load_student),
        default=0
    ) + 1
    
    new_student = {"id": next_id, **new_student_add.model_dump(exclude={"id"})}
    new_student.setdefault("is_registered",False)
    
    print(new_student.setdefault("is_registered",False))
    data_load_student.append(new_student)
    try:
        save_students(data_load_student)
    except Exception:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Student was not added"
        )
    return new_student
    
