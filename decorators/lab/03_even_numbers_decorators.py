from functools import wraps


def even_numbers(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return list(filter(lambda el: el % 2 == 0, result))

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))  # [2, 4]
# nums = [1, 2, 3, 4, 5]
# print(list(filter(lambda el: el % 2 == 0, nums)))
