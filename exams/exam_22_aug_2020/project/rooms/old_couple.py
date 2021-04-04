from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    family_name: str
    pension_one: float
    pension_two: float

    __ROOM_COST = 15

    def __init__(self, family_name, pension_one, pension_two):
        super().__init__(family_name, budget=pension_one + pension_two, members_count=2)
        self.room_cost = OldCouple.__ROOM_COST
        self.appliances = [[TV(), Fridge(), Stove(), TV(), Fridge(), Stove()]]
        self.calculate_expenses(self.appliances)
