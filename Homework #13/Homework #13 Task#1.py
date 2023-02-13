"""
Task 1

Write a Python program to detect the number of local variables
declared in a function.
"""

a = int(input("Enter a:\n"))
b = int(input("Enter b:\n"))


def number_locals(func, a1, b1):
    x = func(a1, b1)
    return len(locals()), x


def adding_numbers(a2, b2):
    answer = a2 + b2
    return answer


test = number_locals(adding_numbers, a, b)

print(test)
