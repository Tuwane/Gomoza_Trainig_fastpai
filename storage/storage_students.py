import json 
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FOR_STUDENTS = BASE_DIR / "data" / "students.json"

def load_students():
    with open(DATA_FOR_STUDENTS, 'r',encoding="utf-8") as student:
        return json.load(student)
    
    
def save_students(student_data):
    with open(DATA_FOR_STUDENTS, 'w', encoding="utf-8") as student:
        json.dump(student_data, student, indent=4, ensure_ascii=False)
    
