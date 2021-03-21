def read_next(*args):
    return (s for el in args for s in el)




for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')
