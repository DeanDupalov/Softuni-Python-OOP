
from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    COFFEE_MILLILITERS = 50
    COFFEE_PRICE = 3.50

    def __init__(self, name, caffeine):
        # HotBeverage.__init__(self, name, Coffee.COFFEE_PRICE, Coffee.COFFEE_MILLILITERS)
        super().__init__(name, self.__class__.COFFEE_PRICE, self.__class__.COFFEE_MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine
