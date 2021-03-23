from functools import wraps


def debug(func):
    """print func name with args, kwargs and result."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ', '.join(map(str, args))
        kwargs_str = ', '.join(f'{key}={v}' for key, v in kwargs.items())

        result = func(*args, **kwargs)
        print(f'{func.__name__}({args_str}.{kwargs_str}) returned {result}')
        return result

    return wrapper





@debug
def say_hi(name='Dean'):
    return f"Hi {name}"


say_hi()
