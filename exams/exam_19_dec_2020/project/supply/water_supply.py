from project.supply.supply import Supply


class WaterSupply(Supply):
    __NEED_INCREASE = 40

    def __init__(self):
        super().__init__(needs_increase=WaterSupply.__NEED_INCREASE)

