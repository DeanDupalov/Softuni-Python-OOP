from functools import wraps


def logged(func):
    @wraps(func)

    def wrapper(*args, **kwargs):
        result = f"you called {func.__name__}({', '.join(map(str, args))})\nit returned {func(*args, **kwargs)}"
        return result

    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))

