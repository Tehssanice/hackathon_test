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
async def conversion(temp: str):

    degree = int(temp[:-1])

    i_convention = temp[-1]

    if i_convention.upper() == "C":
        result = int(round((9 * degree) / 5 + 32))
        o_convention = "Fahrenheit"
    elif i_convention.upper() == "F":
        result = int(round((degree - 32) * 5 / 9))
        o_convention = "Celsius"
    else:
        print("Input proper convention.")
        quit()

    print("The temperature in", o_convention, "is", result, "degrees.")

    return {"message": "Convert temperature"}
