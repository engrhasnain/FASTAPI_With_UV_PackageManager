from fastapi import FastAPI

app = FastAPI(title="Books App A FastAPI Beyond CRUD")


# A simple get function simple welcome
@app.get("/")
async def health():
    return "Welcome"


# As in below we use f"" to show the username var, we use the r"", one is called
# Formatted String Literal and Other is Raw String Literal
# using path parameter and accepting the name and getting the result back to you like return


# this uses the path parameter
@app.get("/greet/{username}")
async def greet(username):
    return f"A warm welcome to {username}"


# here below is the difference between the path and query parameter
# to access it we will do this
# http://greeting/hasnain?age=10    correct one with both path and query parametet


# http://greeting/hasnain           if we do it like this we will get error
# http://greeting?age=10            if we do it like this we will get error
# {
# 	"detail": [
# 		{
# 			"type": "missing",
# 			"loc": [
# 				"query",
# 				"age"
# 			],
# 			"msg": "Field required",
# 			"input": null
# 		}
# 	]
# }


@app.get("/greeting/{name}")
async def greet(name: str, age: int) -> dict:
    return {"messsage": f"My name is {name} and Age is {age}"}


# here we learn the concept of passing the query parameter as an optional
# but here is another concept for learning which is the arguments to
# which is that Non-default argument follows default argument, Pylance
# so we have to define the optional or default below the non default
from typing import Optional


# to call this with two query param we 
# http://localhost:8000/greets?name=hasnain&age=20
@app.get("/greets")
async def greet(
    age: int,
    name: Optional[str] = "User",
) -> dict:
    return {"messsage": f"My name is {name} and Age is {age}"}


# I learn about the black as well, and install it, and use it as black main.py and it reformat everything


# learn here about the pydatic model creating and how to import and use it
from models.books import BookCreate

# the post method is used here and it get data based on the pydantic model and we can display it then
@app.post('/create_book')
async def create_book(book_date : BookCreate):
    return {
        "Title" : f"{book_date.title}",
        "Author" : f"{book_date.author}"
    }


# here comes the concept of headers and status code, how and why header
from fastapi import Header

@app.get("/get_header", status_code=200)
async def get_header(
    accept : str = Header(None),
    content_type : str = Header(None),
    user_agent : str = Header(None),
    host : str = Header(None)
):
    request_header = {}
    request_header["Accept"] = accept
    request_header["Content-Type"] = content_type
    request_header["User-Agent"] = user_agent
    request_header["Host"] = host

    return request_header