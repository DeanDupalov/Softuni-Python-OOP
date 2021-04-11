from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):  # The SaltwaterFish could only live in SaltwaterAquarium!

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, 'SaltwaterFish', 5, price)


    def eat(self):
        self.size += 2


# fish = SaltwaterFish('test', 'test', 2.5)
#
# fish.eat()
#
# a = 5
