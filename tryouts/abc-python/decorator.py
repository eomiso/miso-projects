import functools
from inspect import signature
from typing import Callable


def cache_with_client_id() -> Callable:
    """Decorator that caches the result of a function
    with the client_id given as a parameter of the function.
    """

    def decorating_function(user_function):
        print("This should be called later")
        if user_function is None:
            print("user_function is none")

        @functools.wraps(user_function)
        def wrapper(*args, **kwargs):
            # import pdb; pdb.set_trace()

            print("inside fuction")
            result = user_function()

            return result

        return wrapper

    return decorating_function


def cache_with_client_id2() -> Callable:
    """Decorator that caches the result of a function
    with the client_id given as a parameter of the function.
    """

    def decorating_function(user_function):
        print("This should be called later2")

        @functools.wraps(user_function)
        def wrapper(*args, **kwargs):
            print("inside fuction2")
            result = user_function()

            return result

        return wrapper

    return decorating_function


@cache_with_client_id()
@cache_with_client_id2()
def print_actual():
    print("actual")


def foo():
    print("씨발 ")


if __name__ == "__main__":
    print_actual()

    print("==========")

    cache_with_client_id()(cache_with_client_id2()(foo))
