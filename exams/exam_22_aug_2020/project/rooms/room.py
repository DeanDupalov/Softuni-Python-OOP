class Room:
    name: str
    budget: float
    members_count: int
    children: list

    def __init__(self, name, budget, members_count):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0
        self.appliances = []

    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self._expenses = value

    def calculate_expenses(self, *args):
        self.expenses = sum(el.get_monthly_expense() for seq in args for el in seq)

    def __str__(self):
        result = [f"{self.family_name} with {self.members_count} members."
                  f" Budget: {self.budget:.2f}$, Expenses: {self.expenses:.2f}$"]
        if self.children:
            for i, c in enumerate(self.children):
                result.append(f"--- Child {i + 1} monthly cost: {c.get_monthly_expense():.2f}$")

        result.append(f"--- Appliances monthly cost: "
                      f"{sum([a.get_monthly_expense() for a in self.appliances]):.2f}$")

        return "\n".join(result)
