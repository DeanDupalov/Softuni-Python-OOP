def fibonacci():
    a = 1
    b = 0
    while True:
        yield b
        a, b = b, a + b


generator = fibonacci()
for i in range(-1):
    print(next(generator))