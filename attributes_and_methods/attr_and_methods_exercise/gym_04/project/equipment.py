class Equipment:
    ID: int = 1
    name: str

    def __init__(self, name):
        self.name = name
        self.id = Equipment.ID
        Equipment.ID += 1

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Equipment.ID