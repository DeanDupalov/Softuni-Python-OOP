from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in ["FreshwaterAquarium", "SaltwaterAquarium"]:
            return "Invalid aquarium type."
        aquarium = FreshwaterAquarium(aquarium_name) if aquarium_type == 'FreshwaterAquarium' \
            else SaltwaterAquarium(aquarium_name)
        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in ["Ornament", "Plant"]:
            return "Invalid decoration type."
        decoration = Ornament() if decoration_type == "Ornament" else Plant()
        self.decorations_repository.add(decoration)
        return "Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        if aquarium_name in map(lambda a: a.name, self.aquariums):
            aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
            decoration = self.decorations_repository.find_by_type(decoration_type)
            if decoration == 'None':
                return f"There isn't a decoration of type {decoration_type}."
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        valid_fish_types = ["FreshwaterFish", "SaltwaterFish"]
        if fish_type not in valid_fish_types:
            return f"There isn't a fish of type {fish_type}."
        fish = FreshwaterFish(fish_name, fish_species, price) if fish_type == "FreshwaterFish" \
            else SaltwaterFish(fish_name, fish_species, price)
        if aquarium_name in map(lambda a: a.name, self.aquariums):
            aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]

            aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        if aquarium_name in map(lambda a: a.name, self.aquariums):
            aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]

            aquarium.feed()
            return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        if aquarium_name in map(lambda a: a.name, self.aquariums):
            aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]

            fish_price = sum([f.price for f in aquarium.fish])
            decoration_price = sum([d.price for d in aquarium.decorations])
            value = fish_price + decoration_price
            return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        return '\n'.join([str(a) for a in self.aquariums])
