"""
Task 2

Write a function that takes in two numbers from the user via input(), call the numbers a and b, and then returns
 the value of squared a divided by b, construct a try-except block which raises an exception if the
 two values given by the input function were not numbers, and if value b was zero (cannot divide by zero).
 """


def exception_call():
    while True:
        try:
            a = int(input("Enter a:\n"))
            b = int(input("Enter b:\n"))
            x = (a**2) / b
        except ValueError:
            print("Use numbers only!")
            continue
        except ZeroDivisionError:
            print("Division by zero!")
            continue

        print(x)


exception_call()
