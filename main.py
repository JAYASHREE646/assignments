from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to the calculator!"}


@app.get("/add/{num1}/{num2}")
def add(num1: int, num2: int):
    result = num1 + num2
    return {"result": result}


@app.get("/subtract/{num1}/{num2}")
def subtract(num1: int, num2: int):
    result = num1 - num2
    return {"result": result}


@app.get("/multiply/{num1}/{num2}")
def multiply(num1: int, num2: int):
    result = num1 * num2
    return {"result": result}


@app.get("/divide/{num1}/{num2}")
def divide(num1: float, num2: float):
    if num2 == 0:
        return {"error": "division by zero"}
    result = num1 / num2
    return {"result": result}
