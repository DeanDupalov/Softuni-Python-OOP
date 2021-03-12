from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, amount):
        pass

    def needed_fuel(self, distance):
        return self.fuel_consumption * distance


class Car(Vehicle):
    __increased_fuel_consumption_in_summer = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption + self.__class__.__increased_fuel_consumption_in_summer)

    def refuel(self, amount):
        self.fuel_quantity += amount

    def drive(self, distance):
        needed_fuel = self.needed_fuel(distance)
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel


class Truck(Vehicle):
    __increased_fuel_consumption_in_summer = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption + self.__class__.__increased_fuel_consumption_in_summer)

    def refuel(self, amount):
        self.fuel_quantity += amount * 0.95

    def drive(self, distance):
        needed_fuel = self.needed_fuel(distance)
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

# car = Car(20, 5)
# car.drive(3)
# print(car.fuel_quantity)
# car.refuel(10)
# print(car.fuel_quantity)
# truck = Truck(100, 15)
# truck.drive(5)
# print(truck.fuel_quantity)
# truck.refuel(50)
# print(truck.fuel_quantity)
