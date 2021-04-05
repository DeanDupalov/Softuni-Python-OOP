from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    family_name: str
    salary_one: float
    salary_two: float

    __ROOM_COST = 20

    def __init__(self, family_name, salary_one, salary_two):
        super().__init__(family_name, budget=salary_one + salary_two, members_count=2)
        self.room_cost = YoungCouple.__ROOM_COST
        self.appliances = [TV(), Fridge(), Laptop(), TV(), Fridge(), Laptop()]
        self.calculate_expenses(self.appliances)
