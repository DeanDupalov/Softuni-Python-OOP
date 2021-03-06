def solution():
    def integers():
        start_num = 1

        while True:
            yield start_num
            start_num += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        result = []
        for num in seq:
            if len(result) >= n:
                return result
            result.append(num)

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
