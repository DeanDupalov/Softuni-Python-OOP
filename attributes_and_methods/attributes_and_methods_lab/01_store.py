class Store:
    name: str
    type: str
    capacity: int

    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}  # item_nam: quantity

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"

    @classmethod
    def from_size(cls, name: str, type: str, size: int):
        return cls(name, type, size // 2)

    def capacity_left(self):
        items_quantity = 0
        for v in self.items.values():
            items_quantity += v
        return self.capacity - items_quantity

    def add_item(self, item_name: str):
        if self.capacity_left() <= 0:
            return "Not enough capacity in the store"
        if item_name not in self.items.keys():
            self.items[item_name] = 0

        self.items[item_name] += 1
        self.capacity -= 1
        return f"{item_name} added to the store"

    def remove_item(self, item_name: str, amount: int):
        if item_name not in self.items.keys():
            return f"Cannot remove {amount} {item_name}"

        if amount > self.items[item_name]:
            return f"Cannot remove {amount} {item_name}"

        self.items[item_name] -= amount
        self.capacity += amount
        return f"{amount} {item_name} removed from the store"


first_store = Store("First store", "Fruit and Veg", 20)
second_store = Store.from_size("Second store", "Clothes", 500)

print(first_store)
print(second_store)

print(first_store.add_item("potato"))
print(second_store.add_item("jeans"))
print(first_store.remove_item("tomatoes", 1))
print(second_store.remove_item("jeans", 1))
