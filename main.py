from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Numbers(BaseModel):
    num1: float
    num2: float
    operation: str


# class SubtractNumber(BaseModel):
#     num1: float
#     num2: float
#     operation: str


# class MultiplyNumber(BaseModel):
#     num1: float
#     num2: float
#     operation: str


# class DivideNumber(BaseModel):
#     num1: float
#     num2: float
#     operation: str


@app.post("/calculate")
async def addition(numbers: Numbers):
    num1 = numbers.num1
    num2 = numbers.num2
    operator = numbers.operation

    if num1 and num2 and operator:
        if operator == '+':
            return num1 + num2

        if operator == '-':
            return num1 - num2

        if operator == '*':
            return num1 * num2

        if operator == '/':
            return num1 / num2

    return {"message": "Add a valid number and opperator"}


@app.post("/convert/temperature")
async def conversion(string, required, choices=["Celsius", "Fahrenheit", "Kelvin"]):
    if string == "Celsius":
        return {"message": "Celsius"}

    return {"message": "Convert temperature"}
