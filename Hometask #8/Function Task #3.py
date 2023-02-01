"""
Task 3

A simple calculator.

Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers) as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:

the call make_operation(‘+’, 7, 7, 2) should return 16
the call make_operation(‘-’, 5, 5, -10, -20) should return 30
the call make_operation(‘*’, 7, 6) should return 42
"""


def make_operation(operator, operands):
    operation_sum = 0
    if operator == "+":
        for i in operands:
            operation_sum += int(i)

    if operator == "-":
        for i in operands:
            operation_sum -= int(i)

    if operator == "*":
        operation_sum = 1
        for i in operands:
            operation_sum *= int(i)

    print(operation_sum)


operands = input("Enter your expression. example (+, 7, 7, 2)\n").split()

operator = operands.pop(0)

make_operation(operator, operands)
