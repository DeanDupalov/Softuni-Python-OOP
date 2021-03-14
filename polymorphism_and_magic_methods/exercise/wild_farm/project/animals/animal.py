from abc import ABC, abstractmethod, abstractproperty
from typing import Union, Tuple

from project.food import Food


class Animal(ABC):
    name: str
    weight: float
    food_eaten: int

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food) -> Union[None, str]:
        if self._food_preferences and not isinstance(food, self._food_preferences):  # type: ignore
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'

        self.weight += self._weight_gain_per_food * food.quantity
        self.food_eaten += food.quantity
        return None

    @property
    @abstractmethod
    def _food_preferences(self):
        pass

    @property
    @abstractmethod
    def _weight_gain_per_food(self) -> float:
        pass


class Bird(Animal):
    wing_size: float

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    # def make_sound(self):
    #     pass
    #

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"

class Mammal(Animal):
    living_region: str

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    # def make_sound(self):
    #     pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"