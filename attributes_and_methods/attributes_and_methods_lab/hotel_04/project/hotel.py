
class Hotel:
    name: str

    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        current_room = [r for r in self.rooms if r.number == room_number][0]
        result = current_room.take_room(people)
        if result:
            return result
        self.guests += current_room.guests

    def free_room(self, room_number):
        current_room = [r for r in self.rooms if r.number == room_number][0]
        result = current_room.free_room()
        if result:
            return result
        self.guests -= current_room.guests

    def get_free_rooms(self):
        free_rooms = [r.number for r in self.rooms if not r.is_taken]
        return free_rooms

    def get_taken_rooms(self):
        taken_rooms = [r.number for r in self.rooms if r.is_taken]
        return taken_rooms

    def print_status(self):
        print(f"Hotel {self.name} has {self.guests} total guests")
        print(f"Free rooms: {', '.join(map(str, self.get_free_rooms()))}")
        print(f"Taken rooms: {', '.join(map(str, self.get_taken_rooms()))}")

#
# hotel = Hotel.from_stars(5)
#
# first_room = Room(1, 3)
# second_room = Room(2, 2)
# third_room = Room(3, 1)
#
# hotel.add_room(first_room)
# hotel.add_room(second_room)
# hotel.add_room(third_room)
#
# hotel.take_room(1, 4)
# hotel.take_room(1, 2)
# hotel.take_room(3, 1)
# hotel.take_room(3, 1)
#
# hotel.print_status()
