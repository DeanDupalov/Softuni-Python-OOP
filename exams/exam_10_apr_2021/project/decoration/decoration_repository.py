from project.decoration.ornament import Ornament
from project.decoration.plant import Plant


class DecorationRepository:

    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration not in self.decorations:
            return False
        self.decorations.remove(decoration)
        return True

    def find_by_type(self, decoration_type: str):
        for decoration in self.decorations:
            if decoration.__class__.__name__ == decoration_type:
                return decoration

        return "None"


# plant = Plant()
# ornament = Ornament()
# dec_repo = DecorationRepository()
# dec_repo.add(plant)
# dec_repo.add(ornament)
# # print(dec_repo.remove(ornament))
# print(dec_repo.find_by_type('Plant'))
# print(dec_repo.find_by_type('Ornament'))