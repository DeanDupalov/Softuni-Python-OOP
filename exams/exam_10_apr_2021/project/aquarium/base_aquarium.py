from abc import ABC, abstractmethod


class BaseAquarium(ABC):

    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []
        self.fish_type = "Base"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum([d.comfort for d in self.decorations])

    def add_fish(self, fish):
        if len(self.fish) > self.capacity:
            return "Not enough capacity."

        if fish.species != self.fish_type:
            return "Water not suitable."

        self.fish.append(fish)
        return f"Successfully added {fish.type} to {self.name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for f in self.fish:
            f.eat()

    def __str__(self):
        result = f"{self.name}:\n"
        if not self.fish:
            result += "Fish: none\n"
        else:
            result += f"Fish: {' '.join([f.name for f in self.fish])}\n"
        result += f"Decorations: {len(self.decorations)}\n"
        result += f"Comfort: {self.calculate_comfort()}"

        return result


