from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):  # The FreshwaterFish could only live in FreshwaterAquarium!

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, 'FreshwaterFish', 3, price)


    def eat(self):
        self.size += 3


# fresh_fish = FreshwaterFish('fresh', 'test', 2.5)
#
# fresh_fish.eat()
#
# a= 5