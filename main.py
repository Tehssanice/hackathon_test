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
        else:
            return {"message": "Can not devide zero"}

    return {"message": "Add a valid number and opperator"}


@app.post("/convert/temperature")
async def conversion(temp=Annotated[str | None, Query()], choices=["Celsius", "Fahrenheit", "Kelvin"], value=float):
    celsius = (value - 32) / 1.8
    fahrenheit = (value * 1.8) + 32

    if temp in choices == "Celsius":
        return {"Celsius": celsius}

    if temp in choices == "Fahrenheit":
        return {"Fahrenheit": fahrenheit}
