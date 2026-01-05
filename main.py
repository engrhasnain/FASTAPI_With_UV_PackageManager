from fastapi import FastAPI

app = FastAPI()


# A simple get function simple welcome
@app.get("/")
async def health():
    return "Welcome"


# As in below we use f"" to show the username var, we use the r"", one is called 
# Formatted String Literal and Other is Raw String Literal
# using path parameter and accepting the name and getting the result back to you like return
@app.get("/greet/{username}")
async def greet(username):
    return f"A warm welcome to {username}"