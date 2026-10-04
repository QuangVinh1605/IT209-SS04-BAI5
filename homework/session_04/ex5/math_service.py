"""
Math Service Module - DevOps Session 04 Exercise 5
"""

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print(f"Add: 10 + 5 = {add(10, 5)}")
    print(f"Subtract: 10 - 5 = {subtract(10, 5)}")
    print(f"Multiply: 10 * 5 = {multiply(10, 5)}")
    print(f"Divide: 10 / 5 = {divide(10, 5)}")
