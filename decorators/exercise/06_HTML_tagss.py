from functools import wraps
from OOP.decorators.decorators_exercis.store_results_08 import store_results


def tags(tag):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f'<{tag}>{result}</{tag}>'

        return wrapper

    return decorator

@store_results
@tags('p')
def join_strings(*args):
    return "".join(args)

#<p>Hello you!</p>
print(join_strings("Hello", " you!"))

@store_results
@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))
