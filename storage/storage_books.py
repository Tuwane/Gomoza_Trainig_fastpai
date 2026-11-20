import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_for_BOOKS = BASE_DIR / "data"/ "books.json"

def load_books():
    with open(DATA_for_BOOKS, 'r') as books:
        return json.load(books)
    
def save_books(books_data):
    with open(DATA_for_BOOKS, 'w') as books:
        json.dump(books_data, books, indent=4,ensure_ascii=False)

print(DATA_for_BOOKS)