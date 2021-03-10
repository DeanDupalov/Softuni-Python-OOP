from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, name, caffeine):
        super().__init__(name, price=self.__class__.PRICE, milliliters=self.__class__.MILLILITERS)
        self.caffeine = caffeine

