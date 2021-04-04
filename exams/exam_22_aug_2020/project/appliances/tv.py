from project.appliances.appliance import Appliance


class TV(Appliance):
    __COST = 1.5

    def __init__(self):
        super().__init__(cost=TV.__COST)