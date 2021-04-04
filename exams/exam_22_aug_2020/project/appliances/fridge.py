from project.appliances.appliance import Appliance


class Fridge(Appliance):
    __COST = 1.2

    def __init__(self):
        super().__init__(cost=Fridge.__COST)
