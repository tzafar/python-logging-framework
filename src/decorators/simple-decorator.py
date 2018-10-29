from functools import wraps


def my_decorator(function):
    @wraps(function)
    def decorator_definition():
        ret = function()
        return "<decorator starts> -->" + ret + " <-- <decorator ends>"

    return decorator_definition


@my_decorator
def say_hello():
    return "Hi"

print(say_hello())
