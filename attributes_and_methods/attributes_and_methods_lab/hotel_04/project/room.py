class Room:

    number: int
    capacity: int

    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people: int):
        if self.is_taken or self.capacity < people:
            return f"Room number {self.number} cannot be taken"
        self.is_taken = True
        # self.capacity -= people
        self.guests = people

    def free_room(self):
        if not self.is_taken:
            return f"Room number {self.number} is not taken"

        self.is_taken = False
        self.guests = 0
