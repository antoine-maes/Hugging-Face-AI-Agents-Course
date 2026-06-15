from langchain.tools import tool


@tool
def add(a: float, b: float) -> float:
    """Add two numbers: a + b"""
    return a + b


@tool
def subtract(a: float, b: float) -> float:
    """Subtract two numbers: a - b"""
    return a - b


@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers: a * b"""
    return a * b


@tool
def divide(a: float, b: float) -> float:
    """Divide two numbers: a / b. Raises error if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


@tool
def round_number(number: float, to_nearest: int = 1) -> float:
    """Round a number to the nearest value. E.g., round_number(182000, 1000) = 182000"""
    if to_nearest <= 0:
        raise ValueError("to_nearest must be positive")
    return round(number / to_nearest) * to_nearest
