from functools import wraps


def vowel_filter(function):
    @wraps(function)
    def wrapper():
        vowels = {'a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I'}
        result = function()
        return [ch for ch in result if ch in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]
print(get_letters)
print(get_letters())
