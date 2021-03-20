class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.current_idx = len(iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_idx >= 0:
            temp_idx = self.current_idx
            self.current_idx -= 1
            return self.iterable[temp_idx]
        raise StopIteration()

reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)

