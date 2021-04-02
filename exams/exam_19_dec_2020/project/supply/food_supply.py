from project.supply.supply import Supply


class FoodSupply(Supply):
    __NEED_INCREASE = 20

    def __init__(self):
        super().__init__(needs_increase=FoodSupply.__NEED_INCREASE)



# f = FoodSupply()
#
# print(type(f))