class Appliance:
    cost: float

    def __init__(self, cost):
        self.cost = cost

    def __repr__(self):
        return f"{self.__class__.__name__}"

    def get_monthly_expense(self):
        return self.cost * 30
