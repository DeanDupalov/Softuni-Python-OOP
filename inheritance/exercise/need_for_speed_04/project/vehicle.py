class Vehicle:
    fuel_consumption: float
    fuel: float
    horse_power: int
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def __fuel_needed(self, kilometers):
        return kilometers * self.fuel_consumption

    def drive(self, kilometers):
        needed_fuel = self.__fuel_needed(kilometers)
        if needed_fuel <= self.fuel:
            self.fuel -= needed_fuel

