from project.medicine.medicine import Medicine


class Painkiller(Medicine):
    __health_increase = 20

    def __init__(self):
        super().__init__(health_increase=Painkiller.__health_increase)


