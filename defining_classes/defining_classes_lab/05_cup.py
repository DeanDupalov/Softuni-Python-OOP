class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, milliliters):
        if self.quantity + milliliters > self.size:
            return

        self.quantity += milliliters

    def status(self):
        free_space = self.size - self.quantity
        return free_space


cup = Cup(40, 50)
cup.fill(50)
cup.fill(10)
print(cup.status())