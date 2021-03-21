from itertools import permutations


def possible_permutations(seq: list):
    for nums in permutations(seq):
        yield list(nums)


for n in possible_permutations([1, 2, 3]):
    print(n)
