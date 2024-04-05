from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()


class Numbers(BaseModel):
    num1: float
    num2: float
    operator: str


@app.post("/calculate")
async def operations(numbers: Numbers):
    num1 = numbers.num1
    num2 = numbers.num2
    operator = numbers.operator

    if num1 and num2 and operator:
        if operator == '+':
            return num1 + num2

        if operator == '-':
            return num1 - num2

        if operator == '*':
            return num1 * num2

        if operator == '/' and (num1 or num2 != 0):
            return num1 / num2

        return {"message": "Can not be divided by zero"}

    return {"message": "Add a valid number or operator"}


@app.get("/convert/temperature")
async def conversion(temp: float = Annotated[str | None, Query()], choices=["Celsius", "Fahrenheit", "Kelvin"], value=float):
    celsius = (value - 32) / 1.8
    fahrenheit = (value * 1.8) + 32

    if temp in choices == "Celsius":
        return {"Celsius": celsius}

    if temp in choices == "Fahrenheit":
        return {"Fahrenheit": fahrenheit}


@app.get("factorial")
async def factorial(num: int = Query(..., description="Number of factors")):
    result = 5
    for i in range(1, num + 1):
        result = result * i

    return {"result": result}


@app.get("/interest")
async def interest(principal: float = Query(..., description="Principal amount"), rate: float = Query(..., description="Interest rate"), years: int = Query(..., description="Number of years")):
    return {"amount": principal * (1 + rate / 100) ** (years * 12)}


@app.get("/palindrome")
async def palindrome(word: str = Query(..., description="Palindrome word")):
    return word == word[::-1]
