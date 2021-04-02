from project.medicine.medicine import Medicine


class Salve(Medicine):
    __health_increase = 50

    def __init__(self):
        super().__init__(health_increase=Salve.__health_increase)



