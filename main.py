from fastapi import FastAPI
from routers import (
    authours, books_get,
    books_post,
    students_gets,
    student_post
    
)


app = FastAPI(
    title="Multi Planet"
)

#----------Books Line1

app.include_router(
    books_get.router,
    prefix="/books",
    tags=["Books"],
    
        )

app.include_router(
    books_post.router,
    prefix="/books",
    tags=["Books Add Books"]
)


app.include_router(
    books_get.router,
    prefix="/books",
    tags=["Books"]
)




#---------------------------

"""app.include_router(
        authours.router,
    prefix="/authours",
    tags="/Authours"

)"""
#------------Students Line2--------
app.include_router(
    students_gets.router,
    prefix = "/students",
    tags=["Students "]
)
app.include_router(
    students_gets.router,
    prefix="/students",
    tags=["Students"]
)


app.include_router(
    student_post.router,
    prefix="/students",
    tags = ["Students Add Studnt"]    
)


#------------------------------------