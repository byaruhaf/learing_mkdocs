# calculator/calculations.py
"""
Provides functions for common arithmetic operations.

Examples:
    >>> from calculator import calculations
    >>> calculations.subtract(4.0, 2.0)
    2.0
    >>> calculations.multiply(4, 2)
    8.0
    >>> from calculator.calculations import add, divide
    >>> add(4.0, 2.0)
    6.0
    >>> divide(4, 2)
    2.0


This module includes following functions:
- `add(a,b)` - Returns the sum of two numbers
- `subtract(a,b)` - Returns the difference of two numbers
- `multiply(a,b)` - Returns the product of two numbers
- `divide(a,b)` - Returns the quotient of two numbers
"""

from typing import Union


def add(a: Union[float, int], b: Union[float, int]) -> float:
    """Return the sum of two numbers.

    Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6.0

    Args:
        a (float): A number representing the augend in the addition
        b (float): A number representing the addend in the addition

    Return:
        float: A number that is the sum of `a` and `b`
    """
    return float(a + b)


def subtract(a: Union[float, int], b: Union[float, int]) -> float:
    """Return the difference between two numbers.

    Examples:
        >>> subtract(4.0, 2.0)
        2.0
        >>> subtract(4, 2)
        2.0

    Args:
        a (float): A number representing the Minuend  in the subtraction
        b (float): A number representing the Subtrahend in the subtraction

    Return:
        float: A number that is the difference of `a` and `b`
    """
    return float(a - b)


def multiply(a: Union[float, int], b: Union[float, int]) -> float:
    """Return the multiplication between two numbers.

    Examples:
        >>> multiply(4.0, 2.0)
        8.0
        >>> multiply(4, 2)
        8.0

    Args:
        a (float): A number representing the multiplicand in the multiplication
        b (float): A number representing the multiplier in the multiplication

    Return:
        float: A number that is the product of `a` and `b`
    """
    return float(a * b)


def divide(a: Union[float, int], b: Union[float, int]) -> float:
    """Return the division between two numbers.

    Examples:
        >>> divide(4.0, 2.0)
        2.0
        >>> divide(4, 2)
        2.0

    Args:
        a (float): A number representing the numerator  in the division
        b (float): A number representing the denominator in the division

    Return:
        float: A number representing the quotient of `a` and `b`

    Raises:
        ZeroDivisionError: if the denominator is Zero
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)
