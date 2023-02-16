"""

Task 2

Write a decorator that takes a list of stop words and replaces them with * inside
the decorated function

"""


def stop_words(words: object) -> object:
    def inner_decorator(func):
        def wrapper(name):
            slogan = func(name)
            for word in words:
                slogan = slogan.replace(word, "*")
            return slogan
        return wrapper
    return inner_decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan("Yurii"))
