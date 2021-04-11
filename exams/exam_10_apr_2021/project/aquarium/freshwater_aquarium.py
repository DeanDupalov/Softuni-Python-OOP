from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):

    def __init__(self, name: str):
        super().__init__(name, 50)
        self.fish_type = "FreshwaterFish"


# fresh = FreshwaterAquarium('Test')
# print(fresh)