from fastapi import APIRouter
#from storagy import load_authors

router = APIRouter()


@router.get("/")
def read_authors():
 #   data_authors = load_authors()
    #return data_authors
    pass