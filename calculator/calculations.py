# calculator/calculations.py
from typing import Union


def add(a: Union[float, int], b: Union[float, int]) -> float:
    return float(a + b)


def subtract(a: Union[float, int], b: Union[float, int]) -> float:
    return float(a - b)


def multiply(a: Union[float, int], b: Union[float, int]) -> float:
    return float(a * b)


def divide(a: Union[float, int], b: Union[float, int]) -> float:
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)
