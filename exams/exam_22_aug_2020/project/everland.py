class Everland:

    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        # total_expenses = 0
        # total_room_cost = 0
        # for r in self.rooms:
        #     total_expenses += r.calculate_expenses(r.appliances)
        #     total_room_cost += r.cost
        total_expenses = [r.expenses * 30 for r in self.rooms]
        return f"Monthly consumption: {total_expenses}$."

    def pay(self):
        pass

    def status(self):
        pass

