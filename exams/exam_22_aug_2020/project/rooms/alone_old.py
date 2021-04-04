from project.rooms.room import Room


class AloneOld(Room):
    family_name: str
    pension: float
    __ROOM_COST = 10

    def __init__(self, family_name, pension):
        super().__init__(family_name, pension, 1)
        self.room_cost = AloneOld.__ROOM_COST
        self.appliances = []
