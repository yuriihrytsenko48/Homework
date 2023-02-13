"""
Task 2

Write a Python program to access a function inside a function
(Tips: use function, which returns another function)
"""

a = int(input("Enter a:\n"))
b = int(input("Enter b:\n"))


def number_locals(func, a1, b1):
    return func(a1, b1)


def adding_numbers(a2, b2):
    answer = a2 + b2
    return answer


test = number_locals(adding_numbers, a, b)

print(test)
