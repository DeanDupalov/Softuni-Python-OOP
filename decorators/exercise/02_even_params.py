from functools import wraps


def even_parameters(func):
    def is_even(number):
        return number % 2 == 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            if all(is_even(el) for el in args):
                result = func(*args, **kwargs)
                return result
            else:
                return "Please use only even numbers!"
        except TypeError:
            return "Please use only even numbers!"
    return wrapper


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
