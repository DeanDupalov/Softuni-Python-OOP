# from typing import Optional, Dict
# from project.dough import Dough
# from project.topping import Topping
from exercise.pizza_calories.project.dough import Dough
from exercise.pizza_calories.project.topping import Topping


class Pizza:
    # name: str
    # dough: Optional['dough']
    # toppings: Dict
    # toppings_capacity: int

    def __init__(self, name, dough, toppings_capacity):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}  # topping_type: weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if isinstance(value, Dough):
            self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        self.__toppings_capacity = value

    @property
    def toppings(self):
        return self.__toppings

    @toppings.setter
    def toppings(self, value):
        if isinstance(value, dict):
            self.__toppings = value

    def add_topping(self, topping):
        if self.__toppings_capacity <= len(self.__toppings.keys()):
            raise ValueError("Not enough space for another topping")

        if topping.topping_type not in self.__toppings:
            self.__toppings[topping.topping_type] = 0

        self.__toppings[topping.topping_type] += topping.weight

    def calculate_total_weight(self) -> int:
        return self.__dough.weight + sum(self.__toppings.values())


d = Dough('brown', 'oven', 500)
t1 = Topping('cheese', 50)
t2 = Topping('tomatoes', 30)
t3 = Topping('ham', 70)
t4 = Topping('mayo', 10)
pizza = Pizza('deanie', d, 3)
pizza.add_topping(t1)
pizza.add_topping(t2)
pizza.add_topping(t3)
# pizza.add_topping(t4)

# d = Dough("Sugar", "Mixing", 20)
# p = Pizza("Burger", d, 5)
# print(p._Pizza__toppings_capacity == 5)