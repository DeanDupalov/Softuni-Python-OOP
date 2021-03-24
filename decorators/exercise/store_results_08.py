class store_results:
    _logfile = "results.txt"

    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        result = self._func(*args, **kwargs)
        string = f"Function \"{self._func.__name__}\" was add called. Result: {result}"
        with open(store_results._logfile, 'a') as file:
            file.write(string + "\n")
        return result


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
