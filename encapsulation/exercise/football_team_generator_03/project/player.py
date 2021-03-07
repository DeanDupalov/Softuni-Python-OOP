class Player:
    name: str
    endurance: int
    sprint: int
    dribble: int
    passing: int
    shooting: int

    def __init__(self, name, endurance, sprint, dribble, passing, shooting):
        self.name = name
        self.endurance = endurance
        self.sprint = sprint
        self.dribble = dribble
        self.passing = passing
        self.shooting = shooting

    def __str__(self):
        output = f"Player: {self.name}" \
                 f"\nEndurance: {self.__endurance}" \
                 f"\nSprint: {self.__sprint}" \
                 f"\nDribble: {self.__dribble}" \
                 f"\nPassing: {self.__passing}" \
                 f"\nShooting: {self.__shooting}\n"

        return output

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def endurance(self):
        return self.__endurance

    @endurance.setter
    def endurance(self, value):
        self.__endurance = value

    @property
    def sprint(self):
        return self.__sprint

    @sprint.setter
    def sprint(self, value):
        self.__sprint = value

    @property
    def dribble(self):
        return self.__dribble

    @dribble.setter
    def dribble(self, value):
        self.__dribble = value

    @property
    def passing(self):
        return self.__passing

    @passing.setter
    def passing(self, value):
        self.__passing = value

    @property
    def shooting(self):
        return self.__shooting

    @shooting.setter
    def shooting(self, value):
        self.__shooting = value
