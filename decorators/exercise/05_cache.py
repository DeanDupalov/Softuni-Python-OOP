from functools import wraps


def cache(func):

    @wraps(func)
    def wrapper(n):

        result = func(n)
        wrapper.log[n] = result
        return result

    wrapper.log = {}
    #0: 0, 1: 1,
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)

fibonacci(4)
print(fibonacci.log)
