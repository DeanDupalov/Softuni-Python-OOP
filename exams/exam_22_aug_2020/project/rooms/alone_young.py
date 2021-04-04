from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    family_name: str
    salary: float

    __ROOM_COST = 10

    def __init__(self, family_name, salary):
        super().__init__(family_name, budget=salary, members_count=1)
        self.room_cost = AloneYoung.__ROOM_COST
        self.appliances = [TV()]
        self.calculate_expenses(self.appliances)
