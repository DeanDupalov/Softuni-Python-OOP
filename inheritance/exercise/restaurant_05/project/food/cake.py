from project.food.dessert import Dessert


class Cake(Dessert):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5

    def __init__(self, name):
        super().__init__(name, price=self.__class__.PRICE, grams=self.__class__.GRAMS, calories=self.__class__.CALORIES)
