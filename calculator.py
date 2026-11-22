# This is a simple calculator module that provides basic arithmetic operations such as addition and division.
# python version: 3.8
# The add function takes two numbers as input and returns their sum. The divide function takes two numbers as input and returns the result of dividing the first number by the second number. If the second number is zero, it raises a ValueError to prevent division by zero.

def add(a, b):
    return a + b

# The divide function takes two numbers as input and returns the result of dividing the first number by the second number. If the second number is zero, it raises a ValueError to prevent division by zero.
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b