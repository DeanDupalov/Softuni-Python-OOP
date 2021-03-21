def get_primes(list_of_int: list):

    for num in list_of_int:
        if num > 1:
            # check for factors
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))