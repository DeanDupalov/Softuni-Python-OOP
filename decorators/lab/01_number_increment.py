def number_increment(numbers):
    def increase():
        return list(map(lambda el: el+1, numbers))
        # return [el+1 for el in numbers]
    return increase()



print(number_increment([1, 2, 3]))