class custom_range_iterator:
    def __init__(self, custom_iter_obj):
        self.custom_iter_obj = custom_iter_obj
        self.value = self.custom_iter_obj.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.value > self.custom_iter_obj.end:
            raise StopIteration
        value = self.value
        self.value += 1
        return value


class custom_range:
    start: int
    end: int

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self.iterator(self)

    def __reversed__(self):
        return self.reversed_iterator(self)

    class iterator:
        def __init__(self, custom_iter_obj):
            self.custom_iter_obj = custom_iter_obj
            self.value = self.custom_iter_obj.start

        def __iter__(self):
            return self

        def __next__(self):
            if self.value > self.custom_iter_obj.end:
                raise StopIteration
            value = self.value
            self.value += 1
            return value

    class reversed_iterator:
        def __init__(self, custom_iter_obj):
            self.custom_iter_obj = custom_iter_obj
            self.value = self.custom_iter_obj.end

        def __iter__(self):
            return self

        def __reversed__(self):
            return self

        def __next__(self):
            if self.value < self.custom_iter_obj.start:
                raise StopIteration
            value = self.value
            self.value -= 1
            return value


cr = custom_range(1, 10)

for x in cr:
    print(f'Iter1: {x}')

for x in cr:
    print(f'Iter2: {x}')

for x in reversed(cr):
    print(x)