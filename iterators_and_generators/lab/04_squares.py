# def squares(n):# gen comprehension
#     return (x ** 2 for x in range(1, n + 1))


def squares(n):
    star = 1
    while star <= n:
        yield star ** 2
        star += 1


print(list(squares(5)))
