# def hello_function():
#     def say_hi():
#         return "Hi"
#
#     return say_hi
#
#
# hello = hello_function()
# print(hello())

# """Closure """
# def print_message(message):
#     def message_sender():
#         "Nested Function"
#         print(message)
#
#     message_sender()
#
#
# print_message("Some random message")

# "decorator"
# from functools import wraps
#
#
# def uppercase(function):
#     @wraps(function)
#     def wrapper(*args, **kwargs):
#         result = function(*args, **kwargs)
#         return result.upper()
#     return wrapper
#
#
# @uppercase
# def say_hi(name):
#     return f'hello, I am {name}'
#
#
# print(say_hi('Dean'))


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(4)
def say_hi():
    print("Hello")


say_hi()
