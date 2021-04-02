from typing import List

from project.medicine.painkiller import Painkiller
from project.supply.food_supply import FoodSupply
from project.supply.water_supply import WaterSupply
from project.survivor import Survivor


class Bunker:
    survivors: List
    supplies: List
    medicine: List
    food: List
    water: List
    painkillers: List
    salves: List

    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food_supplies = [fs for fs in self.supplies if fs.__class__.__name__ == 'FoodSupply']
        if len(food_supplies) == 0:
            raise IndexError("There are no food supplies left!")
        return food_supplies

    @property
    def water(self):
        water_supplies = [ws for ws in self.supplies if ws.__class__.__name__ == 'WaterSupply']
        if len(water_supplies) == 0:
            raise IndexError("There are no water supplies left!")
        return water_supplies

    @property
    def painkillers(self):
        painkillers = [p for p in self.medicine if p.__class__.__name__ == 'Painkiller']
        if len(painkillers) == 0:
            raise IndexError("There are no painkillers left!")
        return painkillers

    @property
    def salves(self):
        salves = [salve for salve in self.medicine if salve.__class__.__name__ == 'Salve']
        if len(salves) == 0:
            raise IndexError("There are no salves left!")
        return salves

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type: str):
        if survivor.needs_healing:
            current_medicine = None
            if medicine_type == 'Painkiller':
                current_medicine = self.painkillers.pop()
                del self.medicine[-1]
            elif medicine_type == 'Salve':
                current_medicine = self.salves.pop()
                del self.medicine[-1]
            current_medicine.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"
        else:
            return

    def sustain(self, survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            current_sustain = None
            if sustenance_type == "WaterSupply":
                current_sustain = self.water.pop()
                del self.supplies[-1]
            elif sustenance_type == "FoodSupply":
                current_sustain = self.food.pop()
                del self.supplies[-1]
            current_sustain.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"
        else:
            return

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2

        for survivor in self.survivors:
            self.sustain(survivor, "FoodSupply")
            self.sustain(survivor, "WaterSupply")


# b = Bunker()
#
# f = FoodSupply()
# w = WaterSupply()
# p = Painkiller()
#
#
# b.add_supply(f)
# b.add_supply(w)
# b.add_medicine(p)
# s = Survivor('Dam', 30)
# b.add_survivor(s)
# b.next_day()
# print(b.sustain(s, 'FoodSupply'))