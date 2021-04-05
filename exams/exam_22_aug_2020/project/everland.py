class Everland:

    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_expenses = sum([r.expenses + r.room_cost for r in self.rooms])
        return f"Monthly consumptions: {total_expenses:.2f}$."

    def pay(self):
        result = []
        families_to_leave = []
        for room in self.rooms:
            total_expenses = room.expenses + room.room_cost
            if room.budget >= room.expenses + room.room_cost:
                result.append(f"{room.family_name} paid {total_expenses:.2f}$ and have {room.budget:.2f}$ left.")
                room.budget -= total_expenses
            else:
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                families_to_leave.append(room)

                for r in families_to_leave:
                    self.rooms.remove(r)
        return "\n".join(result)

    def status(self):
        people_in = sum([r.members_count for r in self.rooms])
        result = [f"Total population: {people_in}"] + list(map(str, self.rooms))

        return "\n".join(result)
