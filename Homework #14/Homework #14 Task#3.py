"""
Task 3

Write a decorator `arg_rules` that validates arguments passed to the function.
A decorator should take 3 arguments:

max_length: 15
type_: str
contains: [] - list of symbols that an argument should contain

If someone of the rules checks returns False, the function should return
False and print the reason it failed; otherwise,
return the result.

"""


def arg_rules(type_: type, max_length: int, contains: list):
    def inner_decorator(func):
        def wrapper(name):
            result = func(name)
            flag = True
            if type(result) != type_:
                flag = False

            if len(result) > max_length:
                flag = False

            for arg in contains:
                if arg not in result:
                    flag = False
                    break

            if flag:
                return result
            else:
                return False
        return wrapper
    return inner_decorator


def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan("johndoue3@gmail.com"))
