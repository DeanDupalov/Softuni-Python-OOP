from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    family_name: str
    salary_one: float
    salary_two: float

    __ROOM_COST = 30

    def __init__(self, family_name, salary_one, salary_two, *children):
        super().__init__(family_name, budget=salary_one + salary_two, members_count=2 + len(children))
        self.room_cost = YoungCoupleWithChildren.__ROOM_COST
        self.children = list(children)
        self.appliances = [[TV(), Fridge(), Laptop(), TV(), Fridge(), Laptop()]]
        for _ in children:
            self.appliances.append([TV(), Fridge(), Laptop()])
        self.calculate_expenses(*self.appliances, children)
