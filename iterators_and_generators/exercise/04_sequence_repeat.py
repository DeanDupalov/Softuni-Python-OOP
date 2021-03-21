class sequence_repeat:

    def __init__(self, sequence, number: int):
        self.sequence = sequence
        self.number = number
        self.start_idx = 0
        self.count = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > self.number:
            raise StopIteration

        if self.start_idx == len(self.sequence):
            self.start_idx = 0

        temp = self.sequence[self.start_idx]
        self.start_idx += 1
        self.count += 1
        return temp


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
