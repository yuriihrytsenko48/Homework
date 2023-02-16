"""
Task 1

Write a decorator that prints a function with arguments passed to it.

NOTE! It should print the function, not the result of its execution!

"""
a = 5
b = 7
list_ = [1, 2, 3, -4, 5]


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} called with", repr(args))
        return func
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args, **kwargs):
    return [arg ** 2 for arg in args]


add(a, b)
square_all(list_)
