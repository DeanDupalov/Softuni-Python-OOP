from functools import wraps
from time import perf_counter
from timeit import default_timer as timer


def exec_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # start_time = perf_counter()
        start_time = timer()
        func(*args, **kwargs)
        end_time = timer()
        # end_time = perf_counter()
        execution_time = end_time - start_time
        return execution_time

    return wrapper


# @exec_time
# def loop(start, end):
#     total = 0
#     for x in range(start, end):
#         total += x
#     return total
#
#
# print(loop(1, 10000000))


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result
print(concatenate(["a" for i in range(1000000)]))
